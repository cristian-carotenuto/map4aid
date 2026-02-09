from controllers.service_email.mail_sender import MailSender
from controllers.service_email.EmailControl import EmailControl


class EmailControlBridge(MailSender):

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

    def send_donazione_bene_ente(
        self,
        email_ente,
        email_donatore,
        bene,
        donazione,
        punto_bisogno,
        sottocategoria,
        indirizzo
    ) -> bool:
        return self._email_control.invia_email_donazione_ente(
            email_ente,
            email_donatore,
            bene,
            donazione,
            punto_bisogno,
            sottocategoria,
            indirizzo
        )

    def send_donazione_bene_donatore(
        self,
        email_donatore,
        email_ente,
        bene
    ) -> bool:
        return self._email_control.invia_email_donazione_donatore(
            email_donatore,
            email_ente,
            bene
        )

    def send_prenotazione_beneficiario(
        self,
        email_ente,
        email_beneficiario,
        indirizzo,     
        lat,
        lon,
        prenotazione_id,
        nome_bene=None,
        path_ricetta=None
    ) -> bool:
        return self._email_control.invia_email_prenotazione_beneficiario(
            email_ente,
            email_beneficiario,
            indirizzo, 
            lat,
            lon,
            prenotazione_id,
            nome_bene,
            path_ricetta
        )

    def send_prenotazione_ente(
        self,
        email_ente,
        email_beneficiario,
        indirizzo,     
        lat,
        lon,
        prenotazione_id,
        nome_bene=None,
        path_ricetta=None
    ) -> bool:
        return self._email_control.invia_email_prenotazione_ente(
            email_ente,
            email_beneficiario,
            indirizzo,   
            lat,
            lon,
            prenotazione_id,
            nome_bene,
            path_ricetta
        )

    def send_cancellazione_prenotazione_beneficiario(
        self,
        email_ente,
        email_beneficiario,
        data,
        indirizzo
    ) -> bool:
        return self._email_control.invia_cancellazione_prenotazione_beneficiario(
            email_ente,
            email_beneficiario,
            data,
            indirizzo
        )

    def send_cancellazione_prenotazione_ente(
        self,
        email_ente,
        email_beneficiario,
        data,
        indirizzo
    ) -> bool:
        return self._email_control.invia_cancellazione_prenotazione_ente(
            email_ente,
            email_beneficiario,
            data,
            indirizzo
        )

    def send_conferma_registrazione(
        self,
        email_beneficiario,
        esito
    ) -> bool:
        return self._email_control.invia_conferma_registrazione(
            email_beneficiario,
            esito
        )
