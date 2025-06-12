from fastapi import HTTPException
from src.services.task_service import TaskService
from src.config.settings import get_settings

service = TaskService(get_settings().JSON_DB_PATH)

def listar_tareas_controller(skip: int, limit: int):
    try:
        return service.listar_tareas(skip, limit)
    except Exception:
        raise HTTPException(status_code=500, detail="Error interno")

def obtener_tarea_controller(id: int):
    tarea = service.obtener_tarea(id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

def crear_tarea_controller(data):
    try:
        return service.crear_tarea(data)
    except Exception:
        raise HTTPException(status_code=500, detail="Error al crear tarea")

def actualizar_tarea_controller(id: int, data):
    tarea = service.actualizar_tarea(id, data)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

def eliminar_tarea_controller(id: int):
    eliminado = service.eliminar_tarea(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
