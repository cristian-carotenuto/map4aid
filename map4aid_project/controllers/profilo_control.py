from flask import request, jsonify, send_file
from flask_login import login_required, current_user
from controllers.routes import auth_bp
from controllers.pdf_service import genera_pdf_storico
from controllers.auth_facade import AuthFacade
from controllers.service_email.email_control_bridge import EmailControlBridge
from config import db
from models.models import Prenotazione, DonazioneBene, DonazioneMonetaria, PuntoDistribuzione


@auth_bp.route("/profilo", methods=["GET"])
@login_required
def get_profilo():
    """
    Restituisce i dati del profilo dell'utente autenticato
    """
    user = current_user
    
    # Dati base comuni a tutti
    profilo = {
        "email": user.email,
        "tipo": user.tipo
    }
    
    # Dati specifici per tipo di account
    if user.tipo == "beneficiario":
        profilo.update({
            "nome": user.nome,
            "cognome": user.cognome,
            "data_nascita": user.data_nascita.strftime('%d/%m/%Y') if user.data_nascita else None,
            "allergeni": user.allergeni,
            "patologie": user.patologie
        })
    elif user.tipo == "donatore":
        if user.categoria == "privato":
            profilo.update({
                "nome": user.nome,
                "cognome": user.cognome,
                "categoria": user.categoria
            })
        else:  # azienda
            profilo.update({
                "nome_attivita": user.nome_attivita,
                "partita_iva": user.partita_iva,
                "indirizzo_sede": user.indirizzo_sede,
                "categoria": user.categoria
            })
    elif user.tipo == "ente_erogatore":
        profilo.update({
            "nome_organizzazione": user.nome_organizzazione,
            "tipologia_ente": user.tipologia_ente,
            "indirizzo_sede": user.indirizzo_sede,
            "iban": user.iban
        })
    
    return jsonify(profilo), 200


@auth_bp.route("/prenotazioni", methods=["GET"])
@login_required
def get_prenotazioni():
    """
    Restituisce tutte le prenotazioni dell'utente autenticato (solo beneficiari)
    """
    user = current_user
    
    if user.tipo != "beneficiario":
        return jsonify({"error": "Solo i beneficiari hanno prenotazioni"}), 403
    
    prenotazioni = Prenotazione.query.filter_by(beneficiario_id=user.id).all()
    
    risultato = []
    for p in prenotazioni:
        risultato.append({
            "id": p.id,
            "data": p.data_prenotazione.strftime('%d/%m/%Y'),
            "ora": p.data_prenotazione.strftime('%H:%M'),
            "punto": p.punto.nome if p.punto else "",
            "indirizzo": p.punto.latitudine if p.punto else "",  # placeholder, potresti aggiungere un campo indirizzo
            "bene": p.bene.nome if p.bene else (p.pacco.nome if p.pacco else "N/A"),
            "quantita": 1,  # puoi aggiungere un campo quantità al model se necessario
            "stato": p.stato
        })
    
    return jsonify(risultato), 200


@auth_bp.route("/donazioni", methods=["GET"])
@login_required
def get_donazioni():
    """
    Restituisce tutte le donazioni dell'utente autenticato (solo donatori)
    """
    user = current_user
    
    if user.tipo != "donatore":
        return jsonify({"error": "Solo i donatori hanno donazioni"}), 403
    
    risultato = []
    
    # Donazioni di beni
    don_beni = DonazioneBene.query.filter_by(donatore_id=user.id).all()
    for d in don_beni:
        risultato.append({
            "id": f"DB{d.id}",
            "tipo": "bene",
            "data": d.data.strftime('%d/%m/%Y'),
            "bene": d.bene.nome if d.bene else "N/A",
            "ente": d.ente_erogatore.nome_organizzazione if d.ente_erogatore else "N/A",
            "stato": "completata"
        })
    
    # Donazioni monetarie
    don_money = DonazioneMonetaria.query.filter_by(donatore_id=user.id).all()
    for d in don_money:
        risultato.append({
            "id": f"DM{d.id}",
            "tipo": "monetaria",
            "data": d.data.strftime('%d/%m/%Y'),
            "importo": f"{d.importo:.2f}",
            "ente": d.ente.nome_organizzazione if d.ente else "N/A",
            "stato": "completata"
        })
    
    # Ordina per data (più recenti prima)
    risultato.sort(key=lambda x: x['data'], reverse=True)
    
    return jsonify(risultato), 200


