from datetime import timezone, datetime
from flask import request, session, jsonify
from werkzeug.utils import secure_filename
import os
import threading

from geopy.geocoders import Nominatim       

from controllers.prenotazione_checker import PrenotazioneChecker
from controllers.routes import auth_bp
from controllers.service_email.email_control_bridge import EmailControlBridge
from models import AccountEnteErogatore
from controllers.permessi import require_roles
from config import db
from models.models import (
    AccountDonatore,
    DonazioneMonetaria,
    BeneAlimentare,
    Bene,
    PaccoAlimentare,
    PuntoDistribuzione,
    Prenotazione,
    AccountBeneficiario,
    SottoCategoria,
    Account
)

prenotazione_lock = threading.Lock()
annulla_lock = threading.Lock()


@auth_bp.route("/prenotazione", methods=["POST"])
@require_roles("beneficiario")
def prenotazione():
    with prenotazione_lock:
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

        #geolocator per ottenere indirizzo del punto di distribuzione
        geolocator = Nominatim(user_agent="map4aid_project") 
        location = geolocator.reverse(
            (punto_distribuzione.latitudine, punto_distribuzione.longitudine)
        )  
        indirizzo = location.address if location else "Indirizzo non disponibile"  # AGGIUNTO

        # Check per le prenotazioni
        if is_pacco == "True":
            if is_craftable(id_punto_bisogno):
                try:
                    checker.check("pacco")
                except Exception as e:
                    return jsonify({"error": str(e)}), 200

                sott_pane = SottoCategoria.query.filter_by(nome="Pane").first()
                sott_pasta = SottoCategoria.query.filter_by(nome="Pasta").first()
                sott_carne = SottoCategoria.query.filter_by(nome="Carne").first()
                sott_acqua = SottoCategoria.query.filter_by(nome="Acqua").first()
                sott_pesce = SottoCategoria.query.filter_by(nome="Pesce").first()
                sott_verdura = SottoCategoria.query.filter_by(nome="Verdura").first()

                pane = BeneAlimentare.query.filter_by(
                    punto_distribuzione_id=id_punto_bisogno,
                    sottocategoria_id=sott_pane.id
                ).first()
                pasta = BeneAlimentare.query.filter_by(
                    punto_distribuzione_id=id_punto_bisogno,
                    sottocategoria_id=sott_pasta.id
                ).first()
                carne = BeneAlimentare.query.filter_by(
                    punto_distribuzione_id=id_punto_bisogno,
                    sottocategoria_id=sott_carne.id
                ).first()
                acqua = BeneAlimentare.query.filter_by(
                    punto_distribuzione_id=id_punto_bisogno,
                    sottocategoria_id=sott_acqua.id
                ).first()
                pesce = BeneAlimentare.query.filter_by(
                    punto_distribuzione_id=id_punto_bisogno,
                    sottocategoria_id=sott_pesce.id
                ).first()
                verdura = BeneAlimentare.query.filter_by(
                    punto_distribuzione_id=id_punto_bisogno,
                    sottocategoria_id=sott_verdura.id
                ).first()

                pacco = PaccoAlimentare(
                    nome="Pacco standard",
                    pasta=pasta.id,
                    pane=pane.id,
                    acqua=acqua.id,
                    carne=carne.id,
                    pesce=pesce.id,
                    verdura=verdura.id
                )

                db.session.add(pacco)
                db.session.commit()

                prenotazione = Prenotazione(
                    beneficiario_id=beneficiario.id,
                    bene_id=None,
                    punto_id=punto_distribuzione.id,
                    pacco_id=pacco.id,
                )
                db.session.add(prenotazione)
                pane.quantita -= 1
                pasta.quantita -= 1
                carne.quantita -= 1
                acqua.quantita -= 1
                pesce.quantita -= 1
                verdura.quantita -= 1
                db.session.commit()

                email_ok1 = mail_sender.send_prenotazione_beneficiario(
                    ente.email,
                    user_email,
                    indirizzo,                         
                    punto_distribuzione.latitudine,
                    punto_distribuzione.longitudine,
                    prenotazione.id
                )
                email_ok2 = mail_sender.send_prenotazione_ente(
                    ente.email,
                    user_email,
                    indirizzo,                       
                    punto_distribuzione.latitudine,
                    punto_distribuzione.longitudine,
                    prenotazione.id
                )
                if email_ok1 and email_ok2:
                    return jsonify({"message": "Prenotazione effetuata"}), 200
                return jsonify({"error": "Prenotazione effetuata ma email non inviata"}), 400

            return jsonify({"error": "Prenotazione non effetuata,beni non diponibili"}), 400

        if is_medicinale == "True":
            if "ricetta" not in request.files:
                return jsonify({"error": "Ricetta medica mancante"}), 400

            ricetta = request.files["ricetta"]

            if ricetta.filename == "":
                return jsonify({"error": "File ricetta non valido"}), 400

            filename = secure_filename(ricetta.filename)
            ricetta_path = os.path.join(UPLOAD_FOLDER, filename)
            ricetta.save(ricetta_path)

        id_bene = request.form.get("id_bene")
        bene = Bene.query.filter_by(id=id_bene).first()
        if not bene:
            return jsonify({"error": "Bene non trovato"}), 400
        if bene.quantita < 1:
            return jsonify({"error": "Bene non disponibile"}), 400

        prenotazione = Prenotazione(
            beneficiario_id=beneficiario.id,
            bene_id=bene.id,
            punto_id=punto_distribuzione.id,
            pacco_id=None,
            stato="in_validazione"
        )

        bene.quantita -= 1
        db.session.add(prenotazione)
        db.session.commit()

        email_ok1 = mail_sender.send_prenotazione_beneficiario(
            ente.email,
            user_email,
            indirizzo,                             
            punto_distribuzione.latitudine,
            punto_distribuzione.longitudine,
            prenotazione.id,
            bene.nome,
            ricetta_path
        )
        
        email_ok2 = mail_sender.send_prenotazione_ente(
            ente.email,
            user_email,
            indirizzo,                           
            punto_distribuzione.latitudine,
            punto_distribuzione.longitudine,
            prenotazione.id,
            bene.nome,
            ricetta_path
        )

        if email_ok1 and email_ok2:
            return jsonify({"message": "Prenotazione effetuata"}), 200
        return jsonify({"error": "Prenotazione effetuata ma email non inviata"}), 400


