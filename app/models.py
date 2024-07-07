from sqlalchemy import Column, Integer
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    tokens = Column(Integer, default=0)
    production_speed = Column(Integer, default=1)  # Скорость добычи
    auto_production = Column(Integer, default=0)  # Авто добыча
    knowledge_points = Column(Integer, default=0)  # Очки знаний
    energy = Column(Integer, default=0)  # Количество энергии
    energy_recovery_speed = Column(Integer, default=0)  # Скорость восстановления энергии
