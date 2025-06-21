from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database.database import Base

class Categoria(Base):
    __tablename__ = "categoria"

    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    nome = Column(String(10), unique=True, nullable=False)
