from __future__ import absolute_import
import os
from celery import Celery


def check_local_uname():
    import platform
    return 'linuxkit' in platform.uname().release


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local' if check_local_uname() else 'settings.cloud')

app = Celery('feed')

from . import celeryconfig

app.config_from_object(celeryconfig)

app.autodiscover_tasks()