@auth_bp.route("/conferma_prenotazione", methods=["GET"])
@require_roles("ente_erogatore")
def conferma_prenotazione():
    id = request.args.get("id_prenotazione")
    prenotazione = Prenotazione.query.filter_by(id=id).first()

    if not prenotazione: 
        return jsonify({"error": "Prenotazione non trovata"}), 404
    
    punto = PuntoDistribuzione.query.filter_by(id=prenotazione.punto_id).first()
    ente = Account.query.filter_by(id=punto.ente_erogatore_id).first()
    if ente.email != session["user_email"]:
        return jsonify({"error": "Non hai i permessi per confermare la prenotazione"}), 401
    
    if prenotazione.stato != "in_attesa": 
        return jsonify({"error": "La prenotazione non è pronta per il ritiro"}), 400
    
    prenotazione.stato = "ritirata"
    db.session.commit()
    return jsonify({"message": "Prenotazione ritirata"}), 200


@auth_bp.route("/cancella_prenotazione_ente", methods=["POST"])
@require_roles("ente_erogatore")
def cancella_prenotazione_ente():
    with annulla_lock:
        mail_sender = EmailControlBridge()
        id_prenotazione = request.form.get("id_prenotazione")
        prenotazione = Prenotazione.query.filter_by(id=id_prenotazione).first()
        beneficiario = Account.query.filter_by(id=prenotazione.beneficiario_id).first()
        punto = PuntoDistribuzione.query.filter_by(id=prenotazione.punto_id).first()
        ente = Account.query.filter_by(id=punto.ente_erogatore_id).first()

        #calcolo indirizzo via geopy 
        geolocator = Nominatim(user_agent="map4aid_project") 
        location = geolocator.reverse((punto.latitudine, punto.longitudine)) 
        indirizzo = location.address if location else "Indirizzo non disponibile"

        esito = cancella_prenotazione(prenotazione)
        if not esito:
            return jsonify({"error": "Cancellazione non effetuata,bene già ritirato"}), 400

        email_ok = mail_sender.send_cancellazione_prenotazione_beneficiario(
            ente.email,
            beneficiario.email,
            prenotazione.data_prenotazione,
            indirizzo                            
        )

        if email_ok:
            return jsonify({"message": "Prenotazione cancellata"}), 200

        return jsonify({"error": "Prenotazione cancellata, ma email non inviata"}), 500


