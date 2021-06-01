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
                      unquie = True)
    password = db.Column(db.String(15))
    phone = db.Column(db.Integer(11),
                      nullable = True)
    pref_contact = db.Column(db.String(5))

    def __repr__(self):
        return f"<User user_id = {self.user_id} email = {self.email}>"