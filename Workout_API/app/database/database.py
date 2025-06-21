from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/workout"

# Cria engine async
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory async
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Base para os models
Base = declarative_base()

# Dependency para pegar session async no FastAPI
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

