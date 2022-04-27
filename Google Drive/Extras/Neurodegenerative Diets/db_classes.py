
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
    rating = relationship("DietFood", back_populates= "diet") 

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer)
    name = Column(String)
    rating = relationship("DietFood", back_populates= "item")
    nutritional_value = relationship("FoodNutrition", back_populates="item")


class Nutrition(Base):
    __tablename__ = "nutrition"
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    unit = Column(String)
    nutritional_value = relationship("FoodNutrition", back_populates ="nutrition")


class FoodNutrition(Base):
    __tablename__ = "food_nutrition"
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer, ForeignKey('item.fdc_id'))
    item = relationship("Item", back_populates= "nutritional_value")
    nutrition_id = Column(Integer, ForeignKey('nutrition.id'))
    nutrition = relationship("Nutrition", back_populates= "nutritional_value")


class DietFood(Base):
    __tablename__ = "diet_foods"
    id = Column(Integer, primary_key = True)
    diet_id = Column(Integer, ForeignKey("diets.id"))
    diet = relationship("Diets", back_populates= "rating")
    item_id = Column(Integer, ForeignKey("item.id"))
    item = relationship("Item", back_populates= "rating")
    good = Column(Boolean, nullable = False)

class Diseases(Base):
    __tablename__ = "diseases"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    good = Column(Integer, ForeignKey("diets.id"))
    bad = Column(Integer, ForeignKey("diets.id"))
    user = relationship("User")


# def create_diets():
#     diets = ["Ketogenic", "Mediterranean", "Vegan", "MIND", "Volumetrics", "Paleo"]
#     for d in diets:
#         diet = Diets(name=d)
#         session.add(diet)
#     session.commit()

# def add_test_food():
#     foods = ["Red Meat", "Fish", "Tomato", "Green Apple", "Chicken", "Nuts"]
#     for food in foods:
#         session.add(Item(name=food))
#     session.commit()

# def add_rating():
#     foods = ["Red Meat", "Fish", "Tomato", "Green Apple", "Chicken", "Nuts"]
#     for food in foods:
#         item = session.query(Item).filter(Item.name == food).first()
#         diet = session.query(Diets).filter(Diets.name == diet).first()
#         session.add(Rating(diet_id = diet.id, item_id = item.id, good = False))
#     session.commit()

Base.metadata.create_all(engine)
session.commit()
# create_diets()
# add_test_food()
session.close()
