from pydantic import BaseModel
from typing import Optional


class Chat(BaseModel):
    id: Optional[int] = None
    content: str
    published: bool = True

    class Config:
        from_attributes = True


class ChatRead(Chat):
    id: int
    user: int
