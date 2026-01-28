from controllers.service_email.mail_sender import MailSender
from controllers.service_email.EmailControl import EmailControl


class EmailControlAdapter(MailSender):

    def __init__(self):
        self._email_control = EmailControl()

    def send_otp(self, email: str, codice: int) -> bool:
        return self._email_control.invia_email_codice(email, codice)

    def send_donazione_monetaria(
        self,
        email_ente,
        nome_ente,
        email_donatore,
        importo,
        data
    ) -> bool:
        return self._email_control.invia_email_donazione(
            email_ente,
            nome_ente,
            email_donatore,
            importo,
            data
        )

    def send_segnalazione(
        self,
        email_ente,
        indirizzo,
        lat,
        lon
    ) -> bool:
        return self._email_control.invia_email_segnalazione(
            email_ente,
            indirizzo,
            lat,
            lon
        )