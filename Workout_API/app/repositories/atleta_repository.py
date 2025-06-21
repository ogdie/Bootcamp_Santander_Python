from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from uuid import UUID

from app.models.atleta_model import Atleta
from app.schemas.atleta_schema import AtletaIn

class AtletaRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, atleta_in: AtletaIn) -> Atleta:
        novo_atleta = Atleta(**atleta_in.dict())
        self.session.add(novo_atleta)
        await self.session.commit()
        await self.session.refresh(novo_atleta)
        return novo_atleta

    async def get_all(self) -> List[Atleta]:
        result = await self.session.execute("SELECT * FROM atleta")
        atletas = result.scalars().all()
        return atletas

    async def get_by_id(self, atleta_id: UUID) -> Optional[Atleta]:
        atleta = await self.session.get(Atleta, atleta_id)
        return atleta

    async def update(self, atleta_id: UUID, atleta_in: AtletaIn) -> Optional[Atleta]:
        atleta = await self.get_by_id(atleta_id)
        if not atleta:
            return None
        for key, value in atleta_in.dict().items():
            setattr(atleta, key, value)
        self.session.add(atleta)
        await self.session.commit()
        await self.session.refresh(atleta)
        return atleta

    async def delete(self, atleta_id: UUID) -> bool:
        atleta = await self.get_by_id(atleta_id)
        if not atleta:
            return False
        await self.session.delete(atleta)
        await self.session.commit()
        return True

