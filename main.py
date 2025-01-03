import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/"+"*xlsx")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    name = Path(filepath).stem
    name = name.split("-")

    excelinvoice = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt="Invoice number: " + name[0], ln=1)

    pdf.set_font(family="Times", size=12, style="")
    pdf.cell(w=50, h=8, txt="Date: " + name[1])

    pdf.output("invoices_pdf/"+name[0]+".pdf")
