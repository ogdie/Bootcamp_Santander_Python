from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List
from uuid import uuid4
from datetime import datetime, timezone

from app.schemas.product import ProductIn, ProductOut, ProductUpdate
from app.models.product_model import ProductModel
from app.core.config import settings

app = FastAPI()

# CORS (caso queira acessar via frontend local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Você pode restringir para "http://localhost:3000" por exemplo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexão com MongoDB
@app.on_event("startup")
async def startup_db():
    app.mongodb_client = AsyncIOMotorClient(settings.MONGODB_URI)
    app.database = app.mongodb_client[settings.DATABASE_NAME]
    app.products_collection = app.database["products"]

@app.on_event("shutdown")
async def shutdown_db():
    app.mongodb_client.close()

# POST - Criar Produto
@app.post("/products", response_model=ProductOut, status_code=201)
async def create_product(product: ProductIn):
    now = datetime.now(timezone.utc)
    product_dict = product.model_dump()
    product_dict.update({
        "_id": str(uuid4()),
        "created_at": now,
        "updated_at": now
    })
    await app.products_collection.insert_one(product_dict)
    return ProductModel(**product_dict)

# GET - Listar Produtos
@app.get("/products", response_model=List[ProductOut])
async def list_products():
    products_cursor = app.products_collection.find()
    products = []
    async for product in products_cursor:
        products.append(ProductModel(**product))
    return products

# GET - Obter Produto por ID
@app.get("/products/{product_id}", response_model=ProductOut)
async def get_product(product_id: str):
    product = await app.products_collection.find_one({"_id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return ProductModel(**product)

# PUT - Atualizar Produto
@app.put("/products/{product_id}", response_model=ProductOut)
async def update_product(product_id: str, product_update: ProductUpdate):
    update_data = {k: v for k, v in product_update.model_dump(exclude_unset=True).items()}
    update_data["updated_at"] = datetime.now(timezone.utc)

    result = await app.products_collection.find_one_and_update(
        {"_id": product_id},
        {"$set": update_data},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return ProductModel(**result)

# DELETE - Deletar Produto
@app.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: str):
    result = await app.products_collection.delete_one({"_id": product_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
