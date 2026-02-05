from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

def genera_pdf_storico(titolo, righe):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    pdf.setTitle(titolo)
    pdf.setFont("Times-Roman", 16)

    y = 800
    pdf.drawString(50, y, titolo)
    y -= 40

    pdf.setFont("Times-Roman", 11)

    for riga in righe:
        pdf.drawString(50, y, riga)
        y -= 18

        #nuova pagina se finisce lo spazio
        if y < 50:
            pdf.showPage()
            pdf.setFont("Times-Roman", 11)
            y = 800

    pdf.save()
    buffer.seek(0)
    return buffer
