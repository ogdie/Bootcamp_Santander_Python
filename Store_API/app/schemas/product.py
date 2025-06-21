from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductIn(BaseModel):
    name: str
    description: str
    price: float = Field(..., ge=0)
    in_stock: bool

class ProductOut(ProductIn):
    id: str
    created_at: datetime
    updated_at: datetime

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(None, ge=0)
    in_stock: Optional[bool] = None

