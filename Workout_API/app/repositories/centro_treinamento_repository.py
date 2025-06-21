from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from uuid import UUID

from app.models.centro_treinamento_model import CentroTreinamento
from app.schemas.centro_treinamento_schema import CentroTreinamentoIn

class CentroTreinamentoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, centro_in: CentroTreinamentoIn) -> CentroTreinamento:
        novo_centro = CentroTreinamento(**centro_in.dict())
        self.session.add(novo_centro)
        await self.session.commit()
        await self.session.refresh(novo_centro)
        return novo_centro

    async def get_all(self) -> List[CentroTreinamento]:
        result = await self.session.execute("SELECT * FROM centro_treinamento")
        centros = result.scalars().all()
        return centros

    async def get_by_id(self, centro_id: UUID) -> Optional[CentroTreinamento]:
        centro = await self.session.get(CentroTreinamento, centro_id)
        return centro

    async def update(self, centro_id: UUID, centro_in: CentroTreinamentoIn) -> Optional[CentroTreinamento]:
        centro = await self.get_by_id(centro_id)
        if not centro:
            return None
        for key, value in centro_in.dict().items():
            setattr(centro, key, value)
        self.session.add(centro)
        await self.session.commit()
        await self.session.refresh(centro)
        return centro

    async def delete(self, centro_id: UUID) -> bool:
        centro = await self.get_by_id(centro_id)
        if not centro:
            return False
        await self.session.delete(centro)
        await self.session.commit()
        return True
