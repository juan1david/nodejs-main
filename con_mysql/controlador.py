from fastapi import FastAPI, Form, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()
Base = declarative_base()

# Database model for clients
class RegistroCliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True, index=True)
    documento = Column(Integer, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    correo = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    sexo = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    file_path = Column(String, nullable=False)  # Path to the uploaded file

# Function to get the database session
def get_db():
    # Your logic for obtaining a DB session
    pass

@app.post("/insertardos")
async def registrar_cliente(
    documento: int = Form(...),
    nombre: str = Form(...),
    apellido: str = Form(...),
    correo: str = Form(...),
    celular: str = Form(...),
    sexo: str = Form(...),
    edad: int = Form(...),
    file: UploadFile = File(...),  # Ensure the file parameter is correctly defined
    db: Session = Depends(get_db)
):
    # Process the uploaded file
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Formato de archivo no soportado")

    # Path to save the file
    file_location = f"micarptaing/{file.filename}"

    # Save the file on the server
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    # Add the client data
    cliente_data = {
        "documento": documento,
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "celular": celular,
        "sexo": sexo,
        "edad": edad,
        "file_path": file_location,  # Save the file path for reference
    }

    # Insert the client into the database
    db_item = RegistroCliente(**cliente_data)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)  # Refresh to get the updated item from the database

    return {"message": "Cliente registrado exitosamente", "cliente": cliente_data}
