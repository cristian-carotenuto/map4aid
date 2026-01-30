from datetime import timezone, datetime

from flask import request, session
from controllers.routes import auth_bp
from controllers.service_email.email_control_bridge import EmailControlAdapter
from models import AccountEnteErogatore
from controllers.permessi import require_roles
from config import db
from models.models import AccountDonatore, DonazioneMonetaria


@auth_bp.route("/donazioneMonetaria", methods=["POST"])
@require_roles("donatore","beneficiario","ente_erogatore")
def donazione_monetaria():
        # ---- DATI DA SESSIONE ----
    email_donatore = session.get("user_email")

    # ---- DATI DA FORM ----
    nome_ente = request.form.get("nome_ente_erogatore")
    numero_carta = request.form.get("numero_carta")
    scadenza_str = request.form.get("scadenza")
    scadenza = datetime.strptime(scadenza_str, "%Y-%m-%d").date()
    cvv = request.form.get("cvv")
    mail_sender = EmailControlAdapter()

    importo = 0
    try:
        importo = float(request.form.get("importo"))
    except (TypeError, ValueError):
        return {"errore": "Importo non valido"},400

    ente_erogatore = AccountEnteErogatore.query.filter_by(nome_organizzazione=nome_ente).first()
    ente_donatore = AccountDonatore.query.filter_by(email=email_donatore).first()
    email_ente = ente_erogatore.email
    iban_ente = ente_erogatore.iban

    # ---- VALIDAZIONE ----
    if not all([email_ente, iban_ente, numero_carta, scadenza, cvv]):
        return {"errore": "Dati obbligatori mancanti"},400

    if importo <= 0:
        return {"errore": "Importo non valido"},400

    # ---- TRANSAZIONE MONETARIA ----
    transazione_ok = esegui_transazione(
        numero_carta, scadenza, cvv, iban_ente, importo
    )

    if not transazione_ok:
        return {"successo": False, "errore": "Transazione rifiutata"},400

    # ---- CREAZIONE ENTITY ----
    donazione = DonazioneMonetaria(
        donatore_id=ente_donatore.id,
        ente_id=ente_erogatore.id,
        importo=importo,
        data =  datetime.now(timezone.utc)
    )

    db.session.add(donazione)
    db.session.commit()

    # ---- EMAIL DI CONFERMA ----
    email_ok = mail_sender.send_donazione_monetaria(
        email_ente=email_ente,
        nome_ente=nome_ente,
        email_donatore=email_donatore,
        importo=importo,
        data=donazione.data
    )

    if not email_ok:
        return {
            "errore": "Donazione eseguita ma email non inviata"
        },400

    return {
        "messaggio": "Donazione monetaria completata con successo"
    },200


def esegui_transazione(numero_carta, scadenza, cvv,
                        iban_destinatario, importo):
    print("transazione in elaborazione")
    if len(numero_carta) != 16:
        return False
    if len(cvv) != 3:
        return False
    if not iban_destinatario.startswith("IT"):
        return False
    if scadenza < datetime.now(timezone.utc):
        return False
    return True

