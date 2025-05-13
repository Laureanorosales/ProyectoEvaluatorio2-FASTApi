from pydantic import BaseModel
from typing import Optional
from datetime import date

from src.models.tarea_base import TareaBase


class Tarea(TareaBase):
    id: int
