import datetime
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import crud
from model import User_food

# os.system("source secrets.sh")
# API_KEY = os.environ['API_KEY']
# send_email = os.environ['send_email']

def send_email(user_email, food_name):
    message = Mail(
        from_email=send_email,
        to_emails=user_email,
        subject="Time to toss the {food_name}",
        html_content="<strong>and easy to do anywhere, even in Python</strong>")
    try:
        sg = SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

def job():
    user_food = User_food.query.all()
    exp_date = user_food.end_date
    user_id = user_food.user_id
    food_id = user_food.food_id
    food_name = crud.get_food_by_name(food_id)
    user_info = crud.get_user_by_id(user_id)
    user_email = user_info.email
    print("*"*20)
    print(user_email)
    print("*"*20)
    # Get expiration dates from db
    # find user attached to exp_date
    # Get food name
    # If exp_date = date_now:
    #   send email