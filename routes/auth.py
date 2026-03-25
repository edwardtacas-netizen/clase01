from fastapi import APIRouter, Body

router = APIRouter()

# Lista temporal que simula una base de datos de usuarios
users_db = []


@router.post("/register")
def register(payload: dict = Body(...)):
    # Se espera recibir: {"correo": "...", "contrasena": "..."}
    users_db.append(payload)
    return {"mensaje": "Registro exitoso", "usuario": payload}


@router.post("/login")
def login(payload: dict = Body(...)):
    # Buscar usuario registrado
    correo = payload.get("correo")
    contrasena = payload.get("contrasena")
    for u in users_db:
        if u.get("correo") == correo and u.get("contrasena") == contrasena:
            return {"mensaje": "Login exitoso", "usuario": payload}
    return {"mensaje": "Credenciales inválidas", "usuario": payload}
