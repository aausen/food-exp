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

# Ended on Movie review pt 2 about halfway down where there's a blue box