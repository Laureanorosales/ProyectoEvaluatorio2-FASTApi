from fastapi import APIRouter
from src.routers.tareas_router import router as tareas_router

main_router = APIRouter()
main_router.include_router(tareas_router)