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
def homepage():
    """View homepage"""

    return render_template("homepage.html")

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


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        user_pass = crud.get_user_password(password)
        if user_pass:
            flash("Logged In!")

            return redirect("/")
        else:
            flash("Your password does not match. Please reenter your email and password.")

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug = True)