import secrets
from datetime import datetime

from flask import session

from models import Account
from models.pendingAccounts import PendingAccount
from config import db

class AuthFacade:

    def __init__(self, mail_sender):
        self.mail_sender = mail_sender

    def register_pending_account(self, form_data):
        ruolo = form_data.get("ruolo")
        email = form_data.get("email")
        email = email.lower().strip()
        password = form_data.get("password")

        if not ruolo or not email or not password:
            raise ValueError("Campi obbligatori mancanti")

        if PendingAccount.query.filter_by(email=email).first():
            raise ValueError("Email già registrata")

        extra_data = self._build_extra_data(ruolo, form_data)

        codice = secrets.randbelow(9000) + 1000

        pending = PendingAccount(
            email=email,
            tipo=ruolo,
            extra_data=extra_data,
            token=codice
        )
        pending.set_password(password)

        PendingAccount.query.filter_by(email=email).delete(synchronize_session=False)
        db.session.add(pending)
        db.session.commit()
        db.session.add(pending)
        db.session.commit()
        session["pending_email"] = email

        if not self.mail_sender.send_otp(email, codice):
            raise RuntimeError("Email non inviata")

        return True

    def _build_extra_data(self, ruolo, data):
        if ruolo == "beneficiario":
            return {
                "nome": data.get("nome"),
                "cognome": data.get("cognome"),
                "data_nascita": data.get("data_nascita"),
                "patologie": data.get("patologie")
            }

        elif ruolo == "donatore":
            return {
                "partita_iva": data.get("partita_iva"),
                "nome_attivita": data.get("nome_attivita"),
                "indirizzo_sede": data.get("indirizzo_sede"),
                "nome": data.get("nome"),
                "cognome": data.get("cognome"),
                "categoria": data.get("categoria")
            }

        elif ruolo == "erogatore":
            return {
                "nome_organizzazione": data.get("nome_organizzazione"),
                "indirizzo_sede": data.get("indirizzo_sede"),
                "tipologia_ente": data.get("tipologia_ente"),
                "iban": data.get("iban")
            }

        else:
            raise ValueError("Ruolo non valido")



    def login_with_otp(self, email, password):
        email = email.lower().strip()
        if not email or not password:
            raise ValueError("Email e password obbligatorie")

        user = Account.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            raise ValueError("Credenziali non valide")

        codice = secrets.randbelow(9000) + 1000

        pending = PendingAccount(
            email=email,
            token=codice,
        )

        PendingAccount.query.filter_by(email=email).delete(synchronize_session=False)
        db.session.add(pending)
        db.session.commit()
        db.session.add(pending)
        db.session.commit()
        session["pending_email"] = email

        if not self.mail_sender.send_otp(email, codice):
            raise RuntimeError("Email non inviata")

        return True