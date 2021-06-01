"""Server for food expiration app"""

from flask import (Flask, render_template, request, flash, session, redirect)
from jinja2.runtime import StrictUndefined
from model import connect_to_db
import crud
import jinja2


app = Flask(__name__)
app.secret_key = "dev"
# app.jinja_env.undefined = StrictUndefined





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug = True)