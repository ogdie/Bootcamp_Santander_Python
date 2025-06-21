import pytest
from httpx import AsyncClient
from app.main import app
import asyncio

@pytest.mark.asyncio
async def test_product_lifecycle():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create product
        response = await ac.post("/api/v1/products", json={
            "name": "Teste Prod",
            "description": "Desc teste",
            "price": 123.45,
            "in_stock": True
        })
        assert response.status_code == 201
        product = response.json()
        product_id = product["id"]

        # List products
        list_resp = await ac.get("/api/v1/products")
        assert list_resp.status_code == 200
        assert any(p["id"] == product_id for p in list_resp.json())

        # Get product
        get_resp = await ac.get(f"/api/v1/products/{product_id}")
        assert get_resp.status_code == 200
        assert get_resp.json()["name"] == "Teste Prod"

        # Update product
        update_resp = await ac.put(f"/api/v1/products/{product_id}", json={"price": 200})
        assert update_resp.status_code == 200
        assert update_resp.json()["price"] == 200

        # Delete product
        delete_resp = await ac.delete(f"/api/v1/products/{product_id}")
        assert delete_resp.status_code == 204

        # Confirm deletion
        get_after_delete = await ac.get(f"/api/v1/products/{product_id}")
        assert get_after_delete.status_code == 404
