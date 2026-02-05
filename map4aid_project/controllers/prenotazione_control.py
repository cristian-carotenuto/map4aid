from datetime import timezone, datetime
from flask import request, session, jsonify
from werkzeug.utils import secure_filename
import os
from controllers.prenotazione_checker import PrenotazioneChecker
from controllers.routes import auth_bp
from controllers.service_email.email_control_bridge import EmailControlBridge
from models import AccountEnteErogatore
from controllers.permessi import require_roles
from config import db
from models.models import AccountDonatore, DonazioneMonetaria, BeneAlimentare, Bene, PaccoAlimentare, \
    PuntoDistribuzione, Prenotazione, AccountBeneficiario, SottoCategoria
import threading

prenotazione_lock = threading.Lock()
annulla_lock = threading.Lock()

@auth_bp.route("/prenotazione", methods=["POST"])
@require_roles("beneficiario")
def prenotazione():
    with prenotazione_lock:  # <-- solo un thread alla volta entra qui
        UPLOAD_FOLDER = "uploads/ricette"
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        ricetta_path = None

        id_punto_bisogno = request.form.get("id_punto_bisogno")
        is_pacco = request.form.get("is_pacco")
        user_email = session["user_email"]
        is_medicinale = request.form.get("is_medicinale")


        punto_distribuzione = PuntoDistribuzione.query.filter_by(id=id_punto_bisogno).first()
        id_ente = punto_distribuzione.ente_erogatore_id
        ente = AccountEnteErogatore.query.filter_by(id=id_ente).first()
        beneficiario = AccountBeneficiario.query.filter_by(email=user_email).first()
        checker = PrenotazioneChecker(beneficiario)


        mail_sender = EmailControlBridge()

        #Check per le prenotazione
        if is_pacco == "True":
            if is_craftable(id_punto_bisogno):

                try:
                    checker.check("pacco")
                except Exception as e:
                    return jsonify({"error": str(e)}), 200

                pane = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="pane").first()
                pasta = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="pasta").first()
                carne = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="carne").first()
                acqua = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="acqua").first()
                pesce = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="pesce").first()
                verdura = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="verdura").first()
                pacco = PaccoAlimentare(pasta,pane,acqua,carne,pesce,verdura)
                db.session.add(pacco)
                db.session.commit()
                prenotazione = Prenotazione(
                    beneficiario_id = beneficiario.id,
                    bene_id = None,
                    punto_id = punto_distribuzione.id,
                    pacco_id = pacco.id,
                )
                db.session.add(prenotazione)
                pane.quantita -= 1
                pasta.quantita -= 1
                carne.quantita -= 1
                acqua.quantita -= 1
                pesce.quantita -= 1
                db.session.commit()

                email_ok1 = mail_sender.send_prenotazione_beneficiario(
                    ente.email,
                    user_email,
                    punto_distribuzione.
                    indirizzo,
                    punto_distribuzione.latitude,
                    punto_distribuzione.longitude,
                    prenotazione.id
                    )
                email_ok2 = mail_sender.send_prenotazione_ente(
                    ente.email,
                    user_email,
                    punto_distribuzione.
                    indirizzo,
                    punto_distribuzione.latitude,
                    prenotazione.id
                )
                if email_ok1 and email_ok2:
                    return jsonify({"message": "Prenotazione effetuata"}), 200
                return jsonify({"error": "Prenotazione effetuata ma email non inviata"}), 400

            #Il pacco non è disponibile
            return jsonify({"error": "Prenotazione non effetuata,beni non diponibili"}), 400

        # Controlliamo se ha caricato la ricetta
        if is_medicinale == "True":
            if "ricetta" not in request.files:
                return jsonify({"error": "Ricetta medica mancante"}), 400

            ricetta = request.files["ricetta"]

            if ricetta.filename == "":
                return jsonify({"error": "File ricetta non valido"}), 400

            filename = secure_filename(ricetta.filename)
            ricetta_path = os.path.join(UPLOAD_FOLDER, filename)
            ricetta.save(ricetta_path)

        #L'utente ha prenotato un bene
        id_bene = request.form.get("id_bene")
        bene = Bene.query.filter_by(id=id_bene).first()
        prenotazione = Prenotazione(
            beneficiario_id=beneficiario.id,
            bene_id=bene.id,
            punto_id=punto_distribuzione.id,
            pacco_id=None,
        )
        bene.quantita -= 1
        bene.save()
        db.session.add(prenotazione)
        db.session.commit()

        email_ok1 = mail_sender.send_prenotazione_beneficiario(
            ente.email,
            user_email,
            punto_distribuzione.
            indirizzo,
            punto_distribuzione.latitude,
            punto_distribuzione.longitude,
            prenotazione.id,
            bene.nome,
        )
        email_ok2 = mail_sender.send_prenotazione_ente(
            ente.email,
            user_email,
            punto_distribuzione.
            indirizzo,
            punto_distribuzione.latitude,
            prenotazione.id,
            bene.nome,
            ricetta_path
        )

        if email_ok1 and email_ok2:
            return jsonify({"message": "Prenotazione effetuata"}), 200
        return jsonify({"error": "Prenotazione effetuata ma email non inviata"}), 400


