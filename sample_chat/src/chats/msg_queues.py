from src.core.msg_queues import RedisMsgQWrapper


class ChatMsgQWrapper(RedisMsgQWrapper):
    def __init__(self, channel_id: int, q_type: str):
        self.channel_id = channel_id
        self.q_type = q_type
        super(ChatMsgQWrapper, self).__init__()

    async def publish(self, message):
        await self.rd.publish(f"{self.channel_id}_{self.q_type}", message)
    
    def publish_sync(self, message):
        self.rd_sync.publish(f"{self.channel_id}_{self.q_type}", message)
        
    async def subscribe(self):
        await self.pubsub.subscribe(f"{self.channel_id}_{self.q_type}")
