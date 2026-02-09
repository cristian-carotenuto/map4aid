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

    @abstractmethod
    def send_prenotazione_beneficiario(
        self,
        email_ente: str,
        email_beneficiario: str,
        indirizzo: str,       
        lat: float,
        lon: float,
        prenotazione_id: int,
        nome_bene: str | None = None,
        path_ricetta: str | None = None
    ) -> bool:
        pass

    @abstractmethod
    def send_prenotazione_ente(
        self,
        email_ente: str,
        email_beneficiario: str,
        indirizzo: str,        
        lat: float,
        lon: float,
        prenotazione_id: int,
        nome_bene: str | None = None,
        path_ricetta: str | None = None
    ) -> bool:
        pass

    @abstractmethod
    def send_cancellazione_prenotazione_beneficiario(
        self,
        email_ente: str,
        email_beneficiario: str,
        data,
        indirizzo: str
    ) -> bool:
        pass

    @abstractmethod
    def send_cancellazione_prenotazione_ente(
        self,
        email_ente: str,
        email_beneficiario: str,
        data,
        indirizzo: str
    ) -> bool:
        pass

    @abstractmethod
    def send_conferma_registrazione(
        self,
        email_beneficiario: str,
        esito: bool
    ) -> bool:
        pass
