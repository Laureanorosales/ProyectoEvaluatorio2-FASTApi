from src.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self, db_path):
        self.repo = TaskRepository(db_path)

    def listar_tareas(self, skip: int, limit: int):
        return self.repo.listar(skip, limit)

    def obtener_tarea(self, id: int):
        return self.repo.get(id)

    def crear_tarea(self, data):
        return self.repo.create(data)

    def actualizar_tarea(self, id: int, data):
        return self.repo.update(id, data)

    def eliminar_tarea(self, id: int):
        return self.repo.delete(id)
