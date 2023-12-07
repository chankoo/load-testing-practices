from src.core.msg_queues import RedisMsgQWrapper


class ChatMsgQWrapper(RedisMsgQWrapper):
    def __init__(self, channel_id: int):
        self.channel_id = channel_id
        super(ChatMsgQWrapper, self).__init__()

    async def publish(self, message):
        await self.rd.publish(self.channel_id, message)
