from sqlalchemy import Column, Integer, Text, Boolean, TIMESTAMP, String
from sqlalchemy.sql.expression import text
from src.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    pwd = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
