from fastapi import APIRouter, status
from src.controllers.tarea_controller import (
    obtener_tarea_controller,
    listar_tareas_controller,
    crear_tarea_controller,
    actualizar_tarea_controller,
    eliminar_tarea_controller
)
from src.models.tarea import Tarea
from src.models.tarea_crear import TareaCrear
from src.models.tarea_update import TareaUpdate
from typing import List

router = APIRouter(prefix="/tareas", tags=["Tareas"])

@router.get("/", response_model=List[Tarea])
def get_tareas(skip: int = 0, limit: int = 10):
    return listar_tareas_controller(skip, limit)

@router.get("/{id}", response_model=Tarea, responses={404: {"description": "Tarea no encontrada"}})
def get_tarea(id: int):
    return obtener_tarea_controller(id)

@router.post("/", response_model=Tarea, status_code=status.HTTP_201_CREATED)
def post_tarea(tarea: TareaCrear):
    return crear_tarea_controller(tarea)

@router.put("/{id}", response_model=Tarea, responses={404: {"description": "Tarea no encontrada"}})
def put_tarea(id: int, tarea: TareaUpdate):
    return actualizar_tarea_controller(id, tarea)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tarea(id: int):
    return eliminar_tarea_controller(id)
