from flask import abort, flash, session, redirect, request, render_template
from models import Location
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
                locat = Location(title=int(row[1]), code=row[0])
                db.session.add(locat)
        db.session.commit()

    csv_path = "meetup_locations.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)
    return "Filled"