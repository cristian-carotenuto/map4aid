from datetime import time

from run import app
from config import db
from models.models import MacroCategoria, SottoCategoria, PuntoDistribuzione


def popola_categorie():
    categorie = {
        "Alimentari": [
            "Pasta e riso",
            "Prodotti in scatola",
            "Prodotti freschi",
            "Prodotti per l'infanzia",
            "Bevande"
        ],
        "Igiene": [
            "Igiene personale",
            "Igiene femminile",
            "Igiene orale",
            "Prodotti per bambini"
        ],
        "Vestiario": [
            "Abbigliamento uomo",
            "Abbigliamento donna",
            "Abbigliamento bambino",
            "Scarpe",
            "Accessori"
        ],
        "Medicinali": [
            "Farmaci da banco",
            "Farmaci prescrizione",
            "Dispositivi medici",
            "Integratori"
        ],
        "Mobilità": [
            "Sedie a rotelle",
            "Deambulatori",
            "Stampelle",
            "Carrozzine"
        ]
    }

    for nome_macro, sottocategorie in categorie.items():
        macro = MacroCategoria.query.filter_by(nome=nome_macro).first()
        if not macro:
            macro = MacroCategoria(nome=nome_macro)
            db.session.add(macro)
            db.session.flush()

        for nome_sotto in sottocategorie:
            if not SottoCategoria.query.filter_by(
                nome=nome_sotto,
                macro_categoria_id=macro.id
            ).first():
                db.session.add(
                    SottoCategoria(nome=nome_sotto, macro_categoria=macro)
                )

    db.session.commit()
    print("Categorie inserite correttamente")

def crea_punto_distribuzione():
    punto = PuntoDistribuzione.query.filter_by(id=1).first()

    if not punto:
        print("Punto di distribuzione non trovato")
        return

    punto.ente_erogatore_id = 2
    db.session.commit()

    print("ente_erogatore_id aggiornato a 2")

if __name__ == "__main__":
    with app.app_context():
        crea_punto_distribuzione()


