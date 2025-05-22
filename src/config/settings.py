from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "API de Tareas"
    DEBUG: bool = True
    JSON_DB_PATH: str = "data/tareas.json"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
