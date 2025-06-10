from fastapi import APIRouter
from typing import List
from src.models.tarea import Tarea
from src.models.tarea_crear import TareaCrear
from src.models.tarea_update import TareaUpdate
from src.controllers import tarea_controller as controller

router = APIRouter(prefix="/tareas", tags=["Tareas"])

@router.get("/", response_model=List[Tarea])
def get_tareas(skip: int = 0, limit: int = 10):
    return controller.listar_tareas(skip, limit)

@router.get("/{id}", response_model=Tarea, responses={404: {"description": "Tarea no encontrada"}})
def get_tarea(id: int):
    return controller.obtener_tarea(id)

@router.post("/", response_model=Tarea)
def post_tarea(nueva_tarea: TareaCrear):
    return controller.crear_tarea(nueva_tarea)

@router.put("/{id}", response_model=Tarea, responses={404: {"description": "Tarea no encontrada"}})
def put_tarea(id: int, tarea_actualizada: TareaUpdate):
    return controller.actualizar_tarea(id, tarea_actualizada)

@router.delete("/{id}", status_code=204, responses={404: {"description": "Tarea no encontrada"}})
def delete_tarea(id: int):
    return controller.eliminar_tarea(id)
