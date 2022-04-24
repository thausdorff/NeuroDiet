
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import ARRAY

Base = declarative_base()
# global engine, Session, session
path = "sqlite://///C:/Users/thaus/Google Drive/Extras/Neurodegenerative Diets/data.db"
engine = create_engine(path)
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    first = Column(String)
    last = Column(String)
    age = Column(Integer)
    gender = Column(Integer)
    diagnosis = Column(Integer, ForeignKey('diseases.id'))

class Diets(Base):
    __tablename__ = "diets"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    item = relationship("Item", back_populates='diets')

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    good_for_diet = relationship(ARRAY(Integer), ForeignKey=("diets.id"))
    bad_for_diet = relationship(ARRAY(Integer), ForeignKey=("diets.id"))

class Diseases(Base):
    __tablename__ = "diseases"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    good = relationship(ARRAY(Integer), ForeignKey=("diets.id"))
    bad = relationship(ARRAY(Integer), ForeignKey=("diets.id"))
    user = relationship("User", back_populates='diseases')


def create_diets():
    diets = ["Ketogenic", "Mediterranean", "Vegan", "MIND", "Volumetrics", "Paleo"]
    for diet in diets:
        session.add(Diets(name=diet))
    session.commit()

def add_test_food():
    foods = [("Red Meat", [], ["Mediterranean", "MIND", "Vegan"]), ("Fish", ["Mediterranean"], ["Vegan"])]
    for food in foods:
        item = Item(name= food[0], good_for_diet= food[1], bad_for_diet= food[2])
        session.add(item)
    session.commit()

create_diets()
add_test_food()
session.close()
