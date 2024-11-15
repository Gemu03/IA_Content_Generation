from fastapi import APIRouter

# Crear el enrutador de FastAPI
router = APIRouter()

@router.get("/")
async def healthcheck():
    return {"message": "Bienvenido a Health"}
