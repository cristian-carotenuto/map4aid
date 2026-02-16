from datetime import datetime
from flask import request, session, jsonify, Blueprint
from werkzeug.security import check_password_hash

from config import db
from controllers.routes import auth_bp
from models.pendingAccounts import PendingAccount
from models.models import AccountBeneficiario, AccountDonatore, AccountEnteErogatore, Account
from flask_login import login_user



@auth_bp.route("/2FARegister", methods=["POST"])
def conferma_codice_registrazione():
    email = session.get("pending_email")
    puser = PendingAccount.query.filter_by(email=email).first()

    if not puser:
        return jsonify({"error": "Nessuna registrazione in corso"}), 400

    codice_inserito = request.form.get("codice")
    if not check_password_hash(puser.token,codice_inserito):
        return jsonify({"error": "Codice non valido"}), 401

    # Codice corretto → consenti registrazione
    user = None
    #----BENEFICIARIO-----
    if puser.tipo == "beneficiario":
        data_nascita = datetime.strptime(puser.extra_data["data_nascita"], "%Y-%m-%d").date()
        user = AccountBeneficiario(
            email=email,
            password_hash = puser.password_hash,
            nome = puser.extra_data["nome"],
            cognome = puser.extra_data["cognome"],
            data_nascita = data_nascita,
            patologie = puser.extra_data["patologie"],
            allergeni = puser.extra_data["allergeni"],
            codice_carta_identita = puser.extra_data["codice_carta_identita"],
            path_immagine_carta_identita = puser.extra_data["path_immagine_carta_identita"]
        )

    # ----DONATORE-----
    elif puser.tipo == "donatore":
        user = AccountDonatore(
            email=email,
            password_hash = puser.password_hash,
            nome_attivita = puser.extra_data["nome_attivita"],
            partita_iva = puser.extra_data["partita_iva"],
            indirizzo_sede = puser.extra_data["indirizzo_sede"],
            nome = puser.extra_data["nome"],
            cognome = puser.extra_data["cognome"],
            categoria = puser.extra_data["categoria"]
        )

    #--------ENTE EROGATORE--------
    elif puser.tipo == "erogatore":
        user = AccountEnteErogatore(
            email=email,
            password_hash = puser.password_hash,
            nome_organizzazione = puser.extra_data["nome_organizzazione"],
            iban = puser.extra_data["iban"],
            indirizzo_sede = puser.extra_data["indirizzo_sede"],
            tipologia_ente = puser.extra_data["tipologia_ente"]
        )
    if not user:
        return jsonify({"error": "Nessuna registrazione in corso"}), 400
    tipo = puser.tipo
    db.session.add(user)
    db.session.delete(puser)
    db.session.commit()
    session.pop("pending_email")  # rimuovi email

    if tipo == "beneficiario":
        return jsonify({"message": "Codice valido, registrazione in attessa di validazione dall'admin"}), 200
    return jsonify({"message": "Codice valido, registrazione avvenuta"}), 200


@auth_bp.route("/2FALogin", methods=["POST"])
def conferma_codice_login():
    email = session.get("pending_email")
    puser = PendingAccount.query.filter_by(email=email).first()
    user = Account.query.filter_by(email=email).first()
    if not puser:
        return jsonify({"error": "Nessun login in corso"}), 400

    codice_inserito = str(request.form.get("codice"))
    if not check_password_hash(puser.token,codice_inserito):
        return jsonify({"error": "Codice non valido"}), 401

    # Codice corretto → consenti login
    session["logged_in"] = True
    session["user_email"] = email
    login_user(user)
    db.session.delete(puser)
    db.session.commit()
    session.pop("pending_email")
    return jsonify({
        "message": "Login effettuato con successo",
        "email": email,
        "ruolo": user.tipo
    })


