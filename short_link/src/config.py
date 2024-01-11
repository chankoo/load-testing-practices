import sys
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))


class Settings(BaseSettings):
    database_host: str
    database_port: str
    database_name: str
    database_pwd: str
    database_username: str
    redis_host: str
    redis_port: str
    redis_db: str

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
