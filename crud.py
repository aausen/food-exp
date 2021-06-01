"""CRUD operations"""

from model import db, User, Food, Location, User_food, connect_to_db

def create_user(email, password, pref_contact, phone = "None"):
    """Create and return a new user"""
    user = User(email = email, password = password, phone = phone, pref_contact = pref_contact)

    db.session.add(user)
    db.session.commit()

    return user

def create_food()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)