import os
from flask import Flask
from flask_login import LoginManager

from config import db, migrate
from models import Account
from tasks import start_scheduler
from flask import render_template


def create_app():
    # Attiva la gestione della cartella instance/
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder="html",
        static_folder=".",
        static_url_path="",
        template_folder="html"
    )

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

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Account.query.get(int(user_id))

    from controllers.routes import auth_bp
    from controllers import admin_control
    from controllers import two_fa_control
    from controllers import autenticazione_control
    from controllers import login_control
    from controllers import segnalazione_control
    from controllers import donazione_monetaria_control
    from controllers import donazione_bene
    from controllers import permessi
    from controllers import api_punti
    from controllers import pdf_service
    from controllers import prenotazione_control
    from controllers import profilo_control
    from controllers import feedback_control
    from controllers import gestione_scorte_control
    from controllers.feedback_control import feedback_bp
    app.register_blueprint(feedback_bp)
    app.register_blueprint(api_punti.api, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    print(">>>>>Flask root:", os.getcwd())

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/<path:page>.html")
    def serve_page(page):
        return render_template(f"{page}.html")
    
    @app.route("/login")
    def login_page():
        return render_template("login.html")

    @app.route("/register")
    def register_page():
        return render_template("register.html")

    @app.route("/donazione")
    def donazione_page():
        return render_template("donazione.html")

    @app.route("/donazione-beni")
    def donazione_beni_page():
        return render_template("donazione-beni.html")
    
    @app.route("/recupero-password")
    def recupero_password_page():
        return render_template("recupero-password.html")

    @app.route("/cambio-password")
    def cambio_password_page():
        return render_template("cambio-password.html")
    
    @app.route("/storico-donazioni")
    def storico_donazioni_page():
        return render_template("storico-donazioni.html")      

    @app.route("/storico-prenotazioni")
    def storico_prenotazioni_page():
        return render_template("storico-prenotazioni.html") 
          
    @app.route("/segnalazione")
    def segnalazione_page():
        return render_template("segnalazione.html")

    @app.route("/prenotazione")
    def prenotazione_page():
        return render_template("prenotazione.html")
    
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true' or not app.debug:
        start_scheduler(app)

    return app

