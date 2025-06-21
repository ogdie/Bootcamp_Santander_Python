from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database.database import Base

class Atleta(Base):
    __tablename__ = "atleta"

    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float(10, 2), nullable=False)
    altura = Column(Float(10, 2), nullable=False)
    sexo = Column(String(1), nullable=False)
    centro_treinamento_id = Column(Integer, ForeignKey("centro_treinamento.pk_id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categoria.pk_id"), nullable=False)
