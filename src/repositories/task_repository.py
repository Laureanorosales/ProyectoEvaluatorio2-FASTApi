import json
from src.models.tarea import Tarea
from src.models.tarea_crear import TareaCrear
from src.models.tarea_update import TareaUpdate

class TaskRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _load(self):
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save(self, data):
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def list(self, skip: int, limit: int):
        tareas = self._load()
        total = len(tareas)
        paginadas = tareas[skip:skip+limit]
        return {
            "items": [Tarea(**t) for t in paginadas],
            "total": total
        }

    def get(self, id: int):
        tareas = self._load()
        for t in tareas:
            if t["id"] == id:
                return Tarea(**t)
        return None

    def create(self, data: TareaCrear):
        tareas = self._load()
        new_id = max([t["id"] for t in tareas], default=0) + 1
        nueva = Tarea(id=new_id, **data.dict())
        tareas.append(nueva.dict())
        self._save(tareas)
        return nueva

    def update(self, id: int, data: TareaUpdate):
        tareas = self._load()
        for i, t in enumerate(tareas):
            if t["id"] == id:
                tareas[i].update(data.dict(exclude_unset=True))
                self._save(tareas)
                return Tarea(**tareas[i])
        return None

    def delete(self, id: int):
        tareas = self._load()
        nuevas = [t for t in tareas if t["id"] != id]
        if len(nuevas) == len(tareas):
            return False
        self._save(nuevas)
        return True
