import pandas as pd
import glob 
from fpdf import FPDF
from pathlib import Path
filepaths = glob.glob('invoice/*.xlsx')
for filepath in filepaths:
    df = pd.read_excel(filepath)
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_no = filename.split('-')[0]
    date = filename.split('-')[1]

    pdf.set_font(family='Times',style='B',size=12)
    pdf.cell(w=15, h=10, txt=f'invoice No {invoice_no}',ln=1)

    pdf.set_font(family='Times',style='B',size=15)
    pdf.cell(w=15, h=10, txt=f'Date: {date}',ln=1)

    pdf.output(f'{invoice_no}.pdf')