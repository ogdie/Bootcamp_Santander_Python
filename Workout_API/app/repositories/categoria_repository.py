from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from uuid import UUID

from app.models.categoria_model import Categoria
from app.schemas.categoria_schema import CategoriaIn

class CategoriaRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, categoria_in: CategoriaIn) -> Categoria:
        nova_categoria = Categoria(**categoria_in.dict())
        self.session.add(nova_categoria)
        await self.session.commit()
        await self.session.refresh(nova_categoria)
        return nova_categoria

    async def get_all(self) -> List[Categoria]:
        result = await self.session.execute("SELECT * FROM categoria")
        categorias = result.scalars().all()
        return categorias

    async def get_by_id(self, categoria_id: UUID) -> Optional[Categoria]:
        categoria = await self.session.get(Categoria, categoria_id)
        return categoria

    async def update(self, categoria_id: UUID, categoria_in: CategoriaIn) -> Optional[Categoria]:
        categoria = await self.get_by_id(categoria_id)
        if not categoria:
            return None
        for key, value in categoria_in.dict().items():
            setattr(categoria, key, value)
        self.session.add(categoria)
        await self.session.commit()
        await self.session.refresh(categoria)
        return categoria

    async def delete(self, categoria_id: UUID) -> bool:
        categoria = await self.get_by_id(categoria_id)
        if not categoria:
            return False
        await self.session.delete(categoria)
        await self.session.commit()
        return True

