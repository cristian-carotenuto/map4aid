from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Map4aid.Control.AutenticazioneControl import auth_bp
from Map4aid.map4aid_model.extension import migrate, db

#creazione app flask
app = Flask(__name__)

#configurazione db SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#secretKey (serve per sessioni, login..)
app.config['SECRET_KEY'] = 'skMomentanea'


#inizializzazione del db e migration system
db.init_app(app)
migrate.init_app(app, db)

#import modelli(necessario per farli conoscere a Flask)
app.register_blueprint(auth_bp, url_prefix="/auth")


if __name__ == "__main__":
    app.run(debug=True)

#route di test

@app.route("/")
def home():
    return "sono on"
