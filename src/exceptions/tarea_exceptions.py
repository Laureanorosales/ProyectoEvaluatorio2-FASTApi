from fastapi import HTTPException

class TareaNoEncontrada(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Tarea no encontrada")

class TareaYaExiste(HTTPException):
    def __init__(self):
        super().__init__(status_code=409, detail="La tarea ya existe")

class DatosInvalidos(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Datos de entrada inválidos")        