from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from conexion import crear, get_db
from modelo import Base, RegistroCliente, RegistroUsuario, RegistroDocente, RegistroEstudiante, RegistroMateria, RegistroPadre
from shemas import Cliente as cli, Usuario as usu, Login
from fastapi.middleware.cors import CORSMiddleware
import bcrypt


app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
Base.metadata.create_all(bind=crear)

@app.post("/insertar", response_model=cli )
async def registrar_cliente(clientemodel:cli, db:Session=Depends(get_db)):
    datos=RegistroCliente(**clientemodel.dict())
    db.add(datos)
    db.commit()
    db.refresh(datos)
    return datos

@app.get("/consultaclientes", response_model=list[cli])
async def consultar_clientes(db:Session=Depends(get_db)):
    datos_cliente=db.query(RegistroCliente).all()
    return datos_cliente

@app.get("/clientes/{documento}", response_model=cli)
async def consultar_cliente(documento:int, db:Session=Depends(get_db)):
    dato_cliente=db.query(RegistroCliente).filter(RegistroCliente.documento==documento).first()

    if dato_cliente is None:
        raise HTTPException(status_code=404, detail="Dato no encontrado")
    return dato_cliente

@app.delete("/eliminar", response_model=cli)
async def eliminar_usuario(clientemodel: cli, db: Session = Depends(get_db)):

    datos = db.query(RegistroCliente).filter(RegistroCliente.documento == clientemodel.documento).first()
    if not datos:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    db.delete(datos)
    db.commit()
    return {"mensaje": "Cliente eliminado exitosamente"}

@app.get("/clientes/documento/", response_model=list[int])
async def getdocumentosclientes(db:Session=Depends(get_db)):
    documentos=db.query(RegistroCliente.documento).all()
    return[doc[0]for doc in documentos]

@app.post("/registrousuario")
async def registrar_usuario(user: usu, db: Session = Depends(get_db)):
    existing_user = db.query(RegistroUsuario).filter(RegistroUsuario.nombre_usuario == user.nombre_usuario).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    nuevo_user = RegistroUsuario(
        documento=user.documento,
        nombre_usuario=user.nombre_usuario,
        password=hashed_password,
        rol=user.rol
    )
    db.add(nuevo_user)
    db.commit()
    db.refresh(nuevo_user)
    return {"mensaje": "Usuario registrado con éxito", "documento": nuevo_user.documento, "nombre": nuevo_user.nombre_usuario, "rol": nuevo_user.rol}

@app.post("/login")
async def login(user: Login, db: Session = Depends(get_db)):
    db_user = db.query(RegistroUsuario).filter(RegistroUsuario.nombre_usuario == user.nombre_usuario).first()
    if db_user is None:
        raise HTTPException(status_code=400, detail="Usuario no existe")
    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    return {
        "mensaje": "Inicio de sesión exitoso",
        "nombreUsuario": db_user.nombre_usuario,
        "rol": db_user.rol
    }
