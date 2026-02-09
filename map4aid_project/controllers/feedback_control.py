from flask import Blueprint, request, jsonify, current_app
from sqlalchemy.exc import SQLAlchemyError

from config import db
from models.models import Feedback, Prenotazione, AccountBeneficiario

feedback_bp = Blueprint("feedback", __name__, url_prefix="/api/feedback")


class FeedbackError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


def _sanitize_review(recensione: str | None) -> str | None:
    if recensione is None:
        return None
    recensione = recensione.strip()
    return recensione if recensione else None


class FeedbackService:
    @staticmethod
    def create_feedback(user_email: str, id_prenotazione: int, valutazione: int, recensione: str | None):
        beneficiario = AccountBeneficiario.query.filter_by(email=user_email).first()
        if not beneficiario:
            raise FeedbackError("Beneficiario non trovato", 404)

        prenotazione = Prenotazione.query.get(id_prenotazione)
        if not prenotazione:
            raise FeedbackError("Prenotazione non trovata", 404)

        if prenotazione.beneficiario_id != beneficiario.id:
            raise FeedbackError("Non autorizzato per questa prenotazione", 403)

        if prenotazione.stato != "ritirata":
            raise FeedbackError("Feedback consentito solo dopo il ritiro completato", 400)

        existing = Feedback.query.filter_by(prenotazione_id=prenotazione.id).first()
        if existing:
            raise FeedbackError("Feedback già inviato per questa prenotazione", 409)

        recensione = _sanitize_review(recensione)

        try:
            feedback = Feedback(
                recensione=recensione,
                valutazione=valutazione,
                prenotazione_id=prenotazione.id,
            )

            feedback.prenotazione = prenotazione

            db.session.add(feedback)
            db.session.commit()

            return feedback.id
        except SQLAlchemyError as e:
            db.session.rollback()
            current_app.logger.exception("Errore DB durante creazione feedback")
            raise FeedbackError("Errore interno del server", 500) from e


@feedback_bp.route("", methods=["POST"])
def create_feedback():
    try:
        data = request.get_json() or {}

        user_email = data.get("user_email")
        id_prenotazione = data.get("id_prenotazione")
        valutazione = data.get("valutazione")
        recensione = data.get("recensione")

        if not user_email:
            raise FeedbackError("Utente non autenticato", 401)

        if not id_prenotazione or not isinstance(id_prenotazione, int):
            raise FeedbackError("id_prenotazione non valido", 400)

        if not isinstance(valutazione, int) or not (1 <= valutazione <= 5):
            raise FeedbackError("valutazione deve essere un intero tra 1 e 5", 400)

        feedback_id = FeedbackService.create_feedback(
            user_email=user_email,
            id_prenotazione=id_prenotazione,
            valutazione=valutazione,
            recensione=recensione,
        )

        return jsonify({"feedback_id": feedback_id}), 201

    except FeedbackError as e:
        return jsonify({"error": e.message}), e.status_code

    except Exception:
        current_app.logger.exception("Errore inatteso in /feedback")
        return jsonify({"error": "Errore interno del server"}), 500
