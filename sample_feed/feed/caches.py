from sample_feed.core.caches import RedisCacheWrapper
from typing import List


class FeedCacheWrapper(RedisCacheWrapper):
    def add_feed_posts(self, owner: int, posts: List[dict]):
        scores = {}
        for post in posts:
            scores.update({post["id"]: post["created_at_ts"]})
        self.zadd(f"feed_{owner}", scores)

        for post in posts:
            post_id = post["id"]
            self.hset(f"post_{post_id}", mapping=post)

    def get_feed(self, owner: int) -> list:
        feed = []
        post_ids = self.zrevrange(f"feed_{owner}", 0, -1)
        for post_id in post_ids:
            feed.append(self.hgetall(f"post_{post_id}"))
        return feed
