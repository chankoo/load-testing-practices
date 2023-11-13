"""
WSGI config for load-testing-practices project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""


import os
from django.core.wsgi import get_wsgi_application


def check_local_uname():
    import platform
    return 'linuxkit' in platform.uname().release


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local' if check_local_uname() else 'settings.cloud')


application = get_wsgi_application()


