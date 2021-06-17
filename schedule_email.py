import datetime
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

os.system("source secrets.sh")
API_KEY = os.environ['API_KEY']
send_email = os.environ['send_email']

def send_email():
    message = Mail(
        from_email=send_email,
        to_emails="devtest292@gmail.com",
        subject="New email",
        html_content="<strong>and easy to do anywhere, even in Python</strong>")
    try:
        sg = SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)