from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://myuser:mypassword@localhost/clicker_db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()

async def init_db():
    async with engine.begin() as conn:
        # Здесь можно выполнять инициализацию базы данных, например создание таблиц
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
