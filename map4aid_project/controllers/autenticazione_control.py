from flask import request, jsonify
<<<<<<< HEAD
from controllers.routes import auth_bp
=======

from config import db
from controllers.permessi import require_roles
from controllers.routes import auth_bp
from models import AccountBeneficiario
>>>>>>> controller


@auth_bp.route("/register", methods=["POST"])
def register():
<<<<<<< HEAD
    from controllers.service_email.email_control_adapter import EmailControlAdapter
    from controllers.auth_facade import AuthFacade

    facade = AuthFacade(EmailControlAdapter())

    try:
        facade.register_pending_account(request.form)
=======
    from controllers.service_email.email_control_bridge import EmailControlBridge
    from controllers.auth_facade import AuthFacade

    facade = AuthFacade(EmailControlBridge())

    try:
        facade.register_pending_account(request.form,request.files)
>>>>>>> controller
        return jsonify({"message": "Email inviata. Controlla la tua casella."}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except RuntimeError as e:
<<<<<<< HEAD
        return jsonify({"error": str(e)}), 500
=======
        return jsonify({"error": str(e)}), 500

@auth_bp.route("/admin_register", methods=["POST"])
#@require_roles("admin")
def admin_register():
    id_utente = int(request.form.get("id_utente"))
    utente = AccountBeneficiario.query.filter_by(id=id_utente).first()
    accettato = request.form.get("accettato")

    if not utente:
        return jsonify({"error": "Utente non trovato"}), 404

    if accettato == "True":
        utente.accettato = True
        db.session.add(utente)
        db.session.commit()
        return jsonify({"message": "Utente registrato"}), 200

    db.session.delete(utente)
    db.session.commit()
    return jsonify({"message": "Utente rifiutato dall'admin"}), 200

>>>>>>> controller
