from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID

from app.schemas.centro_treinamento_schema import CentroTreinamentoIn, CentroTreinamentoOut
from app.repositories.centro_treinamento_repository import CentroTreinamentoRepository
from app.database.database import get_session

router = APIRouter()


@router.get("/", response_model=List[CentroTreinamentoOut])
async def listar_centros(session: AsyncSession = Depends(get_session)):
    repo = CentroTreinamentoRepository(session)
    centros = await repo.get_all()
    return centros


@router.get("/{centro_id}", response_model=CentroTreinamentoOut)
async def buscar_centro(centro_id: UUID, session: AsyncSession = Depends(get_session)):
    repo = CentroTreinamentoRepository(session)
    centro = await repo.get_by_id(centro_id)
    if not centro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centro não encontrado")
    return centro


@router.post("/", response_model=CentroTreinamentoOut, status_code=status.HTTP_201_CREATED)
async def criar_centro(centro_in: CentroTreinamentoIn, session: AsyncSession = Depends(get_session)):
    repo = CentroTreinamentoRepository(session)
    centro = await repo.create(centro_in)
    return centro


@router.put("/{centro_id}", response_model=CentroTreinamentoOut)
async def atualizar_centro(centro_id: UUID, centro_in: CentroTreinamentoIn, session: AsyncSession = Depends(get_session)):
    repo = CentroTreinamentoRepository(session)
    centro = await repo.get_by_id(centro_id)
    if not centro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centro não encontrado")
    centro_atualizado = await repo.update(centro, centro_in)
    return centro_atualizado


@router.delete("/{centro_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_centro(centro_id: UUID, session: AsyncSession = Depends(get_session)):
    repo = CentroTreinamentoRepository(session)
    centro = await repo.get_by_id(centro_id)
    if not centro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centro não encontrado")
    await repo.delete(centro)
    return None
