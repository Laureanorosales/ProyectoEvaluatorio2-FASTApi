from fastapi import FastAPI
from src.routers.tareas_router import router as tareas_router

app = FastAPI()

app.include_router(tareas_router)

@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a la API de tareas!"}