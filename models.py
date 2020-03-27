from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, Table
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
db = SQLAlchemy()


Enrollment = Table(
    "enrollments",
    db.metadata,
    Column("id", Integer, primary_key=True),
    Column("event_id", Integer, ForeignKey("events.id")),
    Column("participant_id", Integer, ForeignKey("participants.id")),
    Column("datetime", Integer, nullable=False)
)

# class Enrollment(db.Model):
#     __tablename__ = "enrollments"
#     id = Column(Integer, primary_key=True)
#     event_id = Column(Integer,  ForeignKey("events.id"))
#     participant_id = Column(Integer,  ForeignKey("participants.id"))
#     datetime = Column(Integer)

class Event(db.Model):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
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


class Participant(db.Model):
    @property
    def password(self):
        return self._password

    __tablename__ = "participants"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    picture = Column(String, nullable=False)
    location = Column(String, nullable=False)
    about = Column(String, nullable=False)

    events = relationship(
        "Event", secondary=Enrollment, back_populates="participants"
    )

    @password.setter
    def password(self, passw):
        self.password_hash = generate_password_hash(passw)

    def password_valid(self, password):
        return check_password_hash(self.password_hash, password)

# class Enrollment(db.Model):
#     __tablename__ = "enrollments"
#     id = Column(Integer, primary_key=True)
#     event = relationship("Event", back_populates="participants")
#     participant = relationship("Participant", back_populates="enrollments")
#     datetime = Column(Integer, nullable=False)




class Location(db.Model):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    code = Column(String, nullable=False)
    events = relationship("Event", back_populates="location")

