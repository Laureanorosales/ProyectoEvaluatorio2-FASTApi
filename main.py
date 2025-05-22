from fastapi import FastAPI
from src.routers.tareas_router import router as tareas_router
from src.config.settings import get_settings

app = FastAPI()

app.include_router(tareas_router)


@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a la API de tareas!"}


settings = get_settings()
print(settings.JSON_DB_PATH)