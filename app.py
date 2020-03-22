from flask import Flask
from config import Config

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object(Config)

from models import db, Location

db.init_app(app)
db.create_all(app=app)


admin = Admin(app=app)
admin.add_view(ModelView(Location, db.session))

from views import *

if __name__ == "__main__":

    app.run()