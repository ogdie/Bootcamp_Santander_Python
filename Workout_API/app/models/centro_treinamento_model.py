from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database.database import Base

class CentroTreinamento(Base):
    __tablename__ = "centro_treinamento"

    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    nome = Column(String(20), unique=True, nullable=False)
    endereco = Column(String(60), nullable=False)
    proprietario = Column(String(30), nullable=False)
