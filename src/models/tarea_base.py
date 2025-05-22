from pydantic import BaseModel
from typing import Optional
from datetime import date

class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    estado: str
    fecha_limite: Optional[date] = None
