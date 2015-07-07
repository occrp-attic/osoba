from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

from osoba import settings
from osoba.urls import urls

app = Flask("Osoba")
api = Api(app)
app.config.from_object(settings)
db = SQLAlchemy(app)

for url in urls:
    api.add_resource(*url)
