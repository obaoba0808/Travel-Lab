# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER
import os

# Register fonts
pdfmetrics.registerFont(TTFont("MSJH", "C:/Windows/Fonts/msjh.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("MSJHB", "C:/Windows/Fonts/msjh.ttc", subfontIndex=1))

# Colors
TEAL = colors.HexColor("#0ABAB5")
DARK = colors.HexColor("#1a1a2e")

# Styles
h1 = ParagraphStyle("H1", fontName="MSJHB", fontSize=18, leading=24, textColor=DARK, spaceAfter=12, alignment=TA_CENTER)
h2 = ParagraphStyle("H2", fontName="MSJHB", fontSize=14, leading=20, textColor=TEAL, spaceBefore=16, spaceAfter=8)
body = ParagraphStyle("Body", fontName="MSJH", fontSize=9.5, leading=15, textColor=colors.HexColor("#333333"), spaceAfter=6)
center = ParagraphStyle("Center", fontName="MSJH", fontSize=9, leading=14, alignment=TA_CENTER)

# Build PDF
story = []
story.append(Paragraph("Tokyo Metro Complete Guide", h1))
story.append(Paragraph("Route Map x Transfer Tips x 24H Ticket | Test Version", center))
story.append(Spacer(1, 15))

story.append(Paragraph("Test Section 1", h2))
story.append(Paragraph("[OK] This is a test with ASCII markers only", body))
story.append(Paragraph("[!] No Unicode symbols (no checkmark, no warning sign)", body))
story.append(Paragraph("* Bullet point 1", body))
story.append(Paragraph("* Bullet point 2", body))
story.append(Spacer(1, 10))

story.append(Paragraph("Test Section 2", h2))
story.append(Paragraph("Content without any Unicode symbols", body))
story.append(Paragraph("All markers are ASCII: [OK], [!], *, >, X", body))
story.append(Spacer(1, 10))

# CTA
story.append(Spacer(1, 20))
story.append(Paragraph("[ More Guides Available ]", center))
story.append(Paragraph("golightly.fun - Travel Lab", center))

# Save
output = "downloads/test_clean.pdf"
doc = SimpleDocTemplate(output, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm)
doc.build(story)

size = os.path.getsize(output)
print("[SUCCESS] Test PDF generated:", size, "bytes")
print("[INFO] Check downloads/test_clean.pdf for garbled characters")
print("[INFO] If OK, will generate all 21 PDFs with same method")
