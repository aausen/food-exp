"""CRUD operations"""

from model import db, User, Food, Location, User_food, connect_to_db
from datetime import datetime, timedelta

def create_user(user_name, email, password, user_img):
    """Create and return a new user"""

    user = User(user_name = user_name,
                email = email, 
                password = password,
                user_img = user_img)

    db.session.add(user)
    db.session.commit()

    return user

def create_food(food_name, shelf_life, loc_id):
    """Create and return a new food"""

    food = Food(food_name = food_name, 
                shelf_life = shelf_life, 
                loc_id = loc_id)


    db.session.add(food)
    db.session.commit()

    return food


def create_location(loc_name):
    """Create and return a location"""

    location = Location(loc_name = loc_name)

    db.session.add(location)
    db.session.commit()

    return location

def create_user_foods(user_id, food_id):
    """Create and return new user_foods"""

    # Get shelf_life from api stored in db
    exp_date = Food.query.get(food_id).shelf_life
    # Create a start date
    start_date = datetime.now()
    # Create timedelta variable to use in datetime math
    delta = timedelta(seconds=exp_date)
    # Create end date for the food based on information before this
    end_date = start_date + delta
    user_food = User_food(user_id = user_id,
                          food_id = food_id,
                          start_date = start_date,
                          end_date = end_date)

    db.session.add(user_food)
    db.session.commit()

    return user_food

#_________________________User Query________________________#
def get_user_by_email(email):

    return User.query.filter(User.email == email).first()

def get_user_password(password):

    return User.query.filter(User.password == password).first()

def get_user_by_id(user_id):

    return User.query.filter(User.user_id == user_id).first()

#_________________________Location Query______________________#

def get_loc_by_name(food_loc):

    return Location.query.filter(Location.loc_name == food_loc).first()

def get_loc_by_loc_id(loc_id):

    return Location.query.filter(Location.loc_id == loc_id).first()

#__________________________Food Query ________________________#
def get_food_by_name(food_name):

    return Food.query.filter(Food.food_name == food_name).first()

def get_food_by_id(food_id):
    """Return food information by food_id"""

    return Food.query.filter(Food.food_id == food_id).all()

#_______________________User_food Query______________________#

def get_user_food(user_id):
    """Returns a list of user_food objects"""

    return User_food.query.filter(User_food.user_id == user_id).all()


def delete_food_from_db(user_food_id):
    print(user_food_id)
    del_food = User_food.query.filter(User_food.user_food_id == user_food_id).first()
    db.session.delete(del_food)
    db.session.commit()
    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)