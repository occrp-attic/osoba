from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database

from osoba import settings

app = Flask("Osoba")
api = Api(app)
app.config.from_object(settings)
db = SQLAlchemy(app)

def createdb():
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
    if settings.DROP_DB_ON_RESTART and database_exists(engine.url):
        print "Dropping old database... (because DROP_DB_ON_RESTART=True)"
        drop_database(engine.url)
    if not database_exists(engine.url):
        print "Creating databases..."
        create_database(engine.url)
