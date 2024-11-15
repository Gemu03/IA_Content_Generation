from fastapi import APIRouter, HTTPException
from app.utils.math_operations import square_number

# Crear el enrutador para rutas generales
router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Bienvenido a FastAPI"}

@router.get("/square")
async def calculate_square(number: int):
    try:
        result = square_number(number)
        return {"number": number, "square": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
