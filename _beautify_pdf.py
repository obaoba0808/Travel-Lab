# -*- coding: utf-8 -*-
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
    ])
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
    ])
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
    ])
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
    ])
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


# =============================================================================
# Part 2: Korea PDF Generators
# =============================================================================

def gen_seoul_food():
    """Generate Seoul Food Map PDF - 韓國首爾美食地圖"""
    story = []
    
    # Cover Page
    story += make_cover('首爾美食地圖', '2026 最新版')
    
    # Section 1: Myeongdong Food Overview
    story.append(Paragraph('明洞美食總覽', h1))
    story.append(Paragraph('明洞是首爾最著名的美食街區，聚集了傳統韓式料理、街頭小吃與現代咖啡廳。從明洞站出口步行5分鐘內，就能找到超過50家特色餐廳。本攻略精選15家必吃餐廳，涵蓋烤肉、部隊鍋、韓式炸雞與甜點飲料，價格區間從每人50元到800元台幣不等，適合各種預算的旅客。', body))
    story.append(Spacer(1, 8))
    
    tbl_data = [
        ['餐廳名稱', '類型', '人均價格(台幣)', '推薦度'],
        ['明洞餃子', '韓式湯餃', '250-350', '★★★★★'],
        ['土俗村參雞湯', '參雞湯', '300-400', '★★★★★'],
        ['N首爾塔韓式烤肉', '烤肉', '600-800', '★★★★☆'],
        ['校村炸雞', '炸雞', '200-300', '★★★★☆'],
        ['雪冰咖啡廳', '甜點飲料', '150-250', '★★★★☆'],
        ['明洞街頭小吃攤', '街頭小吃', '50-150', '★★★★★'],
    ]
    story.append(make_table(['餐廳名稱', '類型', '人均價格(台幣)', '推薦度'], tbl_data))
    story.append(Spacer(1, 10))
    
    # Tip Box
    story += make_tip('美食小撇步', [
        '建議避開用餐尖峰時段（12:00-13:30, 18:00-19:30）',
        '部分餐廳需提前電話預約，尤其是週末',
        '街頭小吃攤現金支付較方便，建議準備足夠韓元',
        '明洞餃子與土俗村參雞湯經常排隊，可選擇非尖峰時段前往',
    ])
    
    # Section 2: Must-Try Street Food
    story.append(Paragraph('必吃街頭小吃', h2))
    story.append(Paragraph('首爾的街頭小吃文化豐富多元，明洞、東大門與弘大商圈都有著名的街頭美食集中區。推薦嘗試辣炒年糕（떡볶이）、魚板湯（어묵）、糖餅（호떡）與韓式煎餅（전）。這些小吃不僅價格親民，更能體驗在地人的飲食文化。平均每樣小吃價格約2,000-4,000韓元（約50-100台幣）。', body))
    story.append(Spacer(1, 8))
    
    tbl_data2 = [
        ['小吃名稱', '韓文', '價格(韓元)', '熱量估計'],
        ['辣炒年糕', '떡볶이', '3,000-4,000', '中等'],
        ['魚板湯', '어묵', '2,000-3,000', '低'],
        ['糖餅', '호떡', '2,500-3,500', '高'],
        ['韓式煎餅', '전', '4,000-6,000', '中等'],
        ['烤魷魚', '오징어구이', '5,000-7,000', '低'],
    ]
    story.append(make_table(['小吃名稱', '韓文', '價格(韓元)', '熱量估計'], tbl_data2))
    story.append(Spacer(1, 10))
    
    # Section 3: Restaurant Details
    story.append(Paragraph('精選餐廳詳細介紹', h2))
    story.append(Paragraph('明洞餃子（명동교자）成立於1960年代，是明洞最具代表性的老字號餐廳。招牌菜為手工湯餃與刀削麵，湯頭鮮美，餃子內餡飽滿多汁。營業時間為10:30-21:30，週日公休。土俗村參雞湯（토속촌 삼계탕）位於景福宮附近，以藥膳參雞湯聞名，整隻童子雞腹中填入糯米、人參、紅棗與蒜頭，燉煮4小時以上，湯頭濃郁滋補。', body))
    story.append(Spacer(1, 8))
    
    story += make_tip('預算規劃建議', [
        '經濟型：每日餐飲預算 300-500 台幣（以街頭小吃與平價餐廳為主）',
        '中檔型：每日餐飲預算 600-1000 台幣（包含1-2次烤肉或部隊鍋）',
        '奢華型：每日餐飲預算 1200-2000 台幣（包含高級韓牛烤肉與米其林餐廳）',
        '建議準備現金比例：餐飲費用的30%以現金支付較為方便',
    ])
    
    # Section 4: Food Map and Transportation
    story.append(Paragraph('美食地圖與交通指南', h2))
    story.append(Paragraph('本節提供明洞、弘大、江南三大美食區域的地圖與交通資訊。明洞站（地鐵4號線）周邊步行10分鐘內可達所有推薦餐廳。弘大入口站（地鐵2號線）周邊以德式香腸、創意料理與主題咖啡廳聞名。江南站（地鐵2號線）則有高檔烤肉店與精緻咖啡廳。建議購買T-money卡，方便搭乘地鐵與公車。', body))
    story.append(Spacer(1, 8))
    
    tbl_data3 = [
        ['區域', '地鐵站', '必吃特色', '步行時間'],
        ['明洞', '明洞站(4號線)', '湯餃、參雞湯、街頭小吃', '5-10分鐘'],
        ['弘大', '弘大入口站(2號線)', '德式香腸、創意料理、咖啡廳', '5-15分鐘'],
        ['江南', '江南站(2號線)', '高檔烤肉、精緻甜點', '10-20分鐘'],
        ['東大門', '東大門歷史文化公園站(2/4/5號線)', '夜市小吃、24小時餐廳', '5-10分鐘'],
    ]
    story.append(make_table(['區域', '地鐵站', '必吃特色', '步行時間'], tbl_data3))
    
    # CTA
    story += make_cta()
    
    return story


