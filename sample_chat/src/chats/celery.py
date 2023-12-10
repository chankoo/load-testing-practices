from __future__ import absolute_import
from celery import Celery


app = Celery('chats')

from . import celeryconfig

app.config_from_object(celeryconfig)

app.autodiscover_tasks(['src.chats.tasks'])
