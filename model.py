"""Model for food exp app"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    email = db.Column(db.String(30), 
                      unique = True)
    password = db.Column(db.String(15),
                         nullable = False)
    user_name = db.Column(db.String(20),
                          nullable = False)
    user_img = db.Column(db.String)
    phone = db.Column(db.Integer(),
                      nullable = True)
    pref_contact = db.Column(db.String(5))

    # user_foods = a list of foods the user has added

    def get_id(self):
        """Override UserMixin.get_id."""

        return str(self.user_id)

    def __repr__(self):
        return f"<User user_id = {self.user_id}, email = {self.email}>"


class Food(db.Model):
    """Food user adds to profile"""

    __tablename__ = "food"

    food_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    food_name = db.Column(db.String)
    shelf_life = db.Column(db.Integer)
    loc_id = db.Column(db.Integer, 
                       db.ForeignKey("location.loc_id"),
                       nullable = False)

    # user_foods = a list of foods the user has added

    def __repr__(self):
        return f"<Food food_id = {self.food_id}, food_name = {self.food_name}, loc_id = {self.loc_id}>"


class Location(db.Model):
    """Location of food."""

    __tablename__ = "location"

    loc_id = db.Column(db.Integer,
                       autoincrement = True,
                       primary_key = True)
    loc_name = db.Column(db.String)

    def __repr__(self):
        return f"<Location loc_id = {self.loc_id}, loc_name = {self.loc_name}>"


class User_food(db.Model):
    """Association table between users and food"""

    __tablename__ = "user_foods"

    user_food_id = db.Column(db.Integer,
                             autoincrement = True,
                             primary_key = True)
    food_id = db.Column(db.Integer,
                        db.ForeignKey('food.food_id'),
                        nullable = False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable = False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    user = db.relationship("User", backref = "user_foods")
    food = db.relationship("Food", backref = "user_foods")

    def __repr__(self):
        return f"<User_food user_food_id = {self.user_food_id}, food_id = {self.food_id}, user_id = {self.user_id}>"


def connect_to_db(flask_app, db_uri='postgresql:///food_exp', echo = True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")



if __name__ == '__main__':
    from server import app

    connect_to_db(app)