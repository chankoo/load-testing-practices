from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: Optional[int] = None
    email: EmailStr

    class Config:
        from_attributes = True


class UserCreate(User):
    pwd: str


class UserRead(User):
    created_at: datetime


class UserLogin(User):
    pwd: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


