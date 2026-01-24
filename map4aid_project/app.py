import os
from flask import Flask
from config import db, migrate
from tasks import start_scheduler


def create_app():
    # Attiva la gestione della cartella instance/
    app = Flask(__name__, instance_relative_config=True)

    #mi assicuro che esista la cartella instance
    os.makedirs(app.instance_path, exist_ok=True)

    #configurazione db, sempre dentro instance
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.instance_path}/database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'skMomentanea'

    # Inizializza estensioni
    db.init_app(app)
    migrate.init_app(app, db)

    from models import models
    from models import pendingAccounts

    from controllers.routes import auth_bp
    from controllers import two_fa_contol
    from controllers import autenticazione_control
    app.register_blueprint(auth_bp, url_prefix="/auth")

    print(">>>>>Flask root:", os.getcwd())
    @app.route("/")
    def home():
        return "sono on"

    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true' or not app.debug:
        start_scheduler(app)

    return app

