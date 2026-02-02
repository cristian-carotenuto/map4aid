from flask import request, jsonify
from config import db
from controllers.permessi import require_roles
from controllers.routes import auth_bp
from models import AccountBeneficiario
from flask_login import current_user, login_required


@auth_bp.route("/register", methods=["POST"])
def register():
    from controllers.service_email.email_control_bridge import EmailControlBridge
    from controllers.auth_facade import AuthFacade

    facade = AuthFacade(EmailControlBridge())

    try:
        facade.register_pending_account(request.form,request.files)
        return jsonify({"message": "Email inviata. Controlla la tua casella."}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except RuntimeError as e:
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

