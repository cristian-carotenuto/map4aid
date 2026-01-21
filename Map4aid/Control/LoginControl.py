import random

from flask import Flask, request, session, jsonify
import hashlib
from Model import *

from Map4aid.Control.EmailControl import EmailControl

app = Flask(__name__)
app.secret_key = "9fA!2xZ$kL8@Pq7#sW"

# ---- LOGIN ----
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"error": "Email e password obbligatorie"}), 400

    user = Db.get(email)

    if not user:
        return jsonify({"error": "Credenziali non valide"}), 401

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    if password_hash != user["password_hash"]:
        return jsonify({"error": "Credenziali non valide"}), 401

    #  Salvataggio sessione
    session["logged_in"] = True
    session["user_email"] = email

    return jsonify({
        "message": "Login effettuato con successo",
        "email": email
    })

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logout effettuato"})

@app.route("/recuperoPassword", methods=["POST"])
def recuperoPassword():
    email = request.form.get("email")
    session["user_email"] = email
    codice = int(random.uniform(1000,9999))
    session["codice"] = codice
    EmailControl.invia_email_recupero(email, codice)
    #Invia l'utente alla page in cui deve inserire il codice

@app.route("/confermaRecupero", methods=["POST"])
def confermaRecupero():
    codice = session["codice"]
    email = session["user_email"]
    codice_inserito = request.form.get("codice")
    if(codice == codice_inserito):
        #Predni password dal database e mostrala
        print("password recuperata")
    else:
        return jsonify({"errore": "Codice non valido"}), 401
