import json
from pathlib import Path
from typing import List, Dict
from src.config.settings import get_settings

settings = get_settings()
RUTA_JSON = Path(settings.JSON_DB_PATH)

def cargar_tareas() -> List[dict]:
    if not RUTA_JSON.exists():
        return []
    with open(RUTA_JSON, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def guardar_tareas(tareas: List[Dict]) -> None:
    RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)  # crea /data si no existe
    with open(RUTA_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)
