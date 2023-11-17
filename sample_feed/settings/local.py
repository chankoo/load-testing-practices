from .base import *
import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "sample_feed",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "mysql",
        "PORT": "3306",
    }
}
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0


API_HOST = "0.0.0.0"