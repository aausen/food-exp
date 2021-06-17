"""Server for food expiration app"""

from flask import Flask, render_template, request, flash, session, redirect, jsonify, g
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from jinja2.runtime import StrictUndefined
from model import connect_to_db, User, Location, User_food
import crud
from jinja2 import StrictUndefined
import requests





app = Flask(__name__)
app.secret_key = "dev" #add to secrets.sh
app.jinja_env.undefined = StrictUndefined
JS_TESTING_MODE = False

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    
    return User.query.get(user_id)

@app.before_request
def add_tests():
    g.jasmine_tests = JS_TESTING_MODE

@app.route('/')
def show_homepage():
    """View homepage"""
    if current_user.is_authenticated:
        user_id = current_user.get_id()

        # Returns a list of user_food objects for the user
        user_food = crud.get_user_food(user_id)
   
        food_by_user = []
        for item in user_food:
            # Get exp date from db
            exp = item.end_date
            # Make datetime obj a string
            str_exp = exp.strftime("%a %b %d %Y")
            # Get food_id from db
            food_id = item.food_id
            # Get user_food id
            user_food_id = item.user_food_id
            # Use food_id to get list of foods
            food_lst = crud.get_food_by_id(food_id)
            for food in food_lst:
                # Get food id
                food_id = food.food_id
                #Get food name
                food_name = food.food_name
                # Get location id
                loc_id = food.loc_id
                # Get name of the location based on id
                loc_name_obj = crud.get_loc_by_loc_id(loc_id)
                loc_name = loc_name_obj.loc_name
                # Add name, location, and exp date to list of user foods 
                food_by_user.append((food_id, food_name, loc_name, str_exp, user_food_id))

        return render_template("homepage.html",
                                food_by_user = food_by_user)
    
    else:
        return redirect("/login")


@app.route("/delete", methods=["POST"])
def delete():
    user_food_id = request.form.get("delete-food")

    crud.delete_food_from_db(user_food_id)

    return redirect('/')
  


#____________________________________Register_______________________________________#
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
        flash("A user already exists with that email. Please use a different email or login with current email.")

        return redirect('/register')
    else:
        crud.create_user(email, password, pref_contact, phone=None)
        flash("Account created! Please log in.")

        return redirect('/login')

#___________________________________Login___________________________________________#
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
    
    if user == None:
        flash("That is not a valid email. Please try again.")
        return redirect("/login")
    elif user.password == password:

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

#________________________________Search_______________________________________________#
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

@app.route("/add-item", methods=["GET"])
def add_item():
    """Gets and displays food information on add food page"""

    food_id = request.args.get("select-food")

    # Get the input from the user
    payload = food_id

    # Define the url
    url = "https://shelf-life-api.herokuapp.com/guides/"

    # Make the first request to the api to get the url
    res = requests.get(url, payload)
  
    # Split the url on the ? so the request can be sent properly
    lst = res.url.split("?")
    
    # Create the new url
    new_url = lst[0] + lst[1]

    # Send a get request for the food info
    res = requests.get(new_url)

    # Create a json object
    res = res.json()
    print("*"*20)
    print(res)
    print("*"*20)

    info = []
    name = res['name']
    methods = res['methods']
    for item in methods:
        location = item['location']
        exp = item['expiration']
        exp_time = item['expirationTime']
        food_set = (location, exp, exp_time)
        info.append(food_set)
    tips = res['tips']

    # JSONify the response to be used on another page
    # return jsonify(res)
    
    return render_template("add-item.html", 
                            name = name,
                            info = info,
                            tips = tips, 
                            food_id = food_id)

@app.route("/add-item", methods=["POST"])
def add_item_to_db():
    """Adds new food to user db"""

    # Get food info from radio button submit
    food_info = request.form.get("add-food")

    # Split the list of values at the ,
    lst = food_info.split(',')
    # Get the food_name
    food_name= lst[:-2]
    #make food_name into a string. It is a list right now
    str_food = ""
    for item in food_name:
        str_food = str_food + item
    # Get food_loc
    food_loc = lst[-2]

    # Get expiration time 
    exp_time = lst[-1]

    # Check if location exists
    loc = crud.get_loc_by_name(food_loc)
    if loc == None:
        new_loc = crud.create_location(food_loc)
        loc_id = new_loc.loc_id
    else: 
        loc_id = loc.loc_id

    # Check if food exists
    new_food = crud.get_food_by_name(str_food)
    if new_food == None:
        new_food = crud.create_food(str_food, exp_time, loc_id)
    # Get user_id
    user_id = current_user.get_id()
    # Get food_id from food table
    food_id = new_food.food_id
    # connect user to food
    user_food = crud.create_user_foods(user_id, food_id)


    return redirect('/')
   



if __name__ == '__main__':
    connect_to_db(app)

    import sys
    if sys.argv[-1] == "jstest":
        JS_TESTING_MODE = True

    app.run(host='0.0.0.0', debug = True)