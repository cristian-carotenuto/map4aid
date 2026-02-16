import os
import requests
import json

from difflib import SequenceMatcher
from pathlib import Path
from flask import Flask, request, jsonify, render_template
from flask_login import LoginManager

from config import db, migrate
from models import Account
from tasks import start_scheduler

DATASET_PATH = Path(__file__).parent / "chatbot" / "data" / "training_data_expanded.jsonl"


def _normalize(s: str) -> str:
    return " ".join((s or "").strip().lower().split())


def load_qa_pairs(jsonl_path: Path):
    pairs = []
    with jsonl_path.open("r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            msgs = obj.get("messages", [])
            user = next((m.get("content") for m in reversed(msgs) if m.get("role") == "user"), None)
            assistant = next((m.get("content") for m in reversed(msgs) if m.get("role") == "assistant"), None)
            if user and assistant:
                pairs.append((_normalize(user), assistant.strip()))

    uniq = {}
    for q, a in pairs:
        uniq[q] = a
    return list(uniq.items())


def best_match_answer(query: str, qa_pairs, threshold: float = 0.75):
    qn = _normalize(query)
    best_score, best_ans = 0.0, None
    for q, ans in qa_pairs:
        score = SequenceMatcher(None, qn, q).ratio()
        if score > best_score:
            best_score, best_ans = score, ans
    if best_score >= threshold:
        return best_ans, best_score
    return None, best_score


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder="html"
    )

    os.makedirs(app.instance_path, exist_ok=True)

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{app.instance_path}/database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "skMomentanea"

    db.init_app(app)
    migrate.init_app(app, db)

    from models import models  # noqa: F401
    from models import pendingAccounts  # noqa: F401

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Account.query.get(int(user_id))

    # carica dataset UNA volta all'avvio
    qa_pairs = load_qa_pairs(DATASET_PATH)

    from controllers.routes import auth_bp
    from controllers import admin_control  # noqa: F401
    from controllers import two_fa_contol  # noqa: F401
    from controllers import autenticazione_control  # noqa: F401
    from controllers import login_control  # noqa: F401
    from controllers import segnalazione_control  # noqa: F401
    from controllers import donazione_monetaria_control  # noqa: F401
    from controllers import donazione_bene  # noqa: F401
    from controllers import permessi  # noqa: F401
    from controllers import api_punti
    from controllers import pdf_service  # noqa: F401
    from controllers import prenotazione_control  # noqa: F401
    from controllers import profilo_control  # noqa: F401
    from controllers import feedback_control  # noqa: F401
    from controllers import gestione_scorte_control  # noqa: F401
    from controllers.feedback_control import feedback_bp

    app.register_blueprint(feedback_bp)
    app.register_blueprint(api_punti.api, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    QWEN_URL = "http://127.0.0.1:8000/chat"

    @app.post("/api/chat")
    def api_chat():
        data = request.get_json(silent=True) or {}
        message = (data.get("message") or "").strip()
        history = data.get("history") or []

        if not message:
            return jsonify({"reply": "Scrivi un messaggio."}), 400

        # 1) prova risposta canonica dal dataset
        ans, score = best_match_answer(message, qa_pairs, threshold=0.78)
        if ans:
            return jsonify({"reply": ans, "source": "dataset", "score": score})

        # 2) fallback a Qwen
        try:
            r = requests.post(QWEN_URL, json={"message": message, "history": history}, timeout=60)
            r.raise_for_status()
            out = r.json()
            return jsonify({"reply": out.get("reply", ""), "source": "qwen", "score": score})
        except Exception:
            return jsonify({"reply": "Errore: servizio Aidano non raggiungibile."}), 502

    print(">>>>>Flask root:", os.getcwd())

    @app.route("/")
    def home():
        return render_template("home.html")

    if os.environ.get("WERKZEUG_RUN_MAIN") == "true" or not app.debug:
        start_scheduler(app)

    return app
