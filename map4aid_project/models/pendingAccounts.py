from werkzeug.security import generate_password_hash, check_password_hash

from config import db
from datetime import datetime, timezone, timedelta


class PendingAccount(db.Model):
    __tablename__ = "pending_accounts"

    id = db.Column(db.Integer, primary_key=True)

    # token di verifica
    token = db.Column(db.String(64), unique=True, nullable=False, index=True)

    # dati comuni Account
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(255), nullable=True)
    tipo = db.Column(db.String(50), nullable=True)

    # dati specifici del tipo (beneficiario, ente, ecc.)
    extra_data = db.Column(db.JSON, nullable=True)
    expires_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc) + timedelta(minutes=10))
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    # gestione password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)