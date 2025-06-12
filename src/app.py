from fastapi import FastAPI
from src.routers.tareas_router import router as tareas_router
from src.config.settings import get_settings
from src.config.logging_config import configure_logging

app = FastAPI()

configure_logging()

app.include_router(tareas_router)

@app.get("/")
def inicio():
    return {"mensaje": "Segundo Proyecto evaluatorio, Python+FASTAPI"}

settings = get_settings()
