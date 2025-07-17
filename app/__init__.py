import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from whitenoise import WhiteNoise

app = Flask(__name__)
app = WhiteNoise(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensesDB.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or ''

db = SQLAlchemy(app)

from app import routes

