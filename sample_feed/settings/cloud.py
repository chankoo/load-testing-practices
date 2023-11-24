from .base import *
import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "sample_feed",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "172.31.16.139",
        "PORT": "3306",
    }
}

REDIS_HOST = 'ec-redis-ro.opjm8j.ng.0001.apn2.cache.amazonaws.com'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_BROKER_DB = 1

API_HOST = "alb-sample-feed-917199744.ap-northeast-2.elb.amazonaws.com"
