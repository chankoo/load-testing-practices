from pydantic import BaseModel
from datetime import datetime


class Chat(BaseModel):
    content: str
    published: bool = True

    class Config:
        from_attributes = True


class ChatRead(Chat):
    id: int | str
    channel_id: int
    user: int
    created_at: datetime | str


class ChatCreate(Chat):
    channel_id: int
