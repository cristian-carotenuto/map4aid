from flask import Flask, request, session, jsonify
from Model import *

from Map4aid.Control.EmailControl import EmailControl

app = Flask(__name__)
app.secret_key = "9fA!2xZ$kL8@Pq7#sW"

@app.route("/donazioneMonetaria", methods=["POST"])
def donazione_monetaria():
    if "logged_in" not in session:
        return {"successo": False, "errore": "Utente non autenticato"}

        # ---- DATI DA SESSIONE ----
    email_donatore = session.get("user_email")

    # ---- DATI DA FORM ----
    nome_ente = request.form.get("ente")
    numero_carta = request.form.get("numero_carta")
    scadenza = request.form.get("scadenza")
    cvv = request.form.get("cvv")

    try:
        importo = float(request.form.get("importo"))
    except (TypeError, ValueError):
        return {"successo": False, "errore": "Importo non valido"}

    #Bisogna prendere l'email e l'iban del'ente dal database tramite nome

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
        id_donatore=email_donatore,
        id_erogatore=iban_ente,
        importo=importo
    )

    #Da aggiungere nel database

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


