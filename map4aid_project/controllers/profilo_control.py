from flask import request, jsonify, send_file
from flask_login import login_required, current_user
from geopy import Nominatim
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
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
            "id": user.id,
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
        geolocator = Nominatim(user_agent="map4aid_project")
        location = geolocator.reverse((p.punto.latitudine, p.punto.longitudine))
        indirizzo = location.address if location else "Indirizzo non disponibile"
        risultato.append({
            "id": p.id,
            "data": p.data_prenotazione.strftime('%d/%m/%Y'),
            "ora": p.data_prenotazione.strftime('%H:%M'),
            "punto": p.punto.nome if p.punto else "",
            "indirizzo": indirizzo if p.punto else "",  # placeholder, potresti aggiungere un campo indirizzo
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
    don_money.sort(key=lambda d: d.data, reverse=True)

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

    def fmt_data(dt):
        return dt.strftime('%d/%m/%Y %H:%M') if dt else "—"

    # =========================================================
    # BENEFICIARIO
    # =========================================================
    if user.tipo == "beneficiario":

        righe.append("=== PRENOTAZIONI ===")

        prenotazioni = Prenotazione.query.filter_by(
            beneficiario_id=user.id
        ).all()

        if not prenotazioni:
            righe.append("Nessuna prenotazione")
        else:
            for p in prenotazioni:

                # Gestione corretta bene / pacco
                if p.bene:
                    nome_item = p.bene.nome
                elif p.pacco:
                    nome_item = p.pacco.nome
                else:
                    nome_item = "Elemento non disponibile"

                nome_punto = p.punto.nome if p.punto else "Punto non disponibile"

                righe.append(
                    f"ID {p.id} | Oggetto: {nome_item} | "
                    f"Punto: {nome_punto} | "
                    f"Data: {fmt_data(p.data_prenotazione)} | "
                    f"Stato: {p.stato}"
                )

        righe.append("")
        righe.append("=== DONAZIONI MONETARIE ===")

        don_money = DonazioneMonetaria.query.filter_by(
            donatore_id=user.id
        ).all()

        if not don_money:
            righe.append("Nessuna donazione")
        else:
            for d in don_money:
                nome_ente = (
                    d.ente.nome_organizzazione
                    if d.ente else "Ente non disponibile"
                )

                righe.append(
                    f"Importo: €{d.importo:.2f} | "
                    f"Ente: {nome_ente} | "
                    f"Data: {fmt_data(d.data)}"
                )

    # =========================================================
    # DONATORE
    # =========================================================
    elif user.tipo == "donatore":

        righe.append("=== DONAZIONI DI BENI ===")

        don_beni = DonazioneBene.query.filter_by(
            donatore_id=user.id
        ).all()

        if not don_beni:
            righe.append("Nessuna donazione")
        else:
            for d in don_beni:
                nome_bene = d.bene.nome if d.bene else "Bene non disponibile"
                nome_ente = (
                    d.ente_erogatore.nome_organizzazione
                    if d.ente_erogatore else "Ente non disponibile"
                )

                righe.append(
                    f"Bene: {nome_bene} | "
                    f"Ente: {nome_ente} | "
                    f"Data: {fmt_data(d.data)}"
                )

        righe.append("")
        righe.append("=== DONAZIONI MONETARIE ===")

        don_money = DonazioneMonetaria.query.filter_by(
            donatore_id=user.id
        ).all()

        if not don_money:
            righe.append("Nessuna donazione")
        else:
            for d in don_money:
                nome_ente = (
                    d.ente.nome_organizzazione
                    if d.ente else "Ente non disponibile"
                )

                righe.append(
                    f"Importo: €{d.importo:.2f} | "
                    f"Ente: {nome_ente} | "
                    f"Data: {fmt_data(d.data)}"
                )

    # =========================================================
    # ENTE EROGATORE
    # =========================================================
    elif user.tipo == "ente_erogatore":

        righe.append("=== DONAZIONI DI BENI RICEVUTE ===")

        don_beni = DonazioneBene.query.filter_by(
            ente_erogatore_id=user.id
        ).all()

        if not don_beni:
            righe.append("Nessuna donazione ricevuta")
        else:
            for d in don_beni:
                nome_bene = d.bene.nome if d.bene else "Bene non disponibile"
                email_donatore = (
                    d.donatore.email if d.donatore else "Donatore non disponibile"
                )

                righe.append(
                    f"Bene: {nome_bene} | "
                    f"Donatore: {email_donatore} | "
                    f"Data: {fmt_data(d.data)}"
                )

        righe.append("")
        righe.append("=== DONAZIONI MONETARIE RICEVUTE ===")

        don_money = DonazioneMonetaria.query.filter_by(
            ente_id=user.id
        ).all()

        if not don_money:
            righe.append("Nessuna donazione ricevuta")
        else:
            for d in don_money:
                email_donatore = (
                    d.donatore.email if d.donatore else "Donatore non disponibile"
                )

                righe.append(
                    f"Importo: €{d.importo:.2f} | "
                    f"Donatore: {email_donatore} | "
                    f"Data: {fmt_data(d.data)}"
                )

        righe.append("")
        righe.append("=== PRENOTAZIONI NEI PUNTI DI DISTRIBUZIONE ===")

        punti = PuntoDistribuzione.query.filter_by(
            ente_erogatore_id=user.id
        ).all()

        if not punti:
            righe.append("Nessuna prenotazione")
        else:
            for punto in punti:
                for p in punto.prenotazioni:

                    if p.bene:
                        nome_item = p.bene.nome
                    elif p.pacco:
                        nome_item = p.pacco.nome
                    else:
                        nome_item = "Elemento non disponibile"

                    email_beneficiario = (
                        p.beneficiario.email
                        if p.beneficiario else "Beneficiario non disponibile"
                    )

                    righe.append(
                        f"Punto: {punto.nome} | "
                        f"Oggetto: {nome_item} | "
                        f"Beneficiario: {email_beneficiario} | "
                        f"Data: {fmt_data(p.data_prenotazione)}"
                    )

    # =========================================================
    # GENERAZIONE PDF
    # =========================================================

    pdf_buffer = genera_pdf_storico("Storico Utente", righe)

    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="storico.pdf"
    )