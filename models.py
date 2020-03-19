from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from app import app, db

db = SQLAlchemy()


class Event(db.Model):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)
    type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    location = relationship("Location", back_populates="code")


class Location(db.Model):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    code = Column(String, nullable=False)
