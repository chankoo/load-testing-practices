import asyncio

from fastapi import FastAPI, Depends, status, HTTPException, Response
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from redis import asyncio as aioredis

from .database import get_db
from . import models, schemas
from .caches import URLCacheWrapper, URLCacheLock
from .utils import base62_encode
from .crud import (
    get_exist_short_obj,
    get_short_url_obj,
    save_short_cache,
    create_short,
    update_short_id,
)

app = FastAPI()

redis_lock = URLCacheLock(name='url_create_lock')

@app.post("/short-links")
async def create_short_link(
    url: schemas.URL, db: AsyncSession = Depends(get_db)
) -> JSONResponse:
    async with redis_lock.lock:
        # set asyncio lock
        exist_short = await get_exist_short_obj(url.url, db)
        if exist_short:
            return JSONResponse(
                content={"data": exist_short}, status_code=status.HTTP_200_OK
            )
        new_short = await create_short(url=url.url, db=db)

    short_id = base62_encode(new_short.id)
    new_short = await update_short_id(short_url=new_short, short_id=short_id, db=db)

    data = new_short.to_dict()
    await save_short_cache(short_id, data)
    return JSONResponse(content={"data": data}, status_code=status.HTTP_201_CREATED)


@app.get("/short-links/{short_id}")
async def get_short_url(
    short_id: str, db: AsyncSession = Depends(get_db)
) -> JSONResponse:
    short_url = await get_short_url_obj(short_id, db)
    if not short_url:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{short_id} was Not found")
    return JSONResponse(content={"data": short_url})


@app.get("/r/{short_id}")
async def redirect_to_original_url(
    short_id: str, db: AsyncSession = Depends(get_db)
) -> RedirectResponse:
    # createdAt 가져와 7일 이내면 클릭 로그 추가

    short_url = await get_short_url_obj(short_id, db)
    if not short_url:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{short_id} was Not found")
    return RedirectResponse(short_url["url"], status_code=status.HTTP_302_FOUND)


@app.get("/health")
def health_check() -> JSONResponse:
    return JSONResponse({"message": "success"})


@app.get("/reset")
async def reset(db: AsyncSession = Depends(get_db)):
    # reset cache
    cache_wrapper = URLCacheWrapper()
    await cache_wrapper.reset_redis()

    # delete all rows in all tables
    from sqlalchemy.sql.expression import delete

    all_tables = [
        models.ShortUrl,
    ]

    for table in all_tables:
        await db.execute(delete(table))

    await db.commit()
    return Response(status_code=status.HTTP_200_OK)
