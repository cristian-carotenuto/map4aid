from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

def genera_pdf_storico(titolo, righe):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    # Registrazione font Unicode

    pdf.setTitle(titolo)

    y = 800
    pdf.drawString(50, y, str(titolo))
    y -= 40


    for riga in righe:
        pdf.drawString(50, y, str(riga))
        y -= 18

        # Nuova pagina se finisce lo spazio
        if y < 50:
            pdf.showPage()
            y = 800

    pdf.save()
    buffer.seek(0)
    return buffer
