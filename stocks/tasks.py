from celery import shared_task
from yahoo_fin.stock_info import *
from channels.layers import get_channel_layer
import asyncio
import simplejson as json

@shared_task(bind=True)
def update_stocks(self, stock_list):
    stock_details = {}
    for stock in stock_list:
        stock_detail = json.loads(json.dumps(get_quote_table(stock), ignore_nan = True))
        stock_details.update({stock:stock_detail})
    
    channel_layer = get_channel_layer()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(channel_layer.group_send('stockwatchers', {
        'type':'send_stock_update',
        'message':stock_details
    }))
    return 'Done'