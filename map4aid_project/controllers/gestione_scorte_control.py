from flask import request, session, jsonify
from controllers.routes import auth_bp
from controllers.permessi import require_roles
from models.models import AccountEnteErogatore, PuntoDistribuzione, Bene, SottoCategoria, MacroCategoria
from config import db
import threading

#lock per race condition su scorte
scorte_lock = threading.Lock()


#lista punti dell'ente loggato (inclusi quelli in attesa di approvazione)
@auth_bp.route("/miei_punti", methods=["GET"])
@require_roles("ente_erogatore")
def miei_punti():
    user_email = session.get("user_email")
    ente = AccountEnteErogatore.query.filter_by(email=user_email).first()
    if not ente:
        return jsonify({"error": "Ente non trovato"}), 404
    punti = PuntoDistribuzione.query.filter_by(ente_erogatore_id=ente.id).all()
    return jsonify([{
        "id": p.id,
        "nome": p.nome,
        "giorni_apertura": p.giorni_apertura,
        "orario_apertura": str(p.orario_apertura),
        "orario_chiusura": str(p.orario_chiusura),
        "latitudine": p.latitudine,
        "longitudine": p.longitudine,
        "accettato": p.accettato
    } for p in punti]), 200


#visualizza scorte

@auth_bp.route("/scorte_punto", methods=["GET"])
@require_roles("ente_erogatore")
def scorte_punto():
    user_email = session.get("user_email")
    ente = AccountEnteErogatore.query.filter_by(email=user_email).first()

    punto_id = request.args.get("punto_id")

    if not punto_id:
        return jsonify({"error": "punto_id mancante"}), 400

    punto = PuntoDistribuzione.query.filter_by(id=punto_id, ente_erogatore_id=ente.id).first()

    if not punto:
        return jsonify({"error": "Punto non autorizzato"}), 403

    beni = Bene.query.filter_by(punto_distribuzione_id=punto_id).all()

    return jsonify([
        {
            "id": b.id,
            "nome": b.nome,
            "quantita": b.quantita,
            "sottocategoria": b.sottocategoria.nome
        }
        for b in beni
    ]), 200




#modifica scorte

@auth_bp.route("/gestione_scorte", methods=["POST"])
@require_roles("ente_erogatore")
def gestione_scorte():
    with scorte_lock:  #evita race condition
        user_email = session.get("user_email")
        ente = AccountEnteErogatore.query.filter_by(email=user_email).first()

        punto_id = request.form.get("punto_id")
        bene_id = request.form.get("bene_id")
        operazione = request.form.get("operazione") 
        quantita = request.form.get("quantita")

        if not punto_id or not bene_id or not operazione or quantita is None:
            return jsonify({"error": "Campi mancanti"}), 400

        quantita = int(quantita)

        #controllo del punto
        punto = PuntoDistribuzione.query.filter_by(id=punto_id, ente_erogatore_id=ente.id).first()

        if not punto:
            return jsonify({"error": "Punto non autorizzato"}), 403

        #recupero del bene
        bene = Bene.query.filter_by(id=bene_id, punto_distribuzione_id=punto_id).first()

        if not bene:
            return jsonify({"error": "Bene non trovato in questo punto"}), 404

        #eseguo operazione
        if operazione == "incrementa":
            bene.quantita += quantita

        elif operazione == "decrementa":
            bene.quantita = max(0, bene.quantita - quantita)

        elif operazione == "imposta":
            bene.quantita = max(0, quantita)

        else:
            return jsonify({"error": "Operazione non valida"}), 400

        db.session.commit()

        return jsonify({
            "message": "Scorte aggiornate",
            "bene": bene.nome,
            "quantita": bene.quantita,
            "punto": punto.nome
        }), 200




#aggiunta bene

@auth_bp.route("/aggiungi_bene", methods=["POST"])
@require_roles("ente_erogatore")
def aggiungi_bene():
    with scorte_lock:
        user_email = session.get("user_email")
        ente = AccountEnteErogatore.query.filter_by(email=user_email).first()

        punto_id = request.form.get("punto_id")
        nome = request.form.get("nome")
        quantita = request.form.get("quantita")
        sottocategoria_id = request.form.get("sottocategoria_id")

        if not punto_id or not nome or quantita is None or not sottocategoria_id:
            return jsonify({"error": "Campi mancanti"}), 400

        quantita = int(quantita)

        # 1. Controllo del punto (usiamo .get per velocità se l'ID è PK)
        punto = PuntoDistribuzione.query.filter_by(id=punto_id, ente_erogatore_id=ente.id).first()
        if not punto:
            return jsonify({"error": "Punto non autorizzato"}), 403

        # 2. Controllo della sottocategoria
        sottocategoria = SottoCategoria.query.get(sottocategoria_id)
        if not sottocategoria:
            return jsonify({"error": "Sottocategoria non valida"}), 400

        # 3. Recupero della MacroCategoria e mappatura del TIPO
        # Usiamo la relazione definita nel model per comodità
        macro = sottocategoria.macro_categoria
        nome_macro = macro.nome  # Qui prendiamo la stringa, es: "Alimenti"

        # Mappatura per far coincidere il nome della Macro con la polymorphic_identity
        mappa_tipi = {
            "Alimenti": "alimentare",
            "Medicinali": "medicinale",
            "Vestiario": "vestiario",
            "Igiene": "igiene",
            "Mobilità": "mobilita"
        }

        # Se il nome della macro non è nella mappa, usiamo "bene" come fallback
        tipo_identita = mappa_tipi.get(nome_macro, "bene")

        # 4. Creazione del bene
        # SQLAlchemy userà 'tipo' per capire che è un'istanza polimorfica
        nuovo_bene = Bene(
            nome=nome,
            quantita=quantita,
            punto_distribuzione_id=punto_id,
            sottocategoria_id=sottocategoria_id,
            tipo=tipo_identita
        )

        db.session.add(nuovo_bene)
        db.session.commit()

        return jsonify({"message": f"Bene di tipo {tipo_identita} aggiunto", "id": nuovo_bene.id}), 200



#rimozione
@auth_bp.route("/rimuovi_bene", methods=["POST"])
@require_roles("ente_erogatore")
def rimuovi_bene():
    with scorte_lock:
        user_email = session.get("user_email")
        ente = AccountEnteErogatore.query.filter_by(email=user_email).first()

        punto_id = request.form.get("punto_id")
        bene_id = request.form.get("bene_id")

        if not punto_id or not bene_id:
            return jsonify({"error": "Campi mancanti"}), 400

        punto = PuntoDistribuzione.query.filter_by(id=punto_id, ente_erogatore_id=ente.id).first()

        if not punto:
            return jsonify({"error": "Punto non autorizzato"}), 403

        bene = Bene.query.filter_by(id=bene_id, punto_distribuzione_id=punto_id).first()

        if not bene:
            return jsonify({"error": "Bene non trovato"}), 404

        db.session.delete(bene)
        db.session.commit()

        return jsonify({"message": "Bene rimosso"}), 200
