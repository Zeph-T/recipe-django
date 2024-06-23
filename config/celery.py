from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'config.settings')

app = Celery('config')


app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings,namespace='CELERY')

app.conf.beat_schedule = {
    'daily-email-notification' : {
        'task' : 'mailerapp.tasks.retrieve_author_likes_and_send_email',
        'schedule' : crontab(hour=17,minute=27),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request : {self.request!r}')