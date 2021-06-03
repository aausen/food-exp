"""Server for food expiration app"""

from flask import (Flask, render_template, request, flash, session, redirect)
from jinja2.runtime import StrictUndefined
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def show_homepage():
    """View homepage"""
    if "user_email" in session:
        return render_template("homepage.html")
    
    else:
        return redirect("/login")

@app.route('/users', methods=["POST"])
def register_user():
    """Create a new user"""

    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if user:
        flash("A user already exists with that email. Please use a different email.")
    else:
        crud.create_user(email, password)
        flash("Account created! Please log in.")

        return redirect('login.html')

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
    if not user or user.password != password:
        flash("The email or password you entered are incorrect.")
    
    else:
        #Log in user by storing user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back {user.email}!")

    # if user:
    #     user_pass = crud.get_user_password(password)
    #     if user_pass:
    #         flash("Logged In!")

    #         session["user"] = user

    #         return redirect("/")
    #     else:
    #         flash("Your password does not match. Please reenter your email and password.")

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug = True)