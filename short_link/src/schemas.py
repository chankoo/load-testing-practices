from datetime import datetime, timezone

from pydantic import BaseModel, HttpUrl


class URL(BaseModel):
    url: HttpUrl


class ShortURL(BaseModel):
    shortId: str | None
    url: HttpUrl
    createdAt: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.replace(tzinfo=timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S%z"
            )
        }
