from app import app, db
from flask import abort, flash, session, redirect, request, render_template, url_for, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from models import Location, Event, Enrollment,Participant
from schemas import LocationSchema, EventSchema, ParticipantSchema


@app.route('/locations', methods=['GET'])
def locations():
    locats = LocationSchema(many=True)
    return jsonify(locats.dump(Location.query.all()))


@app.route('/events/', methods=['GET'])
def events():
    # /events?eventtype=meetup
    event = EventSchema(many=True)
    eventtype = request.args.get("eventtype")
    location = request.args.get("location")

    if eventtype:
        return jsonify(event.dump(db.session.query(Event).filter(Event.type == eventtype).all()))
    elif location:
        print(db.session.query(Event).all()[0].location.code)
        return jsonify(event.dump(db.session.query(Event).filter(Event.location.has(code=location)).all()))
    else:
        return jsonify(event.dump(Event.query.all()))


@app.route('/enrollments/<int:eventid>', methods=['POST', 'DELETE'])
@jwt_required
def enroll(eventid):
    current_seats = len(db.session.query(Enrollment).filter(Enrollment.event_id == eventid).all())
    print(get_jwt_identity())
    if current_seats < db.session.query(Event).filter(Event.id == eventid).first().seats:
        enroll = Enrollment(event_id=eventid)
        db.session.add(enroll)
        return {"status": "success"}
    else:
        return {"status": "error"}


@app.route('/register', methods=['DELETE'])
def register():
    email = request.args.get("email")
    name = request.args.get("name")
    location = request.args.get("location")
    about = request.args.get("about")
    password = request.args.get("password")
    if email and name and location and about and password:
        if db.session.query(Participant).filter(Participant.email == email).first():
            return {"status": "error"}
        user = Participant(name=name, email=email, password=password, about=about, location=location)
        db.session.add(user)
        db.session.commit()
        part = ParticipantSchema()
        return jsonify(part.dump(user))
    return {"status":"error"}


@app.route('/auth', methods=['POST'])
def auth():
    email = request.args.get("email")
    password = request.args.get("password")
    user = db.session.query(Participant).filter(Participant.email == email).first()
    if user and user.password_valid(password):
        access_token = create_access_token(identity=email)
        return {"status": "success", "key": access_token}
    else:
        return {"status": "bad data"}


@app.route('/profile/<uid>', methods=['GET'])
def profile(uid):
    user = db.session.query(Participant).get(int(uid))
    if not user:
        return 500
    part = ParticipantSchema()
    return jsonify(part.dump(user))