from datetime import datetime, timezone
import pytest
from pydantic import ValidationError
from app.schemas.product import ProductOut, ProductIn

def test_productout_data():
    product = ProductOut(
        id="abc123",
        name="Notebook ABC",
        description="Notebook leve e potente",
        price=3999.99,
        in_stock=False,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )
    assert product.id == "abc123"
    assert product.name == "Notebook ABC"

def test_productin_invalid_price():
    with pytest.raises(ValidationError):
        ProductIn(
            name="Notebook",
            description="Notebook xyz",
            price=-100,  # preço inválido
            in_stock=True
        )

