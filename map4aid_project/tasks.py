import os
from datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler
from geopy import Nominatim

from config import db
from controllers.prenotazione_control import cancella_prenotazione
from controllers.service_email.email_control_bridge import EmailControlBridge
from models.models import Prenotazione, Account, PuntoDistribuzione
from models.pendingAccounts import PendingAccount


# --- Job unico che fa tutto ---
def job(app):
    with app.app_context():
        now = datetime.now().replace(tzinfo=None)
        print(now)
        # 1 Pulizia account scaduti
        expired_accounts = PendingAccount.query.filter(PendingAccount.expires_at < now).all()
        if expired_accounts:
            for account in expired_accounts:
                db.session.delete(account)
            db.session.commit()
            print(f"[{now}] Cancellati {len(expired_accounts)} account scaduti.")

        # 2 Pulizia prenotazioni scadute
        prenotazioni = Prenotazione.query.all()
        mail_sender = EmailControlBridge()
        for prenotazione in prenotazioni:
            data = prenotazione.data_prenotazione
            differenza = (now - data.replace(tzinfo=None)).days
            if differenza >= 4 and prenotazione.stato == "in_attesa":
                beneficiario = Account.query.filter_by(id=prenotazione.beneficiario_id).first()
                punto = PuntoDistribuzione.query.filter_by(id=prenotazione.punto_id).first()
                ente = Account.query.filter_by(id=punto.ente_erogatore_id).first()
                geolocator = Nominatim(user_agent="my_app")
                indirizzo = geolocator.reverse((punto.latitudine, punto.longitudine), language="it")
                mail_sender.send_cancellazione_prenotazione_beneficiario(ente.email, beneficiario.email,
                                                                         prenotazione.data_prenotazione,
                                                                         indirizzo)
                cancella_prenotazione(prenotazione)




# --- Avvio scheduler ---
def start_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=job,
        trigger='interval',
        minutes=1,
        args=[app],
        id='job_unico',
        replace_existing=True
    )
    scheduler.start()
    print("Scheduler avviato")