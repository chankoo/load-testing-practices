from pydantic import BaseModel
from datetime import datetime


class Chat(BaseModel):
    content: str
    published: bool = True

    class Config:
        from_attributes = True


class ChatRead(Chat):
    id: int
    channel_id: int
    user: int
    created_at: datetime


class ChatCreate(Chat):
    channel_id: int
