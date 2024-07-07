from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

DATABASE_URL = "postgresql+asyncpg://username:password@localhost:5432/clicker_db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

def get_db():
    db = async_session()
    try:
        yield db
    finally:
        db.close()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    tokens = Column(Integer, default=0)
    mining_speed = Column(Integer, default=1)
    auto_mining = Column(Integer, default=0)
    knowledge_points = Column(Integer, default=0)
    energy = Column(Integer, default=100)
    energy_recovery_speed = Column(Integer, default=1)
