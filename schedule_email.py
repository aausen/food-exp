from flask import Flask, request, session
import datetime
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import crud
from model import User_food, connect_to_db

# os.system("source secrets.sh")
API_KEY = os.environ['API_KEY']
send_email = os.environ['send_email']

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

def get_user_info():
    user_food = User_food.query.all()
    user_food_lst = []
    for item in user_food:
        exp_date = item.end_date
        user_id = item.user_id
        food_id = item.food_id
        food_obj_lst = crud.get_food_by_id(food_id)
        for food_obj in food_obj_lst:
            food_name = food_obj.food_name
        user_info = crud.get_user_by_id(user_id)
        user_email = user_info.email
        user_set = (exp_date, user_email, food_name)
        user_food_lst.append(user_set)

    return user_food_lst


def job():

    for item in user_food_lst:
        exp_date = item[0]
        print("*"*20)
        print(exp_date)
        print("*"*20)
        
    # Get expiration dates from db
    # find user attached to exp_date
    # Get food name
    # If exp_date = date_now:
    #   send email

if __name__ == '__main__':
    from server import app
    connect_to_db(app)