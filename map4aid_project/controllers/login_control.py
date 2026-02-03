import secrets

from flask_login import logout_user, current_user

from config import db
from flask import request, session, jsonify
from controllers.service_email.EmailControl import EmailControl
from models.models import Account
from models.pendingAccounts import PendingAccount
from controllers.routes import auth_bp
from controllers.service_email.email_control_bridge import EmailControlBridge
from controllers.auth_facade import AuthFacade

@auth_bp.route("/login", methods=["POST"])
def login():

    if current_user.is_authenticated:
        return jsonify({"error": "Già loggato"}), 400

    facade = AuthFacade(EmailControlBridge())

    try:
        facade.login_with_otp(
            request.form.get("email"),
            request.form.get("password")
        )
        return jsonify({"message": "Email inviata"}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 401

    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    logout_user()
    return jsonify({"message": "Logout effettuato"})

@auth_bp.route("/recuperoPassword", methods=["POST"])
def recupero_password():
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "Email mancante"}), 400

    # Genera codice OTP sicuro a 4 cifre
    codice = secrets.randbelow(9000) + 1000  # tra 1000 e 9999

    # Salva nella sessione email
    session["pending_email"] = email
    puser = PendingAccount(
        email = email,
        token = codice
    )
    db.session.add(puser)
    db.session.commit()

    # Invia email con il codice
    email_control = EmailControl()
    email_ok = email_control.invia_email_codice(email, codice)

    if not email_ok:
        return jsonify({"message": "Email di recupero inviata"}), 200

    return jsonify({"errore": "Email di recupero non inviata"}), 200


@auth_bp.route("/confermaRecupero", methods=["POST"])
def conferma_recupero():
    email = session.get("pending_email")
    puser = PendingAccount.query.filter_by(email=email).first()
    if not puser:
        return jsonify({"error": "Nessuna richiesta in corso"}), 400

    codice_inserito = request.form.get("codice")
    if codice_inserito != puser.token:
        return jsonify({"error": "Codice non valido"}), 401

    # Codice corretto → consenti cambio password
    session["reset_verified"] = email  # salva email verificata
    session.pop("pending_email")  # rimuovi codice

    return jsonify({"message": "Codice valido, puoi cambiare la password"}), 200


@auth_bp.route("/cambiaPassword", methods=["POST"])
def cambia_password():
    email = session.get("reset_verified")
    if not email:
        return jsonify({"error": "Nessuna email verificata"}), 400

    nuova_password = request.form.get("nuova_password")
    if not nuova_password:
        return jsonify({"error": "Password mancante"}), 400

    user = Account.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "Utente non trovato"}), 404

    user.set_password(nuova_password)
    db.session.commit()

    session.pop("reset_verified")  # pulizia sessione
    return jsonify({"message": "Password cambiata con successo"}), 200