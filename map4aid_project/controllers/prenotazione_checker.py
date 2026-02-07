from datetime import datetime, timedelta
from models.models import Prenotazione, Bene

REGOLE_PRENOTAZIONE = {
    "pacco": 30,       
    "mobilita": 60,   
    "igiene": 7,      
    "vestiario": 7,   
    #medicinale gestito con ricetta
}


class PrenotazioneChecker:

    def __init__(self, user):
        self.user = user

    def check(self, tipo_prenotazione, bene=None, ricetta=None):

        if tipo_prenotazione == "pacco":
            return self._check_limite("pacco")

        if tipo_prenotazione == "bene":
            return self._check_bene_singolo(bene, ricetta)

        raise ValueError("Tipo prenotazione non riconosciuto")

    # BENE SINGOLO

    def _check_bene_singolo(self, bene, ricetta):
        tipo = bene.tipo 

        #caso medicinale
        if tipo == "medicinale":
            return self._check_medicinale(ricetta)

        giorni_limite = REGOLE_PRENOTAZIONE[tipo]
        return self._check_limite(tipo, giorni_limite)

    # MEDICINALE

    def _check_medicinale(self, ricetta):
        if not ricetta:
            raise ValueError("Richiesta ricetta per prenotare medicinali")
        return True


    def _check_limite(self, tipo, giorni_limite=None):
        if giorni_limite is None:
            giorni_limite = REGOLE_PRENOTAZIONE[tipo]

        query = Prenotazione.query.filter(
            Prenotazione.beneficiario_id == self.user.id)

        if tipo == "pacco":
            query = query.filter(Prenotazione.pacco_id.isnot(None))
        else:
            query = query.join(Bene).filter(Bene.tipo == tipo)

        ultima = query.order_by(Prenotazione.data_prenotazione.desc()).first()

        if not ultima:
            return True

        limite = datetime.now().replace(tzinfo=None) - timedelta(days=giorni_limite)

        if ultima.data_prenotazione < limite:
            return True

        raise ValueError(
            f"Puoi prenotare un bene di tipo '{tipo}' solo ogni {giorni_limite} giorni"
        )
