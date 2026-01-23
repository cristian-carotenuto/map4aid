from datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler
from app import db
from models.pendingAccounts import PendingAccount


def cleanup_expired_pending_accounts():
    now = datetime.now(timezone.utc)
    expired = PendingAccount.query.filter(PendingAccount.expires_at < now).all()
    for p in expired:
        db.session.delete(p)
    db.session.commit()
    print(f"Cancellati {len(expired)} PendingAccount scaduti")

scheduler = BackgroundScheduler()
scheduler.add_job(cleanup_expired_pending_accounts, 'interval', minutes=10)  # intervallo
scheduler.start()