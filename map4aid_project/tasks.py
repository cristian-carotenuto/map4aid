from datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler
from config import db
from models.pendingAccounts import PendingAccount

def cleanup_expired_pending_accounts(app):
    with app.app_context():
        now = datetime.now(timezone.utc)
        expired = PendingAccount.query.filter(PendingAccount.expires_at < now).all()
        if expired:
            for p in expired:
                db.session.delete(p)
            db.session.commit()
            print(f"[{now}] Cancellati {len(expired)} account scaduti.")

def start_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=cleanup_expired_pending_accounts,
        trigger='interval',
        minutes=5,
        args=[app]
    )
    print("Scheduler avviato")
    scheduler.start()