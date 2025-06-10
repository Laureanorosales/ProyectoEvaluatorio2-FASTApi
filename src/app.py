from fastapi import FastAPI
from src.routers.main_router import main_router
from src.config.settings import get_settings

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(main_router)

    @app.get("/")
    def inicio():
        return {"mensaje": "Segundo Proyecto evaluatorio, Python+FASTAPI"}

    settings = get_settings()
    print(settings.JSON_DB_PATH)

    return app
