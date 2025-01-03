import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/"+"*xlsx")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font(family="Times", size=16, style="B")
pdf.cell(w=50, h=8, txt="Invoice number: " + "1")

for filepath in filepaths:
    name = Path(filepath).stem
    name = name.split("-")
    print(name[0])
    excelinvoice = pd.read_excel(filepath, sheet_name="Sheet 1")
