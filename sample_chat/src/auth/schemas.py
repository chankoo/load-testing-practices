from pydantic import BaseModel, EmailStr
from datetime import datetime


class User(BaseModel):
    id: int | None = None
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
    id: int | None = None


