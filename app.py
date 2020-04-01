from flask import Flask
from config import Config

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
from models import db, Location, Event, Enrollment

db.init_app(app)
db.create_all(app=app)


admin = Admin(app=app)
admin.add_view(ModelView(Location, db.session))
admin.add_view(ModelView(Event, db.session))
#admin.add_view(ModelView(Enrollment, db.session))

from views import *
#from servis_views import *

if __name__ == "__main__":

    app.run()