import json

import redis
from redis import asyncio as aioredis

from src.config import settings


class RedisCacheWrapper(object):
    rd = None

    def __init__(self):
        self.rd_sync = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            charset="utf-8",
            decode_responses=True,
        )
        self.rd = aioredis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            decode_responses=True,
        )

    async def reset_redis(self):
        await self.rd.flushdb()

    def __getattr__(self, name):
        # Delegate method calls to the Redis instance if the method is not defined in this class
        def method(*args, **kwargs):
            return getattr(self.rd, name)(*args, **kwargs)

        return method


class URLCacheWrapper(RedisCacheWrapper):
    pass


class URLCacheLock(RedisCacheWrapper):
    lock = None

    def __init__(self, name: str):
        super().__init__()
        self.lock = self.rd.lock(name)
