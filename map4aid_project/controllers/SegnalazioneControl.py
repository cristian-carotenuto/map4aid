from flask import Flask, request, session, jsonify, Blueprint
from controllers.routes import auth_bp
from EmailControl import EmailControl


@auth_bp.route("/segnalazione", methods=["POST"])
def segnalazione():
    data = request.get_json()

    indirizzo = data["indirizzo"]
    email_ente = data["email_ente"]
    email_control = EmailControl()
    email_ok = email_control.invia_email_segnalazione(email_ente, indirizzo)


    if email_ok:
        #Creazione di un nuovo punto di bisogno con stato in attessa
        return {
            "successo": True,
            "messaggio": "Segnalazione completata con successo"
        }
    else:
        return {
            "successo": False,
            "messaggio": "Segnalazione non avvenuta"
        }




