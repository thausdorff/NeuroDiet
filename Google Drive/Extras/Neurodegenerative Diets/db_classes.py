from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    first = Column(String)
    last = Column(String)
    