@auth_bp.route("/conferma_prenotazione", methods=["GET"])
def conferma_prenotazione():
    id = request.args.get("id_prenotazione")
    prenotazione = Prenotazione.query.filter_by(id=id).first()
    prenotazione.stato = "Completata"
    db.session.commit()
    return jsonify({"message": "Prenotazione ritirata"}), 200

@auth_bp.route("/cancella_prenotazione", methods=["POST"])
@require_roles("ente_erogatore")
def cancella_prenotazione():
    with annulla_lock:  # <-- solo un thread alla volta entra qui
        id = request.form.get("id_prenotazione")
        prenotazione = Prenotazione.query.filter_by(id=id).first()

        if prenotazione.stato == "Completata":
            return jsonify({"error": "Impossibile cancellare prenotazione già ritirata"}), 400

        if prenotazione.pacco_id is not None:
            pacco = PaccoAlimentare.query.filter_by(id=prenotazione.pacco_id).first()
            pasta = PaccoAlimentare.query.filter_by(id=pacco.pasta).first()
            pane = PaccoAlimentare.query.filter_by(id=pacco.pane).first()
            acqua = PaccoAlimentare.query.filter_by(id=pacco.acqua).first()
            carne = PaccoAlimentare.query.filter_by(id=pacco.carne).first()
            pesce = PaccoAlimentare.query.filter_by(id=pacco.pesce).first()
            verdura = PaccoAlimentare.query.filter_by(id=pacco.verdura).first()
            pasta.quantita += 1
            pane.quantita += 1
            acqua.quantita += 1
            carne.quantita += 1
            pesce.quantita += 1
            verdura.quantita += 1
            db.session.delete(prenotazione)
            db.session.commit()
            return jsonify({"message": "Prenotazione cancellata"}), 200

        bene = Bene.query.filter_by(id=prenotazione.bene_id).first()
        bene.quantita += 1
        db.session.delete(prenotazione)
        db.session.commit()
        return jsonify({"message": "Prenotazione cancellata"}), 200
    


def is_craftable(id_punto_bisogno):
    punto = PuntoDistribuzione.query.filter_by(id=id_punto_bisogno).first()
    if not punto:
        return False

    SOTTOCATEGORIE_PACCO = ["Pasta", "Pane", "Acqua", "Carne", "Pesce", "Verdura"]

    for nome_sottocateg in SOTTOCATEGORIE_PACCO:
        sottocateg = SottoCategoria.query.filter_by(nome=nome_sottocateg).first()
        if not sottocateg:
            return False

        bene = Bene.query.filter_by(punto_distribuzione_id=id_punto_bisogno, sottocategoria_id=sottocateg.id).first()

        if not bene or bene.quantita < 1:
            return False

    return True
