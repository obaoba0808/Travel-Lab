# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

# Fonts
pdfmetrics.registerFont(TTFont('MSJH', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('MSJHB', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=1))

# Colors
T = colors.HexColor('#4DB6AC')
TD = colors.HexColor('#26A69A')
TL = colors.HexColor('#B2DFDB')
TP = colors.HexColor('#E0F2F1')
W = colors.white
DT = colors.HexColor('#37474F')

PAGE_W, PAGE_H = A4
M = 20 * mm

# Styles
h1 = ParagraphStyle('h1', fontName='MSJHB', fontSize=24, textColor=TD, spaceBefore=20, spaceAfter=10)
body = ParagraphStyle('body', fontName='MSJH', fontSize=11, textColor=DT, leading=16, alignment=TA_JUSTIFY, spaceAfter=8)

def make_table(headers, data):
    t = Table([headers] + data, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), T),
        ('TEXTCOLOR', (0,0), (-1,0), W),
        ('FONTNAME', (0,0), (-1,0), 'MSJHB'),
        ('FONTSIZE', (0,0), (-1,0), 11),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BACKGROUND', (0,1), (-1,-1), W),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [W, TP]),
        ('GRID', (0,0), (-1,-1), 0.5, TL),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def make_cover(title, subtitle):
    s = []
    s.append(Spacer(1, 60))
    line = Table([['']], colWidths=[100], rowHeights=[3])
    line.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), T)]))
    s.append(line)
    s.append(Spacer(1, 30))
    s.append(Paragraph(title, ParagraphStyle('ct', fontName='MSJHB', fontSize=48, textColor=TD, alignment=TA_CENTER)))
    s.append(Paragraph(subtitle, ParagraphStyle('cs', fontName='MSJH', fontSize=18, textColor=T, alignment=TA_CENTER)))
    s.append(Spacer(1, 40))
    line2 = Table([['']], colWidths=[60], rowHeights=[2])
    line2.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), TL)]))
    s.append(line2)
    s.append(PageBreak())
    return s

def make_cta():
    s = []
    s.append(Spacer(1, 20))
    t = Table([[Paragraph('想要更多旅遊資訊？', ParagraphStyle('cta', fontName='MSJHB', fontSize=16, textColor=TD, alignment=TA_CENTER))]], colWidths=[PAGE_W - 2*M])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), TP),
        ('ROUNDEDCORNERS', [8,8,8,8]),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('PADDING', (0,0), (-1,-1), 15),
    ]))
    s.append(t)
    s.append(Spacer(1, 8))
    s.append(Paragraph('加入 LINE 群組：https://line.me/ti/g/NbNGnW4Eh6', body))
    s.append(Paragraph('更多免費旅遊 PDF：https://golightly.fun', body))
    return s

def gen_tokyo_metro():
    """Generate Tokyo Metro Map PDF"""
    s = []
    s += make_cover('東京地鐵路線圖', '2026 最新版')
    s.append(Paragraph('東京地鐵完整指南', h1))
    s.append(Paragraph('東京擁有13條地鐵路線、285個車站，是全世界最複雜的城市軌道交通系統之一。本指南提供完整路線圖、轉乘車站、票價資訊與旅遊建議，幫助您在東京暢行無阻。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['路線名稱', '代表色', '車站數', '營運長度(km)'],
        ['銀座線', '橘色', '19', '14.3'],
        ['丸之內線', '紅色', '25', '27.4'],
        ['日比谷線', '銀色', '21', '20.3'],
        ['東西線', '天藍色', '23', '30.8'],
        ['千代田線', '綠色', '20', '24.0'],
        ['有樂町線', '金色', '24', '28.3'],
        ['半藏門線', '紫色', '16', '16.8'],
    ]
    s.append(make_table(['路線名稱', '代表色', '車站數', '營運長度(km)'], data))
    s.append(Spacer(1, 10))
    s += make_cta()
    return s

# Main
doc = SimpleDocTemplate('downloads/tokyo-metro-map.pdf')
story = gen_tokyo_metro()
doc.build(story)
print('OK: downloads/tokyo-metro-map.pdf')
