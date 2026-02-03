from datetime import timezone, datetime
from flask import request, session
from controllers.routes import auth_bp
from controllers.service_email.email_control_bridge import EmailControlBridge
from models import AccountEnteErogatore
from controllers.permessi import require_roles
from config import db
from models.models import AccountDonatore, DonazioneMonetaria, BeneAlimentare, Bene, PaccoAlimentare, \
    PuntoDistribuzione, Prenotazione


@auth_bp.route("/prenotazione", methods=["POST"])
@require_roles("beneficiario")
def prenotazione():
    id_punto_bisogno = request.form.get("id_punto_bisogno")
    is_pacco = request.form.get("is_pacco")
    id_bene = request.form.get("id_bene")
    user_email = session["user_email"]

    punto_distribuzione = PuntoDistribuzione.query.filter_by(id=id_punto_bisogno).first()
    id_ente = punto_distribuzione.ente_erogatore_id
    ente = AccountEnteErogatore.query.filter_by(id=id_ente).first()
    bene = Bene.query.filter_by(id=id_bene).first()

    mail_sender = EmailControlBridge()

    #Check per le prenotazione
    if is_pacco == "True":
        if is_craftable(id_punto_bisogno):
            pane = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="pane").first()
            pasta = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="pasta").first()
            carne = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="carne").first()
            acqua = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="acqua").first()
            pesce = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="pesce").first()
            verdura = BeneAlimentare.query.filter_by(id_punto_bisogno=id_punto_bisogno,sottocategoria_id="verdura").first()
            pacco = PaccoAlimentare(pasta,pane,acqua,carne,pesce,verdura)
            prenotazione = Prenotazione()
            pane.quantita -= 1
            pane.save()
            pasta.quantita -= 1
            pasta.save()
            carne.quantita -= 1
            carne.save()
            acqua.quantita -= 1
            acqua.save()
            pesce.quantita -= 1
            pesce.save()
            db.session.add(pacco)
            db.session.commit()

            email_ok1 = mail_sender.send_prenotazione_beneficiario(
                ente.email,
                user_email,
                punto_distribuzione.
                indirizzo,
                punto_distribuzione.latitude,
                punto_distribuzione.longitude,
                )
