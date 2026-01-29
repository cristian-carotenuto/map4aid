from config import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime, timezone
from flask_login import UserMixin

#la classe notifica presente nel RAD non è stata definita
#la classe segnalazione presente nelle direttive clickUp non è stata definita perchè non presente nel RAD

#  ACCOUNT BASE (POLIMORFISMO)

class Account(UserMixin,db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    tipo = db.Column(db.String(50))  # per polimorfismo

    __mapper_args__ = {
        "polymorphic_on": tipo,
        "polymorphic_identity": "account"
    }

    # gestione password
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

    data_nascita = db.Column(db.Date, nullable=True)
    allergeni = db.Column(db.Text, nullable=True)
    patologie = db.Column(db.Text, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "beneficiario"
    }

    prenotazioni = db.relationship("Prenotazione", back_populates="beneficiario")
    feedback = db.relationship("Feedback", back_populates="beneficiario")



#ACCOUNT DONATORE

class AccountDonatore(Account):
    __tablename__ = "account_donatori"

    id = db.Column(db.Integer, db.ForeignKey("accounts.id"), primary_key=True)

    #se azienda
    partita_iva = db.Column(db.String(11), unique=True, nullable=True)
    nome_attivita = db.Column(db.String(150), nullable=True)
    indirizzo_sede = db.Column(db.String(200), nullable=True)

    #non azienda
    nome = db.Column(db.String(100), nullable=True)
    cognome = db.Column(db.String(100), nullable=True)

    #categoaira(azienda,privato)
    categoria = db.Column(db.String(100), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "donatore"
    }

    donazioni_beni = db.relationship("DonazioneBene", back_populates="donatore")
    donazioni_monetarie = db.relationship("DonazioneMonetaria", back_populates="donatore")



#ACCOUNT ENTE EROGATORE

class AccountEnteErogatore(Account):
    __tablename__ = "account_enti_erogatori"

    id = db.Column(db.Integer, db.ForeignKey("accounts.id"), primary_key=True)

    nome_organizzazione = db.Column(db.String(150), nullable=False)
    indirizzo_sede = db.Column(db.String(200), nullable=True)
    tipologia_ente = db.Column(db.String(100), nullable=False)
    iban = db.Column(db.String(34), nullable=True)

    punti_distribuzione = db.relationship("PuntoDistribuzione", back_populates="ente_erogatore")
    donazioni_beni = db.relationship("DonazioneBene", back_populates="ente_erogatore")
    donazioni_monetarie = db.relationship("DonazioneMonetaria", back_populates="ente")

    __mapper_args__ = {
        "polymorphic_identity": "ente_erogatore"
    }



#PUNTO DISTRIBUZIONE

class PuntoDistribuzione(db.Model):
    __tablename__ = "punti_distribuzione"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    
    giorni_apertura = db.Column(db.String(100), nullable=False)
    orario_apertura = db.Column(db.Time, nullable=False)
    orario_chiusura = db.Column(db.Time, nullable=False)
    
    latitudine = db.Column(db.Float, nullable=False)
    longitudine = db.Column(db.Float, nullable=False)
    accettato = db.Column(db.Boolean, nullable=False, default=False)
    
    ente_erogatore_id = db.Column( db.Integer, db.ForeignKey("account_enti_erogatori.id"), nullable=False)

    ente_erogatore = db.relationship("AccountEnteErogatore", back_populates="punti_distribuzione")
    beni = db.relationship("Bene", back_populates="punto_distribuzione")
    prenotazioni = db.relationship("Prenotazione", back_populates="punto")
    feedback = db.relationship("Feedback", back_populates="punto")



#TASSONOMIA: MACROC → SOTTOC → BENE

class MacroCategoria(db.Model):
    __tablename__ = "macro_categorie"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)

    sotto_categorie = db.relationship("SottoCategoria", back_populates="macro_categoria", cascade="all, delete")


class SottoCategoria(db.Model):
    __tablename__ = "sotto_categorie"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    macro_categoria_id = db.Column(db.Integer, db.ForeignKey("macro_categorie.id"))

    macro_categoria = db.relationship("MacroCategoria", back_populates="sotto_categorie")
    beni = db.relationship("Bene", back_populates="sottocategoria")



#BENE 

class Bene(db.Model):
    __tablename__ = "beni"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    quantita = db.Column(db.Integer, nullable=False, default=0)

    tipo = db.Column(db.String(50))  # polimorfismo

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

    __mapper_args__ = {
        "polymorphic_on": tipo,
        "polymorphic_identity": "bene"
    }

    punto_distribuzione = db.relationship("PuntoDistribuzione", back_populates="beni")
    sottocategoria = db.relationship("SottoCategoria", back_populates="beni")
    prenotazioni = db.relationship("Prenotazione", back_populates="bene")
    donazioni_beni = db.relationship("DonazioneBene", back_populates="bene")



