from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID

from app.schemas.categoria_schema import CategoriaIn, CategoriaOut
from app.repositories.categoria_repository import CategoriaRepository
from app.database.database import get_session

router = APIRouter()

@router.post("/", response_model=CategoriaOut, status_code=status.HTTP_201_CREATED)
async def criar_categoria(categoria_in: CategoriaIn, session: AsyncSession = Depends(get_session)):
    repo = CategoriaRepository(session)
    categoria = await repo.create(categoria_in)
    return categoria

@router.get("/", response_model=List[CategoriaOut])
async def listar_categorias(session: AsyncSession = Depends(get_session)):
    repo = CategoriaRepository(session)
    categorias = await repo.get_all()
    return categorias

@router.get("/{categoria_id}", response_model=CategoriaOut)
async def buscar_categoria(categoria_id: UUID, session: AsyncSession = Depends(get_session)):
    repo = CategoriaRepository(session)
    categoria = await repo.get_by_id(categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.put("/{categoria_id}", response_model=CategoriaOut)
async def atualizar_categoria(categoria_id: UUID, categoria_in: CategoriaIn, session: AsyncSession = Depends(get_session)):
    repo = CategoriaRepository(session)
    categoria = await repo.update(categoria_id, categoria_in)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_categoria(categoria_id: UUID, session: AsyncSession = Depends(get_session)):
    repo = CategoriaRepository(session)
    success = await repo.delete(categoria_id)
    if not success:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return None
