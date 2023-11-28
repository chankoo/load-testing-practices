from fastapi import Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select, update

from src.chats import schemas, models
from src.database import get_db

router = APIRouter(
    prefix="/chats",
    tags=["chats"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_chat(chat: schemas.Chat, response: Response, db: Session = Depends(get_db)):
    new_chat = models.Chat(**chat.model_dump())
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    response.status_code = status.HTTP_201_CREATED
    return {"data": chat}


@router.get("/", response_model=list[schemas.Chat])
async def read_chats(db: Session = Depends(get_db)):
    chats = db.scalars(select(models.Chat)).all()
    return chats


@router.get("/{id}", response_model=schemas.Chat)
async def read_chat(id: int, db: Session = Depends(get_db)):
    target = db.get(models.Chat, id)
    if not target:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{id} was Not found")
    return target


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_chat(id: int, db: Session = Depends(get_db)):
    target = db.get(models.Chat, id)
    if not target:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{id} was Not found")
    db.delete(target)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Chat)
async def update_chat(id: int, new_chat: schemas.Chat, db: Session = Depends(get_db)):
    if not db.scalar(select(models.Chat).filter_by(id=id)):
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{id} was Not found")
    new_chat.id = id
    db.execute(update(models.Chat).filter_by(id=id).values(**new_chat.model_dump()))
    db.commit()
    return new_chat
