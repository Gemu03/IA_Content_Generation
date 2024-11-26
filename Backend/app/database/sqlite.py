from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a SQLite (base de datos en archivo local)
DATABASE_URL = "sqlite:///./database.db"

# Configurar el motor de la base de datos
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