#BENI SPECIFICI (POLIMORFISMO)

class BeneAlimentare(Bene):
    __tablename__ = "beni_alimentari"

    id = db.Column(db.Integer, db.ForeignKey("beni.id"), primary_key=True)
    allergeni = db.Column(db.String(255))
    scadenza = db.Column(db.Date)

    __mapper_args__ = {
        "polymorphic_identity": "alimentare"
    }


class BeneMedicinale(Bene):
    __tablename__ = "beni_medicinali"

    id = db.Column(db.Integer, db.ForeignKey("beni.id"), primary_key=True)
    tipo_medicinale = db.Column(db.String(100))
    scadenza = db.Column(db.Date)

    __mapper_args__ = {
        "polymorphic_identity": "medicinale"
    }


class BeneVestiario(Bene):
    __tablename__ = "beni_vestiario"

    id = db.Column(db.Integer, db.ForeignKey("beni.id"), primary_key=True)
    taglia = db.Column(db.String(20))
    condizioni = db.Column(db.String(100))

    __mapper_args__ = {
        "polymorphic_identity": "vestiario"
    }


class BeneIgiene(Bene):
    __tablename__ = "beni_igiene"

    id = db.Column(db.Integer, db.ForeignKey("beni.id"), primary_key=True)
    destinatari = db.Column(db.String(100))

    __mapper_args__ = {
        "polymorphic_identity": "igiene"
    }


class BeneMobilita(Bene):
    __tablename__ = "beni_mobilita"

    id = db.Column(db.Integer, db.ForeignKey("beni.id"), primary_key=True)
    tipo_mobilita = db.Column(db.String(100))
    stato = db.Column(db.String(100))

    __mapper_args__ = {
        "polymorphic_identity": "mobilita"
    }



#DONAZIONE DI BENI

class DonazioneBene(db.Model):
    __tablename__ = "donazioni_beni"

    id = db.Column(db.Integer, primary_key=True)

    donatore_id = db.Column(db.Integer, db.ForeignKey("account_donatori.id"), nullable=False)
    ente_erogatore_id = db.Column(db.Integer, db.ForeignKey("account_enti_erogatori.id"), nullable=False)
    bene_id = db.Column(db.Integer, db.ForeignKey("beni.id"), nullable=False)
    punto_id = db.Column(db.Integer, db.ForeignKey("punti_distribuzione.id"), nullable=False)

    data = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    donatore = db.relationship("AccountDonatore", back_populates="donazioni_beni")
    ente_erogatore = db.relationship("AccountEnteErogatore", back_populates="donazioni_beni")
    bene = db.relationship("Bene", back_populates="donazioni_beni")
    punto = db.relationship("PuntoDistribuzione")



#DONAZIONE MONETARIA

class DonazioneMonetaria(db.Model):
    __tablename__ = "donazioni_monetarie"

    id = db.Column(db.Integer, primary_key=True)

    donatore_id = db.Column(db.Integer, db.ForeignKey("account_donatori.id"), nullable=False)
    ente_id = db.Column(db.Integer, db.ForeignKey("account_enti_erogatori.id"), nullable=False)

    importo = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    donatore = db.relationship("AccountDonatore", back_populates="donazioni_monetarie")
    ente = db.relationship("AccountEnteErogatore", back_populates="donazioni_monetarie")



#PRENOTAZIONE

class Prenotazione(db.Model):
    __tablename__ = "prenotazioni"

    id = db.Column(db.Integer, primary_key=True)

    beneficiario_id = db.Column(db.Integer, db.ForeignKey("account_beneficiari.id"), nullable=False)
    bene_id = db.Column(db.Integer, db.ForeignKey("beni.id"), nullable=False)
    punto_id = db.Column(db.Integer, db.ForeignKey("punti_distribuzione.id"), nullable=False)       #nel RAD non c'è

    data_prenotazione = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    stato = db.Column(db.String(50), nullable=False, default="in_attesa")
    codice_qr = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    beneficiario = db.relationship("AccountBeneficiario", back_populates="prenotazioni")
    bene = db.relationship("Bene", back_populates="prenotazioni")
    punto = db.relationship("PuntoDistribuzione", back_populates="prenotazioni")



#FEEDBACK

class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    recensione = db.Column(db.Text, nullable=True)
    valutazione = db.Column(db.Integer, nullable=False)

    beneficiario_id = db.Column(db.Integer, db.ForeignKey("account_beneficiari.id"), nullable=False)
    punto_id = db.Column(db.Integer, db.ForeignKey("punti_distribuzione.id"), nullable=False)

    beneficiario = db.relationship("AccountBeneficiario", back_populates="feedback")
    punto = db.relationship("PuntoDistribuzione", back_populates="feedback")



