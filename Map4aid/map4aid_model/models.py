
from werkzeug.security import generate_password_hash, check_password_hash
from Map4aid.map4aid_model.extension import db


# CLASSE BASE ACCOUNT (polimorfismo SQLAlchemy)
class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    #distinguo polimorfismo
    tipo = db.Column(db.String(50))

    __mapper_args__ = {
        "polymorphic_on": tipo,
        "polymorphic_identity": "account"
    }

    #gestione password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


#ACCOUNT BENEFICIARIO
class AccountBeneficiario(Account):
    __tablename__ = "account_beneficiari"

    id = db.Column(db.Integer, db.ForeignKey("accounts.id"), primary_key=True)

    nome = db.Column(db.String(100), nullable=False)
    cognome = db.Column(db.String(100), nullable=False)
    codice_fiscale = db.Column(db.String(16), unique=True, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "beneficiario"
    }


#ACCOUNT ENTE DONATORE
class AccountEnteDonatore(Account):
    __tablename__ = "account_enti_donatori"

    id = db.Column(db.Integer, db.ForeignKey("accounts.id"), primary_key=True)

    partita_iva = db.Column(db.String(11), unique=True, nullable=False)
    nome_attivita = db.Column(db.String(150), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "ente_donatore"
    }


# ACCOUNT ENTE EROGATORE
class AccountEnteErogatore(Account):
    __tablename__ = "account_enti_erogatori"

    id = db.Column(db.Integer, db.ForeignKey("accounts.id"), primary_key=True)

    tipologia_ente = db.Column(db.String(100), nullable=False)
    iban = db.Column(db.String(34), nullable=True)
    indirizzo_sede = db.Column(db.String(200), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "ente_erogatore"
    }
