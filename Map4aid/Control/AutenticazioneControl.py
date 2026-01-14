from flask import Flask, request, session, jsonify
import hashlib
from Model import *

app = Flask(__name__)
app.secret_key = "9fA!2xZ$kL8@Pq7#sW"

@app.route("/register", methods=["POST"])
def register():
    ruolo = request.form.get("ruolo")
    email = request.form.get("email")
    password = request.form.get("password")

    if not ruolo or not email or not password:
        return jsonify({"error": "Campi obbligatori mancanti"}), 400

    if email in db:
        return jsonify({"error": "Email già registrata"}), 409

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # ----- BENEFICIARIO -----
    if ruolo == "beneficiario":
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")

        if not nome or not cognome:
            return jsonify({"error": "Dati beneficiario incompleti"}), 400

        user = AccountBeneficiario(email, password_hash, nome, cognome)

    # ----- DONATORE -----
    elif ruolo == "donatore":
        partita_iva = request.form.get("partita_iva")
        categoria = request.form.get("categoria")
        nome_attivita = request.form.get("nome_attivita")
        indirizzo_sede = request.form.get("indirizzo_sede")
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")

        if not all([partita_iva, categoria, nome_attivita,
                    indirizzo_sede, nome, cognome]):
            return jsonify({"error": "Dati donatore incompleti"}), 400

        user = AccountDonatore(
            email, password_hash, partita_iva, categoria,
            nome_attivita, indirizzo_sede, nome, cognome
        )

    # ----- ENTE EROGATORE -----
    elif ruolo == "erogatore":
        nome_org = request.form.get("nome_organizzazione")
        indirizzo_sede = request.form.get("indirizzo_sede")
        tipologia = request.form.get("tipologia_ente")
        iban = request.form.get("iban")

        if not all([nome_org, indirizzo_sede, tipologia, iban]):
            return jsonify({"error": "Dati ente erogatore incompleti"}), 400

        user = AccountEnteErogatore(
            email, password_hash, nome_org,
            indirizzo_sede, tipologia, iban
        )

    else:
        return jsonify({"error": "Ruolo non valido"}), 400

    # Salvataggio (mock DB)
    db[email] = user.__dict__

    return jsonify({
        "message": "Registrazione avvenuta con successo",
        "email": email,
        "ruolo": ruolo
    }), 201