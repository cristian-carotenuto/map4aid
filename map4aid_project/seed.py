#popolo db se è vuoto

from app import create_app
from config import db
from models.models import (
    AccountEnteErogatore,
    PuntoDistribuzione,
    MacroCategoria,
    SottoCategoria
)

def popola_db():
    if AccountEnteErogatore.query.first() is not None:
        print(">> Database già popolato, nessuna azione necessaria.")
        return

    print(">> Popolamento database iniziale...")

    #ente UNISA
    ente = AccountEnteErogatore(
        email="ente@unisa.it",
        nome_organizzazione="UNISA - Università degli Studi di Salerno",
        indirizzo_sede="Via Giovanni Paolo II, 132 - Fisciano (SA)",
        tipologia_ente="università",
        iban=None
    )
    ente.set_password("password123")
    db.session.add(ente)
    db.session.flush()

    # Punto distribuzione UNISA
    punto_unisa = PuntoDistribuzione(
        nome="Punto Distribuzione UNISA",
        regione="Campania",
        citta="Fisciano",
        latitudine=40.7718,
        longitudine=14.7900,
        ente_erogatore_id=ente.id
    )
    db.session.add(punto_unisa)

    #macroCategorie
    alimenti = MacroCategoria(nome="Alimenti")
    igiene = MacroCategoria(nome="Igiene")
    vestiario = MacroCategoria(nome="Vestiario")
    db.session.add_all([alimenti, igiene, vestiario])
    db.session.flush()

    #sottoCategorie
    sotto = [
        SottoCategoria(nome="Pasta", macro_categoria_id=alimenti.id),
        SottoCategoria(nome="Riso", macro_categoria_id=alimenti.id),
        SottoCategoria(nome="Sapone", macro_categoria_id=igiene.id),
        SottoCategoria(nome="Shampoo", macro_categoria_id=igiene.id),
        SottoCategoria(nome="Magliette", macro_categoria_id=vestiario.id),
        SottoCategoria(nome="Pantaloni", macro_categoria_id=vestiario.id),
    ]
    db.session.add_all(sotto)

    db.session.commit()
    print("Database popolato con successo!")


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        popola_db()
