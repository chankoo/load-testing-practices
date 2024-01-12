from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select, update
from pydantic import HttpUrl

from . import models
from .caches import URLCacheWrapper


async def get_exist_short_obj(url: HttpUrl, db: AsyncSession) -> dict | None:
    stmt = select(models.ShortUrl).filter(models.ShortUrl.url == url)
    result = await db.execute(stmt)
    short_url = result.scalars().first()
    return short_url and short_url.to_dict()


async def get_short_url_obj(short_id: str, db: AsyncSession) -> dict | None:
    cache_wrapper = URLCacheWrapper()
    short_url = await cache_wrapper.hgetall(short_id)
    if short_url:
        return short_url

    stmt = select(models.ShortUrl).filter(models.ShortUrl.shortId == short_id)
    result = await db.execute(stmt)
    short_url = result.scalars().first()

    if short_url:
        await save_short_cache(short_id, short_url.to_dict())
    return short_url and short_url.to_dict()


async def create_short(url: HttpUrl, db: AsyncSession) -> models.ShortUrl:
    new_short_url = models.ShortUrl(url=url)
    db.add(new_short_url)
    await db.commit()
    await db.refresh(new_short_url)
    return new_short_url


async def update_short_id(
    short_url: models.ShortUrl, short_id: str, db: AsyncSession
) -> models.ShortUrl:
    stmt = update(models.ShortUrl).filter_by(id=short_url.id).values(shortId=short_id)
    await db.execute(stmt)
    await db.commit()
    return short_url


async def save_short_cache(short_id: str, short_url: dict):
    cache_wrapper = URLCacheWrapper()
    await cache_wrapper.hset(short_id, mapping=short_url)
