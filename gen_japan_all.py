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
        ('ROUNDEDCORNERS', [8,8,8,8]),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('PADDING', (0,0), (-1,-1), 15),
    ]))
    s.append(t)
    s.append(Spacer(1, 8))
    s.append(Paragraph('加入 LINE 群組：https://line.me/ti/g/NbNGnW4Eh6', body))
    s.append(Paragraph('更多免費旅遊 PDF：https://golightly.fun', body))
    return s

# ============ PDF 1: Tokyo Metro Map ============
def gen_tokyo_metro():
    doc = SimpleDocTemplate('downloads/tokyo-metro-map.pdf')
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
    ]
    s.append(make_table(['路線名稱', '代表色', '車站數', '營運長度(km)'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('票價與優惠票券', h2))
    s.append(Paragraph('東京地鐵票價依距離計算，成人單程票價格介於170-320日圓之間。建議購買「東京地鐵24小時券」（800日圓）或「都營地鐵+東京地鐵共通券」（1,590日圓/24小時），可無限次搭乘。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: tokyo-metro-map.pdf')

# ============ PDF 2: Kansai Pass Calculator ============
def gen_kansai_pass():
    doc = SimpleDocTemplate('downloads/kansai-pass-calculator.pdf')
    s = []
    s += make_cover('關西地區鐵路周遊券', '2026 計算機與購買指南')
    s.append(Paragraph('關西地區鐵路周遊券完整攻略', h1))
    s.append(Paragraph('關西地區鐵路周遊券（Kansai Area Pass）是前往大阪、京都、奈良、神戶、和歌山的經濟實惠選擇。本指南提供票價比較、使用範圍、購買方式與省錢技巧。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['票券種類', '價格(日圓)', '使用天數', '適用範圍'],
        ['關西機場快車', '1,430', '1天', '關空往返'],
        ['關西地區周遊券', '2,800', '1天', '大阪/京都/奈良'],
        ['關西廣域周遊券', '5,000', '3天', '關西全區+和歌山'],
        ['JR關西地區鐵路周遊券', '4,000', '1天', 'JR線全線'],
    ]
    s.append(make_table(['票券種類', '價格(日圓)', '使用天數', '適用範圍'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('購買建議', h2))
    s.append(Paragraph('如果您計劃在關西地區停留2天以上，購買「關西地區周遊券」可節省約30%交通費用。建議提前在台灣旅行社或網路預購，可享有9折優惠。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: kansai-pass-calculator.pdf')

# ============ PDF 3: Hokkaido Packing List ============
def gen_hokkaido_packing():
    doc = SimpleDocTemplate('downloads/hokkaido-packing-list.pdf')
    s = []
    s += make_cover('北海道打包清單', '2026 四季必備物品')
    s.append(Paragraph('北海道旅遊打包完整指南', h1))
    s.append(Paragraph('北海道氣候涼爽，四季分明，夏季平均溫度20-25°C，冬季則可達-10°C以下。本指南提供四季打包清單、服裝建議、必備用品與當地購物推薦。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['季節', '平均溫度', '必備衣物', '推薦物品'],
        ['春季(4-6月)', '5-15°C', '薄外套、長褲', '防曬乳液中'],
        ['夏季(7-8月)', '20-28°C', '短袖、薄長褲', '防蚊液、帽子'],
        ['秋季(9-11月)', '5-20°C', '厚外套、毛衣', '保濕乳液、口罩'],
        ['冬季(12-3月)', '-10-5°C', '羽絨衣、毛帽', '暖暖包、防風手套'],
    ]
    s.append(make_table(['季節', '平均溫度', '必備衣物', '推薦物品'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('北海道特有物品', h2))
    s.append(Paragraph('北海道紫外線較強，即使夏季也建議攜帶防曬用品。冬季則需準備足夠的保暖裝備，當地亦可購買平價保暖衣物。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: hokkaido-packing-list.pdf')

# ============ PDF 4: Okinawa Driving Map ============
def gen_okinawa_driving():
    doc = SimpleDocTemplate('downloads/okinawa-driving-map.pdf')
    s = []
    s += make_cover('沖繩自駕地圖', '2026 自駕路線與租車指南')
    s.append(Paragraph('沖繩自駕完整攻略', h1))
    s.append(Paragraph('沖繩本島面積約1,200平方公里，環島公路全長約120公里。自駕是遊覽沖繩最自由便利的方式，可以隨意停靠景點、調整行程節奏。本攻略精選3條自駕路線，涵蓋北部、中部、南部，每條路線規劃1-2天行程。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['路線名稱', '天數', '總里程(km)', '適合族群'],
        ['北部海岸路線', '2天1夜', '80', '海灘愛好者'],
        ['中部文化路線', '1天', '60', '親子同遊'],
        ['南部歷史路線', '1天', '50', '歷史文化愛好者'],
        ['環島深度路線', '3天2夜', '180', '深度旅遊玩家'],
    ]
    s.append(make_table(['路線名稱', '天數', '總里程(km)', '適合族群'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('租車注意事項', h2))
    s.append(Paragraph('台灣遊客需準備國際駕照（IDP）與台灣駕照正本。建議提前線上預約租車，現場租車價格較高。沖繩加油站多為自助式，建議學習日文加油操作流程。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: okinawa-driving-map.pdf')

# ============ PDF 5: Kyoto Momiji Schedule ============
def gen_kyoto_momiji():
    doc = SimpleDocTemplate('downloads/kyoto-momiji-schedule.pdf')
    s = []
    s += make_cover('京都紅葉日程表', '2026 紅葉前線與攝影攻略')
    s.append(Paragraph('京都紅葉完整指南', h1))
    s.append(Paragraph('京都紅葉季節通常從11月中旬開始，至12月上旬達到巔峰。本指南提供2026年紅葉預測、最佳攝影時間、推薦景點與行程規劃，讓您捕捉京都最美的秋日風情。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['景點名稱', '預測最佳觀賞期', '入場費', '攝影建議時間'],
        ['清水寺', '11月20日-12月5日', '400日圓', '清晨6:00-8:00'],
        ['金閣寺', '11月25日-12月10日', '500日圓', '下午3:00-4:00'],
        ['嵐山', '11月15日-11月30日', '免費', '全天皆可'],
        ['永觀堂', '11月10日-12月5日', '1,000日圓', '下午1:00-3:00'],
    ]
    s.append(make_table(['景點名稱', '預測最佳觀賞期', '入場費', '攝影建議時間'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('攝影技巧', h2))
    s.append(Paragraph('紅葉攝影建議使用偏光鏡減少反光，並利用逆光拍攝創造透亮感。清晨時分遊客較少，可拍攝到無人的美景。建議攜帶三腳架，但部分寺廟禁止架設。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: kyoto-momiji-schedule.pdf')

# ============ PDF 6: Osaka Food Map ============
def gen_osaka_food():
    doc = SimpleDocTemplate('downloads/osaka-food-map.pdf')
    s = []
    s += make_cover('大阪美食地圖', '2026 必吃美食與餐廳推薦')
    s.append(Paragraph('大阪美食完整指南', h1))
    s.append(Paragraph('大阪被稱為「日本的廚房」，擁有豐富的街頭美食與高級料理。本指南精選20間必訪餐廳，涵蓋章魚燒、大阪燒、拉麵、壽司等經典美食，並提供預約方式與價位參考。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['美食種類', '推薦餐廳', '人均消費(日圓)', '所在地'],
        ['章魚燒', '大阪王將', '500-800', '道頓堀'],
        ['大阪燒', '美津の', '1,000-1,500', '難波'],
        ['拉麵', '一蘭拉麵', '1,000-1,200', '心齋橋'],
        ['壽司', '黑門市場壽司', '2,000-3,000', '黑門市場'],
    ]
    s.append(make_table(['美食種類', '推薦餐廳', '人均消費(日圓)', '所在地'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('美食區域推薦', h2))
    s.append(Paragraph('道頓堀是大阪美食的核心區域，聚集了最多經典小吃。黑門市場則提供新鮮海鮮與熟食，適合喜歡嘗鮮的旅人。高級料理建議預約，平價美食則可直接前往。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: osaka-food-map.pdf')

# ============ PDF 7: USJ Quick Pass ============
def gen_usj_quick_pass():
    doc = SimpleDocTemplate('downloads/usj-quick-pass.pdf')
    s = []
    s += make_cover('USJ 快速通關攻略', '2026 最新快速通關購買與使用指南')
    s.append(Paragraph('日本環球影城快速通關完整攻略', h1))
    s.append(Paragraph('日本環球影城（USJ）是關西地區最受歡迎的主題樂園，每年吸引超過1,500萬遊客。本攻略提供快速通關（Express Pass）購買方式、使用技巧、推薦行程與省錢秘訣。', body))
    s.append(Spacer(1, 10))
    
    data = [
        ['快速通關種類', '價格(日圓)', '包含設施數', '推薦指數'],
        ['Express Pass 4', '8,800-12,800', '4個', '★★★★★'],
        ['Express Pass 7', '13,800-18,800', '7個', '★★★★☆'],
        ['Express Pass VIP', '23,800-33,800', '全部', '★★★☆☆'],
    ]
    s.append(make_table(['快速通關種類', '價格(日圓)', '包含設施數', '推薦指數'], data))
    s.append(Spacer(1, 10))
    
    s.append(Paragraph('購買建議', h2))
    s.append(Paragraph('快速通關建議提前1-2個月在官方網站預購，熱門日期（週末、假日）容易售罄。若預算有限，可選擇「Express Pass 4」，涵蓋最熱門的4個設施，性價比最高。', body))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    doc.build(s)
    print('OK: usj-quick-pass.pdf')

# Main
if __name__ == '__main__':
    gen_tokyo_metro()
    gen_kansai_pass()
    gen_hokkaido_packing()
    gen_okinawa_driving()
    gen_kyoto_momiji()
    gen_osaka_food()
    gen_usj_quick_pass()
    print('All 7 Japan PDFs generated successfully!')
