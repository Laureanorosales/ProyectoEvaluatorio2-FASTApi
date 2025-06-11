import json
from typing import List, Optional
from src.models.tarea import Tarea

class TaskRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _leer_datos(self) -> List[dict]:
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _escribir_datos(self, data: List[dict]):
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def obtener_todas(self) -> List[Tarea]:
        datos = self._leer_datos()
        return [Tarea(**d) for d in datos]

    def obtener_por_id(self, id: int) -> Optional[Tarea]:
        tareas = self.obtener_todas()
        for tarea in tareas:
            if tarea.id == id:
                return tarea
        return None

    def guardar(self, tarea: Tarea):
        tareas = self.obtener_todas()
        tareas.append(tarea)
        self._escribir_datos([t.dict() for t in tareas])

    def actualizar(self, id: int, nueva_tarea: Tarea) -> bool:
        tareas = self.obtener_todas()
        for i, tarea in enumerate(tareas):
            if tarea.id == id:
                tareas[i] = nueva_tarea
                self._escribir_datos([t.dict() for t in tareas])
                return True
        return False

    def eliminar(self, id: int) -> bool:
        tareas = self.obtener_todas()
        tareas_nuevas = [t for t in tareas if t.id != id]
        if len(tareas) == len(tareas_nuevas):
            return False
        self._escribir_datos([t.dict() for t in tareas_nuevas])
        return True