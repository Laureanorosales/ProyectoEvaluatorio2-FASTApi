from typing import List, Optional
from src.models.tarea import Tarea
from src.models.tarea_crear import TareaCrear
from src.models.tarea_update import TareaUpdate
from src.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def listar_tareas(self, skip: int = 0, limit: int = 10) -> List[Tarea]:
        tareas = self.repo.obtener_todas()
        return tareas[skip: skip + limit]

    def obtener_tarea(self, id: int) -> Optional[Tarea]:
        return self.repo.obtener_por_id(id)

    def crear_tarea(self, datos: TareaCrear) -> Tarea:
        tareas = self.repo.obtener_todas()
        nuevo_id = max([t.id for t in tareas], default=0) + 1
        nueva_tarea = Tarea(id=nuevo_id, **datos.dict())
        self.repo.guardar(nueva_tarea)
        return nueva_tarea

    def actualizar_tarea(self, id: int, datos: TareaUpdate) -> Optional[Tarea]:
        tarea_actual = self.repo.obtener_por_id(id)
        if not tarea_actual:
            return None
        tarea_dict = tarea_actual.dict()
        tarea_dict.update(datos.dict(exclude_unset=True))
        tarea_actualizada = Tarea(**tarea_dict)
        if self.repo.actualizar(id, tarea_actualizada):
            return tarea_actualizada
        return None

    def eliminar_tarea(self, id: int) -> bool:
        return self.repo.eliminar(id)