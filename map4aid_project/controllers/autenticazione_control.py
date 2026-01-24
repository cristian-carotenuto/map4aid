import secrets
from datetime import datetime, timedelta
from flask import request, session, jsonify, Blueprint
from controllers.EmailControl import EmailControl
from config import db
from controllers.routes import auth_bp
from models.models import Account, AccountBeneficiario, AccountDonatore, AccountEnteErogatore
from models.pendingAccounts import PendingAccount


@auth_bp.route("/register", methods=["POST"])
def register():
    ruolo = request.form.get("ruolo")
    email = request.form.get("email")
    password = request.form.get("password")

    if not ruolo or not email or not password:
        return jsonify({"error": "Campi obbligatori mancanti"}), 400

    # Controlla se email già registrata nel database
    if Account.query.filter_by(email=email).first():
        return jsonify({"error": "Email già registrata"}), 409

    # ----- BENEFICIARIO -----
    if ruolo == "beneficiario":
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")
        cf = request.form.get("codice_fiscale")

        if not all([nome, cognome, cf]):
            return jsonify({"error": "Dati beneficiario incompleti"}), 400

        extra_data = {
            "nome": nome,
            "cognome": cognome,
            "codice_fiscale": cf
        }

    # ----- DONATORE -----
    elif ruolo == "donatore":
        partita_iva = request.form.get("partita_iva")

        nome_attivita = request.form.get("nome_attivita")


        if not all([partita_iva, nome_attivita]):
            return jsonify({"error": "Dati donatore incompleti"}), 400

        extra_data = {
            "partita_iva": partita_iva,
            "nome_attivita": nome_attivita,
        }

    # ----- ENTE EROGATORE -----
    elif ruolo == "erogatore":
        nome_org = request.form.get("nome_organizzazione")
        indirizzo_sede = request.form.get("indirizzo_sede")
        tipologia = request.form.get("tipologia_ente")
        iban = request.form.get("iban")

        if not all([nome_org, indirizzo_sede, tipologia, iban]):
            return jsonify({"error": "Dati ente erogatore incompleti"}), 400

        extra_data = {
            "nome_organizzazione": nome_org,
            "indirizzo_sede": indirizzo_sede,
            "tipologia_ente": tipologia,
            "iban": iban
        }

    else:
        return jsonify({"error": "Ruolo non valido"}), 400

    # Genera OTP a 4 cifre
    codice = secrets.randbelow(9000) + 1000  # 1000-9999

    # Salva i dati temporanei in sessione (senza password chiaro)
    pending_account = PendingAccount(
        email = email,
        tipo = ruolo,
        extra_data = extra_data,
        token = codice
    )
    session["pending_email"] = email
    pending_account.set_password(password)
    db.session.add(pending_account)
    db.session.commit()

    # Invia email con codice OTP
    email_control = EmailControl()
    email_ok = email_control.invia_email_codice(email, codice)

    if email_ok:
        return jsonify({"message": "Email inviata. Controlla la tua casella."}), 200
    else:
        return jsonify({"error": "Email non inviata"}), 400