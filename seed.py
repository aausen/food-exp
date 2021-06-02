"""Script to seed database."""

import os
import json
import crud
import model
import server


os.system('dropdb food_exp')
os.system('createdb food_exp')

model.connect_to_db(server.app)
model.db.create_all()

# Set the location
Location = ((loc_id = 1, loc_name = "refrigerator"),
            (loc_id = 2, loc_name = "freezer"),
            (loc_id = 3, loc_name = "pantry"))