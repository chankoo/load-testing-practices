from typing import List
from celery import shared_task
from .caches import FeedCacheWrapper


@shared_task
def update_feed_cache(post: dict, related_persons: List[int]):
    fc = FeedCacheWrapper()
    # Add feed cache for post owner
    fc.add_feed_posts(owner=post["person"], posts=[post])

    # Add feed cache for friends of post owner
    for related_person in related_persons:
        fc.add_feed_posts(owner=related_person, posts=[post])
