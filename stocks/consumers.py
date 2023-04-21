from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from urllib.parse import parse_qs
from .models import StockDetail, UserSessionId
import json
import copy

class StockConsumer(AsyncWebsocketConsumer):

    @sync_to_async
    def addToCeleryBeat(self, stock_list):
        task = PeriodicTask.objects.filter(name = 'every-10-seconds')
        if len(task)>0:
            task = task.first()
            args = json.loads(task.args)
            args = args[0]
            for x in stock_list:
                if x not in args:
                    args.append(x)
            task.args = json.dumps([args])
            task.save()
        else:
            schedule, created = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS)
            task = PeriodicTask.objects.create(interval=schedule, name='every-10-seconds', task='stocks.tasks.update_stocks', args=json.dumps([stock_list]))

    @sync_to_async    
    def addToStockDetail(self, stock_list):
        session_id = self.scope['session'].session_key
        user, _ = UserSessionId.objects.get_or_create(session_id = session_id)
        for i in stock_list:
            stock, created = StockDetail.objects.get_or_create(stock = i)
            stock.user.add(user)

    async def connect(self):
        await self.channel_layer.group_add('stockwatchers', self.channel_name)
        query_params = parse_qs(self.scope["query_string"].decode())
        stock_list = query_params['stock_list']
        await self.addToCeleryBeat(stock_list)
        await self.addToStockDetail(stock_list)
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        await self.channel_layer.group_send(
            'stockwatchers', {"type": "send_stock_update", "message": message}
        )

    @sync_to_async
    def selectUserStocks(self):
        session_id = self.scope['session'].session_key
        session_id = UserSessionId.objects.get(session_id = session_id)
        user_stocks = session_id.stockdetail_set.values_list('stock', flat = True)
        return list(user_stocks)
    
    async def send_stock_update(self, event):
        message = event["message"]
        message = copy.copy(message)
        user_stocks = await self.selectUserStocks()
        keys = message.keys()
        for key in list(keys):
            if key in user_stocks:
                pass
            else:
                del message[key]

        await self.send(text_data=json.dumps(message))
    
    @sync_to_async
    def helper_func(self):
        session_id = self.scope['session'].session_key
        session_id = UserSessionId.objects.get(session_id = session_id)
        stocks = StockDetail.objects.filter(user__id = session_id.id)
        task = PeriodicTask.objects.get(name = "every-10-seconds")
        args = json.loads(task.args)
        args = args[0]
        for i in stocks:
            i.user.remove(session_id)
            if i.user.count() == 0:
                args.remove(i.stock)
                i.delete()
        session_id.delete()
        if args == None:
            args = []
        if len(args) == 0:
            task.delete()
        else:
            task.args = json.dumps([args])
            task.save()

    async def disconnect(self, close_code):
        await self.helper_func()
        await self.channel_layer.group_discard('stockwatchers', self.channel_name)