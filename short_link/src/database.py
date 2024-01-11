from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import settings

DATABASE_URL = f"mysql+aiomysql://{settings.database_username}:{settings.database_pwd}@{settings.database_host}:{settings.database_port}/{settings.database_name}"
DATABASE_URL_SYNC = f"mysql+pymysql://{settings.database_username}:{settings.database_pwd}@{settings.database_host}:{settings.database_port}/{settings.database_name}"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()


async def get_db():
    try:
        db = async_session()
        yield db
    finally:
        await db.close()
