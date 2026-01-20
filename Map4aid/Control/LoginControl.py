from flask import Flask, request, session, jsonify
import hashlib
from Model import *
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