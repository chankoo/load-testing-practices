import json
from src.core.caches import RedisCacheWrapper


class ChatCacheWrapper(RedisCacheWrapper):
    def __init__(self, channel_id: int):
        self.channel_id = channel_id
        super(ChatCacheWrapper, self).__init__()

    async def add_chats(self, chats: list[dict]):
        for chat in chats:
            await self.rpush(f"chat_channel_{self.channel_id}", json.dumps(chat))

    def add_chats_sync(self, chats: list[dict]):
        for chat in chats:
            self.rd_sync.rpush(f"chat_channel_{self.channel_id}", json.dumps(chat))

    async def get_chats(self, start=0, end=-1) -> list:
        res = []
        chats = await self.lrange(f"chat_channel_{self.channel_id}", start, end)
        for chat in chats:
            res.append(json.loads(chat))
        return res
