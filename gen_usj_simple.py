# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

# 注册字体
pdfmetrics.registerFont(TTFont('MSJH', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('MSJH-Bold', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=1))

# Tiffany Green 配色
TIFFANY = HexColor('#4DB6AC')
TIFFANY_DARK = HexColor('#00897B')
TIFFANY_LIGHT = HexColor('#E8F5E9')

# 样式
title_style = ParagraphStyle('Title', fontName='MSJH-Bold', fontSize=18, textColor=colors.white, alignment=TA_CENTER, spaceAfter=12)
heading_style = ParagraphStyle('Heading', fontName='MSJH-Bold', fontSize=14, textColor=TIFFANY_DARK, spaceBefore=12, spaceAfter=8)
body_style = ParagraphStyle('Body', fontName='MSJH', fontSize=11, textColor=colors.black, spaceAfter=6)

# 生成 PDF
output_path = 'pdfs/usj-simple-test.pdf'
doc = SimpleDocTemplate(output_path, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm)
story = []

# 封面
cover_title = Paragraph('USJ 快速通关攻略', title_style)
cover_data = [[cover_title]]
cover_tbl = Table(cover_data, colWidths=[14*cm])
cover_tbl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), TIFFANY),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 40),
    ('BOTTOMPADDING', (0,0), (-1,-1), 40),
]))
story.append(cover_tbl)

# 简单内容
content = [
    '1. 快速通关是什么？',
    '快速通关（Express Pass）是USJ的付费优先权',
    '无需排队，走专用通道',
    '',
    '2. 价格指南',
    '平日：3000-5000日元',
    '周末：5000-9000日元',
]
for item in content:
    if item:
        p = Paragraph(item, heading_style if item.startswith(('1.', '2.', '3.', '4.', '5.')) else body_style)
        story.append(p)

doc.build(story)
print('SUCCESS:', output_path)
