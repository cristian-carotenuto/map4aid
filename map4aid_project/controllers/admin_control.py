from flask import request, session, jsonify
from controllers.routes import auth_bp
from controllers.permessi import require_admin
from functools import wraps
from config import ADMIN_EMAIL, ADMIN_CODE, db
from controllers.service_email.email_control_bridge import EmailControlBridge
from models import AccountBeneficiario


#login
@auth_bp.route("/adminLogin", methods=["POST"])
def admin_login():

    if session.get("is_admin"):
        return jsonify({"error": "Già loggato come admin"}), 400

    email = request.form.get("email")
    codice = request.form.get("codice")

    if not email or not codice:
        return jsonify({"error": "Campi mancanti"}), 400

    if email == ADMIN_EMAIL and codice == ADMIN_CODE:
        session.clear()
        session["logged_in"] = True
        session["is_admin"] = True
        session["user_email"] = email

        return jsonify({"message": "Accesso admin effettuato"}), 200

    return jsonify({"error": "Credenziali non valide"}), 401



#logout
@auth_bp.route("/adminLogout", methods=["POST"])
@require_admin
def admin_logout():
    session.clear()
    return jsonify({"message": "Logout admin effettuato"}), 200



#dashbord da continuare
@auth_bp.route("/admin/dashboard", methods=["GET"])
@require_admin
def admin_dashboard():
    return jsonify({"message": "Benvenuto nel pannello admin"}), 200

#funzione per accetare registrazioni
@auth_bp.route("/admin/conferma_regitrazione", methods=["POST"])
@require_admin
def admin_confirm():
    id_beneficiario = session.get("id_beneficiario")
    esito = session.get("esito")#True se l'account è stato confermato,altrimenti viene cancellato
    account = AccountBeneficiario.query.filter_by(id=id_beneficiario).first()

    if esito == "True":
        account.accettato = True
        db.session.commit()
    else:
        db.session.delete(account)
        db.session.commit()

    mail_sender = EmailControlBridge()
    email_ok=mail_sender.send_conferma_registrazione(account.email,esito)


    if email_ok:
        return jsonify({"message": "Email inviata"}), 200
    return jsonify({"error": "Email non inviata"}), 400





