from flask import request, jsonify, send_file
from flask_login import login_required, current_user
from controllers.routes import auth_bp
from controllers.pdf_service import genera_pdf_storico
from controllers.auth_facade import AuthFacade
from controllers.service_email.email_control_bridge import EmailControlBridge
from config import db
from models import Prenotazione, DonazioneBene, DonazioneMonetaria, PuntoDistribuzione


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
