from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

def genera_pdf_storico(titolo, righe):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    # Registrazione font Unicode
    pdfmetrics.registerFont(TTFont("DejaVuSans", "DejaVuSans.ttf"))

    pdf.setTitle(titolo)
    pdf.setFont("DejaVuSans", 16)

    y = 800
    pdf.drawString(50, y, str(titolo))
    y -= 40

    pdf.setFont("DejaVuSans", 11)

    for riga in righe:
        pdf.drawString(50, y, str(riga))
        y -= 18

        # Nuova pagina se finisce lo spazio
        if y < 50:
            pdf.showPage()
            pdf.setFont("DejaVuSans", 11)
            y = 800

    pdf.save()
    buffer.seek(0)
    return buffer
