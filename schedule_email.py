import datetime
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

os.system("source secrets.sh")
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

def job():
    # Get expiration dates from db
    # find user attached to exp_date
    # Get food name
    # If exp_date = date_now:
    #   send email