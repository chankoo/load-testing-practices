from sqlalchemy import Column, Integer, Text, Boolean, TIMESTAMP
from sqlalchemy.sql.expression import text
from src.database import Base


class Chat(Base):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(Text, nullable=False, default='')
    user = Column(Integer, nullable=True)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
