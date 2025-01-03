from fpdf import FPDF
from glob import glob
from pathlib import Path

paths = glob("Text+Files/" + "*txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font(family="Times", size=24, style="B")

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
    pdf.cell(w=50, h=8, txt=filenames.title())

pdf.output("Text+Files/animals.pdf")