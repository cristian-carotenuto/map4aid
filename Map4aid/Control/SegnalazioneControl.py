from flask import Flask, request, session, jsonify

from Map4aid.Control.EmailControl import EmailControl

app = Flask(__name__)
app.secret_key = "9fA!2xZ$kL8@Pq7#sW"
@app.route("/segnalazione", methods=["POST"])
def segnalazione():
    data = request.get_json()

    indirizzo = data["indirizzo"]
    email_ente = data["email_ente"]

    email_ok = EmailControl.invia_email_segnalazione(email_ente, indirizzo)


    if email_ok:
        return {
            "successo": True,
            "messaggio": "Segnalazione completata con successo"
        }
    else:
        return {
            "successo": False,
            "messaggio": "Segnalazione non avvenuta"
        }





