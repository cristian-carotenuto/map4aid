import os
from flask import Flask
from config import db, migrate

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    os.makedirs(app.instance_path, exist_ok=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.instance_path}/database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'skMomentanea'

    db.init_app(app)
    migrate.init_app(app, db)

    import models

    from controllers.autenticazione_control import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    @app.route("/")
    def home():
        return "sono on"

    return app
