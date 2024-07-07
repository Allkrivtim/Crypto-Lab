import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, text

DATABASE_URL = "postgresql+asyncpg://myuser:mypassword@localhost:5432/clicker_db"

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    tokens = Column(Integer, default=0)
    mining_speed = Column(Integer, default=1)  # Скорость добычи
    auto_mining = Column(Integer, default=0)  # Авто добыча
    knowledge_points = Column(Integer, default=0)  # Очки знаний
    energy = Column(Integer, default=100)  # Количество энергии
    energy_recovery_speed = Column(Integer, default=1)  # Скорость восстановления энергии

async def add_columns():
    engine = create_async_engine(DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.execute(
            text("ALTER TABLE users ADD COLUMN IF NOT EXISTS mining_speed INTEGER DEFAULT 1")
        )
        await conn.execute(
            text("ALTER TABLE users ADD COLUMN IF NOT EXISTS auto_mining INTEGER DEFAULT 0")
        )
        await conn.execute(
            text("ALTER TABLE users ADD COLUMN IF NOT EXISTS knowledge_points INTEGER DEFAULT 0")
        )
        await conn.execute(
            text("ALTER TABLE users ADD COLUMN IF NOT EXISTS energy INTEGER DEFAULT 100")
        )
        await conn.execute(
            text("ALTER TABLE users ADD COLUMN IF NOT EXISTS energy_recovery_speed INTEGER DEFAULT 1")
        )

asyncio.run(add_columns())
