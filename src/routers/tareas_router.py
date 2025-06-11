from fastapi import APIRouter, HTTPException
from typing import List
from src.models.tarea import Tarea
from src.models.tarea_crear import TareaCrear
from src.models.tarea_update import TareaUpdate
from src.services.task_service import TaskService
from src.repositories.task_repository import TaskRepository
from src.config.settings import get_settings

router = APIRouter(prefix="/tareas", tags=["Tareas"])

settings = get_settings()
repo = TaskRepository(settings.JSON_DB_PATH)
service = TaskService(repo)

@router.get("/", response_model=List[Tarea])
def get_tareas(skip: int = 0, limit: int = 10):
    return service.listar_tareas(skip, limit)

@router.get("/{id}", response_model=Tarea, responses={404: {"description": "Tarea no encontrada"}})
def get_tarea(id: int):
    tarea = service.obtener_tarea(id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.post("/", response_model=Tarea)
def post_tarea(nueva_tarea: TareaCrear):
    return service.crear_tarea(nueva_tarea)

@router.put("/{id}", response_model=Tarea, responses={404: {"description": "Tarea no encontrada"}})
def put_tarea(id: int, tarea_actualizada: TareaUpdate):
    tarea = service.actualizar_tarea(id, tarea_actualizada)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.delete("/{id}", status_code=204, responses={404: {"description": "Tarea no encontrada"}})
def delete_tarea(id: int):
    if not service.eliminar_tarea(id):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
