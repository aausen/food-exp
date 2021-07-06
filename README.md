# Toss it!

Toss it is a web application that allows users to search and save foods they have in their home and will notify the user when it is no longer safe to eat. The user first searches for foods they have, then are prompted to select where they are keeping it. Using the ShelfLife API and Python’s datetime library, the shelf life for that particular food is calculated and stored in the PostgreSQL database. When the food expires, the date turns red on the homepage using Javascript’s date library and an email is sent to the user using Schedule and Twilio’s Sendgrid APIs. When the user logs in again, they are able to see all of their food and are then able to delete any that they have either finished or has gone bad.

# Tech Stack

Python, JavaScript, Flask, HTML, CSS, Jinja, Bootstrap, PostgreSQL, SQLAlchemy

# APIs Used

ShelfLife, Twilio Sendgrid, Schedule

# Features