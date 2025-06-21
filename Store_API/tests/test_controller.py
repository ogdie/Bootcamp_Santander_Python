import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_update_product():
    # Criar produto
    response = client.post("/products", json={
        "name": "Produto Teste",
        "description": "Descrição do teste",
        "price": 100.0,
        "in_stock": True
    })
    assert response.status_code == 201
    product = response.json()
    product_id = product["id"]

    # Atualizar produto
    update_response = client.put(f"/products/{product_id}", json={
        "name": "Produto Teste Atualizado",
        "price": 150.0
    })
    assert update_response.status_code == 200
    updated_product = update_response.json()
    assert updated_product["name"] == "Produto Teste Atualizado"
    assert updated_product["price"] == 150.0

    # Atualizar produto inexistente
    invalid_response = client.put("/products/invalid-id", json={
        "name": "Novo Nome"
    })
    assert invalid_response.status_code == 404