def gen_busan_capsule():
    """Generate Busan Capsule Guide PDF - 釜山膠囊列車預約攻略"""
    story = []
    
    # Cover Page
    story += make_cover('釜山膠囊列車預約攻略', '2026 完整預約教學')
    
    # Section 1: Overview
    story.append(Paragraph('釜山膠囊列車完整指南', h1))
    story.append(Paragraph('釜山膠囊列車（Busan Air Cruise）是韓國釜山廣安里海灘的標誌性觀光設施，於2020年重新開幕。這是一條全長約2公里的海上纜車路線，連接海雲台尾浦碼頭與冬柏島，全程約15-20分鐘。膠囊車廂為透明玻璃地板設計，可360度欣賞釜山海岸線、廣安大橋與海雲台夜景。本攻略提供完整預約流程、票價比較、最佳搭乘時段與攝影技巧。', body))
    story.append(Spacer(1, 8))
    
    tbl_data = [
        ['票種', '成人票價(韓元)', '兒童票價(韓元)', '台幣約略價格'],
        ['單程票（一般車厢）', '17,000', '12,000', '380 / 270'],
        ['來回票（一般車厢）', '24,000', '18,000', '540 / 400'],
        ['單程票（水晶車廂）', '22,000', '16,000', '490 / 360'],
        ['來回票（水晶車廂）', '30,000', '22,000', '670 / 490'],
        ['快速通關券', '35,000', '25,000', '780 / 560'],
    ]
    story.append(make_table(['票種', '成人票價(韓元)', '兒童票價(韓元)', '台幣約略價格'], tbl_data))
    story.append(Spacer(1, 10))
    
    # Tip Box
    story += make_tip('預約小撇步', [
        '強烈建議提前線上預約，現場購票經常售罄',
        '水晶車廂（透明地板）最受歡迎，建議提前3-7天預約',
        '日落時段（17:00-19:00）景色最美，但也是最熱門時段',
        '週間上午時段人潮較少，可享更舒適的搭乘體驗',
        '購買來回票比兩張單程票便宜約10%',
    ])
    
    # Section 2: Reservation Process
    story.append(Paragraph('線上預約完整流程', h2))
    story.append(Paragraph('釜山膠囊列車官方網站提供多語言介面（含中文），預約流程簡單明瞭。首先進入官網（busanaircruise.com），選擇「線上預約」並註冊會員。接著選擇搭乘日期、時段、票種與數量。付款支援信用卡（VISA/MasterCard/JCB）與PayPal。預約成功後會收到電子票券Email，現場出示QR Code即可搭乘。建議列印實體票券或確保手機網路暢通。', body))
    story.append(Spacer(1, 8))
    
    tbl_data2 = [
        ['步驟', '操作說明', '注意事項'],
        ['1. 進入官網', '前往 busanaircruise.com', '建議使用電腦版網頁'],
        ['2. 選擇日期', '挑選搭乘日期與時段', '熱門時段需提前預約'],
        ['3. 選擇票種', '一般車廂或水晶車廂', '水晶車廂視野較佳'],
        ['4. 填寫資料', '輸入護照英文名與人數', '姓名需與護照一致'],
        ['5. 付款', '信用卡或 PayPal', '付款後不可退款'],
        ['6. 收到票券', 'Email 收到 QR Code', '建議截圖保存'],
    ]
    story.append(make_table(['步驟', '操作說明', '注意事項'], tbl_data2))
    story.append(Spacer(1, 10))
    
    # Section 3: Best Viewing Times
    story.append(Paragraph('最佳搭乘時段推薦', h2))
    story.append(Paragraph('釜山膠囊列車全年無休（僅農曆春節暫停），營運時間為10:00-22:00（最後入場21:30）。不同時段有不同風景特色：上午時段（10:00-12:00）光線充足，適合拍攝清晰海景；下午時段（14:00-16:00）可拍攝藍天白雲與海岸線對比；日落時段（17:00-19:00）可欣賞夕陽西下與漸層天空；夜間時段（19:00-22:00）則能欣賞廣安大橋燈光秀與釜山夜景。', body))
    story.append(Spacer(1, 8))
    
    story += make_tip('攝影技巧', [
        '使用廣角鏡頭（24-35mm）拍攝車廂內部與海景',
        '透明地板拍攝時注意反光，可穿深色衣服減少倒影',
        '日落時段使用HDR模式平衡亮部與暗部',
        '夜間拍攝建議使用三腳架或穩定器',
        '避免穿著白色衣服，容易造成玻璃反光',
    ])
    
    # Section 4: Transportation and Nearby Attractions
    story.append(Paragraph('交通方式與周邊景點', h2))
    story.append(Paragraph('釜山膠囊列車尾浦站距離地鐵2號線海雲台站約15分鐘步行距離。也可搭乘公車至「尾浦碼頭」站下車。冬柏島站則可從地鐵2號線冬柏站步行10分鐘抵達。周邊景點包含海雲台海水浴場（步行5分鐘）、廣安里海水浴場（步行15分鐘）、BIFF廣場（車程20分鐘）。建議安排半天行程，上午搭乘膠囊列車，下午遊覽海雲台周邊景點。', body))
    story.append(Spacer(1, 8))
    
    tbl_data3 = [
        ['交通方式', '路線說明', '所需時間', '費用'],
        ['地鐵', '2號線海雲台站→步行', '15分鐘', '約1,400韓元'],
        ['公車', '海雲台站搭乘公車至尾浦碼頭', '10分鐘', '約1,300韓元'],
        ['計程車', '從海雲台站出發', '5分鐘', '約5,000-7,000韓元'],
        ['步行', '從海雲台海水浴場出發', '15-20分鐘', '免費'],
    ]
    story.append(make_table(['交通方式', '路線說明', '所需時間', '費用'], tbl_data3))
    
    # CTA
    story += make_cta()
    
    return story


