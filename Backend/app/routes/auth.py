from fastapi import APIRouter
from app.utils.auth_functions import login, register, forgot_password

router = APIRouter()


@router.get("/login") # /login?username=admin&password=admin
async def login_user(username: str, password: str): #? 
    try:
        return login(username, password)
    except Exception as e:
        return {"message": "Login failed"}

@router.get("/register") # /register?username=admin&password=admin
async def register_user(username: str, password: str):
    try:
        return register(username, password)
    except Exception as e:
        return {"message": "Registration failed"}

@router.get("/forgot_password") # /forgot_password?username=admin
async def user_forgot_password(username: str):
    try:
        return forgot_password(username)
    except Exception as e:
        return {"message": "Error sending recovery email"}