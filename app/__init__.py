import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from whitenoise import WhiteNoise

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensesDB.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or ''

db = SQLAlchemy(app)

from app import routes

# app.wsgi_app = WhiteNoise(app.wsgi_app, root="app/static/")

