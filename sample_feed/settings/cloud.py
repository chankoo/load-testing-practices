from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REDIS_HOST = 'test-redis-micro.opjm8j.ng.0001.apn2.cache.amazonaws.com'
REDIS_PORT = 6379
REDIS_DB = 0
