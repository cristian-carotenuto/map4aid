import secrets
from datetime import datetime, timedelta
from flask import Blueprint, request, session, jsonify

from models import ( Account, AccountBeneficiario, AccountEnteDonatore, AccountEnteErogatore )
from controllers.EmailControl import EmailControl

from config import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    ruolo = request.form.get("ruolo")
    email = request.form.get("email")
    password = request.form.get("password")
    user = Account.query.filter_by(email=email).first()

    if not ruolo or not email or not password:
        return jsonify({"error": "Campi obbligatori mancanti"}), 400

    if user:
        return jsonify({"error": "Email già registrata"}), 409

    if ruolo == "beneficiario":
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")
        codice_fiscale = request.form.get("codice_fiscale")

        if not nome or not cognome:
            return jsonify({"error": "Dati beneficiario incompleti"}), 400

        user = AccountBeneficiario(
            email=email,
            nome=nome,
            cognome=cognome,
            codice_fiscale=codice_fiscale
        )

        user.set_password(password)

    elif ruolo == "donatore":
        partita_iva = request.form.get("partita_iva")
        categoria = request.form.get("categoria")
        nome_attivita = request.form.get("nome_attivita")
        indirizzo_sede = request.form.get("indirizzo_sede")
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")

        if not all([partita_iva, categoria, nome_attivita,
                    indirizzo_sede, nome, cognome]):
            return jsonify({"error": "Dati donatore incompleti"}), 400

        user = AccountEnteDonatore(
            email=email,
            nome=nome,
            cognome=cognome,
            partita_iva=partita_iva,
            categoria=categoria,
            nome_attivita=nome_attivita,
            indirizzo_sede=indirizzo_sede
        )
        user.set_password(password)

    elif ruolo == "erogatore":
        nome_org = request.form.get("nome_organizzazione")
        indirizzo_sede = request.form.get("indirizzo_sede")
        tipologia = request.form.get("tipologia_ente")
        iban = request.form.get("iban")

        if not all([nome_org, indirizzo_sede, tipologia, iban]):
            return jsonify({"error": "Dati ente erogatore incompleti"}), 400

        user = AccountEnteErogatore(
            email=email,
            nome_attivita=nome_org,
            indirizzo_sede=indirizzo_sede,
            tipologia=tipologia,
            iban=iban
        )
        user.set_password(password)

        # Salvo nel DB prima di inviare email
        db.session.add(user)
        db.session.commit()

        codice = secrets.randbelow(9000) + 1000

        session["registrazione"] = {
            "email": email,
            "codice": str(codice),
            "expires_at": (datetime.utcnow() + timedelta(minutes=10)).isoformat()
        }

        email_control = EmailControl()

        if email_control.invia_email_codice(email, codice) :
            return jsonify({"message": "Email inviata"}), 200

        return jsonify({"message": "Email non inviata"}), 200

    else:
        return jsonify({"error": "Ruolo non valido"}), 400

    # Salvo beneficiario o donatore
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Registrazione completata"}), 200
