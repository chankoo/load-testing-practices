from pydantic import BaseModel
from datetime import datetime


class Chat(BaseModel):
    content: str
    published: bool = True

    class Config:
        from_attributes = True


class ChatRead(Chat):
    id: int
    user: int
    created_at: datetime
