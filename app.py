from flask import Flask
from Map4aid.map4aid_model.extension import db, migrate

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'skMomentanea'

    db.init_app(app)
    migrate.init_app(app, db)

    # importa i modelli DOPO aver inizializzato db
    from Map4aid.map4aid_model import models

    # importa i controller DOPO i modelli
    from Map4aid.Control import AutenticazioneControl
    AutenticazioneControl.init_routes(app)


    @app.route("/")
    def home():
        return "sono on"

    return app
