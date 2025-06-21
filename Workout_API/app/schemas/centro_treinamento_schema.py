# app/schemas/centro_treinamento_schema.py
from typing import Annotated
from pydantic import UUID4, Field
from app.schemas.base_schema import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT São Paulo', max_length=50)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua XYZ, 123', max_length=100)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]