@auth_bp.route("/modifica_profilo", methods=["POST"])
@login_required
def modifica_profilo():
    from controllers.service_email.email_control_bridge import EmailControlBridge 
    from controllers.auth_facade import AuthFacade
    facade = AuthFacade(EmailControlBridge())

    user = current_user
    data = request.form

    #validazione email
    if "email" in data:
        try:
            facade.validate_email(data["email"],user)
            user.email = data["email"]
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    #BENEFICIARIO
    if user.tipo == "beneficiario":
        for field in ["nome", "cognome", "allergeni", "patologie"]:
            if field in data:
                setattr(user, field, data[field])

    #DONATORE
    elif user.tipo == "donatore":
        # privato
        if user.categoria == "privato":
            for field in ["nome", "cognome"]:
                if field in data:
                    setattr(user, field, data[field])
        # azienda
        else:
            for field in ["nome_attivita", "indirizzo_sede"]:
                if field in data:
                    setattr(user, field, data[field])

    #ENTE EROGATORE
    elif user.tipo == "ente_erogatore":
        for field in ["nome_organizzazione", "indirizzo_sede", "iban"]:
            if field in data:
                setattr(user, field, data[field])

    #salva
    db.session.commit()

    return jsonify({"message": "Profilo aggiornato con successo"}), 200


@auth_bp.route("/storico_pdf", methods=["GET"])
@login_required
def storico_pdf():
    user = current_user
    righe = []

    if user.tipo == "beneficiario":
        prenotazioni = Prenotazione.query.filter_by(beneficiario_id=user.id).all()
        righe.append("=== PRENOTAZIONI ===")
        for p in prenotazioni:
            righe.append(
                f"ID {p.id} | Bene: {p.bene.nome} | Punto: {p.punto.nome} | "
                f"Data: {p.data_prenotazione.strftime('%d/%m/%Y %H:%M')} | Stato: {p.stato}"
            )

    elif user.tipo == "donatore":
        righe.append("=== DONAZIONI DI BENI ===")
        don_beni = DonazioneBene.query.filter_by(donatore_id=user.id).all()
        for d in don_beni:
            righe.append(
                f"Bene: {d.bene.nome} | Quantità: {d.bene.quantita} | "
                f"Ente: {d.ente_erogatore.nome_organizzazione} | "
                f"Data: {d.data.strftime('%d/%m/%Y %H:%M')}"
            )

        righe.append("")
        righe.append("=== DONAZIONI MONETARIE ===")
        don_money = DonazioneMonetaria.query.filter_by(donatore_id=user.id).all()
        for d in don_money:
            righe.append(
                f"Importo: €{d.importo:.2f} | Ente: {d.ente.nome_organizzazione} | "
                f"Data: {d.data.strftime('%d/%m/%Y %H:%M')}"
            )

    elif user.tipo == "ente_erogatore":
        righe.append("=== DONAZIONI DI BENI RICEVUTE ===")
        don_beni = DonazioneBene.query.filter_by(ente_erogatore_id=user.id).all()
        for d in don_beni:
            righe.append(
                f"Bene: {d.bene.nome} | Donatore: {d.donatore.email} | "
                f"Data: {d.data.strftime('%d/%m/%Y %H:%M')}"
            )

        righe.append("")
        righe.append("=== DONAZIONI MONETARIE RICEVUTE ===")
        don_money = DonazioneMonetaria.query.filter_by(ente_id=user.id).all()
        for d in don_money:
            righe.append(
                f"Importo: €{d.importo:.2f} | Donatore: {d.donatore.email} | "
                f"Data: {d.data.strftime('%d/%m/%Y %H:%M')}"
            )

        righe.append("")
        righe.append("=== PRENOTAZIONI NEI PUNTI DI DISTRIBUZIONE ===")
        punti = PuntoDistribuzione.query.filter_by(ente_erogatore_id=user.id).all()
        for punto in punti:
            for p in punto.prenotazioni:
                righe.append(
                    f"Punto: {punto.nome} | Bene: {p.bene.nome} | "
                    f"Beneficiario: {p.beneficiario.email} | "
                    f"Data: {p.data_prenotazione.strftime('%d/%m/%Y %H:%M')}"
                )

    pdf_buffer = genera_pdf_storico("Storico Utente", righe)

    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="storico.pdf"
    )
