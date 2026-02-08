import os
import smtplib
from datetime import datetime, timezone
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from io import BytesIO

import qrcode
from flask import request


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

    def invia_email_prenotazione_beneficiario(self,email_ente,email_beneficiario,lan,lon,prenotazione_id,nome_bene=None):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_beneficiario
        msg["Subject"] = "Email per conferma prenotazione"

        #Creazione qrCode
        buffer = BytesIO()
        url = f"""{request.url_root}auth/conferma_prenotazione?prenotazione_id={prenotazione_id}"""
        qr = qrcode.make(url)
        qr.save(buffer, format="PNG")
        buffer.seek(0)

        if nome_bene == None:
            corpo = f"""
E' stata confermata una prenotazione per un pacco alimentare presso il seguente punto di bisogno posseduto da {email_ente} in data {datetime.now(timezone.utc)}.
Latitudine: {lan}
Longitudine: {lon}
La preghiamo di ritirare il pacco il prima possibile

Cordiali saluti,
Map4Aid
"""
        else:
            corpo = f"""
E' stata confermata una prenotazione per il seguente bene:{nome_bene} presso il seguente punto di bisogno posseduto da {email_ente} in data {datetime.now(timezone.utc)}.
Latitudine: {lan}
Longitudine: {lon}
La preghiamo di ritirare il bene il prima possibile

Mostrare il qrCode al punto di bisogno per confermare la prenotazione

Cordiali saluti,
Map4Aid"""

        msg.attach(MIMEText(corpo, "plain", "utf-8"))
        img = MIMEImage(buffer.read())
        img.add_header("Content-ID", "<qrcode>")
        msg.attach(img)

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

    def invia_email_prenotazione_ente(self,email_ente,email_beneficiario,lan,lon,prenotazione,nome_bene=None,path_ricetta=None):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_ente
        msg["Subject"] = "Email per conferma prenotazione"

        if nome_bene == None:
            corpo = f"""
E' stata confermata una prenotazione per un pacco alimentare presso il seguente punto di bisogno in vostro posseso da parte di {email_beneficiario} in data {datetime.now(timezone.utc)}.
Latitudine: {lan}
Longitudine: {lon}

Cordiali saluti,
Map4Aid
"""
        else:
            corpo = f"""
E' stata confermata una prenotazione per il seguente bene:{nome_bene} presso il seguente punto di bisogno in vostro posseso da parte di {email_beneficiario} in data {datetime.now(timezone.utc)}.
Latitudine: {lan}
Longitudine: {lon}

Cordiali saluti,
Map4Aid"""

            msg.attach(MIMEText(corpo, "plain", "utf-8"))
            # Allegato ricetta medica (se presente)
            if path_ricetta is not None:
                try:
                    with open(path_ricetta, "rb") as f:
                        parte = MIMEBase("application", "octet-stream")
                        parte.set_payload(f.read())

                    encoders.encode_base64(parte)

                    nome_file = os.path.basename(path_ricetta)
                    parte.add_header(
                        "Content-Disposition",
                        f'attachment; filename="{nome_file}"'
                    )

                    msg.attach(parte)

                except Exception as e:
                    print(f"Errore allegato ricetta: {e}")
                    return False

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


    def invia_cancellazione_prenotazione_beneficiario(self,email_ente,email_beneficiario,data,indirizzo):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_beneficiario
        msg["Subject"] = "Email per cancellazione prenotazione"

        corpo = f"""
Salve,
questa email è un avviso riguardo la cancellazione della sua prenotazione fatta in data {data} in {indirizzo}.
La prenotazione potrebbe essere scaduta o stata cancellata dall'ente che possiede il punto di bisgono.
Per maggiori informazioni contattare {email_ente}
        
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

    def invia_cancellazione_prenotazione_ente(self, email_ente, email_beneficiario, data, indirizzo):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_ente
        msg["Subject"] = "Email per cancellazione prenotazione"

        corpo = f"""
Salve,
questa email è un avviso riguardo la cancellazione della prenotazione fatta in data {data} in {indirizzo} da {email_beneficiario}.
La prenotazione è stata cancellata dall'utente che possiede questo indirizzo email.

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

    def invia_conferma_registrazione(self, email_beneficiario, esito):
        msg = MIMEMultipart()
        msg["From"] = self.config["email"]
        msg["To"] = email_beneficiario
        msg["Subject"] = "Email per cancellazione prenotazione"

        if esito == "True":
            corpo = f"""
Salve,
la informiamo che la sua registrazione è stata validata e confermata da un nostro amministratore. Da ora può accedere e prenotare beni di prima necessità.

Cordiali saluti,
Map4Aid"""

        else:
            corpo = f"""
            Salve,
            la informiamo che la sua registrazione è stata rifiutata da un nostro amministratore. Probabilmente ciò è dovuto a carta d'identità non valida o codice non corrispondente.
            La invitiamo a riprovare prestando attenzione ai dati da lei inseriti. Controlli anche che la carta d'identità non sia scaduta

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