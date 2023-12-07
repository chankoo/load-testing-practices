import redis
from redis import asyncio as aioredis
from src.config import settings


class RedisMsgQWrapper(object):
    rd = None

    def __init__(self):
        self.rd_sync = redis.Redis(host=settings.redis_host, port=settings.redis_port, db=settings.redis_db, charset="utf-8", decode_responses=True)
        self.rd = aioredis.Redis(host=settings.redis_host, port=settings.redis_port, db=settings.redis_db, decode_responses=True)
        self.pubsub = self.rd.pubsub()

    def __getattr__(self, name):
        # Delegate method calls to the Redis instance if the method is not defined in this class
        def method(*args, **kwargs):
            return getattr(self.pubsub, name)(*args, **kwargs)
        return method
