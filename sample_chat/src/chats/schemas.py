from pydantic import BaseModel
from typing import Optional


class Chat(BaseModel):
    id: Optional[int] = None
    content: str
    user: int
    published: bool = True
    featured: Optional[int] = None