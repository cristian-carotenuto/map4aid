import os
import secrets
from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask import session
from werkzeug.security import generate_password_hash
from models import Account, AccountBeneficiario
from models.pendingAccounts import PendingAccount
from config import db

UPLOAD_FOLDER = "controllers/upload/documenti"


def _build_extra_data(ruolo, data, files):
    # -------------------------
    # Gestione upload documento
    # -------------------------
    file_ci = files.get("carta_identita")

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    if file_ci:
        filename = secure_filename(file_ci.filename)
        unique_name = f"{secrets.token_hex(8)}_{filename}"
        file_path = os.path.join(UPLOAD_FOLDER, unique_name)
        file_ci.save(file_path)

    if ruolo == "beneficiario":
        return {
            "nome": data.get("nome"),
            "cognome": data.get("cognome"),
            "data_nascita": data.get("data_nascita"),
            "allergeni": data.get("allergeni"),
            "patologie": data.get("patologie"),
            "codice_carta_identita": data.get("codice_carta_identita"),
            "path_immagine_carta_identita": file_path
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


class AuthFacade:

    def __init__(self, mail_sender):
        self.mail_sender = mail_sender

    def register_pending_account(self, form_data, files):
        ruolo = form_data.get("ruolo")
        email = form_data.get("email")
        password = form_data.get("password")

        if not ruolo or not email or not password:
            raise ValueError("Campi obbligatori mancanti")

        email = email.lower().strip()

        if PendingAccount.query.filter_by(email=email).first():
            raise ValueError("Email già in fase di registrazione")


        # -------------------------
        # Extra data per ruolo
        # -------------------------
        extra_data = _build_extra_data(
            ruolo,
            form_data,
            files
        )

        # -------------------------
        # OTP
        # -------------------------
        codice = secrets.randbelow(9000) + 1000

        pending = PendingAccount(
            email=email,
            tipo=ruolo,
            extra_data=extra_data,
            token=generate_password_hash(str(codice))
        )
        pending.set_password(password)

        PendingAccount.query.filter_by(email=email).delete(
            synchronize_session=False
        )

        db.session.add(pending)
        db.session.commit()

        session["pending_email"] = email

        if not self.mail_sender.send_otp(email, codice):
            raise RuntimeError("Email non inviata")

        return True

    def login_with_otp(self, email, password):
        email = email.lower().strip()
        if not email or not password:
            raise ValueError("Email e password obbligatorie")

        user = Account.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            raise ValueError("Credenziali non valide")

        if user.tipo == "beneficiario":
            user = AccountBeneficiario.query.filter_by(email=email).first()
            if not user.accettato:
                raise ValueError("Account ancora non accettato")

        codice = secrets.randbelow(9000) + 1000
        pending = PendingAccount(
            email=email,
            token=generate_password_hash(str(codice)),
        )

        PendingAccount.query.filter_by(email=email).delete(synchronize_session=False)
        db.session.add(pending)
        db.session.add(pending)
        db.session.commit()
        session["pending_email"] = email

        if not self.mail_sender.send_otp(email, codice):
            raise RuntimeError("Email non inviata")

        return True
    
    def validate_email(self, email, current_user=None):
        email = email.lower().strip()

        #se email coincide ok
        if current_user and email == current_user.email:
            return True

        #controllo su account
        if Account.query.filter_by(email=email).first():
            raise ValueError("Email già in uso")

        #controllo su pending
        if PendingAccount.query.filter_by(email=email).first():
            raise ValueError("Email già in uso (in attesa di conferma)")

        return True
