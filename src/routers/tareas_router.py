from fastapi import APIRouter, HTTPException
from typing import List

from src.models.tarea import Tarea
from src.db.tareas_db import cargar_tareas, guardar_tareas
from src.models.tarea_update import TareaUpdate

router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)

@router.get("/", response_model=List[Tarea])
def listar_tareas():
    return cargar_tareas()

@router.put("/{id}", response_model=Tarea)
def actualizar_tarea(id: int, tarea_actualizada: TareaUpdate):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["id"] == id:
            datos = tarea_actualizada.dict(exclude_unset=True)
            tarea.update(datos)
            guardar_tareas(tareas)
            return tarea

    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@router.delete("/{id}", status_code=204)
def eliminar_tarea(id: int):
    tareas = cargar_tareas()
    tareas_filtradas = [t for t in tareas if t["id"] != id]

    if len(tareas) == len(tareas_filtradas):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    guardar_tareas(tareas_filtradas)