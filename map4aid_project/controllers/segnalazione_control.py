from flask import Flask, request, session, jsonify, Blueprint
from controllers.routes import auth_bp
from controllers.EmailControl import EmailControl
from models.models import AccountEnteErogatore

@auth_bp.route("/segnalazione", methods=["POST"])
def segnalazione():
    data = request.get_json()
    lat = data["latitudine"]
    lon = data["longitudine"]
    indirizzo = data["indirizzo"]
    email_control = EmailControl()
    resoconto = {
        "successo": True,
        "email_non_inviate": []
    }
    enti_erogatori = AccountEnteErogatore.query.all()
    for ente in enti_erogatori:
        email_ok = email_control.invia_email_segnalazione(ente.email,indirizzo,lat,lon)
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




