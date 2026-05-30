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
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('PADDING', (0,0), (-1,-1), 15),
    ]))
    s.append(t)
    s.append(Spacer(1, 8))
    s.append(Paragraph('加入 LINE 群組：https://line.me/ti/g/NbNGnW4Eh6', body))
    s.append(Paragraph('更多免費旅遊 PDF：https://golightly.fun', body))
    return s

# ============ PDF 1: Chiang Mai Guide ============
def gen_chiang_mai():
    doc = SimpleDocTemplate('downloads/chiang-mai-guide.pdf')
    s = []
    s += make_cover('清邁攻略', '2026 古城與咖哩文化')
    s.append(Paragraph('清邁完整旅遊指南', h1))
    s.append(Paragraph('清邁是泰國北部最大的城市，擁有豐富的歷史文化與美麗的自然風景。本指南提供古城區景點、週末夜市、咖哩學校、大象保育與周邊一日遊建議。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['景點名稱', '門票價格(泰銖)', '建議遊覽時間', '最佳參觀時段'],
        ['帕辛寺', '免費', '1-2小時', '清晨6:00-8:00'],
        ['清邁古城', '免費', '半天', '全天皆可'],
        ['素貼寺', '30泰銖', '1小時', '上午8:00-10:00'],
        ['週末夜市', '免費', '2-3小時', '18:00-22:00'],
    ]
    s.append(make_table(['景點名稱', '門票價格(泰銖)', '建議遊覽時間', '最佳參觀時段'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('必體驗活動', h2))
    s.append(Paragraph('1. 咖哩烹飪課（1天，約1,000-1,500泰銖）\n2. 大象保育區（半天，約2,500泰銖）\n3. 叢林飛躍（半天，約3,000泰銖）\n4. 清邁夜市美食（每晚18:00-24:00）', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: chiang-mai-guide.pdf')

# ============ PDF 2: Bangkok Food Map ============
def gen_bangkok_food():
    doc = SimpleDocTemplate('downloads/bangkok-food-map.pdf')
    s = []
    s += make_cover('曼谷美食地圖', '2026 必吃美食與餐廳推薦')
    s.append(Paragraph('曼谷美食完整指南', h1))
    s.append(Paragraph('曼谷是美食天堂，從街頭小吃到米其林餐廳，應有盡有。本指南精選20間必訪餐廳，涵蓋泰式炒菜、河粉、打拋豬、芒果糯米等經典美食，並提供預約方式與價位參考。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['美食種類', '推薦餐廳', '人均消費(泰銖)', '所在地'],
        ['泰式炒菜', '連環功', '100-200', '暹邏'],
        ['河粉', '泰式河粉店', '80-150', '考山路'],
        ['打拋豬', '街頭小吃', '50-100', '全曼谷'],
        ['芒果糯米', '芒果糯米專賣店', '80-120', '中央世界'],
        ['咖哩 crab', '建興酒家', '500-800', '暹邏'],
    ]
    s.append(make_table(['美食種類', '推薦餐廳', '人均消費(泰銖)', '所在地'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('美食區域推薦', h2))
    s.append(Paragraph('考山路是曼谷美食的核心區域，聚集了最多經典小吃。暹邏區則有高級餐廳與購物中心美食街。街頭小吃建議嘗試，但需注意衛生。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: bangkok-food-map.pdf')

# ============ PDF 3: Bangkok Massage Map ============
def gen_bangkok_massage():
    doc = SimpleDocTemplate('downloads/bangkok-massage-map.pdf')
    s = []
    s += make_cover('曼谷按摩地圖', '2026 正宗泰式按摩推薦')
    s.append(Paragraph('曼谷按摩完整指南', h1))
    s.append(Paragraph('曼谷是泰式按摩的發源地，擁有全世界最便宜且高品質的按摩服務。本指南精選15間正宗泰式按摩店，涵蓋傳統按摩、精油按摩、熱石按摩與足部按摩，並提供價位與預約建議。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['按摩種類', '推薦店家', '價格(泰銖/小時)', '所在地'],
        ['傳統按摩', '臥佛寺按摩學校', '420', '大皇宮'],
        ['精油按摩', 'Health Land', '1,200-1,800', '全曼谷'],
        ['熱石按摩', 'Divana Spa', '2,500-3,500', '暹邏'],
        ['足部按摩', '街頭攤位', '200-300', '考山路'],
        ['Head Spa', '專業SPA館', '800-1,200', '中央世界'],
    ]
    s.append(make_table(['按摩種類', '推薦店家', '價格(泰銖/小時)', '所在地'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('按摩注意事項', h2))
    s.append(Paragraph('1. 傳統按摩建議穿著寬鬆衣物\n2. 精油按摩前2小時避免進食\n3. 熱石按摩不適合孕婦與高血壓患者\n4. 足部按摩可穿著鞋襪\n5. 建議提前1-2小時預約，週末容易客滿', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: bangkok-massage-map.pdf')

# ============ PDF 4: Danang Map ============
def gen_danang():
    doc = SimpleDocTemplate('downloads/danang-map.pdf')
    s = []
    s += make_cover('峴港地圖', '2026 海灘與古蹟攻略')
    s.append(Paragraph('峴港完整旅遊指南', h1))
    s.append(Paragraph('峴港是越南中部最大的城市，擁有美麗的海灘與豐富的歷史文化。本指南提供海灘推薦、古蹟景點、美食推薦與周邊一日遊建議（會安、順化）。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['景點名稱', '門票價格(越南盾)', '建議遊覽時間', '最佳參觀時段'],
        ['峴港大教堂', '免費', '1小時', '全天皆可'],
        ['五行山', '40,000越南盾', '2-3小時', '上午7:00-10:00'],
        ['山茶半島', '免費', '半天', '下午14:00-17:00'],
        ['會安古鎮', '120,000越南盾', '1天', '下午+夜晚'],
        ['順化皇城', '150,000越南盾', '半天', '上午8:00-11:00'],
    ]
    s.append(make_table(['景點名稱', '門票價格(越南盾)', '建議遊覽時間', '最佳參觀時段'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('必體驗活動', h2))
    s.append(Paragraph('1. 峴港海灘日光浴（免費，全天）\n2. 會安古鎮夜遊（傍晚17:00-21:00）\n3. 順化皇城歷史之旅（半天）\n4. 峴港美食之旅（全天候）\n5. 巴拿山纜車體驗（1天，約700,000越南盾）', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: danang-map.pdf')

# ============ PDF 5: SEA Budget Sheet ============
def gen_sea_budget():
    doc = SimpleDocTemplate('downloads/sea-budget-sheet.pdf')
    s = []
    s += make_cover('東南亞旅遊預算表', '2026 精算旅遊花費')
    s.append(Paragraph('東南亞旅遊預算完整指南', h1))
    s.append(Paragraph('東南亞旅遊預算依國家、旅遊風格與天數而異。本指南提供詳細預算表，涵蓋機票、住宿、交通、餐飲、門票、購物等各項費用，並提供省錢技巧與預算分配建議。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['項目', '經濟型(美元)', '舒適型(美元)', '豪華型(美元)'],
        ['機票（來回）', '300-500', '500-800', '800-1,500'],
        ['住宿（每晚）', '15-30', '50-100', '150-300'],
        ['交通（每日）', '5-15', '20-40', '50-100'],
        ['餐飲（每日）', '10-25', '30-60', '80-150'],
        ['門票/活動', '30-80', '100-200', '200-400'],
        ['購物', '50-200', '200-500', '500-1,000'],
        ['總計（7天）', '500-900', '1,200-2,200', '3,000-6,000'],
    ]
    s.append(make_table(['項目', '經濟型(美元)', '舒適型(美元)', '豪華型(美元)'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('省錢技巧', h2))
    s.append(Paragraph('1. 提前2-3個月預訂機票，價格可省30-50%\n2. 選擇民宿或青年旅館，住宿費可省50%\n3. 購買當地SIM卡，網路費用可省70%\n4. 利用當地交通工具（公車、地鐵），交通費可省60%\n5. 避開旺季（12-1月、7-8月），住宿與機票較便宜', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: sea-budget-sheet.pdf')

# Main
if __name__ == '__main__':
    gen_chiang_mai()
    gen_bangkok_food()
    gen_bangkok_massage()
    gen_danang()
    gen_sea_budget()
    print('All 5 SEA PDFs generated successfully!')
