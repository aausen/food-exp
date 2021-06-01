"""Model for food exp app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    email = db.Column(db.String(30), 
                      unique = True)
    password = db.Column(db.String(15))
    phone = db.Column(db.Integer(11),
                      nullable = True)
    pref_contact = db.Column(db.String(5))

    def __repr__(self):
        return f"<User user_id = {self.user_id} email = {self.email}>"


class Food(db.Model):
    """Food user adds to profile"""

    __tablename__ = "food"

    food_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    food_name = db.Column(db.String(30))
    shelf_life = db.Column(db.Integer)
    loc_id = db.Column(db.Integer, 
                       db.ForeignKey("location.loc_id"),
                       nullable = False)

    def __repr__(self):
        return f"<Food food_id = {self.food_id} food_name = {self.food_name} loc_id = {self.loc_id}>"


class Location(db.Model):
    """Location of food."""

    __tablename__ = "location"

    loc_id = db.Column(db.Integer,
                       autoincrement = True,
                       primary_key = True)
    loc_name = db.Column(db.String(12))

    def __repr__(self):
        return f"<Location loc_id = {self.loc_id} loc_name = {self.loc_name}>"


class User_food(db.Model):
    """Association table between users and food"""

    __tablename__ = "user_food"

    user_food_id = db.Column(db.Integer,
                             autorincrement = True,
                             primary_key = True)
    food_id = db.Column(db.Integer,
                        db.ForeignKey('Food.food_id'),
                        nullable = False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('User.user_id'),
                        nullable = False)

    def __repr__(self):
        return f"<User_food user_food_id = {self.user_food_id} food_id = {self.food_id} user_id = {self.user_id}>"