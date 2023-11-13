from .base import *
import pymysql

pymysql.install_as_MySQLdb()

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

REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0
