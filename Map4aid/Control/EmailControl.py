import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailControl:


    def invia_email_donazione(self, email_ente, nome_ente,
                              email_donatore, importo, data):

        msg = MIMEMultipart()
        msg["From"] = email_donatore
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
Piattaforma di gestione donazioni
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

