from src.db.tareas_db import cargar_tareas, guardar_tareas
from src.models.tarea_crear import TareaCrear
from src.models.tarea_update import TareaUpdate


def get_all_tasks():
    return cargar_tareas()


def get_task_by_id(task_id: int):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["id"] == task_id:
            return tarea
    return None


def save_task(tarea_crear: TareaCrear):
    tareas = cargar_tareas()
    nuevo_id = 1 if not tareas else max(t["id"] for t in tareas) + 1
    tarea_dict = tarea_crear.model_dump()  

    
    if tarea_dict.get("fecha_limite"):
        tarea_dict["fecha_limite"] = tarea_dict["fecha_limite"].isoformat()

    tarea_dict["id"] = nuevo_id
    tareas.append(tarea_dict)
    guardar_tareas(tareas)
    return tarea_dict


def update_task(task_id: int, tarea_update: TareaUpdate):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["id"] == task_id:
            datos = tarea_update.model_dump(exclude_unset=True)

            if "fecha_limite" in datos and datos["fecha_limite"]:
                datos["fecha_limite"] = datos["fecha_limite"].isoformat()

            tarea.update(datos)
            guardar_tareas(tareas)
            return tarea
    return None


def delete_task_by_id(task_id: int):
    tareas = cargar_tareas()
    tareas_filtradas = [t for t in tareas if t["id"] != task_id]
    if len(tareas) == len(tareas_filtradas):
        return False
    guardar_tareas(tareas_filtradas)
    return True
