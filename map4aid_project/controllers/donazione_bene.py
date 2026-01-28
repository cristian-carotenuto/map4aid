from datetime import timezone, datetime

from geopy.geocoders import Nominatim
from flask import request, session
from controllers.routes import auth_bp
from models import AccountEnteErogatore
from controllers.service_email.EmailControl import EmailControl
from controllers.permessi import require_roles
from config import db
from models.models import AccountDonatore, PuntoDistribuzione, BeneAlimentare, SottoCategoria, \
    BeneIgiene, BeneMobilita, DonazioneBene


@auth_bp.route("/donazioneBene", methods=["POST"])
@require_roles("donatore")
def donazioneBene():
    geolocator = Nominatim(user_agent="map4aid_project")#per convertire latitudine e longitudine in indirizzo
    email_donatore = session.get("user_email")
    nome = request.form.get("nome")
    quantita = request.form.get("quantita")
    tipo = request.form.get("tipo")
    punto_nome = request.form.get("punto_distribuzione_nome")
    sottocategoria_nome = request.form.get("sottocategoria")

    if not all([nome,quantita,tipo,punto_nome]):
        return {"Errore","Campi obbligatori mancanti"},400

    punto_distribuzione = PuntoDistribuzione.query.filter_by(nome=punto_nome).first()
    location = geolocator.reverse((punto_distribuzione.latitudine,punto_distribuzione.longitudine))
    sottocategoria = SottoCategoria.query.filter_by(nome=sottocategoria_nome).first()
    donatore = AccountDonatore.query.filter_by(email=email_donatore).first()
    erogatore = AccountEnteErogatore.query.filter_by(id=punto_distribuzione.ente_erogatore_id).first()

    #Bene alimentare
    if tipo == "alimentare":
        bene = BeneAlimentare(
            nome = nome,
            quantita = quantita,
            punto_distribuzione_id = punto_distribuzione.id,
            sottocategoria_id = sottocategoria.id,
            allergeni=request.form.get("allergeni"),
            scadenza = datetime.strptime(request.form.get("scadenza"), "%Y-%m-%d").date()
        )

    #Bene per l'igiene
    elif tipo == "igiene":
        bene = BeneIgiene(
            nome=nome,
            quantita=quantita,
            punto_distribuzione_id=punto_distribuzione.id,
            sottocategoria_id=sottocategoria.id,
            destinatari = request.form.get("destinatari")
        )


    #Medicinale
    elif tipo == "medicinale":
        bene = BeneIgiene(
            nome=nome,
            quantita=quantita,
            punto_distribuzione_id=punto_distribuzione.id,
            sottocategoria_id=sottocategoria.id,
            tipo_medicinale=request.form.get("tipo_medicinale"),
            scadenza = datetime.strptime(request.form.get("scadenza"), "%Y-%m-%d").date()
        )


    #Beni per la mobilità
    elif tipo == "mobilità":
        bene = BeneMobilita(
            nome=nome,
            quantita=quantita,
            punto_distribuzione_id=punto_distribuzione.id,
            sottocategoria_id=sottocategoria.id,
            tipo_mobilita=request.form.get("tipo_mobilita"),
            stato = request.form.get("stato"),
        )

    #Vestiti
    elif tipo == "vestiario":
        bene = BeneMobilita(
            nome=nome,
            quantita=quantita,
            punto_distribuzione_id=punto_distribuzione.id,
            sottocategoria_id=sottocategoria.id,
            taglia=request.form.get("taglia"),
            condizioni = request.form.get("condizioni")
        )

    db.session.add(bene)
    db.session.commit()

    donazione = DonazioneBene(
        donatore_id = donatore.id,
        ente_erogatore_id = punto_distribuzione.ente_erogatore_id,
        bene_id = bene.id,
        punto_id = punto_distribuzione.id,
        data = datetime.now(timezone.utc)
    )
    db.session.add(donazione)
    db.session.commit()
    email_control = EmailControl()
    email_ok1 = email_control.invia_email_donazione_ente(erogatore.email,donatore.email,bene,donazione,punto_distribuzione,sottocategoria_nome,location.address)
    email_ok2 = email_control.invia_email_donazione_donatore(donatore.email,erogatore.email,bene)

    if email_ok1 and email_ok2:
        return {"message":"Donazione di bene effetuata"},200
    else:
        return {"errore":"Donazione effetuata ma email non inviate"},500



