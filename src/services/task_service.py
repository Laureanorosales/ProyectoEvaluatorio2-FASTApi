from src.repositories.task_repository import TaskRepository
from src.config.logger import logger

class TaskService:
    def __init__(self, db_path):
        self.repo = TaskRepository(db_path)

    def listar_tareas(self, skip: int, limit: int):
        logger.info(f"Listando tareas desde {skip} hasta {skip + limit}")
        datos = self.repo.list(skip, limit)
        return {
            "total": datos["total"],
            "tareas": datos["items"]
        }

    def obtener_tarea(self, id: int):
        logger.info(f"Obteniendo tarea con ID {id}")
        return self.repo.get(id)

    def crear_tarea(self, data):
        logger.info(f"Creando nueva tarea: {data}")
        return self.repo.create(data)

    def actualizar_tarea(self, id: int, data):
        logger.info(f"Actualizando tarea {id} con datos: {data}")
        return self.repo.update(id, data)

    def eliminar_tarea(self, id: int):
        logger.info(f"Eliminando tarea con ID {id}")
        return self.repo.delete(id)
