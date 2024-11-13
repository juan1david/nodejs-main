from pydantic import BaseModel, constr
from enum import Enum

# Enum de roles
class RolEnum(str, Enum):
    estudiante = "estudiante"
    padre = "padre"
    docente = "docente"

# Esquema de Cliente
class Cliente(BaseModel):
    documento: int
    nombre: str
    apellido: str
    correo: str

# Esquema de Usuario
class Usuario(BaseModel):
    documento: int
    nombre_usuario: constr(min_length=3, max_length=50)
    password: constr(min_length=6)  
    rol: RolEnum

class Login(BaseModel):
    nombre_usuario:str
    password:str