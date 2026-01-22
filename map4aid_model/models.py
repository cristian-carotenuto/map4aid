from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime


#CLASSE BASE ACCOUNT (polimorfismo SQLAlchemy)
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


class AccountBeneficiario(Account):
    __tablename__ = "account_beneficiari"

    id = db.Column(db.Integer, db.ForeignKey("accounts.id"), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cognome = db.Column(db.String(100), nullable=False)
    codice_fiscale = db.Column(db.String(16), unique=True, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "beneficiario"
    }


class AccountEnteDonatore(Account):
    __tablename__ = "account_enti_donatori"

    id = db.Column(db.Integer, db.ForeignKey("accounts.id"), primary_key=True)
    partita_iva = db.Column(db.String(11), unique=True, nullable=False)
    nome_attivita = db.Column(db.String(150), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "ente_donatore"
    }


class AccountEnteErogatore(Account):
    __tablename__ = "account_enti_erogatori"

    id = db.Column(db.Integer, db.ForeignKey("accounts.id"), primary_key=True)
    tipologia_ente = db.Column(db.String(100), nullable=False)
    iban = db.Column(db.String(34), nullable=True)
    indirizzo_sede = db.Column(db.String(200), nullable=True)

    punti_distribuzione = db.relationship("PuntoDistribuzione", back_populates="ente_erogatore")

    __mapper_args__ = {
        "polymorphic_identity": "ente_erogatore"
    }


class PuntoDistribuzione(db.Model):
    __tablename__ = "punti_distribuzione"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    indirizzo = db.Column(db.String(255), nullable=False)
    latitudine = db.Column(db.Float, nullable=False)
    longitudine = db.Column(db.Float, nullable=False)
    orari = db.Column(db.String(255), nullable=True)    #json?

    ente_erogatore_id = db.Column(db.Integer, db.ForeignKey("account_enti_erogatori.id"), nullable=False)
    ente_erogatore = db.relationship("AccountEnteErogatore", back_populates="punti_distribuzione")

class MacroCategoria(db.Model):
    __tablename__ = "macro_categorie"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)

    sotto_categorie = db.relationship("SottoCategoria", back_populates="macro_categoria", cascade="all, delete")

class SottoCategoria(db.Model):
    __tablename__ = "sotto_categorie"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    macro_categoria_id = db.Column(db.Integer, db.ForeignKey("macro_categorie.id"), nullable=False)

    macro_categoria = db.relationship("MacroCategoria", back_populates="sotto_categorie")

class Bene(db.Model):
    __tablename__ = "beni"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    quantita = db.Column(db.Integer, nullable=False, default=0)

    punto_distribuzione_id = db.Column(
        db.Integer,
        db.ForeignKey("punti_distribuzione.id"),
        nullable=False
    )

    sottocategoria_id = db.Column(
        db.Integer,
        db.ForeignKey("sotto_categorie.id"),
        nullable=False
    )

    punto_distribuzione = db.relationship(
        "PuntoDistribuzione",
        backref="beni"
    )

    sottocategoria = db.relationship(
        "SottoCategoria",
        backref="beni"
    )

    import uuid
from datetime import datetime
from app import db


class Prenotazione(db.Model):
    __tablename__ = "prenotazioni"

    id = db.Column(db.Integer, primary_key=True)

    # FK beneficiario
    beneficiario_id = db.Column(
        db.Integer,
        db.ForeignKey("account_beneficiari.id"),
        nullable=False
    )

    # FK bene
    bene_id = db.Column(
        db.Integer,
        db.ForeignKey("beni.id"),
        nullable=False
    )

    # Timestamp prenotazione
    data_prenotazione = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # Stato prenotazione
    stato = db.Column(
        db.String(50),
        nullable=False,
        default="in_attesa"  
    )

    # Codice univoco per QR
    codice_qr = db.Column(
        db.String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4())
    )

    # Relazioni
    beneficiario = db.relationship("AccountBeneficiario")
    bene = db.relationship("Bene")
