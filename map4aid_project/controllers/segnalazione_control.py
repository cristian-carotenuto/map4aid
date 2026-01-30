from flask import request

from controllers.permessi import require_roles
from controllers.routes import auth_bp
from controllers.service_email.EmailControl import EmailControl
from controllers.service_email.email_control_bridge import EmailControlAdapter
from models.models import AccountEnteErogatore

@auth_bp.route("/segnalazione", methods=["POST"])
def segnalazione():
    data = request.get_json()
    lat = data["latitudine"]
    lon = data["longitudine"]
    indirizzo = data["indirizzo"]
    mail_sender = EmailControlAdapter()
    resoconto = {
        "successo": True,
        "email_non_inviate": []
    }
    enti_erogatori = AccountEnteErogatore.query.all()
    for ente in enti_erogatori:
        email_ok = mail_sender.send_segnalazione(
            email_ente=ente.email,
            indirizzo=indirizzo,
            lat=lat,
            lon=lon
        )
        if not email_ok:
            resoconto["successo"] = False
            resoconto["email_non_inviate"].append(ente.email)



    if resoconto["successo"]:
        return {
            "successo": True,
            "messaggio": "Segnalazione completata con successo"
        }
    else:
        return {
            "successo": False,
            "messaggio": "Segnalazione non avvenuta con successo",
            "email_non_inviate": resoconto["email_non_inviate"]
        }




