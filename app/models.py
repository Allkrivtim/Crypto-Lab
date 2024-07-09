from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, index=True)
    tokens = Column(Integer, default=0)
