const fs = require('fs');
const path = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab/_beautify_pdf.py';

// Part 1: Header + Styles + Helpers
const part1 = `# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
    TableStyle, PageBreak)
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os

# Fonts
pdfmetrics.registerFont(TTFont('MSJH', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('MSJHB', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=1))

# Tiffany Green Palette
TIFFANY = colors.HexColor('#4DB6AC')
TIFFANY_DARK = colors.HexColor('#26A69A')
TIFFANY_LIGHT = colors.HexColor('#B2DFDB')
TIFFANY_PALE = colors.HexColor('#E0F2F1')
DARK = colors.HexColor('#1a1a2e')
BODY_TEXT = colors.HexColor('#37474F')
SUBTLE = colors.HexColor('#78909C')
WHITE = colors.white

PAGE_W, PAGE_H = A4
M = 20*mm

# Styles
cover_title = ParagraphStyle('CT', fontName='MSJHB', fontSize=28, leading=36,
    textColor=WHITE, alignment=TA_CENTER, spaceAfter=10)
cover_sub = ParagraphStyle('CS', fontName='MSJH', fontSize=14, leading=20,
    textColor=TIFFANY_LIGHT, alignment=TA_CENTER, spaceAfter=6)

h1 = ParagraphStyle('H1', fontName='MSJHB', fontSize=18, leading=26,
    textColor=DARK, spaceBefore=16, spaceAfter=10)
h2 = ParagraphStyle('H2', fontName='MSJHB', fontSize=14, leading=20,
    textColor=TIFFANY_DARK, spaceBefore=12, spaceAfter=8)
h3 = ParagraphStyle('H3', fontName='MSJHB', fontSize=12, leading=17,
    textColor=DARK, spaceBefore=10, spaceAfter=6)
body = ParagraphStyle('B', fontName='MSJH', fontSize=10, leading=17,
    textColor=BODY_TEXT, spaceAfter=7, alignment=TA_JUSTIFY)
body_sm = ParagraphStyle('BS', fontName='MSJH', fontSize=9.5, leading=15,
    textColor=BODY_TEXT, spaceAfter=5)
tip_t = ParagraphStyle('TT', fontName='MSJHB', fontSize=10, leading=15,
    textColor=TIFFANY_DARK, spaceAfter=4)
tip_b = ParagraphStyle('TB', fontName='MSJH', fontSize=9, leading=14,
    textColor=BODY_TEXT)
th = ParagraphStyle('TH', fontName='MSJHB', fontSize=9, leading=13,
    textColor=WHITE, alignment=TA_CENTER)
tc = ParagraphStyle('TC', fontName='MSJH', fontSize=9, leading=13,
    textColor=BODY_TEXT)
ft = ParagraphStyle('FT', fontName='MSJH', fontSize=8, leading=11,
    textColor=SUBTLE, alignment=TA_CENTER)
cta_big = ParagraphStyle('CB', fontName='MSJHB', fontSize=13, leading=19,
    textColor=WHITE, alignment=TA_CENTER)
cta_sub = ParagraphStyle('CS2', fontName='MSJH', fontSize=10, leading=14,
    textColor=TIFFANY_LIGHT, alignment=TA_CENTER)
toc_t = ParagraphStyle('ToCT', fontName='MSJHB', fontSize=16, leading=22,
    textColor=DARK, alignment=TA_CENTER, spaceAfter=16)
toc_i = ParagraphStyle('ToCI', fontName='MSJH', fontSize=10, leading=18,
    textColor=BODY_TEXT)

def make_table(headers, rows, col_widths=None):
    data = [[Paragraph(str(h), th) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), tc) for c in row])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), TIFFANY),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,-1), 'MSJH'),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('ALIGN', (0,1), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, TIFFANY_LIGHT),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, TIFFANY_PALE]),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    return t

def make_tip(title_text, lines):
    td = [[Paragraph('[!] ' + title_text, tip_t)]]
    for ln in lines:
        td.append([Paragraph('* ' + ln, tip_b)])
    tt = Table(td, colWidths=[PAGE_W - 2*M - 16])
    tt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), TIFFANY_LIGHT),
        ('BACKGROUND', (0,1), (-1,-1), TIFFANY_PALE),
        ('BOX', (0,0), (-1,-1), 1.5, TIFFANY),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    return [Spacer(1,6), tt, Spacer(1,6)]

def make_cover(title, subtitle):
    s = []
    s.append(Spacer(1, 75*mm))
    s.append(Paragraph(title, cover_title))
    s.append(Paragraph(subtitle, cover_sub))
    s.append(Spacer(1, 45*mm))
    bd = [[Paragraph('<font color="#B2DFDB">golightly.fun</font> | <font color="#B2DFDB">均在路上的旅遊實驗室</font>', ft)]]
    bt = Table(bd, colWidths=[PAGE_W-2*M])
    bt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), TIFFANY),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 14),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    s.append(bt)
    s.append(PageBreak())
    return s

def make_cta():
    s = []
    s.append(Spacer(1, 18))
    cd = [
        [Paragraph('<font size="14">下載更多完整攻略</font>', cta_big)],
        [Paragraph('前往 golightly.fun 取得所有免費旅遊資源', cta_sub)],
    ]
    ct = Table(cd, colWidths=[PAGE_W-2*M-20])
    ct.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), TIFFANY),
        ('TOPPADDING', (0,0), (-1,0), 16),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('TOPPADDING', (0,1), (-1,1), 8),
        ('BOTTOMPADDING', (0,1), (-1,1), 16),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    s.append(ct)
    s.append(Spacer(1, 10))
    s.append(Paragraph('golightly.fun - 均在路上的旅遊實驗室 | 2026', ft))
    return s

def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont('MSJH', 8)
    canvas.setFillColor(SUBTLE)
    canvas.drawCentredString(PAGE_W/2, 12*mm, '- %d -' % canvas.getPageNumber())
    canvas.restoreState()
`;

fs.writeFileSync(path, part1, 'utf-8');
console.log('Part 1 written:', fs.statSync(path).size, 'bytes');
