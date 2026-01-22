from functools import wraps
from flask import jsonify
from sqlalchemy.sql.functions import current_user


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