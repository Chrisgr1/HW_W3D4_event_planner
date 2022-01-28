from flask import render_template, request
from app import app
from models.event import Event
from models.events import events, add_new_event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=["POST"])
def add_event():
    event_date = request.form.get("date")
    event_name = request.form["name_of_event"]
    event_number_of_guests = request.form["number_of_guests"]
    event_room_location =request.form["room_location"]
    event_description = request.form["description"]
    new_event = Event(event_date, event_name, event_number_of_guests, event_room_location, event_description)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)