"""Script to seed database."""

import os
import json
import crud
from  model import db, connect_to_db, Location, User, Food
from server import app
from random import randint


os.system('dropdb food_exp')
os.system('createdb food_exp')

connect_to_db(app)
db.create_all()


# Set the location

refrigerator = Location(loc_name = "refrigerator")
freezer = Location(loc_name = "freezer")
pantry = Location(loc_name = "pantry")

db.session.add(refrigerator)
db.session.add(freezer)
db.session.add(pantry)

db.session.commit()

for n in range(10):
    email = f"user{n}@test.com"
    password = "test"
    phone = None
    pref_contact = "email"

    new_user = crud.create_user(email, password, pref_contact, phone)

    for a in range(10):
        food_name = f"food{a}"
        shelf_life = 5
        loc_id = randint(1, 3)

        new_food = crud.create_food(food_name, shelf_life, loc_id)

        crud.create_user_foods(new_user.user_id, new_food.food_id)