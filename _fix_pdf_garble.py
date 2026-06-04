# -*- coding: utf-8 -*-
import sys; sys.stdout.reconfigure(encoding="utf-8")
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

pdfmetrics.registerFont(TTFont("MSJH", "C:/Windows/Fonts/msjh.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("MSJHB", "C:/Windows/Fonts/msjh.ttc", subfontIndex=1))

TEAL = colors.HexColor("#0ABAB5")
DARK = colors.HexColor("#1a1a2e")
LIGHT_BG = colors.HexColor("#e8f8f7")

h1 = ParagraphStyle("H1", fontName="MSJHB", fontSize=18, leading=24, textColor=DARK, spaceAfter=12, alignment=TA_CENTER)
h2 = ParagraphStyle("H2", fontName="MSJHB", fontSize=14, leading=20, textColor=TEAL, spaceBefore=16, spaceAfter=8)
h3 = ParagraphStyle("H3", fontName="MSJHB", fontSize=11, leading=16, textColor=DARK, spaceBefore=10, spaceAfter=6)
body = ParagraphStyle("Body", fontName="MSJH", fontSize=9.5, leading=15, textColor=colors.HexColor("#333333"), spaceAfter=6)
tip = ParagraphStyle("Tip", fontName="MSJH", fontSize=9, leading=14, textColor=colors.HexColor("#d35400"), leftIndent=15, spaceAfter=4)
center = ParagraphStyle("Center", fontName="MSJH", fontSize=9, leading=14, alignment=TA_CENTER)
sc = ParagraphStyle("SC", fontName="MSJH", fontSize=8, leading=12, textColor=colors.HexColor("#888888"), alignment=TA_CENTER)

def tbl(headers, rows, widths):
    d = [[Paragraph("<b>"+h+"</b>", body) for h in headers]
    for r in rows: d.append([Paragraph(str(c), body) for c in r])
    t = Table(d, colWidths=widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TEAL),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("FONTNAME", (0,0), (-1,-1), "MSJH"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    return t

def cta(story):
    story.append(Spacer(1, 20))
    bd = [
        [Paragraph("<b>[ 更多完整攻略 ]</b>", center)],
        [Paragraph("golightly.fun - 均在路上的旅游实验室", center)],
        [Paragraph("<b>[ 即时旅游咨询 ]</b>", center)],
        [Paragraph("加入 LINE 群组，免费获得行程建议", center)],
    ]
    b = Table(bd, [380])
    b.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 2, TEAL),
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#f0fffe")),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    story.append(b)
    story.append(Spacer(1, 15))
    story.append(Paragraph("均在路上 Travel Lab (c) 2026 | golightly.fun", sc))
    story.append(Paragraph("价格与资讯可能随时变动，出发前请再次确认", sc))

def build(fn, title, sub, secs):
    p = "downloads/" + fn + ".pdf"
    doc = SimpleDocTemplate(p, pagesize=A4, leftMargin=25*mm, rightMargin=25*mm, topMargin=20*mm, bottomMargin=20*mm)
    s = []
    s.append(Paragraph(title, h1))
    s.append(Paragraph(sub, center))
    s.append(Spacer(1, 8))
    for sec in secs: sec(s)
    cta(s)
    doc.build(s)
    return os.path.getsize(p)

OK = "[OK] "
WRN = "[!] "
STAR = "* "
ARROW = "> "
CROSS = "X "

