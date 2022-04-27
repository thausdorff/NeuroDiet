import pandas as pd
from db_classes import *

path = "sqlite:///C:/Users/thaus/Google Drive/Extras/Neurodegenerative Diets/neuroDiet.db"
engine = create_engine(path)
Session = sessionmaker(bind=engine)
session = Session()

def fill_items(folder: str):
    file = f'{folder}/food.csv'
    dataFrame = pd.read_csv(file, header=0)
    print(dataFrame.columns)
    dataFrame = dataFrame.drop(['data_type', 'food_category_id', 'publication_date'], axis=1)
    all_items = []
    for index, row in dataFrame.iterrows():
        item = Item(fdc_id= row[0], name= row[1])
        all_items.append(item)
    session.add_all(all_items)
    session.commit()

def fill_nutritions(folder: str):
    pass

def fill_nutritional_values(folder: str):
    pass

def main():
    folder_location_path = "C:/Users/thaus/Google Drive/Extras/Neurodegenerative Diets/FoodData"
    fill_items(folder_location_path)
    fill_nutritions(folder_location_path)
    fill_nutritional_values(folder_location_path)

if __name__ == "__main__":
    main()