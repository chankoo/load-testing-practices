from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "test",
        "USER": "chankoo",
        "PASSWORD": "01234567",
        "HOST": "test-rds-mysql.czxmv1r9akq3.ap-northeast-2.rds.amazonaws.com",
        "PORT": "3306",
    }
}

REDIS_HOST = 'test-redis-micro.opjm8j.ng.0001.apn2.cache.amazonaws.com'
REDIS_PORT = 6379
REDIS_DB = 0
