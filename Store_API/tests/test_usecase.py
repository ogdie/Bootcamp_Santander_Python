import pytest
from app.usecases.product_usecase import create_product, ProductCreationError
from app.schemas.product import ProductIn

def test_create_product_success():
    data = {
        "name": "Notebook Gamer",
        "description": "Notebook com RTX 4060",
        "price": 7999.99,
        "in_stock": True
    }
    product = create_product(data)
    assert isinstance(product, ProductIn)
    assert product.name == "Notebook Gamer"
    assert product.price == 7999.99

def test_create_product_failure():
    data = {
        "name": "Notebook Ultra",
        "description": "Notebook ultra caro",
        "price": 15000,  # preço muito alto que vai falhar
        "in_stock": True
    }
    with pytest.raises(ProductCreationError):
        create_product(data)