def gen_jeju_driving():
    """Generate Jeju Driving Route PDF - 濟州島自駕路線"""
    story = []
    
    # Cover Page
    story += make_cover('濟州島自駕路線', '2026 精選5條必走路線')
    
    # Section 1: Overview
    story.append(Paragraph('濟州島自駕完整攻略', h1))
    story.append(Paragraph('濟州島是韓國最大的島嶼，面積約1,849平方公里，環島公路全長約181公里。自駕是遊覽濟州島最自由便利的方式，可以隨意停靠景點、調整行程節奏。本攻略精選5條自駕路線，涵蓋東部、西部、南部、北部與環島路線，每條路線規劃2-3天行程。同時提供租車流程、交通規則、停車資訊與路況提醒，讓您的濟州自駕之旅安全順利。', body))
    story.append(Spacer(1, 8))
    
    tbl_data = [
        ['路線名稱', '天數', '總里程(km)', '適合族群'],
        ['東部海岸路線', '2天1夜', '120', '第一次來濟州'],
        ['西部田園路線', '2天1夜', '110', '喜歡自然風景'],
        ['南部文化路線', '1天', '80', '親子同遊'],
        ['北部都市路線', '1天', '60', '購物美食愛好者'],
        ['環島深度路線', '3天2夜', '200', '深度旅遊玩家'],
    ]
    story.append(make_table(['路線名稱', '天數', '總里程(km)', '適合族群'], tbl_data))
    story.append(Spacer(1, 10))
    
    # Tip Box
    story += make_tip('租車注意事項', [
        '台灣遊客需準備國際駕照（IDP）與台灣駕照正本',
        '建議提前線上預約租車，現場租車價格較高',
        '濟州島加油站多為自助式，建議學習韓文加油操作流程',
        '停車場收費約每小時1,000-2,000韓元，部分景點有免費停車場',
        '濟州島限速：市區50km/h，郊區80km/h，高速公路100km/h',
    ])
    
    # Section 2: Route Details - Eastern Route
    story.append(Paragraph('路線一：東部海岸路線（2天1夜）', h2))
    story.append(Paragraph('東部路線是濟州島最經典的自駕路線，包含城山日出峰、涉地可支、牛島與表善海水浴場等知名景點。第一天從濟州機場出發，沿著1100道路往東部行駛，約1小時抵達城山日出峰。下午遊覽涉地可支與牛島，晚上住宿城山或表善地區。第二天前往萬丈窟熔岩洞與水族館，下午返回濟州市區。全程約120公里，預計駕駛時間4-5小時（不含景點停留）。', body))
    story.append(Spacer(1, 8))
    
    tbl_data2 = [
        ['景點', '停留時間', '停車資訊', '門票費用'],
        ['城山日出峰', '2-3小時', '有收費停車場(2,000韓元)', '5,000韓元'],
        ['涉地可治', '1-2小時', '免費停車場', '免費'],
        ['牛島', '3-4小時', '渡輪停車場(5,000韓元)', '渡輪來回8,000韓元'],
        ['萬丈窟', '1-2小時', '有收費停車場(2,000韓元)', '4,000韓元'],
        ['表善海水浴場', '1-2小時', '免費停車場', '免費'],
    ]
    story.append(make_table(['景點', '停留時間', '停車資訊', '門票費用'], tbl_data2))
    story.append(Spacer(1, 10))
    
    # Section 3: Car Rental Process
    story.append(Paragraph('租車流程與費用估算', h2))
    story.append(Paragraph('濟州島租車公司眾多，推薦使用RentalCars、Klook或直接在濟州機場櫃檯租車。經濟型小客車（如Hyundai Avante）每日租金約50,000-70,000韓元（約1,100-1,600台幣），包含基本保險。若升級至SUV或進口車，每日租金約80,000-120,000韓元。建議購買全險（CDW+TPL），每日約增加10,000-15,000韓元。油費預算：環島一圈約需加油1-2次，每次約60,000-80,000韓元。', body))
    story.append(Spacer(1, 8))
    
    story += make_tip('自駕安全提醒', [
        '濟州島多彎道與坡道，請減速慢行注意號誌',
        '部分景點路段無人行道，遊客穿梭需特別小心',
        '雨天路面濕滑，尤其火山岩地形容易打滑',
        '導航建議使用韓文版Naver Map或Kakao Map',
        '緊急聯絡電話：112（警察）、119（消防救護）',
    ])
    
    # Section 4: Recommended 3-Day Itinerary
    story.append(Paragraph('推薦3天2夜自駕行程', h2))
    story.append(Paragraph('若時間充裕，推薦安排3天2夜的環島自駕行程。第一天：濟州市區→翰林公園→Aqua Planet濟州→城山日出峰（住宿城山）。第二天：牛島→萬丈窟→四季之星→正房瀑布→大浦柱狀節理（住宿西歸浦）。第三天：Hello Kitty島→Eco Land→東門市場→返程。此行程涵蓋濟州島精華景點，每天駕駛時間控制在3-4小時內，留有充足時間遊覽與休息。', body))
    story.append(Spacer(1, 8))
    
    tbl_data3 = [
        ['天數', '上午行程', '下午行程', '住宿地點'],
        ['Day 1', '濟州市區→翰林公園', 'Aqua Planet→城山日出峰', '城山/表善'],
        ['Day 2', '牛島→萬丈窟', '四季之星→正房瀑布', '西歸浦'],
        ['Day 3', 'Hello Kitty島→Eco Land', '東門市場→返程', '無'],
    ]
    story.append(make_table(['天數', '上午行程', '下午行程', '住宿地點'], tbl_data3))
    
    # CTA
    story += make_cta()
    
    return story


