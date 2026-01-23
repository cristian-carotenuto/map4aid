import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailControl:


    def __init__(self):
        self.config = {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "email": "map4aid@gmail.com",
            "password": "PASSWORD_APP"
        }

    def invia_email_donazione(self, email_ente, nome_ente,
                              email_donatore, importo, data):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_ente
        msg["Subject"] = "Notifica di donazione monetaria ricevuta"

        corpo = f"""
Gentile {nome_ente},

la informiamo che in data {data.strftime('%d/%m/%Y %H:%M')}
è stata ricevuta una donazione monetaria tramite la piattaforma.

Dettagli della donazione:
- Importo: € {importo:.2f}
- Donatore: {email_donatore}

Cordiali saluti,
Map4Aid
"""

        msg.attach(MIMEText(corpo, "plain", "utf-8"))

        try:
            with smtplib.SMTP(self.config["smtp_server"],
                              self.config["smtp_port"]) as server:
                server.starttls()
                server.login(
                    self.config["email"],
                    self.config["password"]
                )
                server.send_message(msg)
            return True

        except Exception as e:
            print(f"Errore SMTP: {e}")
            return False

    def invia_email_codice(self, email_utente,codice):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_utente
        msg["Subject"] = "Email per recupero password"

        corpo = f"""
        Per favore inserire il seguente codice per confermare l'emaill:
        {codice}
        Il codice scadrà dopo 10 minuti
        
        Cordiali saluti,
        Map4Aid
"""

        msg.attach(MIMEText(corpo, "plain", "utf-8"))

        try:
            with smtplib.SMTP(self.config["smtp_server"],
                              self.config["smtp_port"]) as server:
                server.starttls()
                server.login(
                    self.config["email"],
                    self.config["password"]
                )
                server.send_message(msg)
            return True

        except Exception as e:
            print(f"Errore SMTP: {e}")
            return False

    def invia_email_segnalazione(self,indirizzo,email_ente):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_ente
        msg["Subject"] = "Email per segnalazione punto di bisogno"

        corpo = f"""
E' arrivata una segnalazione per un punto di bisogno.
L'indirizzo è {indirizzo}
Cordiali saluti,
Map4Aid
"""

        msg.attach(MIMEText(corpo, "plain", "utf-8"))

        try:
            with smtplib.SMTP(self.config["smtp_server"],
                              self.config["smtp_port"]) as server:
                server.starttls()
                server.login(
                    self.config["email"],
                    self.config["password"]
                )
                server.send_message(msg)
            return True

        except Exception as e:
            print(f"Errore SMTP: {e}")
            return False