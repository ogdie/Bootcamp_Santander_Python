from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ProductModel(BaseModel):
    id: str
    name: str
    description: Optional[str]
    price: float
    in_stock: bool
    created_at: datetime
    updated_at: datetime

