import pandas as pd
from db_classes import *

path = "sqlite:///C:/Users/thaus/Google Drive/Extras/Neurodegenerative Diets/neuroDiet.db"
engine = create_engine(path)
Session = sessionmaker(bind=engine)
session = Session()

def fill_items(folder: str):
    file = f'{folder}/food.csv'
    dataFrame = pd.read_csv(file, header=0)
    dataFrame = dataFrame.drop(['data_type', 'food_category_id', 'publication_date'], axis=1)
    all_items = []
    for index, row in dataFrame.iterrows():
        item = Item(id= row[0], name= row[1])
        all_items.append(item)
    session.add_all(all_items)
    session.commit()

def fill_nutrients(folder: str):
    file = f'{folder}/nutrient.csv'
    dataFrame = pd.read_csv(file, header=0)
    dataFrame = dataFrame.drop(['nutrient_nbr', 'rank'], axis=1)
    all_nutrients = []
    for index, row in dataFrame.iterrows():
        nutrient = Nutrient(id= row[0], name= row[1], unit= row[2])
        all_nutrients.append(nutrient)
    session.add_all(all_nutrients)
    session.commit()



def fill_nutritional_values(folder: str):
    file = f'{folder}/food_nutrient.csv'
    dataFrame = pd.read_csv(file, header=0)
    dataFrame = dataFrame.drop(['id'], axis=1)
    all_values = []
    for index, row in dataFrame.iterrows():
        value = FoodNutrition(item_id= row[0], nutrient_id= row[1], amount= row[2])
        all_values.append(value)
    session.add_all(all_values)
    session.commit()

def main():
    create_db()
    folder_location_path = "C:/Users/thaus/Google Drive/Extras/Neurodegenerative Diets/FoodData"
    fill_items(folder_location_path)
    fill_nutrients(folder_location_path)
    fill_nutritional_values(folder_location_path)

if __name__ == "__main__":
    main()