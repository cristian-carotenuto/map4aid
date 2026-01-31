import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailControl:


    def __init__(self):
        self.config = {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "email": "map4aid01@gmail.com",
            "password": "cmtf ymqz iekk lqbq"
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
        msg["Subject"] = "Email per conferma codice"

        corpo = f"""
Per favore inserire il seguente codice per confermare l'emaill:
{codice}
Il codice scadrà dopo 10 minuti
Se hai ricevuto questa email senza aver provato a registrarti probabilmente un utente ha inseirito la tua mail per sbaglio
        
Cordiali saluti,
Map4Aid"""

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

    def invia_email_segnalazione(self,email_ente,indirizzo,lan,lon):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_ente
        msg["Subject"] = "Email per segnalazione punto di bisogno"

        corpo = f"""
E' arrivata una segnalazione per un punto di bisogno.
L'indirizzo è {indirizzo}
Latitudine: {lan}
Longitudine: {lon}
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

    def invia_email_donazione_ente(self, email_ente, email_donatore,bene,donazione,punto_bisogno,sottocategoria,indirizzo):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_ente
        msg["Subject"] = "Email per conferma donazione bene"

        corpo = f"""
E' stata effetuata una donazione da parte di {email_donatore} in data {donazione.data.day}-{donazione.data.month}-{donazione.data.year} presso un vostro punto di bisogno.
La invitiamo a contattare il donatore per confermare la donazione.
Il punto di bisogno a cui hanno donato è {punto_bisogno.nome} con indirizzo {indirizzo}
Di seguito sono riportate le informazioni del bene donato:
nome: {bene.nome}
quantita: {bene.quantita}
tipo: {bene.tipo}
sottocategoria: {sottocategoria}
"""
        if bene.tipo == "alimentare":
            extra_data = f"""
scadenza: {bene.scadenza}
allergeni: {bene.allergeni}
"""
            corpo += extra_data

        # Bene per l'igiene
        elif bene.tipo == "igiene":
            extra_data = f"""
destinatari: {bene.destinatari}
"""
            corpo += extra_data

        # Medicinale
        elif bene.tipo == "medicinale":
            extra_data = f"""
tipo medicinale: {bene.tipo_medicinale}
scadenza: {bene.scadenza}
"""
            corpo += extra_data


        # Beni per la mobilità
        elif bene.tipo == "mobilità":
            extra_data = f"""
tipo mobilita: {bene.tipo_mobilita}
stato: {bene.stato}
"""
            corpo += extra_data

        # Vestiti
        elif bene.tipo == "vestiario":
            extra_data = f"""
taglia: {bene.taglia}
condizioni: {bene.condizioni}
"""
            corpo += extra_data

        saluti = f"""
Cordiali saluti,
Map4Aid"""
        corpo += saluti
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

    def invia_email_donazione_donatore(self,email_donatore,email_ente,bene):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_donatore
        msg["Subject"] = "Email per conferma donazione bene"

        corpo = f"""
La donazione di {bene.nome} è andata a buon fine.
Si aspetti un'email o contatti direttamente {email_donatore}.
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
