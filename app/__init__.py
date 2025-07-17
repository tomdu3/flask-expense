import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from whitenoise import WhiteNoise
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI') or 'sqlite:///expensesDB.db'
print("Using database URI:", app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or ''

db = SQLAlchemy(app)

from app import routes

app.wsgi_app = WhiteNoise(app.wsgi_app, root=os.path.join(os.path.dirname(__file__), "static"))

