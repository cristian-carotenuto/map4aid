from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#creazione app flask
app = Flask(__name__)

#configurazione db SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#secretKey (serve per sessioni, login..)
app.config['SECRET_KEY'] = 'skMomentanea'


#inizializzazione del db e migration system
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#import modelli(necessario per farli conoscere a Flask)
from models import *


#route di test

@app.route("/")
def home():
    return "sono on"
