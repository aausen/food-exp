"""CRUD operations"""

from model import db, User, Food, Location, User_food, connect_to_db

def create_user(email, password, pref_contact, phone = None):
    """Create and return a new user"""

    user = User(email = email, 
                password = password, 
                phone = phone, 
                pref_contact = pref_contact)

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

    user_food = User_food(user_id = user_id,
                          food_id = food_id)

    db.session.add(user_food)
    db.session.commit()

    return user_food

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()

def get_user_password(password):

    return User.query.filter(User.password == password).first()

def get_loc_by_name(food_loc):

    return Location.query.filter(Location.loc_name == food_loc).first()

def get_food_by_name(food_name):

    return Food.query.filter(Food.food_name == food_name).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)