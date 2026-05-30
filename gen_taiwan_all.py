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

# ============ PDF 1: Hualien Itinerary ============
def gen_hualien():
    doc = SimpleDocTemplate('downloads/hualien-itinerary.pdf')
    s = []
    s += make_cover('花蓮行程推薦', '2026 太魯閣與東海岸攻略')
    s.append(Paragraph('花蓮完整旅遊指南', h1))
    s.append(Paragraph('花蓮是台灣東部最美的縣市，擁有壯闊的太魯閣峽谷、碧藍的清水斷崖與豐富的原住民文化。本指南提供2天1夜與3天2夜行程建議，涵蓋必訪景點、美食推薦與交通建議。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['天數', '行程重點', '交通方式', '預算(NTD)'],
        ['2天1夜', '太魯閣+清水斷崖+七星潭', '租車/包車', '5,000-8,000'],
        ['3天2夜', '以上+瑞穗牧場+鯉魚潭', '租車/包車', '8,000-12,000'],
        ['4天3夜', '以上+三仙台+綠島船潛', '租車+船', '12,000-18,000'],
    ]
    s.append(make_table(['天數', '行程重點', '交通方式', '預算(NTD)'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('必吃美食', h2))
    s.append(Paragraph('公正街純手工蛋餅、液香蛋餅、曾記麻糬、洄瀾薯道、扁食（餛飩）。推薦早餐吃蛋餅，中午吃扁食，下午茶吃麻糬，晚餐吃海鮮。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: hualien-itinerary.pdf')

# ============ PDF 2: Tainan Food Map ============
def gen_tainan_food():
    doc = SimpleDocTemplate('downloads/tainan-food-map.pdf')
    s = []
    s += make_cover('台南美食地圖', '2026 必吃美食與老店推薦')
    s.append(Paragraph('台南美食完整指南', h1))
    s.append(Paragraph('台南是台灣的美食之都，擁有最道地的台灣小吃與百年老店。本指南精選20間必訪美食店，涵蓋擔仔麵、蝦仁飯、牛肉湯、碗粿、蚵仔煎等經典台南美食，並提供營業時間與避開人潮的技巧。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['美食種類', '推薦店家', '人均消費(NTD)', '所在地區'],
        ['擔仔麵', '度小月', '100-150', '中正路'],
        ['蝦仁飯', '金得旺', '80-120', '國華街'],
        ['牛肉湯', '阿村牛肉湯', '100-150', '民族路'],
        ['碗粿', '再發號', '50-80', '民權路'],
        ['蚵仔煎', '阿美綠豆湯', '60-100', '保安路'],
    ]
    s.append(make_table(['美食種類', '推薦店家', '人均消費(NTD)', '所在地區'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('最佳旅遊時間', h2))
    s.append(Paragraph('台南夏季炎熱（30-35°C），建議春秋兩季前往（20-28°C）。早餐建議7:00出門避開人潮，午餐11:30前到達，下午茶14:00-16:00，晚餐18:00前。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: tainan-food-map.pdf')

# ============ PDF 3: Kenting Night Market ============
def gen_kenting_night():
    doc = SimpleDocTemplate('downloads/kenting-night-market.pdf')
    s = []
    s += make_cover('墾丁夜市攻略', '2026 大街美食與活動指南')
    s.append(Paragraph('墾丁夜市完整攻略', h1))
    s.append(Paragraph('墾丁大街夜市是台灣最南端的觀光夜市，全長約1.5公里，聚集了數百家美食攤位與特色小店。本指南提供必吃美食、砍價技巧、最佳遊覽時間與附近住宿推薦。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['美食名稱', '推薦攤位', '價格(NTD)', '評分'],
        ['蒙古烤肉', '大街入口第3攤', '100-150', '★★★★★'],
        ['紅茶牛奶冰', '伯朗大道紅茶', '60-80', '★★★★☆'],
        ['烤玉米', '大街中段左手邊', '50-70', '★★★☆☆'],
        ['刈包', '廟口前第2攤', '50-80', '★★★★☆'],
        ['水果冰', '海邊最後一家', '80-120', '★★★★★'],
    ]
    s.append(make_table(['美食名稱', '推薦攤位', '價格(NTD)', '評分'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('砍價技巧', h2))
    s.append(Paragraph('墾丁夜市可以砍價，一般可砍10-20%。購買多件或與朋友合購效果更佳。避免周五-周日晚上前往，人潮最多且攤商不願降價。建議週一至週四晚上19:00-21:00前往。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: kenting-night-market.pdf')

# ============ PDF 4: Taipei Food Map ============
def gen_taipei_food():
    doc = SimpleDocTemplate('downloads/taipei-food-map.pdf')
    s = []
    s += make_cover('台北夜市美食', '2026 士林+饒河+寧夏攻略')
    s.append(Paragraph('台北夜市完整指南', h1))
    s.append(Paragraph('台北擁有台灣最豐富的夜市文化，士林夜市、饒河街觀光夜市、寧夏夜市是三大必訪夜市。本指南提供各夜市特色美食、必吃攤位、交通方式與最佳遊覽順序。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['夜市名稱', '特色美食', '營業時間', '捷運站'],
        ['士林夜市', '豪大大雞排+大餅包小餅', '16:00-01:00', '劍潭站'],
        ['饒河街夜市', '藥燉排骨+胡椒餅', '17:00-23:00', '松山站'],
        ['寧夏夜市', '劉芋仔+賴記蚵仔煎', '18:00-01:00', '南京復興站'],
        ['遼寧夜市', '臨江街觀光夜市', '18:00-02:00', '國父紀念館站'],
    ]
    s.append(make_table(['夜市名稱', '特色美食', '營業時間', '捷運站'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('最佳遊覽順序', h2))
    s.append(Paragraph('建議18:30出發先逛寧夏夜市（較小，1小時可逛完），20:00前往士林夜市（最大，至少2小時），21:30前往饒河街夜市（1.5小時）。週末人潮較多，建議平日前往。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: taipei-food-map.pdf')

# ============ PDF 5: Jiufen Guide ============
def gen_jiufen():
    doc = SimpleDocTemplate('downloads/jiufen-guide.pdf')
    s = []
    s += make_cover('九份老街指南', '2026 山城美食與攝影攻略')
    s.append(Paragraph('九份完整旅遊指南', h1))
    s.append(Paragraph('九份是台灣最具魅力的山城小鎮，保留著日治時期的老街風貌與豐富的茶樓文化。本指南提供必吃美食、最佳攝影點、交通方式與住宿推薦，讓您深度體驗九份的魅力。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['美食名稱', '推薦店家', '價格(NTD)', '必吃指數'],
        ['芋圓', '阿柑姨芋圓', '50-80', '★★★★★'],
        ['草仔粿', '老街入口左手邊', '30-50', '★★★★☆'],
        ['紅糟肉圓', '九份國小對面', '60-90', '★★★☆☆'],
        ['魚丸湯', '基山街第2家', '50-70', '★★★★☆'],
        ['綠茶冰淇淋', '茶坊附近', '70-100', '★★★★★'],
    ]
    s.append(make_table(['美食名稱', '推薦店家', '價格(NTD)', '必吃指數'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('最佳攝影時間', h2))
    s.append(Paragraph('九份清晨（06:00-08:00）與黃昏（16:00-18:00）光線最柔和，適合攝影。夜晚（19:00-21:00）老街點燈後別有一番風味，但人潮較多。雨天（11-12月）容易拍出迷霧山城的氛圍。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: jiufen-guide.pdf')

# Main
if __name__ == '__main__':
    gen_hualien()
    gen_tainan_food()
    gen_kenting_night()
    gen_taipei_food()
    gen_jiufen()
    print('All 5 Taiwan PDFs generated successfully!')
