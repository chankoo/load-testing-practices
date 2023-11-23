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
        "OPTIONS": {
            "isolation_level": "READ COMMITTED"
        }
    }
}
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0


API_HOST = "0.0.0.0"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}
