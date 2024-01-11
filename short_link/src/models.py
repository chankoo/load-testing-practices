from datetime import timezone

from sqlalchemy import Column, Integer, CHAR, Text, TIMESTAMP
from sqlalchemy.sql.expression import text

from .database import Base


class ShortUrl(Base):
    __tablename__ = "short_url"

    id = Column(Integer, primary_key=True, autoincrement=True)
    shortId = Column(CHAR(6), unique=True, index=True, nullable=True)
    url = Column(Text)
    createdAt = Column(
        TIMESTAMP(timezone=True), server_default=text("CURRENT_TIMESTAMP")
    )

    def to_dict(self):
        return {
            "shortId": self.shortId,
            "url": self.url,
            "createdAt": self.createdAt.replace(tzinfo=timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S%z"
            ),
        }
