# Toss it!

Toss it is a web application that allows users to search and save foods they have in their home and will notify the user when it is no longer safe to eat. The user first searches for foods they have, then are prompted to select where they are keeping it. Using the ShelfLife API and Python’s datetime library, the shelf life for that particular food is calculated and stored in the PostgreSQL database. When the food expires, the date turns red on the homepage using Javascript’s date library and an email is sent to the user using Schedule and Twilio’s Sendgrid APIs. When the user logs in again, they are able to see all of their food and are then able to delete any that they have either finished or has gone bad.

# Tech Stack

Python, JavaScript, Flask, HTML, CSS, Jinja, Bootstrap, PostgreSQL, SQLAlchemy

# APIs Used

ShelfLife, Twilio Sendgrid, Schedule

# Features

## Create an Account to Begin
Users create an account to join the platform. 


![](https://media.giphy.com/media/e2YE7ILFscoBa8X5zs/giphy.gif)

## Search for Foods 
Users can search for foods they have in their home and select where they are keeping them.
The shelf life is computed for them and will display on the homepage. 


![](https://media.giphy.com/media/VNMiXJeboWhgPzfBkV/giphy.gif)

## Notifications
When the expiration date arrives the date on the user's homepage will turn red and an email will be sent to 
the user's email they signed up with. 

![](static/img/turn-red.png)

## Filter
Users can select which location they want to view their food in and can toggle between them. 

![](https://media.giphy.com/media/yCt0x8sdI85KOAOngi/giphy.gif)