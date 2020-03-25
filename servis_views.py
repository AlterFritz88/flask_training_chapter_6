from flask import abort, flash, session, redirect, request, render_template
from models import Location, Event
from app import app, db
import csv


@app.route("/locat")
def locat_add():
    def csv_reader(file_obj):
        reader = csv.reader(file_obj)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            else:
                print(row)
                locat = Location(title=row[1], code=row[0])
                db.session.add(locat)
        db.session.commit()

    csv_path = "meetup_locations.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)
    return "Filled"


@app.route("/events")
def events_add():
    def csv_reader(file_obj):
        reader = csv.reader(file_obj)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            else:
                print(row[6])
                location = db.session.query(Location).filter(Location.code == row[6].split(", ")[0]).first()
                event = Event(title=row[0], description=row[1], date=row[2], time=row[3], type=row[4], category=row[5],
                              location=location, location_id=location.id, seats=row[8], address=row[7])
                db.session.add(event)
        db.session.commit()

    csv_path = "meetup_events.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)
    return "Filled"

"""
title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)
    type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    location = relationship("Location", back_populates="events")
    location_id = Column(Integer, ForeignKey("locations.id"))
    seats = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    participants = relationship(
        "Participant", secondary=Enrollment, back_populates="events"
    )
"""