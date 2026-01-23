from datetime import datetime
from flask import request, session, jsonify, Blueprint

from config import db
from models.models import AccountBeneficiario, AccountEnteDonatore, AccountEnteErogatore
from models.pendingAccounts import PendingAccount

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/2FARegister", methods=["POST"])
def conferma_codice():
    email = session.get("pending_email")
    puser = PendingAccount(PendingAccount.query.filter_by(email=email).first())
    if not puser:
        return jsonify({"error": "Nessuna registrazionein corso"}), 400

    codice_inserito = request.form.get("codice")
    if codice_inserito != puser.token:
        return jsonify({"error": "Codice non valido"}), 401

    # Codice corretto → consenti registrazione
    user = None
    #----BENEFICIARIO-----
    if puser.tipo == "beneficiario":
        user = AccountBeneficiario(
            email=email,
            password_hash = puser.password_hash,
            nome = puser.extra_data["nome"],
            cognome = puser.extra_data["cognome"],
            codice_fiscale = puser.extra_data["codice_fiscale"]
        )

    # ----DONATORE-----
    if puser.tipo == "ente_donatore":
        user = AccountEnteDonatore(
            email=email,
            password_hash = puser.password_hash,
            nome_attivita = puser.extra_data["nome_attivita"],
            partita_iva = puser.extra_data["partita_iva"]
        )

    #--------ENTE EROGATORE--------
    if puser.tipo == "ente_erogatore":
        user = AccountEnteErogatore(
            email=email,
            password_hash = puser.password_hash,
            iban = puser.extra_data["iban"],
            indirizzo_sede = puser.extra_data["indirizzo_sede"],
            tipologia_ente = puser.extra_data["tipologia_ente"]
        )
    if(user == None):
        return jsonify({"error": "Nessuna registrazionein corso"}), 400
    db.session.add(user)
    db.session.commit()
    session.pop("email")  # rimuovi email

    return jsonify({"message": "Codice valido, registrazione avvenuta"}), 200


@auth_bp.route("/2FALogin", methods=["POST"])
def conferma_codice():
    email = session.get("pending_email")
    puser = PendingAccount(PendingAccount.query.filter_by(email=email).first())
    if not puser:
        return jsonify({"error": "Nessun login in corso"}), 400

    codice_inserito = request.form.get("codice")
    if codice_inserito != puser.token:
        return jsonify({"error": "Codice non valido"}), 401

    # Codice corretto → consenti login
    session["logged_in"] = True
    session["user_email"] = email
    session.pop("pendindg_email")  # rimuovi codice
    return jsonify({
        "message": "Login effettuato con successo",
        "email": email
    })


