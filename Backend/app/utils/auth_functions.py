

def login(username: str, password: str) -> bool:
    if username == "admin" and password == "admin":
        return True
    return False

def register(username: str, password: str) -> bool:
    return True

def forgot_password(username: str) -> str:
    try:
        return "Email sent to {}".format(username)
    except Exception as e:
        return "Error al enviar recovery: {}".format(str(e))