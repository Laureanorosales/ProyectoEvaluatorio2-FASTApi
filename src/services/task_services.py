from src.repositories.task_repository import (
    get_all_tasks,
    get_task_by_id,
    save_task,
    update_task,
    delete_task_by_id
)
from src.models.tarea_crear import TareaCrear
from src.models.tarea_update import TareaUpdate
from src.exceptions.tarea_exceptions import TareaNoEncontrada


def listar_tareas():
    return get_all_tasks()


def obtener_tarea(id: int):
    tarea = get_task_by_id(id)
    if not tarea:
        raise TareaNoEncontrada()
    return tarea


def crear_tarea(nueva_tarea: TareaCrear):
    return save_task(nueva_tarea)


def actualizar_tarea(id: int, tarea_actualizada: TareaUpdate):
    tarea = update_task(id, tarea_actualizada)
    if not tarea:
        raise TareaNoEncontrada()
    return tarea


def eliminar_tarea(id: int):
    eliminado = delete_task_by_id(id)
    if not eliminado:
        raise TareaNoEncontrada()