def gen_korea_budget():
    """Generate Korea Budget Sheet PDF - 韓國旅遊預算表"""
    story = []
    
    # Cover Page
    story += make_cover('韓國旅遊預算表', '2026 完整費用規劃')
    
    # Section 1: Overview
    story.append(Paragraph('韓國旅遊預算完整規劃', h1))
    story.append(Paragraph('規劃韓國旅遊預算需要考慮多項因素：旅遊天數、城市選擇、住宿等級、餐飲標準與購物預算。本預算表以7天6夜行程為基準，分為經濟型、中檔型與奢華型三種預算等級，詳細列出各項費用明細。同時提供匯率換算、省錢技巧與預算調整建議，幫助您打造最適合的韓國旅遊財務計畫。所有金額以台幣計算，並附上韓元參考價格。', body))
    story.append(Spacer(1, 8))
    
    tbl_data = [
        ['預算等級', '總費用範圍(台幣)', '每日平均(台幣)', '適合對象'],
        ['經濟型', '25,000-35,000', '3,500-5,000', '背包客、學生族群'],
        ['中檔型', '40,000-60,000', '5,700-8,600', '一般上班族、家庭'],
        ['奢華型', '70,000-120,000', '10,000-17,000', '追求品質的旅客'],
    ]
    story.append(make_table(['預算等級', '總費用範圍(台幣)', '每日平均(台幣)', '適合對象'], tbl_data))
    story.append(Spacer(1, 10))
    
    # Tip Box
    story += make_tip('省錢小撇步', [
        '提前2-3個月預訂機票，可省下3,000-5,000台幣',
        '選擇民宿或青年旅館，住宿費可減少50%',
        '利用便利商店與街頭小吃，餐費可控制在每日300台幣內',
        '購買T-money卡並搭乘大眾運輸，交通費比計程車便宜70%',
        '免稅店商品可退稅（Tax Refund），記得索取退稅單',
    ])
    
    # Section 2: Detailed Budget Breakdown
    story.append(Paragraph('各項費用詳細分析', h2))
    story.append(Paragraph('機票費用佔旅遊預算的30-40%，經濟型預算可選擇廉航（如台灣虎航、濟州航空），來回機票約8,000-12,000台幣；中檔型可選擇傳統航空（如華航、大韓航空），來回機票約15,000-25,000台幣。住宿費用：青年旅館床位每晚500-800台幣，商務旅館每晚2,000-3,500台幣，五星級飯店每晚5,000-10,000台幣。餐飲費用：經濟型每日300-500台幣，中檔型每日600-1,000台幣，奢華型每日1,200-2,000台幣。', body))
    story.append(Spacer(1, 8))
    
    tbl_data2 = [
        ['費用項目', '經濟型(台幣)', '中檔型(台幣)', '奢華型(台幣)'],
        ['機票（來回）', '8,000-12,000', '15,000-25,000', '25,000-35,000'],
        ['住宿（6晚）', '3,000-5,000', '12,000-20,000', '30,000-60,000'],
        ['餐飲（7天）', '2,100-3,500', '4,200-7,000', '8,400-14,000'],
        ['交通（市內+跨市）', '1,500-2,500', '3,000-5,000', '5,000-10,000'],
        ['門票與活動', '1,000-2,000', '3,000-5,000', '5,000-10,000'],
        ['購物與雜支', '3,000-5,000', '8,000-15,000', '20,000-40,000'],
        ['預備金', '2,000-3,000', '5,000-8,000', '10,000-15,000'],
        ['總計', '20,600-32,000', '45,200-70,000', '103,400-184,000'],
    ]
    story.append(make_table(['費用項目', '經濟型(台幣)', '中檔型(台幣)', '奢華型(台幣)'], tbl_data2))
    story.append(Spacer(1, 10))
    
    # Section 3: Money Exchange and Payment
    story.append(Paragraph('換匯與付款方式建議', h2))
    story.append(Paragraph('韓元（KRW）與台幣（TWD）匯率約為1:0.022-0.025（即1台幣約40-45韓元）。建議在台灣先換部分韓元現金（約總預算的30%），其餘使用提款卡在韓國ATM領取或信用卡消費。韓國ATM提款手續費約100-150台幣/次，匯率較現金換匯優惠。信用卡在韓國普及率高，大部分商店、餐廳與交通都接受VISA/MasterCard。建議攜帶至少兩張不同發卡組織的信用卡以備不時之需。', body))
    story.append(Spacer(1, 8))
    
    story += make_tip('付款方式比較', [
        '現金：適合小吃攤、傳統市場、部分交通（如公車）',
        '信用卡：適合百貨公司、餐廳、網購，部分有海外回饋',
        'T-money卡：適合地鐵、公車、便利商店，可退卡費與餘額',
        '支付寶/微信支付：部分免稅店與觀光區商店接受',
        '旅行支票：已較少使用，不建議攜帶',
    ])
    
    # Section 4: Budget Adjustment by City
    story.append(Paragraph('不同城市預算調整建議', h2))
    story.append(Paragraph('首爾是韓國消費最高的城市，住宿與餐飲價格比其它城市貴20-30%。釜山與濟州島的物價相對較低，但濟州島交通費（租車或計程車）較高。若行程包含多個城市，建議預算分配為：首爾50%、釜山30%、濟州島20%。若只在首爾一地旅遊，可將預算集中在住宿地段（明洞、弘大較貴，東大門、江南CP值較高）與餐飲選擇（混合高檔餐廳與平價小吃）。', body))
    story.append(Spacer(1, 8))
    
    tbl_data3 = [
        ['城市', '物價指數', '住宿價差', '餐飲價差', '推薦住宿區域'],
        ['首爾', '100% (基準)', '基準', '基準', '明洞、弘大、江南'],
        ['釜山', '85-90%', '便宜15-20%', '便宜10-15%', '海雲台、西面'],
        ['濟州島', '80-85%', '便宜20-25%', '便宜15-20%', '濟州市、西歸浦'],
        ['仁川', '90-95%', '便宜5-10%', '便宜5-10%', '仁川機場周邊'],
    ]
    story.append(make_table(['城市', '物價指數', '住宿價差', '餐飲價差', '推薦住宿區域'], tbl_data3))
    story.append(Spacer(1, 8))
    
    story += make_tip('預算追蹤工具', [
        '推薦使用TravelSpend、TrabeePocket等APP記帳',
        '每天晚上花5分鐘記錄當日花費',
        '設定每日預算上限，避免超支',
        '保留收據或拍照存證，方便回國報稅（如有需要）',
        '回國後分析花費比例，作為下次旅遊參考',
    ])
    
    # CTA
    story += make_cta()
    
    return story


# =============================================================================
# Main execution: Build all Korea PDFs
# =============================================================================

if __name__ == '__main__':
    import os
    
    # Define output directory
    output_dir = 'pdfs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate all Korea PDFs
    pdf_configs = [
        ('seoul_food_map.pdf', '韓國首爾美食地圖', gen_seoul_food),
        ('busan_capsule_guide.pdf', '釜山膠囊列車預約攻略', gen_busan_capsule),
        ('jeju_driving_route.pdf', '濟州島自駕路線', gen_jeju_driving),
        ('korea_budget_sheet.pdf', '韓國旅遊預算表', gen_korea_budget),
    ]
    
    for filename, title, gen_func in pdf_configs:
        output_path = os.path.join(output_dir, filename)
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            leftMargin=M, rightMargin=M,
            topMargin=M+10, bottomMargin=M+10
        )
        story = gen_func()
        doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
        print(f'✓ Generated: {output_path}')
    
    print('\nAll Korea PDFs generated successfully!')


