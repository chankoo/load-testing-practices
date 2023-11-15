import redis

from django.conf import settings


class RedisCacheWrapper(object):
    rd = None

    def __init__(self):
        self.rd = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
