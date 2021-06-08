"""Server for food expiration app"""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from jinja2.runtime import StrictUndefined
from model import connect_to_db, User
import crud
from jinja2 import StrictUndefined
import requests


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

@app.route('/register', methods=["GET"])
def register_form():
    """Show registration form."""

    return render_template('register.html')

@app.route('/register', methods=["POST"])
def register_process():
    """Create a new user"""

    email = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")
    pref_contact = request.form.get("pref-contact")
    user = crud.get_user_by_email(email)

    if user:
        flash("A user already exists with that email. Please use a different email.")

        return redirect('/register')
    else:
        crud.create_user(email, password, pref_contact, phone=None)
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

@app.route("/search")
def food_search():
    """Search the api for possible foods"""
    input_food = request.args.get("searchBar") 
    
    

    # Get the input from the user
    payload = input_food

    # Define the search url
    url = "https://shelf-life-api.herokuapp.com/search?q="

    # Get request to API
    res = requests.get(url, payload)

    # Defining a variable so we can take out the &
    lst = res.url.split('&')

    # Putting our pieces back together 
    new_url = lst[0] + lst[1]

    # New get request using the new_url
    res = requests.get(new_url)

    # JSONify the result to be used in next step
    res = res.json()
    
    #parse through the information that comes back from res
    food_choice = {}
    for item in res: 
        food_name = item["name"]
        food_id = item['id']
        food_choice[food_id] = food_name
   
    return render_template('search.html',
                            food_choice = food_choice)

    # res = requests.get('https://shelf-life-api.herokuapp.com/guides/18794')
    # print(res.json())

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug = True)