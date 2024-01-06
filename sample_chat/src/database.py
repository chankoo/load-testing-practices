from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings, check_local_uname

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_pwd}@{settings.database_host}:{settings.database_port}/{settings.database_name}"

if not check_local_uname():
    SQLALCHEMY_DATABASE_URL = f"sqlite:///./{settings.database_name}.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
