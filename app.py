from flask import Flask
from config import Config

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

from models import db

db.init_app(app)
db.create_all(app=app)

from views import *

if __name__ == "__main__":

    app.run()