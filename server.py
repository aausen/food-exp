"""Server for food expiration app"""

from flask import (Flask, render_template, request, flash, session, redirect)
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from jinja2.runtime import StrictUndefined
from model import connect_to_db, User
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    
    return User.query.get(user_id)

@app.route('/')
def show_homepage():
    """View homepage"""
    if current_user.is_authenticated:
        return render_template("homepage.html")
    
    else:
        return redirect("/login")

@app.route('/users', method=["GET"])
def register_form():

    return render_template('register.html')

@app.route('/users', methods=["POST"])
def register_process():
    """Create a new user"""

    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if user:
        flash("A user already exists with that email. Please use a different email.")

        return redirect('/users')
    else:
        crud.create_user(email, password)
        flash("Account created! Please log in.")

        return redirect('/login')

@app.route("/login", methods=["GET"])
def login_form():
    """Show login form."""
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_process():
    """Process login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user.password == password:

        login_user(user)

        flash("Logged in successfully!")

        return redirect("/")
    
    else:
        flash("Sorry, try again.")
        return redirect("/login")

@app.route("/logout")
def logout():
    """Process logout."""

    logout_user()

    return redirect('/login')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug = True)