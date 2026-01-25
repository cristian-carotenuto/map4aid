from datetime import timezone, datetime

from flask import request, session, Blueprint
from controllers.routes import auth_bp
from models import models, AccountEnteErogatore
from EmailControl import EmailControl
from Permessi import require_roles
from config import db
from models.models import AccountDonatore, DonazioneMonetaria


@auth_bp.route("/donazioneMonetaria", methods=["POST"])
@require_roles("ente_donatore")
def donazione_monetaria():
        # ---- DATI DA SESSIONE ----
    email_donatore = session.get("user_email")

    # ---- DATI DA FORM ----
    nome_ente = request.form.get("nome_ente_erogatore")
    numero_carta = request.form.get("numero_carta")
    scadenza = request.form.get("scadenza")
    cvv = request.form.get("cvv")

    try:
        importo = float(request.form.get("importo"))
    except (TypeError, ValueError):
        return {"successo": False, "errore": "Importo non valido"}

    ente_erogatore = AccountEnteErogatore.query.filter_by(nome_organizzazione=nome_ente).first()
    ente_donatore = AccountDonatore.query.filter_by(email=email_donatore).first()
    email_ente = ente_erogatore.email
    iban_ente = ente_erogatore.iban

    # ---- VALIDAZIONE ----
    if not all([email_ente, iban_ente, numero_carta, scadenza, cvv]):
        return {"successo": False, "errore": "Dati obbligatori mancanti"}

    if importo <= 0:
        return {"successo": False, "errore": "Importo non valido"}

    # ---- TRANSAZIONE MONETARIA ----
    transazione_ok = esegui_transazione(
        numero_carta, scadenza, cvv, iban_ente, importo
    )

    if not transazione_ok:
        return {"successo": False, "errore": "Transazione rifiutata"}

    # ---- CREAZIONE ENTITY ----
    donazione = DonazioneMonetaria(
        id_donatore=ente_donatore.id,
        id_erogatore=ente_erogatore.id,
        importo=importo,
        data =  datetime.now(timezone.utc)
    )

    db.session.add(donazione)
    db.session.commit()

    # ---- EMAIL DI CONFERMA ----
    email_ok = EmailControl.invia_email_donazione(
        email_ente=email_ente,
        nome_ente=nome_ente,
        email_donatore=email_donatore,
        importo=importo,
        data=donazione.data
    )

    if not email_ok:
        return {
            "successo": False,
            "errore": "Donazione eseguita ma email non inviata"
        }

    return {
        "successo": True,
        "messaggio": "Donazione monetaria completata con successo"
    }


def esegui_transazione(self, numero_carta, scadenza, cvv,
                        iban_destinatario, importo):
    print("transazione in elaborazione")
    if len(numero_carta) != 16:
        return False
    if len(cvv) != 3:
        return False
    if not iban_destinatario.startswith("IT"):
        return False
    return True

