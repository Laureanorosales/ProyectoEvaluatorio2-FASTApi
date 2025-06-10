from src.db.tareas_db import cargar_tareas, guardar_tareas
from src.models.tarea import Tarea
from src.models.tarea_crear import TareaCrear
from src.models.tarea_update import TareaUpdate
from src.exceptions.tarea_exceptions import TareaNoEncontrada

def listar_tareas(skip: int = 0, limit: int = 10):
    tareas = cargar_tareas()
    return tareas[skip : skip + limit]


def obtener_tarea(id: int):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise TareaNoEncontrada()

def crear_tarea(nueva_tarea: TareaCrear):
    tareas = cargar_tareas()
    nuevo_id = 1 if not tareas else max(t["id"] for t in tareas) + 1
    tarea_dict = nueva_tarea.dict()
    tarea_dict["id"] = nuevo_id
    tareas.append(tarea_dict)
    guardar_tareas(tareas)
    return tarea_dict

def actualizar_tarea(id: int, tarea_actualizada: TareaUpdate):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["id"] == id:
            datos = tarea_actualizada.dict(exclude_unset=True)
            tarea.update(datos)
            guardar_tareas(tareas)
            return tarea
    raise TareaNoEncontrada()

def eliminar_tarea(id: int):
    tareas = cargar_tareas()
    tareas_filtradas = [t for t in tareas if t["id"] != id]
    if len(tareas) == len(tareas_filtradas):
        raise TareaNoEncontrada()
    guardar_tareas(tareas_filtradas)