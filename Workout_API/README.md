
# WorkoutAPI

API para gerenciamento de competições de Crossfit, construída com FastAPI, SQLAlchemy, PostgreSQL e Docker.

---

## Tecnologias

- Python 3.11+
- FastAPI (async)
- SQLAlchemy (ORM)
- Alembic (migrations)
- Pydantic (validação e schemas)
- PostgreSQL (banco de dados)
- Docker e Docker Compose (para banco)

---

## Funcionalidades

- CRUD para Atletas, Categorias e Centros de Treinamento
- Validação de dados com Pydantic
- Migrations e controle do banco com Alembic
- API Documentada com Swagger UI (disponível em `/docs`)
- Suporte a async para alta performance

---

## Como rodar

### Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.11+ (para rodar local sem container)

### Passos para rodar com Docker

1. Suba o container do banco com:

```bash
docker-compose up -d
```

2. Crie as migrations e aplique no banco:

```bash
make create-migrations d="initial"
make run-migrations
```

3. Rode a API localmente:

```bash
uvicorn app.main:app --reload
```

4. Acesse a documentação em:

```
http://127.0.0.1:8000/docs
```

---

## Como rodar sem Docker

1. Configure o PostgreSQL localmente com as credenciais no arquivo `.env` (se houver)
2. Ative seu ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode as migrations e a aplicação local:

```bash
alembic upgrade head
uvicorn app.main:app --reload
```

---

## Endpoints principais

- `/categoria` - CRUD categorias
- `/centro_treinamento` - CRUD centros de treinamento
- `/atleta` - CRUD atletas

Consulte a documentação Swagger para detalhes e testes.

---

## Desafios futuros / melhorias

- Paginação dos resultados (ex: fastapi-pagination)
- Tratamento customizado para erros de integridade (ex: CPF duplicado)
- Filtros por query params (ex: buscar atleta por nome ou CPF)
- Autenticação e autorização

---

## Autor

Diego Menezes Monteiro
