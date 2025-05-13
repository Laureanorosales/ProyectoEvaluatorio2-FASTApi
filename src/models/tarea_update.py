from pydantic import BaseModel
from typing import Optional
from datetime import date

class TareaUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    fecha_limite: Optional[date] = None