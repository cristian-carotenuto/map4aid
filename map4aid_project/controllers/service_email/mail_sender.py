from abc import ABC, abstractmethod


class MailSender(ABC):

    @abstractmethod
    def send_otp(self, email: str, codice: int) -> bool:
        pass

    @abstractmethod
    def send_donazione_monetaria(
        self,
        email_ente: str,
        nome_ente: str,
        email_donatore: str,
        importo: float,
        data
    ) -> bool:
        pass

    @abstractmethod
    def send_segnalazione(
        self,
        email_ente: str,
        indirizzo: str,
        lat: float,
        lon: float
    ) -> bool:
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def send_donazione_bene_donatore(
            self,
            email_donatore,
            email_ente,
            bene
    ) -> bool:
        pass