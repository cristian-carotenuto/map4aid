import secrets
from datetime import datetime, timedelta
from flask import request, session, jsonify
from map4aid_model.models import *
from Map4aid.Control.EmailControl import EmailControl
from Map4aid.app import app


# ---- LOGIN ----
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"error": "Email e password obbligatorie"}), 400

    user = Account.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Credenziali non valide"}), 401

    if  not user.check_password(password):
        return jsonify({"error": "Credenziali non valide"}), 401

    # Genera codice OTP sicuro a 4 cifre
    codice = secrets.randbelow(9000) + 1000  # tra 1000 e 9999
    # Salva nella sessione solo temporaneamente con scadenza
    session["login"] = {
            "email": email,
            "codice": str(codice),
            "expires_at": (datetime.utcnow() + timedelta(minutes=10)).isoformat()
    }
    email_ok = EmailControl.invia_email_codice(email,codice)
    if not email_ok:
        return jsonify({"error": "Email non inviata"}), 401

    return jsonify({"message": "Email inviata"}), 401


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logout effettuato"})

@app.route("/recuperoPassword", methods=["POST"])
def recupero_password():
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "Email mancante"}), 400

    # Genera codice OTP sicuro a 4 cifre
    codice = secrets.randbelow(9000) + 1000  # tra 1000 e 9999

    # Salva nella sessione solo temporaneamente con scadenza
    session["reset_password"] = {
        "email": email,
        "codice": str(codice),
        "expires_at": (datetime.utcnow() + timedelta(minutes=10)).isoformat()
    }

    # Invia email con il codice
    EmailControl.invia_email_codice(email, codice)

    return jsonify({"message": "Email di recupero inviata"}), 200


@app.route("/confermaRecupero", methods=["POST"])
def conferma_recupero():
    data = session.get("reset_password")
    if not data:
        return jsonify({"error": "Nessuna richiesta in corso"}), 400

    # Controlla scadenza
    if datetime.utcnow() > datetime.fromisoformat(data["expires_at"]):
        session.pop("reset_password")
        return jsonify({"error": "Codice scaduto"}), 400

    codice_inserito = request.form.get("codice")
    if codice_inserito != data["codice"]:
        return jsonify({"error": "Codice non valido"}), 401

    # Codice corretto → consenti cambio password
    session["reset_verified"] = data["email"]  # salva email verificata
    session.pop("reset_password")  # rimuovi codice

    return jsonify({"message": "Codice valido, puoi cambiare la password"}), 200


@app.route("/cambiaPassword", methods=["POST"])
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