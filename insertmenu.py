from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

menu_file = open('menu_list.txt')
menu = [x.strip() for x in menu_file.readlines()]

restaurant = Restaurant(name="Urban Burguer")
session.add(restaurant)

for row in menu:
    row = row.strip().split(',')
    item = MenuItem(name=row[0], description=row[1], price=row[2],
        course=row[3], restaurant=restaurant)
    session.add(item)

session.commit()
