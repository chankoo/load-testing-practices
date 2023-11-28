from fastapi import Response, status, HTTPException, APIRouter

from src.chats.schemas import Chat

router = APIRouter(
    prefix="/chats",
    tags=["chats"],
    responses={404: {"description": "Not found"}},
)

chats = []


@router.post("/")
async def create_chat(chat: Chat, response: Response):
    chat = {**chat.model_dump(), "id": len(chats)+1}
    chats.append(chat)
    response.status_code = status.HTTP_201_CREATED
    return {"data": chat}


@router.get("/")
async def read_chats():
    return {"data": chats}


@router.get("/{id}")
async def read_chat(id: int):
    res = None
    for chat in chats:
        if chat["id"] == id:
            res = chat
    if not res:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{id} was Not found")
    return {"data": res}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_chat(id: int):
    target = None
    target_idx = None
    for idx, chat in enumerate(chats):
        if chat["id"] == id:
            target = chat
            target_idx = idx
    if not target:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{id} was Not found")
    chats.pop(target_idx)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
async def update_chat(id: int, new_chat: Chat):
    target_idx = None
    for idx, chat in enumerate(chats):
        if chat["id"] == id:
            target_idx = idx
    if target_idx is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{id} was Not found")
    chats[target_idx] = {**new_chat.model_dump(), "id": id}
    return {"data": chats[target_idx]}
