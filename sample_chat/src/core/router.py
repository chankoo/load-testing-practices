import json

from fastapi import Response, APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from .caches import RedisCacheWrapper


router = APIRouter(
    prefix="",
    tags=["core"],
    responses={404: {"description": "Not found"}},
)


@router.get("/reset-data/")
def reset_data(db: Session = Depends(get_db)):
    redis = RedisCacheWrapper()
    redis.reset_redis()
    return Response(json.dumps({"status": "success"}))


@router.get("/health")
async def health():
    return {"status": "ok"}
