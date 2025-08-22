import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__, static_folder='static', static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI') or 'sqlite:///expensesDB.db'
print("Using database URI:", app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or ''

db = SQLAlchemy(app)

from app import routes