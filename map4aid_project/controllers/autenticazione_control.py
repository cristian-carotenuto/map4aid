from flask import request, jsonify
from controllers.routes import auth_bp


@auth_bp.route("/register", methods=["POST"])
def register():
    from controllers.service_email.email_control_bridge import EmailControlAdapter
    from controllers.auth_facade import AuthFacade

    facade = AuthFacade(EmailControlAdapter())

    try:
        facade.register_pending_account(request.form)
        return jsonify({"message": "Email inviata. Controlla la tua casella."}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500