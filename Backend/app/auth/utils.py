from sqlalchemy.orm import Session
from app.models import User
from app.auth.schemas import UserCreate
from passlib.context import CryptContext

# Configuración para el hash de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def register(db: Session, user: UserCreate):
    # Verifica si el correo ya está registrado
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise ValueError("El correo ya está registrado.")
    
    # Crea un nuevo usuario
    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login(username: str, password: str) -> bool:
    if username == "admin" and password == "admin":
        return True
    return False

def forgot_password(username: str) -> str:
    try:
        return "Email sent to {}".format(username)
    except Exception as e:
        return "Error al enviar recovery: {}".format(str(e))