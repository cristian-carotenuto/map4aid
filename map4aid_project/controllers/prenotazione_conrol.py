from datetime import timezone, datetime
from flask import request, session
from controllers.routes import auth_bp
from controllers.service_email.email_control_bridge import EmailControlAdapter
from models import AccountEnteErogatore
from controllers.permessi import require_roles
from config import db
from models.models import AccountDonatore, DonazioneMonetaria


@auth_bp.route("/prenotazione", methods=["POST"])
@require_roles("beneficiario")
def prenotazione():