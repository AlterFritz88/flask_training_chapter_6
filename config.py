import os

current_path = os.path.dirname(os.path.realpath(__file__))
db_path = "sqlite:///data_base.db"


class Config:
    DEBUG = True
    SECRET_KEY = "secret_key"
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "olololo"
