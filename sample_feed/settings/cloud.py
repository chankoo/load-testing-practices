from .base import *
import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "sample_feed",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "172.31.31.105",
        "PORT": "3306",
    }
}

REDIS_HOST = 'test-redis-micro.opjm8j.ng.0001.apn2.cache.amazonaws.com'
REDIS_PORT = 6379
REDIS_DB = 0

API_HOST = "alb-ecs-1586857067.ap-northeast-2.elb.amazonaws.com"
