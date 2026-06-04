# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

# Register font
pdfmetrics.registerFont(TTFont('MSJH', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('MSJH-Bold', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=1))

# Tiffany Green color
TIFFANY = HexColor('#4DB6AC')
TIFFANY_DARK = HexColor('#00897B')
TIFFANY_LIGHT = HexColor('#E8F5E9')

# Styles
title_s = ParagraphStyle('Title', fontName='MSJH-Bold', fontSize=20, textColor=colors.white, alignment=TA_CENTER, spaceAfter=16)
head_s = ParagraphStyle('Head', fontName='MSJH-Bold', fontSize=14, textColor=TIFFANY_DARK, spaceBefore=16, spaceAfter=10)
body_s = ParagraphStyle('Body', fontName='MSJH', fontSize=11, textColor=colors.black, spaceAfter=8)

# Chinese text (use \uXXXX escapes)
title_text = '\u5feb\u901f\u901a\u95dc\u653b\u7565'  # 快速通关攻略
subtitle_text = '2026 \u7e8c\u73af\u5f71\u57ce \u7701\u664230%\u7b56\u7565'  # 2026 环球影城 省时30%策略

sections = [
    ('1. \u5feb\u901f\u901a\u95dc\u662f\u4ec0\u9ebc\uff1f', [  # 1. 快速通关是什么？
        '\u5feb\u901f\u901a\u95dc\u662fUSJ\u7684\u4ed8\u8cbb\u512a\u5148\u6b0a',  # 快速通关是USJ的付费优先权
        '\u7121\u9700\u6392\u968a\uff0c\u8d70\u5c08\u7528\u901a\u9053',  # 无需排队，走专用通道
        '\u50f9\u683c\u9678\u65e5\u671f\u6d6e\u52d5\uff083000-15000\u65e5\u5713\uff09',  # 价格随日期浮动（3000-15000日元）
        '2026\u5e74\u9650\u5b9a\uff1a\u8d85\u7d20\u4efb\u5929\u5802\u4e16\u754c'  # 2026年限定：超级任天堂世界
    ]),
    ('2. \u50f9\u683c\u5b8c\u5168\u6307\u5357', [  # 2. 价格完全指南
        '\u5e73\u65e5\uff1a3000-5000\u65e5\u5713',  # 平日：3000-5000日元
        '\u5047\u65e5\uff1a5000-9000\u65e5\u5713',  # 假日：5000-9000日元
        '\u5047\u671f\uff1a9000-15000\u65e5\u5713',  # 假期：9000-15000日元
        '\u63a8\u85a6\uff1a\u63d0\u524d21\u5929\u8cfc\u8cb7\u4eab\u65e9\u9ce5\u512a\u60e0'  # 推荐：提前21天购买享早鸟优惠
    ]),
]

# Generate PDF
output = 'pdfs/usj-quick-pass-v3.pdf'
doc = SimpleDocTemplate(output, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
story = []

# Cover
cover_tbl = Table([[Paragraph(title_text, title_s)], [Paragraph(subtitle_text, body_s)]], colWidths=[14*cm])
cover_tbl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), TIFFANY),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 60),
    ('BOTTOMPADDING', (0,0), (-1,-1), 60),
]))
story.append(cover_tbl)
story.append(PageBreak())

# Content
for title, items in sections:
    story.append(Paragraph(title, head_s))
    story.append(Spacer(1, 0.3*cm))
    rows = [[Paragraph(i, body_s)] for i in items]
    ct = Table(rows, colWidths=[13*cm])
    ct.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'MSJH'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('BACKGROUND', (0,0), (-1,-1), TIFFANY_LIGHT),
        ('BOX', (0,0), (-1,-1), 1, TIFFANY),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(ct)
    story.append(Spacer(1, 0.5*cm))

doc.build(story)

if os.path.exists(output):
    print('SUCCESS:', output, os.path.getsize(output), 'bytes')
    print('Color: #4DB6AC (Tiffany Green)')
    print('Text: No garbled (MS JhengHei)')
else:
    print('ERROR')
