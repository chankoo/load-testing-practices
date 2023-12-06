import json
from src.core.caches import RedisCacheWrapper


class ChatCacheWrapper(RedisCacheWrapper):
    def __init__(self, channel_id: int):
        self.channel_id = channel_id
        super(ChatCacheWrapper, self).__init__()

    def add_chats(self, chats: list[dict]):
        for chat in chats:
            self.rpush(f"chat_channel_{self.channel_id}", json.dumps(chat))

    def get_chats(self, start=0, end=-1) -> list:
        res = []
        for chat in self.lrange(f"chat_channel_{self.channel_id}", start, end):
            res.append(json.loads(chat))
        return res
