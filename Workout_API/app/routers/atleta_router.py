from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID

from app.schemas.atleta_schema import AtletaIn, AtletaOut
from app.repositories.atleta_repository import AtletaRepository
from app.database.database import get_session


router = APIRouter()

@router.get("/", response_model=List[AtletaOut])
async def listar_atletas(session: AsyncSession = Depends(get_session)):
    repo = AtletaRepository(session)
    atletas = await repo.get_all()
    return atletas


@router.get("/{atleta_id}", response_model=AtletaOut)
async def buscar_atleta(atleta_id: UUID, session: AsyncSession = Depends(get_session)):
    repo = AtletaRepository(session)
    atleta = await repo.get_by_id(atleta_id)
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Atleta não encontrado")
    return atleta


@router.post("/", response_model=AtletaOut, status_code=status.HTTP_201_CREATED)
async def criar_atleta(atleta_in: AtletaIn, session: AsyncSession = Depends(get_session)):
    repo = AtletaRepository(session)
    atleta = await repo.create(atleta_in)
    return atleta


@router.put("/{atleta_id}", response_model=AtletaOut)
async def atualizar_atleta(atleta_id: UUID, atleta_in: AtletaIn, session: AsyncSession = Depends(get_session)):
    repo = AtletaRepository(session)
    atleta = await repo.get_by_id(atleta_id)
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Atleta não encontrado")
    atleta_atualizado = await repo.update(atleta, atleta_in)
    return atleta_atualizado


@router.delete("/{atleta_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_atleta(atleta_id: UUID, session: AsyncSession = Depends(get_session)):
    repo = AtletaRepository(session)
    atleta = await repo.get_by_id(atleta_id)
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Atleta não encontrado")
    await repo.delete(atleta)
    return None