# ============================================================
# PART 2: JAPAN PDFS (7)
# ============================================================

def gen_tokyo_metro():
    """東京地鐵路線圖 - 完整攻略"""
    s = []
    s += make_cover('東京地鐵路線圖', '2026 最新版')
    
    # Section 1
    s.append(Paragraph('東京地鐵系統總覽', h1))
    s.append(Paragraph('東京的地鐵系統主要由兩大公司營運：東京Metro（9條路線）與都營地下鐵（4條路線）。對觀光客來說，最實用的是JR山手線、銀座線、丸之內線、千代田線。2026年票價調漲至180-320日圓，建議購買24/48/72小時券更划算。', body))
    
    tokyo_data = [
        ['路線', '顏色', '主要車站', '推薦用途'],
        ['山手線', '綠色', '東京/新宿/澀谷/池袋', '環狀線，觀光首選'],
        ['銀座線', '橙色', '銀座/日本橋/淺草', '連接淺草與銀座'],
        ['丸之內線', '紅色', '東京站/新宿/池袋', '東西向主幹線'],
        ['千代田線', '綠色(淺)', '表參道/明治神宮前', '前往原宿、表參道'],
        ['日比谷線', '銀色', '中目黑/惠比壽', '前往中目黑櫻花'],
        ['東西線', '藍色', '日本橋/茅場町', '連接東西兩岸'],
    ]
    s.append(make_table(['路線', '顏色', '主要車站', '推薦用途'], tokyo_data[1:]))
    s.append(Spacer(1, 10))
    
    # Section 2
    s.append(Paragraph('地鐵票券比較', h2))
    s.append(Paragraph('東京地鐵票券分為「Tokyo Subway Ticket」（機場購買）與「24/48/72小時券」（市區購買）。成田機場來回者強烈建議購買Tokyo Subway Ticket，包含機場來回N\'EX優惠。', body))
    
    ticket_data = [
        ['票券', '價格(日圓)', '適用範圍', '推薦對象'],
        ['24小時券', '800', 'Metro+都營共13條線', '當日來回3個景點'],
        ['48小時券', '1,200', 'Metro+都營共13條線', '2天短住旅人'],
        ['72小時券', '1,500', 'Metro+都營共13條線', '3天深度遊'],
        ['Tokyo Subway Ticket 24h', '1,600', '含N\'EX來回+地鐵', '成田機場出入國'],
    ]
    s.append(make_table(['票券', '價格(日圓)', '適用範圍', '推薦對象'], ticket_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s.append(Paragraph('搭乘技巧與注意事項', h2))
    s += make_tip('搭乘地鐵必知', [
        '尖峰時段（7:30-9:00 / 17:00-19:00）人潮擁擠，建議避開',
        '女性專用車廂（平日7:30-9:30）標示紫色，男性請勿進入',
        '優先座（優先席）請禮讓老人、孕婦、行動不便者',
        '通話請用Line或簡訊，車廂內講電話視為極度失禮',
        '成田/羽田機場建議搭N\'EX或Skyliner，地鐵需轉乘較麻煩',
    ])
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('從機場到市區', h2))
    airport_data = [
        ['出發地', '交通方式', '時間', '價格(日圓)'],
        ['成田機場', 'N\'EX成田特快', '60分', '3,250'],
        ['成田機場', 'Skyliner', '41分', '2,640'],
        ['成田機場', '京成特急', '50分', '1,050'],
        ['羽田機場', '東京單軌電車', '30分', '650'],
        ['羽田機場', '京急線', '35分', '620'],
    ]
    s.append(make_table(['出發地', '交通方式', '時間', '價格(日圓)'], airport_data[1:]))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_kansai_pass():
    """關西機場轉乘計算機 - 完整攻略"""
    s = []
    s += make_cover('關西機場轉乘計算機', '2026 最新版')
    
    s.append(Paragraph('關西機場交通總覽', h1))
    s.append(Paragraph('關西國際機場（KIX）是關西地區最大國際機場，前往大阪、京都、奈良、神戶各有不同交通方式。選擇的關鍵在於「住宿區域」、「人數」、「是否購買ICOCA卡」。本攻略幫你計算出最省錢的方案。', body))
    
    # Section 1
    s.append(Paragraph('關西機場 → 大阪市區', h2))
    osaka_data = [
        ['交通方式', '目的地', '時間', '價格(日圓)', '推薦度'],
        ['南海電鐵特急Rapi:t', '難波', '38分', '1,490', '★★★★★'],
        ['南海電鐵機場急行', '難波', '45分', '970', '★★★★☆'],
        ['JR特急Haruka', '天王寺/大阪', '50分', '3,430', '★★★☆☆'],
        ['機場巴士', '大阪站/梅田', '60分', '1,300', '★★★☆☆'],
        ['計程車', '難波', '45分', '18,000+', '★☆☆☆☆'],
    ]
    s.append(make_table(['交通方式', '目的地', '時間', '價格(日圓)', '推薦度'], osaka_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('關西機場 → 京都', h2))
    kyoto_data = [
        ['交通方式', '時間', '價格(日圓)', '優點'],
        ['JR特急Haruka', '75分', '3,430', '直達京都站，最舒適'],
        ['機場巴士', '90分', '2,600', '直達京都站，不用拖行李轉乘'],
        ['南海電鐵+新幹線', '80分', '2,100', '最便宜，但需轉乘'],
    ]
    s.append(make_table(['交通方式', '時間', '價格(日圓)', '優點'], kyoto_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s.append(Paragraph('ICOCA卡 vs 关西機場券', h2))
    s.append(Paragraph('ICOCA是關西地區的IC卡（類似東京的Suica），可在地鐵、巴士、商店使用。關西機場券（Kansai Airport Ticket）則包含機場來回+南海電鐵無限搭乘。以下比較兩者：', body))
    
    icoca_data = [
        ['項目', 'ICOCA卡', '關西機場券'],
        ['價格', '2,000（含500押金）', '1,490（單程）'],
        ['適用範圍', '關西地區全部交通', '僅南海電鐵'],
        ['購買地點', '機場/車站', '機場限時櫃檯'],
        ['推薦對象', '停留3天以上', '當日來回/住宿難波'],
    ]
    s.append(make_table(['項目', 'ICOCA卡', '關西機場券'], icoca_data[1:]))
    s.append(Spacer(1, 8))
    
    s += make_tip('省錢小撇步', [
        '2人以上同行建議買「南海電鐵來回券」（來回2,000日圓，比單程便宜）',
        '住宿難波區域選南海電鐵，住宿京都站選JR Haruka',
        '關西機場的免稅店比市區便宜，可先買化妝品',
        '7-11 ATM可以用台灣金融卡領日圓，手續費僅110日圓',
    ])
    s.append(Spacer(1, 8))
    
    # Section 4: Quick calculator
    s.append(Paragraph('快速計算機：你該選哪個方案？', h2))
    s.append(Paragraph('情況A：1人、住宿難波、停留2天 → 南海電鐵單程票（970日圓）\n'
                     '情況B：2人、住宿難波、停留2天 → 南海電鐵來回券（2,000日圓/人）\n'
                     '情況C：1人、住宿京都、停留3天 → JR Haruka單程票（3,430日圓）+ ICOCA卡\n'
                     '情況D：家庭4人、住宿大阪 → 計程車（約18,000日圓，人均4,500）', body_compact))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_hokkaido_packing():
    """北海道冬季穿搭清單 - 完整攻略"""
    s = []
    s += make_cover('北海道冬季穿搭清單', '2026 最新版')
    
    s.append(Paragraph('北海道冬季溫度須知', h1))
    s.append(Paragraph('北海道冬季（12月-2月）平均氣溫-5°C到-15°C，強風時體感可達-30°C。不同地區溫差大：札幌較溫暖（-1°C至-4°C），紋別/網走最冷（-4°C至-6°C）。1月下旬至2月上旬是「嚴冬期」，氣溫最低。', body))
    
    temp_data = [
        ['地區', '12月', '1月', '2月', '嚴冬期'],
        ['札幌', '-1°C', '-4°C', '-3°C', '-6°C（體感-15°C）'],
        ['小樽', '-2°C', '-5°C', '-4°C', '-8°C（體感-20°C）'],
        ['函館', '0°C', '-3°C', '-2°C', '-5°C（體感-10°C）'],
        ['紋別/網走', '-4°C', '-6°C', '-5°C', '-10°C（體感-25°C）'],
        ['帶廣', '2°C', '0°C', '1°C', '-3°C（體感-8°C）'],
    ]
    s.append(make_table(['地區', '12月', '1月', '2月', '嚴冬期'], temp_data[1:]))
    s.append(Spacer(1, 10))
    
    # Section 2
    s.append(Paragraph('必備穿搭清單', h2))
    s.append(Paragraph('北海道冬季穿搭核心觀念：「洋蔥式穿法」+「防風防水最外層」。室內暖氣充足（22-25°C），但進出溫差高達40°C，建議分層穿搭。', body))
    
    packing_data = [
        ['類別', '必備物品', '推薦品牌/規格', '備註'],
        ['外層', '-30°C級防風外套', 'UNIQLO Ultra Light Down', '需防風防水'],
        ['中層', '刷毛/羊毛中層', '優衣庫刷毛利品', '保暖且透氣'],
        ['內層', '發熱衣（上下）', 'UNIQLO HEATTECH', '至少帶2套替換'],
        ['下半身', '刷毛褲/羊毛褲', 'UNIQLO 刷毛褲', '不可穿棉褲（不透氣）'],
        ['鞋襪', '雪靴+5雙羊毛襪', 'Columbia/Timberland', '鞋底需防滑'],
        ['配件', '保暖手套+圍巾+耳罩', 'UNIQLO 刷毛系列', '口罩也要保暖型'],
        ['小物', '暖暖包（懷爐）', '日本製一次性', '7-11/全家有賣'],
    ]
    s.append(make_table(['類別', '必備物品', '推薦品牌/規格', '備註'], packing_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s.append(Paragraph('室內外溫差應對', h2))
    s += make_tip('洋蔥式穿法示範', [
        '室內（22°C）：發熱衣+薄長袖（可捲袖）',
        '室外（--5°C）：發熱衣+刷毛中層+防風外套+圍巾+手套',
        '進室內：先脫外套→再脫中層→保留發熱衣',
        '避免滿頭大汗進室內（容易感冒）',
    ])
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('購買地點與預算', h2))
    s.append(Paragraph('台灣出發前建議在UNIQLO/寶雅購齊發熱衣、刷毛褲、保暖配件。日本當地UNIQLO價格與台灣差不多，但Selection系列更保暖。雪靴建議在台灣買好，日本雪靴價格較高（8,000-15,000日圓）。', body))
    
    budget_data = [
        ['物品', '台灣購買價格', '日本購買價格', '建議'],
        ['發熱衣（2件）', 'NT$800', '1,200日圓（約NT$260）', '台灣買'],
        ['刷毛中層', 'NT$1,200', '2,500日圓（約NT$550）', '台灣買'],
        ['防風外套', 'NT$3,000', '8,000日圓（約NT$1,750）', '台灣買'],
        ['雪靴', 'NT$2,500', '12,000日圓（約NT$2,630）', '台灣買'],
        ['暖暖包（50入）', 'NT$150', '500日圓（約NT$110）', '均可'],
    ]
    s.append(make_table(['物品', '台灣購買價格', '日本購買價格', '建議'], budget_data[1:]))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_okinawa_driving():
    """沖繩自駕地圖 - 完整攻略"""
    s = []
    s += make_cover('沖繩自駕地圖', '2026 最新版')
    
    s.append(Paragraph('沖繩自駕總覽', h1))
    s.append(Paragraph('沖繩本島（那霸）是台灣人最愛的自駕目的地之一。從台灣飛那霸僅需1.5小時，租車便宜（3天約NT$4,500），油價與台灣差不多。本攻略涵蓋沖繩本島最美自駕路線、停車資訊、預算分配。', body))
    
    # Section 1
    s.append(Paragraph('沖繩本島自駕路線推薦', h2))
    route_data = [
        ['天數', '路線', '距離', '景點數', '難度'],
        ['1天', '那霸→名護→古宇利島（來回）', '約180km', '5-6個', '中等'],
        ['2天', '那霸→名護→本部→名護（住宿）→古宇利→美麗海水族館', '約250km', '8-10個', '中等'],
        ['3天', '那霸→名護→本部→宮古→石垣（需搭飛機）', '跨島', '12+個', '困難'],
        ['5天', '本島環島+宮古島+石垣島', '跨島', '20+個', '困難'],
    ]
    s.append(make_table(['天數', '路線', '距離', '景點數', '難度'], route_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('本島必停景點（南部→中部→北部）', h2))
    spots_data = [
        ['區域', '景點', '停車費', '遊覽時間', '推薦度'],
        ['南部', '首里城公園', '免費', '1.5小時', '★★★★☆'],
        ['南部', '沖繩優美海水族館', '2,000日圓', '3小時', '★★★★★'],
        ['中部', '美國村', '免費', '2小時', '★★★★☆'],
        ['中部', '殘波岬', '免費', '30分', '★★★☆☆'],
        ['北部', '古宇利島大橋', '免費', '1小時', '★★★★★'],
        ['北部', '名護鳳梨園', '1,200日圓', '1.5小時', '★★★☆☆'],
    ]
    s.append(make_table(['區域', '景點', '停車費', '遊覽時間', '推薦度'], spots_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s.append(Paragraph('租車與交通規則', h2))
    s += make_tip('沖繩自駕必知', [
        '台灣駕照需辦「國際駕照」或「JPD翻譯本」才能在沖繩開車',
        '沖繩車速限制：高速公路80km/h，一般道路60km/h，市區40km/h',
        '停車場：景點多有免費停車場，但美國村/那霸市區需付費（100-300日圓/小時）',
        '加油：沖繩油價約170日圓/公升（比台灣貴約30%）',
        '導航：Google Maps在沖繩準確度極高，建議下載離線地圖',
    ])
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('3天2夜自駕預算表', h2))
    budget_data = [
        ['項目', '費用(日圓)', '台幣約', '備註'],
        ['租車（小型車3天）', '15,000', 'NT$3,300', '含保險'],
        ['油費（約300km）', '6,000', 'NT$1,320', '油耗約20km/L'],
        ['停車費（市區）', '2,000', 'NT$440', '那霸/美國村'],
        ['過路費（高速公路）', '1,500', 'NT$330', '那霸→名護'],
        ['景點門票', '5,200', 'NT$1,140', '水族館+首里城'],
        ['合計', '29,700', 'NT$6,530', '不含住宿/餐飲'],
    ]
    s.append(make_table(['項目', '費用(日圓)', '台幣約', '備註'], budget_data[1:]))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_kyoto_momiji():
    """京都紅葉日程表 - 完整攻略"""
    s = []
    s += make_cover('京都紅葉日程表', '2026 最新版')
    
    s.append(Paragraph('京都紅葉季總覽', h1))
    s.append(Paragraph('京都紅葉季（Momiji Season）通常在11月中旬至12月上旬，2026年預測：11月20日至12月5日為滿紅期。清水寺、金閣寺、嵐山是熱門景點，但人潮極多。本攻略提供鮮為人知的紅葉名所、攝影技巧、交通建議。', body))
    
    # Section 1
    s.append(Paragraph('2026年紅葉預測日程', h2))
    schedule_data = [
        ['時期', '紅葉狀態', '推薦景點', '人潮'],
        ['11月10-15日', '葉子開始轉黃/轉紅', '貴船神社、鞍馬寺', '少'],
        ['11月16-20日', '半紅半綠（最美時刻）', '嵐山、渡月橋', '中等'],
        ['11月21-30日', '滿紅（紅得像火）', '清水寺、金閣寺、南禪寺', '極多'],
        ['12月1-5日', '滿紅末期（葉子開始掉落）', '大原寂光院、三千院', '中等'],
        ['12月6-10日', '葉子掉光（僅剩枯枝）', '不推薦', '—'],
    ]
    s.append(make_table(['時期', '紅葉狀態', '推薦景點', '人潮'], schedule_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('紅葉名所推薦（避開人潮版）', h2))
    spots_data = [
        ['景點', '紅葉時期', '入場費', '攝影難度', '推薦度'],
        ['清水寺', '11月20-30日', '400日圓', '困難（太多人）', '★★★☆☆'],
        ['金閣寺', '11月20-30日', '500日圓', '困難（太多人）', '★★★☆☆'],
        ['嵐山渡月橋', '11月16-25日', '免費', '中等', '★★★★☆'],
        ['貴船神社', '11月10-20日', '免費', '容易', '★★★★★'],
        ['大原三千院', '11月25-12月5日', '700日圓', '容易', '★★★★★'],
        ['南禪寺', '11月20-30日', '500日圓', '中等', '★★★★☆'],
    ]
    s.append(make_table(['景點', '紅葉時期', '入場費', '攝影難度', '推薦度'], spots_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s.append(Paragraph('紅葉攝影技巧', h2))
    s += make_tip('攝影黃金時段', [
        '最佳光線：早上8:00-9:30（側光，紅葉呈現金黃色）',
        '避免頂光：10:00-14:00（光線太強，紅葉會過曝）',
        '夕陽紅葉：15:30-16:30（逆光，紅葉呈現透明感）',
        '必備濾鏡：CPL偏光鏡（消除葉面反光）、ND減光鏡（拍流水）',
        '鏡頭推薦：廣角16-35mm（拍大景）、微距100mm（拍葉子細節）',
    ])
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('一日行程範例（避開人潮）', h2))
    s.append(Paragraph('07:30 出發（從京都站）\n'
                     '08:30 貴船神社（紅葉+流水，人少）\n'
                     '10:30 鞍馬寺（紅葉隧道，極美）\n'
                     '12:00 貴船車站附近吃湯豆腐\n'
                     '13:30 大原三千院（紅葉+苔蘚，極美）\n'
                     '15:30 南禪寺（水路閣，紅葉名所）\n'
                     '17:00 嵐山渡月橋夕陽（免費，最美夕陽）\n'
                     '18:30 返回京都站', body_compact))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_osaka_food():
    """大阪美食地圖 - 完整攻略"""
    s = []
    s += make_cover('大阪美食地圖', '2026 最新版')
    
    s.append(Paragraph('大阪美食總覽', h1))
    s.append(Paragraph('大阪被稱為「日本的廚房」，美食密度全日本第一。道頓堀、黑門市場、新世界是三大美食聖地。2026年大阪關西世界博覽會（4-10月）期間，美食街上將湧入大量外國遊客，建議避開4-10月或早上9:00前抵達。', body))
    
    # Section 1
    s.append(Paragraph('必吃美食排行榜', h2))
    food_data = [
        ['美食', '價格(日圓)', '推薦店家', '必吃理由'],
        ['章魚燒（たこ焼き）', '500-800', '會津屋（道頓堀）', '章魚燒發源地'],
        ['大阪燒（お好み焼き）', '800-1,200', '美津の（法善寺橫丁）', '大阪靈魂美食'],
        ['串炸（串カツ）', '100-300/串', '達摩（新世界）', '禁止回沾醬料'],
        ['拉麵（らーめん）', '900-1,300', '一蘭（道頓堀）', '24小時營業'],
        ['河豚料理（ふぐ）', '3,000-8,000', 'づぼらや（新世界）', '冬季限定'],
        ['文字燒（もんじゃ）', '1,000-1,500', '文字燒街道（月島）', '東京傳來'],
    ]
    s.append(make_table(['美食', '價格(日圓)', '推薦店家', '必吃理由'], food_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('黑門市場攻略', h2))
    s.append(Paragraph('黑門市場（くろもんいちば）是大阪的「廚房」，全長580公尺，約150間店舖。新鮮海產、和牛、水果、甜點應有盡有。早上9:00開門，11:00前人潮較少。', body))
    
    kuromon_data = [
        ['類別', '推薦店家', '價格', '必吃'],
        ['海鮮', '黑門三平', '1,500-3,000日圓', '新鮮生魚片'],
        ['和牛', '松田牛店', '2,000-5,000日圓', 'A5和牛串'],
        ['水果', '匠果子', '500-1,500日圓', '高級麝香葡萄'],
        ['甜點', '製麵處', '300-800日圓', '抹茶霜淇淋'],
    ]
    s.append(make_table(['類別', '推薦店家', '價格', '必吃'], kuromon_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('美食小撇步', [
        '章魚燒剛出爐很燙（90°C），裡面溫度更高，建議戳破讓熱氣散出',
        '串炸禁止回沾醬料（違者罰1000日圓），醬料在桌上方共用',
        '道頓堀的「くくる」章魚燒有會跳舞的醬料表演，適合拍照',
        '黑門市場可以試吃（店家會主動招呼），但不要只試不吃',
        '世博期間（4-10月）避開週末，平日早上9:00前抵達最佳',
    ])
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('美食街地圖（道頓堀→黑門市場→新世界）', h2))
    s.append(Paragraph('路線：難波站 → 道頓堀（30分） → 黑門市場（10分） → 新世界（地鐵10分）\n\n'
                     '預算：每人每天約3,000-5,000日圓（不含高級和牛）\n'
                     '推薦時段：早上9:00-11:00（黑門市場人潮少）\n'
                     '避雷：道頓堀的「觀光客專用店」價格貴30%，往裡面走較便宜', body_compact))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_usj_quick_pass():
    """USJ快速通關攻略 - 完整攻略"""
    s = []
    s += make_cover('USJ快速通關攻略', '2026 最新版')
    
    s.append(Paragraph('USJ快速通關總覽', h1))
    s.append(Paragraph('日本環球影城（USJ）位於大阪，假日等候時間可達120-180分鐘。快速通關（Express Pass）是節省時間的神器，但價格不便宜（3,800-14,800日圓）。本攻略幫你分析是否值得買、如何買、怎麼用。', body))
    
    # Section 1
    s.append(Paragraph('快速通關種類比較', h2))
    pass_data = [
        ['種類', '價格(日圓)', '設施數', '包含設施', '推薦度'],
        ['快速3（Express 3）', '3,800-5,800', '3個', '任天堂+小黃人+侏羅紀', '★★★★☆'],
        ['快速7（Express 7）', '6,800-9,800', '7個', '含所有熱門設施', '★★★★★'],
        ['快速9（Express 9）', '9,800-14,800', '9個', '全部設施+VIP席', '★★★☆☆'],
        ['單項快速券', '1,500-2,500', '1個', '指定1個設施', '★★☆☆☆'],
    ]
    s.append(make_table(['種類', '價格(日圓)', '設施數', '包含設施', '推薦度'], pass_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('超級任天堂世界（SNW）攻略', h2))
    s.append(Paragraph('SNW是USJ最熱門的區域，馬利歐賽車（Mario Kart: Koopa\'s Challenge）等候時間可達180分鐘。進入SNW有兩種方式：1. 購買快速通關、2. 取得「區域入場確約券」（當日早上7:00在USJ官網搶）。', body))
    
    snw_data = [
        ['項目', '說明'],
        ['區域入場確約券', '免費，當日7:00在USJ官網搶，名額有限'],
        ['快速通關', '保證進入SNW，不需搶券'],
        ['現場排隊', '開園即衝，可能進得去，但不保證'],
        ['推薦方式', '快速7以上（含SNW）最穩定'],
    ]
    s.append(make_table(['項目', '說明'], snw_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('USJ必知技巧', [
        '開園時間（8:30-9:00）一定要在門口等，開園後直衝SNW',
        '快速通關建議在進園後立即使用（避免下午人潮更多）',
        '哈利波特禁忌之旅（Forbidden Journey）值得排90分鐘，效果極佳',
        '小黃人瘋狂乘車（Minion Mayhem）適合兒童，等候時間較短',
        'USJ手環（Power Up Band）可在SNW互動集章，建議購買（3,900日圓）',
    ])
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('一日行程範例（有買快速7）', h2))
    s.append(Paragraph('08:30 開園，直衝SNW（馬利歐賽車）\n'
                     '10:30 哈利波特禁忌之旅（快速通關）\n'
                     '12:00 午餐（三根掃帚酒吧）\n'
                     '13:30 小黃人瘋狂乘車（快速通關）\n'
                     '15:00 侏羅紀公園（快速通關）\n'
                     '16:30 蜘蛛人驚魂歷險（現場排隊，約60分）\n'
                     '18:00 遊行/夜間燈光秀\n'
                     '20:00 出園', body_compact))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s

