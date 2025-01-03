from fpdf import FPDF
from glob import glob
from pathlib import Path

paths = glob("Text+Files/" + "*txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for path in paths:
    filenames = Path(path).stem

    # different ways to create filenames
    # filenames = path.split("/")
    # filenames = filenames[1]
    # filenames = filenames[:len(filenames)-4]

    # different ways to create filenames
    # filenames = filenames[1].split(".")
    # filenames = filenames[0]

    pdf.add_page()

    pdf.set_font(family="Times", size=24, style="B")
    pdf.cell(w=50, h=8, txt=filenames.title(), ln=1)

    with open(path, "r") as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("Text+Files/animals.pdf")