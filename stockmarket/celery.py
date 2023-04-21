from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockmarket.settings')

app = Celery('stockmarket')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    # 'every-10-seconds' : {
    #     'task' : 'stocks.tasks.update_stocks',
    #     'schedule' : 10,
    #     'args' : (['RELIANCE.NS', 'BAJAJFINSV.NS'],)
    # }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    (f'Request: {self.request!r}')