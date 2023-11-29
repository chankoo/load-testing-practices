from fastapi import FastAPI
from .chats import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


from src.chats.router import router as chat_router
from src.auth.router import router as auth_router

app.include_router(chat_router)
app.include_router(auth_router)
