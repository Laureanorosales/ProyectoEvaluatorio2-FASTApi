import json
from pathlib import Path
from typing import List, Dict

RUTA_JSON = Path("data/tareas.json")

def cargar_tareas() -> List[dict]:
    if not RUTA_JSON.exists():
        return []
    with open(RUTA_JSON, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)
    
def guardar_tareas(tareas: List[Dict]) -> None:
    with open(RUTA_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)