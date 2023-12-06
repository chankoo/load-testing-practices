from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


from src.core.router import router as core_router
from src.chats.router import router as chat_router
from src.auth.router import router as auth_router

app.include_router(core_router)
app.include_router(chat_router)
app.include_router(auth_router)
