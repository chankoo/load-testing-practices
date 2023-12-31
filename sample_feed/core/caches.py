import redis
from django.conf import settings


class RedisCacheWrapper(object):
    rd = None

    def __init__(self):
        self.rd = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB, charset="utf-8", decode_responses=True)

    def invalidate_key(self, key: str):
        # Delete a specific key from Redis cache
        return self.rd.delete(key)

    def reset_redis(self):
        # Remove all keys from the currently selected database
        return self.rd.flushdb()

    def __getattr__(self, name):
        # Delegate method calls to the Redis instance if the method is not defined in this class
        def method(*args, **kwargs):
            return getattr(self.rd, name)(*args, **kwargs)
        return method
