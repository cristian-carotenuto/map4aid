from functools import wraps
from flask import jsonify, session
from flask_login import current_user

#permessi su ruolo db
def require_roles(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                return jsonify({"error": "Non autenticato"}), 401

            if current_user.tipo not in roles:
                return jsonify({"error": "Permessi insufficienti"}), 403

            return f(*args, **kwargs)
        return wrapper
    return decorator


#permessi admin su sessione
def require_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("is_admin"):
            return jsonify({"error": "Accesso non autorizzato"}), 403
        return f(*args, **kwargs)
    return wrapper
