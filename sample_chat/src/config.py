import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    database_host: str
    database_port: str
    database_name: str
    database_pwd: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire: int
    redis_host: str
    redis_port: str
    redis_db: str
    redis_broker_db: str
    id_generator_host: str
    grpc_port: int

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
