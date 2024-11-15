from fastapi import APIRouter

# Crear el enrutador para rutas generales
router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Bienvenido a FastAPI"}

@router.get("/notimplemented")
async def not_implemented():
    return {"message": "This endpoint is not implemented yet"}