// Node.js script to append Part 3 PDF content (Taiwan + SEA batch) to _beautify_pdf.py
const fs = require('fs');
const path = require('path');

const targetFile = 'C:\\Users\\FH01\\.qclaw\\workspace-cwapojim0yfmyvq8\\Travel-Lab\\_beautify_pdf.py';

const pythonCode = `

# ============================================================================
# Part 3: Taiwan + SEA Batch (9 PDFs)
# ============================================================================

def gen_hualien():
    """花蓮行程規劃 - Hualien Itinerary"""
    story = []
    story += make_cover('花蓮行程規劃', '2026 太魯閣·清水斷崖·七星潭')
    
    # Section 1
    story.append(Paragraph('花蓮必遊景點總覽', h1))
    story.append(Paragraph('花蓮位於台灣東部，以壯麗的太魯閣國家公園、蔚藍的七星潭、險峻的清水斷崖聞名。這座城市融合了山海美景與原民文化，是台灣最值得深度旅遊的縣市之一。三天兩夜的行程可以涵蓋主要景點，並體驗在地美食與自然生態。', body))
    
    tbl_data = [
        ['景點', '門票', '建議停留'],
        ['太魯閣國家公園', '免費', '3-4 小時'],
        ['七星潭', '免費', '1-2 小時'],
        ['清水斷崖', '免費', '30 分鐘'],
        ['鯉魚潭', '免費', '1-2 小時'],
        ['豐濱北回歸線標誌', '免費', '20 分鐘']
    ]
    story.append(make_table(['景點', '門票', '建議停留'], tbl_data))
    story += make_tip('行程小撇步', ['太魯閣建議早上 8 點前抵達避開遊覽車人潮', '七星潭風浪較大，請勿戲水', '清水斷崖視野開闊，適合拍網美照'])
    
    # Section 2
    story.append(Paragraph('推薦行程安排', h2))
    story.append(Paragraph('第一天：抵達花蓮後前往七星潭欣賞夕陽，晚上逛東大門夜市品嚐炸彈蔥油餅與麻糬。第二天：早上出發太魯閣，中午在崇德服務區用餐，下午走砂卡礑步道，傍晚前往清水斷崖。第三天：探訪鯉魚潭與豐濱北回歸線標誌，購買伴手禮後返程。', body))
    
    tbl_data = [
        ['時間', '行程', '交通'],
        ['Day 1 下午', '七星潭→東大門夜市', '租機車'],
        ['Day 2 上午', '太魯閣國家公園', '包車/跟團'],
        ['Day 2 下午', '砂卡礑步道→清水斷崖', '包車'],
        ['Day 3 上午', '鯉魚潭→豐濱', '租機車']
    ]
    story.append(make_table(['時間', '行程', '交通'], tbl_data))
    
    # Section 3
    story.append(Paragraph('美食推薦', h2))
    story.append(Paragraph('花蓮美食以原住民風味、海鮮、麻糬最具特色。炸彈蔥油餅是東大門夜市的靈魂美食，外酥內軟配上滿滿蔥花與蛋液，一份 60 元。液香扁食的餛飩湯鮮美實惠，一碗 50 元。曾記麻糬是花蓮名產，原味麻糬一盒 120 元。海埔蚵仔煎使用肥美鮮蚵，一份 80 元。', body))
    
    tbl_data = [
        ['美食', '價格', '推薦店家'],
        ['炸彈蔥油餅', '60 TWD', '東大門夜市'],
        ['液香扁食', '50 TWD', '中山路'],
        ['曾記麻糬', '120 TWD/盒', '中正路'],
        ['海埔蚵仔煎', '80 TWD', '舊站夜市']
    ]
    story.append(make_table(['美食', '價格', '推薦店家'], tbl_data))
    story += make_tip('美食小撇步', ['東大門夜市 18:00 開始營業，建議 19:00 前到達', '曾記麻糬有試吃，可先品嚐再購買', '自強夜市週日休市，請注意營業時間'])
    
    # CTA
    story += make_cta()
    return story


def gen_tainan_food():
    """台南美食地圖 - Tainan Food Map"""
    story = []
    story += make_cover('台南美食地圖', '2026 擔子麵·蝦捲·碗粿·牛肉湯')
    
    # Section 1
    story.append(Paragraph('台南必吃美食總覽', h1))
    story.append(Paragraph('台南被譽為台灣的美食首都，擔子麵、蝦捲、碗粿、牛肉湯、蝦仁飯、米糕等都是在地經典。這座古城擁有數