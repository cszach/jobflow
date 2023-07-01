from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.from_object("app.config.Config")

mongo = PyMongo(app)
db = mongo.db

from app import routes
