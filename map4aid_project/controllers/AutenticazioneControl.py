import secrets
from datetime import datetime, timedelta
from flask import request, session, jsonify
from .EmailControl import EmailControl
from Map4aid.map4aid_model.models import Account, AccountBeneficiario, AccountEnteDonatore, AccountEnteErogatore


def init_routes(app):
    @app.route("/register", methods=["POST"])
    def register():
        ruolo = request.form.get("ruolo")
        email = request.form.get("email")
        password = request.form.get("password")
        user = Account.query.filter_by(email=email).first()

        if not ruolo or not email or not password:
            return jsonify({"error": "Campi obbligatori mancanti"}), 400

        if user:
            return jsonify({"error": "Email già registrata"}), 409


        # ----- BENEFICIARIO -----
        if ruolo == "beneficiario":
            nome = request.form.get("nome")
            cognome = request.form.get("cognome")

            if not nome or not cognome:
                return jsonify({"error": "Dati beneficiario incompleti"}), 400

            user = AccountBeneficiario(
                email=email,
                nome=nome,
                cognome=cognome
            )
            user.set_password(password)

        # ----- DONATORE -----
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
                email = email,
                nome = nome,
                cognome = cognome,
                partita_iva = partita_iva,
                categoria = categoria,
                nome_attivita = nome_attivita,
                indirizzo_sede = indirizzo_sede
            )
            user.set_password(password)

        # ----- ENTE EROGATORE -----
        elif ruolo == "erogatore":
            nome_org = request.form.get("nome_organizzazione")
            indirizzo_sede = request.form.get("indirizzo_sede")
            tipologia = request.form.get("tipologia_ente")
            iban = request.form.get("iban")

            if not all([nome_org, indirizzo_sede, tipologia, iban]):
                return jsonify({"error": "Dati ente erogatore incompleti"}), 400

            user = AccountEnteErogatore(
                email = email,
                nome_attivita = nome_org,
                indirizzo_sede = indirizzo_sede,
                tipologia = tipologia,
                iban = iban
            )
            user.set_password(password)
            email = request.form.get("email")
            if not email:
                return jsonify({"error": "Email mancante"}), 400

            # Genera codice OTP sicuro a 4 cifre
            codice = secrets.randbelow(9000) + 1000  # tra 1000 e 9999

            # Salva nella sessione solo temporaneamente con scadenza
            session["registrazione"] = {
                "user": user,
                "codice": str(codice),
                "expires_at": (datetime.utcnow() + timedelta(minutes=10)).isoformat()
            }

            # Invia email con il codice
            email_ok = EmailControl.invia_email_codice(email, codice)


            if email_ok:
                return jsonify({"message": "Email inviata"}), 200
            else:
                return jsonify({"error": "Email non inviata"}), 400

        else:
            return jsonify({"error": "Ruolo non valido"}), 400