import json
from celery import shared_task
from .caches import ChatCacheWrapper
from .msg_queues import ChatMsgQWrapper 


@shared_task
def save_chat(channel_id: int, chat: dict):
    msg_q = ChatMsgQWrapper(channel_id=channel_id, q_type="broadcast")
    msg_q.publish_sync(json.dumps(chat))

    # Store message in the cache
    cache = ChatCacheWrapper(channel_id=channel_id)
    cache.add_chats_sync([chat])

    # # Store message in the database
    # chat_message = models.Chat(user=user_id, content=data, channel_id=channel_id)
    # db.add(chat_message)
    # db.commit()
