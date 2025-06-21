from typing import List, Optional
from app.schemas.product import ProductIn, ProductOut, ProductUpdate
from app.crud.product_crud import create_product as crud_create_product, list_products as crud_list_products, get_product as crud_get_product, update_product as crud_update_product, delete_product

class ProductCreationError(Exception):
    pass

def create_product(data: dict) -> ProductOut:
    # Validar dados se quiser (pode lançar ProductCreationError)
    product_model = crud_create_product(data)
    return ProductOut.model_validate(product_model)

def list_products() -> List[ProductOut]:
    products = crud_list_products()
    return [ProductOut.model_validate(p) for p in products]

def get_product(product_id: str) -> Optional[ProductOut]:
    product = crud_get_product(product_id)
    if not product:
        return None
    return ProductOut.model_validate(product)

def update_product(product_id: str, data: dict) -> Optional[ProductOut]:
    updated = crud_update_product(product_id, data)
    if not updated:
        return None
    return ProductOut.model_validate(updated)

def delete_product_usecase(product_id: str) -> bool:
    return delete_product(product_id)