from flask import request

from controllers.permessi import require_roles
from controllers.routes import auth_bp
from controllers.service_email.EmailControl import EmailControl
from controllers.service_email.email_control_bridge import EmailControlBridge
from models.models import AccountEnteErogatore

@auth_bp.route("/segnalazione", methods=["POST"])
def segnalazione():
    lat = request.form.get("latitudine")
    lon = request.form.get("longitudine")
    indirizzo = request.form.get("indirizzo")

    if not lat or not lon or not indirizzo:
        return {
            "successo": False,
            "messaggio": "Dati mancanti: latitudine, longitudine e indirizzo sono obbligatori"
        }, 400

    mail_sender = EmailControlBridge()
    enti_erogatori = AccountEnteErogatore.query.all()
    
    for ente in enti_erogatori:
        # Esegue l'invio ma ignora se l'esito è True o False
        mail_sender.send_segnalazione(
            email_ente=ente.email,
            indirizzo=indirizzo,
            lat=lat,
            lon=lon
        )
   

    return {
        "successo": True,
        "messaggio": "Segnalazione completata con successo"
    }
   