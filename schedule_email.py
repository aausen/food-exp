"""Schedule and send user emails."""

from flask import Flask, request, session
import datetime
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import crud
from model import User_food, connect_to_db
import schedule
import time

# os.system("source secrets.sh")
API_KEY = os.environ['API_KEY']
sent_email = os.environ['sent_email']

def send_email(user_email, food_name):
    """Send email to user that food is expired."""

    user = crud.get_user_by_email(user_email)
    user_name = user.user_name

    message = Mail(
        from_email=sent_email,
        to_emails=user_email,
        subject=f"Time to the {food_name}",
        html_content=f"Hi {user_name}, Your {food_name} has gone bad. It is time to toss it!  Thanks for being a part of Toss It!")
    try:
        sg = SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(f"the email didn't send")

def get_user_info():
    """Get the user information to use for the email."""

    # Get information from the db
    user_food = User_food.query.all()
    # Create a list to store the user sets
    user_food_lst = []
    # Loop through the results to get the exp
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
    """Send the email when the expiration time has elapsed."""

    # Get user information from get_user_info function.
    user_food_lst = get_user_info()
    # Loop through results
    for item in user_food_lst:
        # Get expiration date (datetime object)
        exp_date_datetime = item[0]
        exp_date = exp_date_datetime.strftime("%m %d %Y %H %M")
        print("*"*20)
        print(item[2], exp_date)
        print("*"*20)
        # Create new datetime object
        now_datetime = datetime.datetime.now()
        now = now_datetime.strftime("%m %d %Y %H %M")
        print("!"*20)
        print(item[2], now)
        print("!"*20)
        # Compare datetime objects, send email if the current date is the expiration date
        if exp_date == now:
            send_email(item[1], item[2])
# def job():
#     print("I'm working")

# Schedule every hour to check if exp_date has elapsed.
schedule.every().minutes.do(job)
        
    # Get expiration dates from db
    # find user attached to exp_date
    # Get food name
    # If exp_date = date_now:
    #   send email

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    schedule.run_continuously()