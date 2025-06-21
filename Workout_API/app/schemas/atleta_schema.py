# app/schemas/atleta_schema.py
from typing import Annotated
from pydantic import UUID4, Field, conint
from app.schemas.base_schema import BaseSchema

class AtletaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='João Silva', max_length=50)]
    idade: Annotated[conint(gt=0, lt=100), Field(description='Idade do atleta', example=25)]
    categoria_id: Annotated[UUID4, Field(description='ID da categoria do atleta')]
    centro_treinamento_id: Annotated[UUID4, Field(description='ID do centro de treinamento do atleta')]

class AtletaOut(AtletaIn):
    id: Annotated[UUID4, Field(description='Identificador do atleta')]
