from reportlab.pdfgen import canvas
from reportlab.lib import colors

class HelloWorldPDF:
  """
  A simple class to generate a PDF with "Hello World" text.
  """

  def __init__(self, filename):
    """
    Constructor to initialize the PDF filename.

    Args:
        filename (str): Path to the output PDF file.
    """
    self.filename = filename

  def generate_pdf(self):
    """
    Generates a PDF with "Hello World" text.
    """
    c = canvas.Canvas(self.filename)
    c.setFont("Helvetica", 50)
    c.drawInlineImage("C://HealStream//images//logo1.png", 4, 750, width=99, height=78)
    c.drawInlineImage("C://HealStream//images//verma.png", 100, 750, width=200, height=80)
    c.drawString(310, 754, "HOSPITAL" , mode=2)
    c.setStrokeColor(colors.blue)
    c.rect(310, 800, 270, 30)
    c.setFont("Helvetica", 14)
    c.setFillColor(colors.red)
    c.drawString(314, 808, "MULTISPECIALITY & TRAUMA CENTER")
    c.line(0, 740, 600, 740)

    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(colors.black)
    c.drawString(20, 720, "PATIENT NAME")
    c.drawString(120, 720, ":- ")
    c.drawString(20, 705, "AGE/SEX")
    c.drawString(120, 705, ":- ")
    c.drawString(20, 690, "ADDRESS")
    c.drawString(120, 690, ":- ")
    c.drawString(20, 675, "PHONE NO")
    c.drawString(120, 675, ":- ")
    c.drawString(20, 660, "CONSULTANT")
    c.drawString(120, 660, ":- ")
    c.drawString(20, 645, "DEPTT")
    c.drawString(120, 645, ":- ")

    c.drawString(300, 720, "REG.FEES")
    c.drawString(400, 720, ":- ")
    c.drawString(300, 705, "OPD NO.")
    c.drawString(400, 705, ":- ")
    c.drawString(300, 690, "UHID NO.")
    c.drawString(400, 690, ":- ")
    c.drawString(300, 675, "DATE & TIME")
    c.drawString(400, 675, ":- ")
    c.drawString(300, 660, "VALID UPTO")
    c.drawString(400, 660, ":- ")
    c.drawString(300, 645, "GUARDIAN")
    c.drawString(400, 645, ":- ")


    c.setStrokeColor(colors.red)
    c.setLineWidth(2)
    c.line(0, 635, 600, 635)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(220, 614, "OPD ASSESSMENT" )
    c.setFont("Helvetica", 12)
    c.drawString(20, 594, "BP       mm/hg            Pulse …… min        Temp……… f          SpO2.- …………            RR.:-………………" )
    c.setLineWidth(1)
    c.line(0, 590, 600, 590)

    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, 540, "O/E" )
    c.drawString(220, 460, "Rx" )
    c.drawString(50, 340, "Investigation" )
    c.drawString(50, 325, "Required" )
    c.drawInlineImage("C://HealStream//images//service.png", 470, 80, width=100, height=90)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, 60, "NEAR GODARA PETROL PUMP, AZAD NAGAR HISAR" )
    c.setFont("Helvetica-Bold", 22)
    c.drawString(420, 60, "01662-315044" )
    c.setFont("Helvetica", 12)
    c.drawString(180, 40, "NOT VALID FOR MEDICO LEGAL PURPOSE" )

    c.save()
    # c.print()


# Create an object and generate the PDF
hello_world_pdf = HelloWorldPDF("temp.pdf")
hello_world_pdf.generate_pdf()
# print("PDF generated successfully!")