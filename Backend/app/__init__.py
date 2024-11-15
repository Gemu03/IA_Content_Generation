from fastapi import FastAPI
from app.routes import general, health, test, auth

# Crear la aplicación de FastAPI
app = FastAPI()

# Incluir las rutas de los archivos en la carpeta router
app.include_router(general.router, tags=["General"])
app.include_router(auth.router, tags=["Auth"])
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(test.router, prefix="/test", tags=["Test"])