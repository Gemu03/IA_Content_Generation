from fastapi import FastAPI
from app.auth import routes as auth
from app.routes import general, health

# Importar modelos 
from app.models import User

# Importar el motor de la base de datos
from app.database.sqlite import Base, engine



from contextlib import asynccontextmanager
from fastapi import FastAPI

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creando tablas en la base de datos (si no existen)...")
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

# Incluir las rutas de los archivos en la carpeta router
app.include_router(general.router, tags=["General"])
app.include_router(auth.router, tags=["Auth"])
app.include_router(health.router, prefix="/health", tags=["Health"])
