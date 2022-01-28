from models.event import Event
import datetime
# self, date, name_of_event, number_of_guests, room_location,description

event1= Event(datetime.date(2022,2,1),"Party", 4, "Space", "smiles and laughter")
event2= Event(datetime.date(2022,3,1),"Peeeeerty", 3, "Rome", "Wine and stuff")


events =[event1, event2]

def add_new_event(event):
    events.append(event)