# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

# Register font
pdfmetrics.registerFont(TTFont('MSJH', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=0))

# Tiffany Green color
TIFFANY = HexColor('#4DB6AC')

# Create style
title_style = ParagraphStyle(
    'Title',
    fontName='MSJH',
    fontSize=18,
    textColor=colors.white,
    alignment=TA_CENTER,
    spaceAfter=12
)

# Create PDF
output_path = 'pdfs/usj-color-test.pdf'
doc = SimpleDocTemplate(output_path, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm)
story = []

# Add cover
title = Paragraph('USJ Quick Pass Guide', title_style)
cover_data = [[title]]
cover_tbl = Table(cover_data, colWidths=[14*cm])
cover_tbl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), TIFFANY),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 40),
    ('BOTTOMPADDING', (0,0), (-1,-1), 40),
]))
story.append(cover_tbl)

doc.build(story)

# Check result
if os.path.exists(output_path):
    size = os.path.getsize(output_path)
    print('SUCCESS: Generated', output_path)
    print('Size:', size, 'bytes')
    print('Color: Tiffany Green (#4DB6AC)')
    print('Please check this PDF to verify color!')
else:
    print('ERROR: Failed to generate PDF')
