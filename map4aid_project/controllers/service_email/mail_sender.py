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