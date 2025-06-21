# Store API com FastAPI e MongoDB

---

## Descrição

Este projeto é uma API RESTful para gerenciamento de produtos, desenvolvida com **FastAPI** e **MongoDB**. Permite operações CRUD (Criar, Ler, Atualizar, Deletar) para produtos, utilizando **Pydantic** para validação e **Motor** para acesso assíncrono ao banco de dados.

---

## Tecnologias

* Python 3.10+
* FastAPI
* Motor
* Pydantic
* MongoDB
* Uvicorn

---

## Funcionalidades

* Criar produto (`POST /products`)
* Listar todos os produtos (`GET /products`)
* Obter produto por ID (`GET /products/{product_id}`)
* Atualizar produto (`PUT /products/{product_id}`)
* Deletar produto (`DELETE /products/{product_id}`)

---

## Como rodar
Execute o servidor FastAPI:

```bash
uvicorn app.main:app --reload
A API estará disponível em: http://localhost:8000


Projeto realizado para o Bootcamp Santander Python Backend, por:
Diego Menezes Monteiro

