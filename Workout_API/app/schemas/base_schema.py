# app/schemas/base_schema.py
from pydantic import BaseModel

class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
