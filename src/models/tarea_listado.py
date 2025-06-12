from pydantic import BaseModel
from typing import List
from src.models.tarea import Tarea

class TareaListado(BaseModel):
    total: int
    tareas: List[Tarea]
