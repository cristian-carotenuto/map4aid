from datetime import datetime
from flask import request, session, jsonify, Blueprint

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/2FARegister", methods=["POST"])
def conferma_codice():
    data = session.get("registrazione")
    if not data:
        return jsonify({"error": "Nessuna registrazionein corso"}), 400

    # Controlla scadenza
    if datetime.utcnow() > datetime.fromisoformat(data["expires_at"]):
        session.pop("registrazione")
        return jsonify({"error": "Codice scaduto"}), 400

    codice_inserito = request.form.get("codice")
    if codice_inserito != data["codice"]:
        return jsonify({"error": "Codice non valido"}), 401

    # Codice corretto → consenti registrazione
    user = data["user"]
    db.session.add(user)
    db.session.commit()
    session.pop("registrazione")  # rimuovi codice

    return jsonify({"message": "Codice valido, registrazione avvenuta"}), 200

@app.route("/2FALogin", methods=["POST"])
def conferma_codice():
    data = session.get("login")
    if not data:
        return jsonify({"error": "Nessun login in corso"}), 400

    # Controlla scadenza
    if datetime.utcnow() > datetime.fromisoformat(data["expires_at"]):
        session.pop("login")
        return jsonify({"error": "Codice scaduto"}), 400

    codice_inserito = request.form.get("codice")
    if codice_inserito != data["codice"]:
        return jsonify({"error": "Codice non valido"}), 401

    # Codice corretto → consenti login
    email = data["email"]
    session["logged_in"] = True
    session["user_email"] = email
    session.pop("registrazione")  # rimuovi codice
    return jsonify({
        "message": "Login effettuato con successo",
        "email": email
    })



