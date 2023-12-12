import datetime
import asyncio
import json

from fastapi import Response, status, HTTPException, APIRouter, Depends
from fastapi import WebSocket, WebSocketDisconnect, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select, update
from snowflake import SnowflakeGenerator

from src.chats import schemas, models
from src.database import get_db
from src.auth.services import get_current_user
from .caches import ChatCacheWrapper
from .msg_queues import ChatMsgQWrapper
from .tasks import save_chat

router = APIRouter(
    prefix="/chats",
    tags=["chats"],
    responses={404: {"description": "Not found"}},
)

connected_users = {}

async def get_id(instance: int):
    epoch = 1702379129
    gen = SnowflakeGenerator(instance, epoch=epoch)
    return next(gen)


@router.websocket("/ws/{channel_id}/")
async def ws_channel(websocket: WebSocket, channel_id: int, token: str = Query(None), db: Session = Depends(get_db)):
    # user_id = await get_current_user(token)
    # if not user_id:

    #     await websocket.close()
    #     return
    user_id = 1

    await websocket.accept()
    connected_users[user_id] = websocket

    # Subscribe to Redis channel for this chat room
    msg_q = ChatMsgQWrapper(channel_id=channel_id, q_type="broadcast")
    await msg_q.subscribe()
    asyncio.create_task(redis_message_handler(websocket, msg_q))
    
    try:
        while True:
            data = await websocket.receive_text()
            now = datetime.datetime.now()
            chat = {
                "id": await get_id(instance=user_id),
                "user": user_id,
                "content": data,
                "channel_id": channel_id, "created_at": now.isoformat(), "published": True,
            }

            # celery task
            save_chat.delay(channel_id=channel_id, chat=chat)
    except Exception as e:
        # Handle disconnection or errors
        connected_users.pop(user_id, None)
        raise e


async def redis_message_handler(websocket, msg_q):
    try:
        while True:
            msg = await msg_q.get_message()
            if msg and msg['type'] == 'message':
                await websocket.send_text(msg['data'])
    except:
        await msg_q.unsubscribe()



@router.get("/channels/{channel_id}", response_model=list[schemas.ChatRead])
async def read_chats(channel_id: int, db: Session = Depends(get_db), cache: str = Query(None)):
    if cache:
        cache = ChatCacheWrapper(channel_id=channel_id)
        chats = await cache.get_chats()
    else:
        chats = db.scalars(select(models.Chat).filter_by(channel_id=channel_id)).all()
    return chats


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ChatRead)
async def create_chat(chat: schemas.ChatCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    new_chat = models.Chat(user=user_id, **chat.model_dump())
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat


@router.get("/", response_model=list[schemas.ChatRead])
async def read_chats(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    chats = db.scalars(select(models.Chat).filter_by(user=user_id)).all()
    return chats


@router.get("/{id}", response_model=schemas.ChatRead)
async def read_chat(id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    target = db.get(models.Chat, id)
    if not target:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{id} was Not found")
    if target.user != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"user_id not matched.")
    return target


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_chat(id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    target = db.get(models.Chat, id)
    if not target:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{id} was Not found")
    if target.user != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"user_id not matched.")
    db.delete(target)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.ChatRead)
async def update_chat(id: int, new_chat: schemas.Chat, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    target = db.scalar(select(models.Chat).filter_by(id=id))
    if not target:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{id} was Not found")
    if target.user != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"user_id not matched.")

    db.execute(update(models.Chat).filter_by(id=id).values(id=id, user=user_id, **new_chat.model_dump()))
    db.commit()
    return target
