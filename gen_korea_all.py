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

# Colors (Tiffany Green)
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
h2 = ParagraphStyle('h2', fontName='MSJHB', fontSize=18, textColor=T, spaceBefore=15, spaceAfter=8)
body = ParagraphStyle('body', fontName='MSJH', fontSize=11, textColor=DT, leading=16, alignment=TA_JUSTIFY, spaceAfter=8)

def make_table(headers, data):
    t = Table([headers] + data, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), T),
        ('TEXTCOLOR', (0,0), (-1,0), W),
        ('FONTNAME', (0,0), (-1,0), 'MSJHB'),
        ('FONTSIZE', (0,0), (-1,0), 11),
        ('FONTNAME', (0,1), (-1,-1), 'MSJH'),
        ('FONTSIZE', (0,1), (-1,-1), 10),
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

# ============ PDF 1: Seoul Food Map ============
def gen_seoul_food():
    doc = SimpleDocTemplate('downloads/seoul-food-map.pdf')
    s = []
    s += make_cover('首爾美食地圖', '2026 必吃美食與餐廳推薦')
    s.append(Paragraph('首爾美食完整指南', h1))
    s.append(Paragraph('首爾是美食天堂，從街頭小吃到米其林餐廳，應有盡有。本指南精選20間必訪餐廳，涵蓋韓式烤肉、部隊鍋、人參雞湯、炒年糕等經典美食，並提供預約方式與價位參考。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['美食種類', '推薦餐廳', '人均消費(韓元)', '所在地'],
        ['韓式烤肉', '新村姜虎東白丁烤肉', '30,000-50,000', '新村'],
        ['部隊鍋', '新村部隊鍋一條街', '10,000-15,000', '新村'],
        ['人參雞湯', '土俗村人參雞湯', '15,000-20,000', '景福宮'],
        ['炒年糕', '新堂洞炒年糕街', '8,000-12,000', '東大門'],
    ]
    s.append(make_table(['美食種類', '推薦餐廳', '人均消費(韓元)', '所在地'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('美食區域推薦', h2))
    s.append(Paragraph('新村是首爾美食的核心區域，聚集了最多經典小吃。明洞則以街頭美食聞名，適合喜愛嘗鮮的旅人。高級料理建議預約，平價美食則可直接前往。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: seoul-food-map.pdf')

# ============ PDF 2: Busan Capsule Guide ============
def gen_busan_capsule():
    doc = SimpleDocTemplate('downloads/busan-capsule-guide.pdf')
    s = []
    s += make_cover('釜山膠囊列車預約攻略', '2026 最新預約流程與乘車指南')
    s.append(Paragraph('釜山膠囊列車完整攻略', h1))
    s.append(Paragraph('釜山膠囊列車（Haeundae Blueline Park）是釜山最新的觀光地標，全長4.8公里，連接海雲台與青沙浦。本攻略提供預約流程、乘車體驗、攝影攻略與周邊景點推薦。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['項目', '說明'],
        ['票價', '成人 15,000 韓元（來回）'],
        ['營運時間', '09:00-20:00（季節調整）'],
        ['乘車地點', '海雲台站 / 尾浦站'],
        ['預約方式', '官網線上預約（建議提前3天）'],
        ['最佳攝影點', '尾浦站展望台（海景+列車）'],
    ]
    s.append(make_table(['項目', '說明'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('乘車建議', h2))
    s.append(Paragraph('建議選擇右側座位（靠海側），可欣賞最美海景。黃昏時分（17:00-18:00）光線最柔和，適合攝影。週末與假日容易客滿，建議平日前往。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: busan-capsule-guide.pdf')

# ============ PDF 3: Jeju Driving Route ============
def gen_jeju_driving():
    doc = SimpleDocTemplate('downloads/jeju-driving-route.pdf')
    s = []
    s += make_cover('濟州島自駕路線', '2026 精選5條必走路線')
    s.append(Paragraph('濟州島自駕完整攻略', h1))
    s.append(Paragraph('濟州島是韓國最大的島嶼，面積約1,849平方公里，環島公路全長約181公里。自駕是遊覽濟州島最自由便利的方式，可以隨意停靠景點、調整行程節奏。本攻略精選5條自駕路線，涵蓋東部、西部、南部、北部與環島路線，每條路線規劃2-3天行程。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['路線名稱', '天數', '總里程(km)', '適合族群'],
        ['東部海岸路線', '2天1夜', '120', '第一次來濟州'],
        ['西部田園路線', '2天1夜', '110', '喜歡自然風景'],
        ['南部文化路線', '1天', '80', '親子同遊'],
        ['北部都市路線', '1天', '60', '購物美食愛好者'],
        ['環島深度路線', '3天2夜', '200', '深度旅遊玩家'],
    ]
    s.append(make_table(['路線名稱', '天數', '總里程(km)', '適合族群'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('租車注意事項', h2))
    s.append(Paragraph('台灣遊客需準備國際駕照（IDP）與台灣駕照正本。建議提前線上預約租車，現場租車價格較高。濟州島加油站多為自助式，建議學習韓文加油操作流程。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: jeju-driving-route.pdf')

# ============ PDF 4: Korea Budget Sheet ============
def gen_korea_budget():
    doc = SimpleDocTemplate('downloads/korea-budget-sheet.pdf')
    s = []
    s += make_cover('韓國旅遊預算表', '2026 精算旅遊花費')
    s.append(Paragraph('韓國旅遊預算完整指南', h1))
    s.append(Paragraph('韓國旅遊預算依旅遊風格與天數而異。本指南提供詳細預算表，涵蓋機票、住宿、交通、餐飲、門票、購物等各項費用，並提供省錢技巧與預算分配建議。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['項目', '經濟型(美元)', '舒適型(美元)', '豪華型(美元)'],
        ['機票（來回）', '400-600', '600-900', '900-1,500'],
        ['住宿（每晚）', '30-50', '80-150', '200-400'],
        ['交通（每日）', '10-20', '30-50', '50-100'],
        ['餐飲（每日）', '20-40', '50-80', '100-200'],
        ['門票/活動', '50-100', '150-250', '300-500'],
        ['購物', '100-300', '300-600', '600-1,500'],
        ['總計（7天）', '1,000-1,500', '2,000-3,500', '4,000-8,000'],
    ]
    s.append(make_table(['項目', '經濟型(美元)', '舒適型(美元)', '豪華型(美元)'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('省錢技巧', h2))
    s.append(Paragraph('1. 提前2-3個月預訂機票，價格可省30-50%\n2. 選擇民宿或青年旅館，住宿費可省50%\n3. 購買T-money卡，大眾運輸享有折扣\n4. 利用旅遊免稅店購物，可退稅8-10%\n5. 避開旺季（7-8月、12-1月），住宿與機票較便宜', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: korea-budget-sheet.pdf')

# Main
if __name__ == '__main__':
    gen_seoul_food()
    gen_busan_capsule()
    gen_jeju_driving()
    gen_korea_budget()
    print('All 4 Korea PDFs generated successfully!')
