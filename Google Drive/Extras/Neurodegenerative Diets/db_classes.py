from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    first = Column(String)
    last = Column(String)
    diagnosis = relationship('Diseases')

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    family = Column(String)

class Diseases(Base):
    __tablename__ = "diseases"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    good = Column(String)
    bad = Column(String)