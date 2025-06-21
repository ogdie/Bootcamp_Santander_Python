from typing import List, Optional
from app.crud.product_crud import ProductCRUD
from app.schemas.product import ProductIn, ProductUpdate
from app.models.product_model import ProductModel

class ProductService:
    def __init__(self, crud: ProductCRUD):
        self.crud = crud

    async def create_product(self, data: ProductIn) -> ProductModel:
        product_dict = data.model_dump()
        product = await self.crud.create(product_dict)
        return ProductModel(**product)

    async def list_products(self) -> List[ProductModel]:
        products = await self.crud.list()
        return [ProductModel(**p) for p in products]

    async def get_product(self, product_id: str) -> Optional[ProductModel]:
        product = await self.crud.get(product_id)
        if product:
            return ProductModel(**product)
        return None

    async def update_product(self, product_id: str, data: ProductUpdate) -> Optional[ProductModel]:
        update_dict = data.model_dump(exclude_unset=True)
        updated = await self.crud.update(product_id, update_dict)
        if updated:
            return ProductModel(**updated)
        return None

    async def delete_product(self, product_id: str) -> bool:
        return await self.crud.delete(product_id)
