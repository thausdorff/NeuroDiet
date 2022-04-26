
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import ARRAY

Base = declarative_base()
# global engine, Session, session
path = "sqlite:///C:/Users/thaus/Google Drive/Extras/Neurodegenerative Diets/neuroDiet.db"
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
    # item = relationship("Item", back_populates='diets')

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    good_for_diet_ids = Column(Integer, ForeignKey("diets.id"))
    bad_for_diet_ids = Column(Integer, ForeignKey("diets.id"))

    good_for_diet = relationship("Diets", foreign_keys=[good_for_diet_ids])
    bad_for_diet = relationship("Diets", foreign_keys=[bad_for_diet_ids])

class Diseases(Base):
    __tablename__ = "diseases"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    good = Column(Integer, ForeignKey("diets.id"))
    bad = Column(Integer, ForeignKey("diets.id"))
    user = relationship("User")


def create_diets():
    diets = ["Ketogenic", "Mediterranean", "Vegan", "MIND", "Volumetrics", "Paleo"]
    for d in diets:
        diet = Diets(name=d)
        session.add(diet)
    session.commit()

def add_test_food():
    foods = ["Red Meat, "Mediterranean", "MIND", "Vegan"]), ("Fish", ["Mediterranean"], ["Vegan"])]
    for food in foods:
        item = Item(name= food[0], good_for_diet= food[1], bad_for_diet= food[2])
        session.add(item)
    session.commit()

Base.metadata.create_all(engine)
session.commit()
create_diets()
add_test_food()
session.close()
