# 📝 API de Tareas - Proyecto con FastAPI

Este es un proyecto evaluatorio desarrollado con **FastAPI** que implementa un CRUD completo sobre tareas.

## 🚀 Tecnologías utilizadas

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- JSON (como método de persistencia)
- Logging
- Variables de entorno con `python-dotenv`

---

## ⚙️ Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/Laureanorosales/ProyectoEvaluatorio2-FASTApi.git
cd api-tareas
```

2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar entorno virtual:

- Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- Linux/macOS:
  ```bash
  source venv/bin/activate
  ```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

5. Crear el archivo `.env`:

```env
DB_PATH=data/tareas.json
```

6. Ejecutar el servidor:

```bash
uvicorn main:app --reload
```

---

## 📬 Endpoints disponibles

| Método | Ruta           | Descripción                     |
|--------|----------------|---------------------------------|
| GET    | /tareas        | Listar todas las tareas         |
| GET    | /tareas/{id}   | Ver tarea específica            |
| POST   | /tareas        | Crear una nueva tarea           |
| PUT    | /tareas/{id}   | Actualizar una tarea existente  |
| DELETE | /tareas/{id}   | Eliminar una tarea              |

---

## 👨‍💻 Autor

Proyecto realizado por **Laureano Rosales** para la segunda instancia evaluatoria del curso de Python + FastAPI 2025.
