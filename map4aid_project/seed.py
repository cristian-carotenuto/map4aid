from app import create_app
from config import db
from models.models import (
    AccountEnteErogatore,
    AccountBeneficiario,
    AccountDonatore,
    PuntoDistribuzione,
    MacroCategoria,
    SottoCategoria,
    Bene,
    BeneAlimentare,
    BeneIgiene,
    BeneVestiario,
    BeneMedicinale,
    BeneMobilita,
    DonazioneBene,
    DonazioneMonetaria,
    PaccoAlimentare,
    Prenotazione,
    Feedback
)
from datetime import datetime, date, timezone


def popola_db():
    print(">> Avvio popolamento database...")

    #esci se già popolato
    if AccountEnteErogatore.query.first() is not None:
        print(">> Database già popolato.")
        return

    #enti erogatori
    ente1 = AccountEnteErogatore(
        email="ente@unisa.it",
        nome_organizzazione="UNISA - Università degli Studi di Salerno",
        indirizzo_sede="Via Giovanni Paolo II, 132 - Fisciano (SA)",
        tipologia_ente="università",
        iban=None
    )
    ente1.set_password("password123")

    ente2 = AccountEnteErogatore(
        email="caritas@salerno.it",
        nome_organizzazione="Caritas Salerno",
        indirizzo_sede="Via Roma 10, Salerno",
        tipologia_ente="associazione",
        iban="IT00X0000000000000000000000"
    )
    ente2.set_password("password123")

    db.session.add_all([ente1, ente2])
    db.session.flush()

    #punti distribuzione
    punto1 = PuntoDistribuzione(
        nome="Punto Distribuzione UNISA",
        giorni_apertura="Lun-Ven",
        orario_apertura=datetime.strptime("09:00", "%H:%M").time(),
        orario_chiusura=datetime.strptime("17:00", "%H:%M").time(),
        latitudine=40.7718,
        longitudine=14.7900,
        accettato=True,
        ente_erogatore_id=ente1.id
    )

    punto2 = PuntoDistribuzione(
        nome="Caritas Centro",
        giorni_apertura="Lun-Sab",
        orario_apertura=datetime.strptime("08:00", "%H:%M").time(),
        orario_chiusura=datetime.strptime("18:00", "%H:%M").time(),
        latitudine=40.6800,
        longitudine=14.7600,
        accettato=True,
        ente_erogatore_id=ente2.id
    )

    punto3 = PuntoDistribuzione(
        nome="Caritas Zona Est",
        giorni_apertura="Mar-Dom",
        orario_apertura=datetime.strptime("10:00", "%H:%M").time(),
        orario_chiusura=datetime.strptime("16:00", "%H:%M").time(),
        latitudine=40.6900,
        longitudine=14.8000,
        accettato=True,
        ente_erogatore_id=ente2.id
    )

    db.session.add_all([punto1, punto2, punto3])
    db.session.flush()


    #macro categorie
    mc_alimenti = MacroCategoria(nome="Alimenti")
    mc_igiene = MacroCategoria(nome="Igiene")
    mc_vestiario = MacroCategoria(nome="Vestiario")
    mc_medicinali = MacroCategoria(nome="Medicinali")
    mc_mobilita = MacroCategoria(nome="Mobilità")

    db.session.add_all([mc_alimenti, mc_igiene, mc_vestiario, mc_medicinali, mc_mobilita])
    db.session.flush()


    #sottocategorie
    sotto = {
        "Pasta": SottoCategoria(nome="Pasta", macro_categoria_id=mc_alimenti.id),
        "Pane": SottoCategoria(nome="Pane", macro_categoria_id=mc_alimenti.id),
        "Acqua": SottoCategoria(nome="Acqua", macro_categoria_id=mc_alimenti.id),
        "Carne": SottoCategoria(nome="Carne", macro_categoria_id=mc_alimenti.id),
        "Pesce": SottoCategoria(nome="Pesce", macro_categoria_id=mc_alimenti.id),
        "Verdura": SottoCategoria(nome="Verdura", macro_categoria_id=mc_alimenti.id),

        "Sapone": SottoCategoria(nome="Sapone", macro_categoria_id=mc_igiene.id),
        "Shampoo": SottoCategoria(nome="Shampoo", macro_categoria_id=mc_igiene.id),

        "Magliette": SottoCategoria(nome="Magliette", macro_categoria_id=mc_vestiario.id),
        "Pantaloni": SottoCategoria(nome="Pantaloni", macro_categoria_id=mc_vestiario.id),

        "Tachipirina": SottoCategoria(nome="Tachipirina", macro_categoria_id=mc_medicinali.id),
        "Oki": SottoCategoria(nome="Oki", macro_categoria_id=mc_medicinali.id),

        "Sedia a rotelle": SottoCategoria(nome="Sedia a rotelle", macro_categoria_id=mc_mobilita.id),
        "Stampella singola" :SottoCategoria(nome="Stampella singola", macro_categoria_id=mc_mobilita.id)
    }

    db.session.add_all(sotto.values())
    db.session.flush()


    # 5)beni stock
    beni = [
        BeneAlimentare(nome="Pasta Barilla 1kg", quantita=30, punto_distribuzione_id=punto1.id, sottocategoria_id=sotto["Pasta"].id),
        BeneAlimentare(nome="Pane fresco", quantita=20, punto_distribuzione_id=punto1.id, sottocategoria_id=sotto["Pane"].id),
        BeneAlimentare(nome="Acqua 1.5L", quantita=50, punto_distribuzione_id=punto1.id, sottocategoria_id=sotto["Acqua"].id),
        BeneAlimentare(nome="Carne macinata", quantita=10, punto_distribuzione_id=punto1.id, sottocategoria_id=sotto["Carne"].id),
        BeneAlimentare(nome="Pesce surgelato", quantita=15, punto_distribuzione_id=punto1.id, sottocategoria_id=sotto["Pesce"].id),
        BeneAlimentare(nome="Verdura mista", quantita=25, punto_distribuzione_id=punto1.id, sottocategoria_id=sotto["Verdura"].id),

        BeneIgiene(nome="Sapone neutro", quantita=40, punto_distribuzione_id=punto2.id, sottocategoria_id=sotto["Sapone"].id),
        BeneIgiene(nome="Shampoo delicato", quantita=35, punto_distribuzione_id=punto2.id, sottocategoria_id=sotto["Shampoo"].id),

        BeneVestiario(nome="Maglietta cotone", quantita=15, punto_distribuzione_id=punto3.id, sottocategoria_id=sotto["Magliette"].id),
        BeneVestiario(nome="Pantaloni jeans", quantita=10, punto_distribuzione_id=punto3.id, sottocategoria_id=sotto["Pantaloni"].id),

        BeneMedicinale(nome="Tachipirina 500mg", quantita=50, punto_distribuzione_id=punto1.id, sottocategoria_id=sotto["Tachipirina"].id),
        BeneMedicinale(nome="Oki solubile", quantita=50, punto_distribuzione_id=punto2.id, sottocategoria_id=sotto["Oki"].id),

        BeneMobilita(nome="Sedia a rotelle standard", quantita=3, punto_distribuzione_id=punto2.id, sottocategoria_id=sotto["Sedia a rotelle"].id),
        BeneMobilita(nome="Stampella singola", quantita=10, punto_distribuzione_id=punto2.id, sottocategoria_id=sotto["Stampella singola"].id),
    ]

    db.session.add_all(beni)


    #beneficiari
    ben1 = AccountBeneficiario(
        email="nico.rossi@example.com",
        nome="Nico",
        cognome="Rossi",
        codice_carta_identita="ABC123",
        path_immagine_carta_identita="img1.png",
        accettato=True
    )
    ben1.set_password("password123")

    ben2 = AccountBeneficiario(
        email="gio.verdi@example.com",
        nome="Giovanni",
        cognome="Verdi",
        codice_carta_identita="XYZ789",
        path_immagine_carta_identita="img2.png",
        accettato=True
    )
    ben2.set_password("password123")

    db.session.add_all([ben1, ben2])


    #donatori
    don1 = AccountDonatore(
        email="azienda@food.it",
        categoria="azienda",
        partita_iva="12345678901",
        nome_attivita="FoodCorp",
        indirizzo_sede="Via Industria 10, Salerno"
    )
    don1.set_password("password123")

    don2 = AccountDonatore(
        email="privato@example.com",
        categoria="privato",
        nome="Giuseppe",
        cognome="Bianchi"
    )
    don2.set_password("password123")

    db.session.add_all([don1, don2])
    db.session.flush()


    #donazioni
    donazione1 = DonazioneBene(
        donatore_id=don1.id,
        ente_erogatore_id=ente1.id,
        bene_id=beni[0].id,
        punto_id=punto1.id
    )

    donazione2 = DonazioneMonetaria(
        donatore_id=don2.id,
        ente_id=ente2.id,
        importo=50.0
    )

    db.session.add_all([donazione1, donazione2])


    #pacco
    pacco = PaccoAlimentare(
        nome="Pacco Standard",
        pasta=1,
        pane=1,
        acqua=1,
        carne=1,
        pesce=1,
        verdura=1
    )
    db.session.add(pacco)



    #prenotazioni
    pren1 = Prenotazione(
        beneficiario_id=ben1.id,
        bene_id=beni[0].id,  # esempio: pasta
        punto_id=punto1.id,
        pacco_id=pacco.id,
        stato="ritirata"
    )

    pren2 = Prenotazione(
        beneficiario_id=ben2.id,
        bene_id=beni[1].id,  # esempio: pane
        punto_id=punto2.id,
        pacco_id=pacco.id,
        stato="ritirata"
    )

    db.session.add_all([pren1, pren2])
    db.session.flush()

    #feedback
    fb1 = Feedback(
        prenotazione_id=pren1.id,
        valutazione=5,
        recensione="Servizio impeccabile, personale gentilissimo."
    )

    fb2 = Feedback(
        prenotazione_id=pren2.id,
        valutazione=4,
        recensione="Tutto ok, ma un po' di attesa."
    )

    db.session.add_all([fb1, fb2])



    db.session.commit()
    print(">> Database popolato con successo!")


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        popola_db()
