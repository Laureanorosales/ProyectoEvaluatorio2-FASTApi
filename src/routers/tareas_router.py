from fastapi import APIRouter
from typing import List
from src.models.tarea import Tarea
from src.models.tarea_crear import TareaCrear
from src.models.tarea_update import TareaUpdate
from src.services.task_services import (
    listar_tareas,
    obtener_tarea,
    crear_tarea,
    actualizar_tarea,
    eliminar_tarea
)

router = APIRouter(prefix="/tareas", tags=["Tareas"])

@router.get("/", response_model=List[Tarea])
def get_tareas():
    return listar_tareas()

@router.get("/{id}", response_model=Tarea)
def get_tarea(id: int):
    return obtener_tarea(id)

@router.post("/", response_model=Tarea)
def post_tarea(nueva_tarea: TareaCrear):
    return crear_tarea(nueva_tarea)

@router.put("/{id}", response_model=Tarea)
def put_tarea(id: int, tarea_actualizada: TareaUpdate):
    return actualizar_tarea(id, tarea_actualizada)

@router.delete("/{id}", status_code=204)
def delete_tarea(id: int):
    eliminar_tarea(id)