@auth_bp.route("/cancella_prenotazione_beneficiario", methods=["POST"])
@require_roles("beneficiario")
def cancella_prenotazione_beneficiario():
    with annulla_lock:
        mail_sender = EmailControlBridge()
        id_prenotazione = request.form.get("id_prenotazione")
        prenotazione = Prenotazione.query.filter_by(id=id_prenotazione).first()
        beneficiario = Account.query.filter_by(id=prenotazione.beneficiario_id).first()
        punto = PuntoDistribuzione.query.filter_by(id=prenotazione.punto_id).first()
        ente = Account.query.filter_by(id=punto.ente_erogatore_id).first()


        geolocator = Nominatim(user_agent="map4aid_project")
        location = geolocator.reverse((punto.latitudine, punto.longitudine)) 
        indirizzo = location.address if location else "Indirizzo non disponibile" 

        esito = cancella_prenotazione(prenotazione)
        if not esito:
            return jsonify({"error": "Cancellazione non effetuata,bene già ritirato"}), 400

        email_ok = mail_sender.send_cancellazione_prenotazione_ente(
            ente.email,
            beneficiario.email,
            prenotazione.data_prenotazione,
            indirizzo                              
        )

        if email_ok:
            return jsonify({"message": "Prenotazione cancellata"}), 200

        return jsonify({"error": "Prenotazione cancellata, ma email non inviata"}), 500




@auth_bp.route("/approva_ricetta", methods=["GET"])
@require_roles("ente_erogatore")
def approva_ricetta():
    mail_sender = EmailControlBridge()
    id = request.args.get("id_prenotazione", type=int)
    prenotazione = Prenotazione.query.filter_by(id=id).first()

    if not prenotazione:
        return jsonify({"error": "Prenotazione non trovata"}), 404

    punto = PuntoDistribuzione.query.filter_by(id=prenotazione.punto_id).first()
    ente = Account.query.filter_by(id=punto.ente_erogatore_id).first()

    if ente.email != session["user_email"]:
        return jsonify({"error": "Non hai i permessi per approvare"}), 401

    if prenotazione.stato != "in_validazione":
        return jsonify({"error": "La prenotazione non è in validazione"}), 400

    beneficiario = Account.query.filter_by(id=prenotazione.beneficiario_id).first()
    bene = Bene.query.filter_by(id=prenotazione.bene_id).first()

    prenotazione.stato = "in_attesa"
    db.session.commit()

    email_ok = mail_sender.send_validazione_medicinale(
        beneficiario.email,   
        ente.email,           
        bene.nome             
    )

    if email_ok:
        return jsonify({"message": "Ricetta approvata. Il beneficiario è stato avvisato."}), 200

    return jsonify({"message": "Ricetta approvata, ma email non inviata"}), 200



def cancella_prenotazione(prenotazione):

    if prenotazione.stato == "Completata":
        return False

    if prenotazione.pacco_id is not None:
        pacco = PaccoAlimentare.query.get(prenotazione.pacco_id)

        beni_ids = [
            pacco.pasta,
            pacco.pane,
            pacco.acqua,
            pacco.carne,
            pacco.pesce,
            pacco.verdura
        ]

        for bene_id in beni_ids:
            bene = Bene.query.get(bene_id)
            bene.quantita += 1

        db.session.delete(prenotazione)
        db.session.commit()
        return True

    bene = Bene.query.filter_by(id=prenotazione.bene_id).first()
    bene.quantita += 1
    db.session.delete(prenotazione)
    db.session.commit()
    return True


def is_craftable(id_punto_bisogno):
    punto = PuntoDistribuzione.query.filter_by(id=id_punto_bisogno).first()
    if not punto:
        return False

    SOTTOCATEGORIE_PACCO = ["Pasta", "Pane", "Acqua", "Carne", "Pesce", "Verdura"]

    for nome_sottocateg in SOTTOCATEGORIE_PACCO:
        sottocateg = SottoCategoria.query.filter_by(nome=nome_sottocateg).first()
        if not sottocateg:
            return False

        bene = Bene.query.filter_by(
            punto_distribuzione_id=id_punto_bisogno,
            sottocategoria_id=sottocateg.id
        ).first()

        if not bene or bene.quantita < 1:
            return False

    return True
