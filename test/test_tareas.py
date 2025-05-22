import sys
import os


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)


from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_tareas_vacia():
    response = client.get("/tareas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_crear_tarea():
    nueva_tarea = {
        "titulo": "TEST FastAPI",
        "descripcion": "Primer test",
        "estado": "pendiente",
        "fecha_limite": "2025-06-01"
    }
    response = client.post("/tareas/", json=nueva_tarea)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["titulo"] == nueva_tarea["titulo"]
