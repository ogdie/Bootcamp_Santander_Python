from typing import List, Optional
from datetime import datetime
from app.models.product_model import ProductModel
import uuid

# Usando uma lista como "banco de dados" fake
db: List[ProductModel] = []

def create_product(data: dict) -> ProductModel:
    new_product = ProductModel(
        id=str(uuid.uuid4()),
        name=data["name"],
        description=data.get("description"),
        price=data["price"],
        in_stock=data["in_stock"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.append(new_product)
    return new_product

def list_products() -> List[ProductModel]:
    return db

def get_product(product_id: str) -> Optional[ProductModel]:
    for product in db:
        if product.id == product_id:
            return product
    return None

def update_product(product_id: str, data: dict) -> Optional[ProductModel]:
    product = get_product(product_id)
    if not product:
        return None
    if "name" in data:
        product.name = data["name"]
    if "description" in data:
        product.description = data["description"]
    if "price" in data:
        product.price = data["price"]
    if "in_stock" in data:
        product.in_stock = data["in_stock"]
    product.updated_at = datetime.now()
    return product

def delete_product(product_id: str) -> bool:
    global db
    for i, product in enumerate(db):
        if product.id == product_id:
            del db[i]
            return True
    return False
