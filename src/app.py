from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

import logging
from src.routers.main_router import main_router
from src.config.settings import get_settings
from src.config.logging_config import configurar_logging


def create_app() -> FastAPI:
    configurar_logging()

    app = FastAPI()

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={"error": "Datos de entrada inválidos",
                     "detalles": exc.errors()},
        )

    app.include_router(main_router)

    @app.get("/")
    def inicio():
        return {"mensaje": "Segundo Proyecto evaluatorio, Python+FASTAPI"}

    settings = get_settings()
    logging.info(f"JSON_DB_PATH configurado en: {settings.JSON_DB_PATH}")

    return app
