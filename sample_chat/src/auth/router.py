from fastapi import Response, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select, update

from src.auth import schemas, models, utils
from src.database import get_db
from .services import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
def login(user_credential: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.scalar(select(models.User).filter_by(email=user_credential.email))
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not utils.verify(user_credential.pwd, user.pwd):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_token = create_access_token(data={
        "user_id": user.id
    })
    return {"token": access_token, "token_type": "Bearer"}


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserRead)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = utils.hash_pwd(user.pwd)
    user.pwd = hashed

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users", response_model=list[schemas.UserRead])
async def read_users(db: Session = Depends(get_db)):
    users = db.scalars(select(models.User)).all()
    return users


@router.get("/users/{id}/", response_model=schemas.UserRead)
async def read_users(id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return user
