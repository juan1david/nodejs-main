from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from conexion import Base

class RegistroCliente(Base):
    __tablename__ = "clientes"
    documento = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    correo = Column(String(50), unique=True, nullable=False)

# Modelo de Usuario
class RegistroUsuario(Base):
    __tablename__ = "usuarios"
    documento = Column(Integer, ForeignKey('clientes.documento', ondelete="CASCADE"), primary_key=True, index=True)
    nombre_usuario = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # Aumentamos la longitud a 255
    rol = Column(Enum('estudiante', 'padre', 'docente', name="rol_enum"), nullable=False)
    cliente = relationship("RegistroCliente", back_populates="usuario")

RegistroCliente.usuario = relationship("RegistroUsuario", uselist=False, back_populates="cliente")

# Modelo de Docente
class RegistroDocente(Base):
    __tablename__ = "docentes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    documento_usuario = Column(Integer, ForeignKey('usuarios.documento', ondelete="CASCADE"))
    nombre = Column(String(50), nullable=False)
    especialidad = Column(String(100), nullable=False)

# Modelo de Estudiante
class RegistroEstudiante(Base):
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    documento_usuario = Column(Integer, ForeignKey('usuarios.documento', ondelete="CASCADE"))
    nombre = Column(String(50), nullable=False)
    grado = Column(String(50), nullable=False)

# Modelo de Materia
class RegistroMateria(Base):
    __tablename__ = "materias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))

# Relación many-to-many entre docentes y materias
docente_materia_table = Table(
    'docente_materia', Base.metadata,
    Column('docente_id', Integer, ForeignKey('docentes.id', ondelete="CASCADE"), primary_key=True),
    Column('materia_id', Integer, ForeignKey('materias.id', ondelete="CASCADE"), primary_key=True)
)

# Modelo de Padre
class RegistroPadre(Base):
    __tablename__ = "padres"
    id = Column(Integer, primary_key=True, autoincrement=True)
    documento_usuario = Column(Integer, ForeignKey('usuarios.documento', ondelete="CASCADE"))
    nombre = Column(String(50), nullable=False)
    telefono = Column(String(20))