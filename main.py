import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/"+"*xlsx")

for filepath in filepaths:
    name = Path(filepath).stem
    name = name.split("-")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt="Invoice number: " + name[0], ln=1)

    pdf.set_font(family="Times", size=14, style="I")
    pdf.cell(w=50, h=8, txt="Date: " + name[1], ln=1)

    print(filepath)
    df_excel = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf.set_font(family="Times", size=10, style="")

    w = [30, 60, 40, 30, 30]

    #headers
    pdf.set_font(family="Times", size=10, style="B")
    col = list(df_excel.columns)
    for i in range(4):
        col[i] = col[i].replace("_", " ")
        col[i] = col[i].capitalize()
        pdf.cell(w=w[i], h=8, txt=col[i], border=1)
    col[4] = col[4].replace("_", " ")
    col[4] = col[4].capitalize()
    pdf.cell(w=w[4], h=8, txt=col[4], border=1, ln=1)

    # pdf.cell(w=w[0], h=8, txt=col[0], border=1)
    # pdf.cell(w=w[1], h=8, txt=col[1], border=1)
    # pdf.cell(w=w[2], h=8, txt=col[2], border=1)
    # pdf.cell(w=w[3], h=8, txt=col[3], border=1)
    # pdf.cell(w=w[4], h=8, txt=col[4], border=1, ln=1)

    total_price = str(df_excel["total_price"].sum())

    #normal rows
    pdf.set_font(family="Times", size=10, style="")
    for index, row in df_excel.iterrows():
        for i in range(4):
            pdf.cell(w=w[i], h=8, txt=str(row[df_excel.columns[i]]), border=1)
        pdf.cell(w=w[4], h=8, txt=str(row[df_excel.columns[4]]), border=1, ln=1)

    #total price row
    for i in range(4):
        pdf.cell(w=w[i], h=8, txt="", border=1)
    pdf.cell(w=w[4], h=8, txt=total_price, border=1, ln=1)

    pdf.set_font(family="Times", size=11, style="")
    total = f"The total due amount is {total_price} Euros."
    pdf.cell(w=30, h=8, txt=total, ln=1)
    pdf.set_font(family="Times", size=15, style="B")
    pdf.cell(w=30, h=8, txt=f"Pythonhow")
    pdf.image("pythonhow.png", w=10)

    # for index, row in df_excel.iterrows():
    #     pdf.cell(w=w[0], h=8, txt=str(row[df_excel.columns[0]]), border=1)
    #     pdf.cell(w=w[1], h=8, txt=str(row[df_excel.columns[1]]), border=1)
    #     pdf.cell(w=w[2], h=8, txt=str(row[df_excel.columns[2]]), border=1)
    #     pdf.cell(w=w[3], h=8, txt=str(row[df_excel.columns[3]]), border=1)
    #     pdf.cell(w=w[4], h=8, txt=str(row[df_excel.columns[4]]), border=1, ln=1)

    pdf.output("invoices_pdf/"+name[0]+".pdf")
    pdf.close()
