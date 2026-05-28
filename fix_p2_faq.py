#!/usr/bin/env python3
"""
P2-2 修復：補充 FAQ 數量至 4-6 題
"""

import re
import json
from pathlib import Path

WORK_DIR = Path("C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab")

# FAQ 模板庫（根據文章主題）
FAQ_TEMPLATES = {
    'japan': [
        ('日本旅遊最佳季節是什麼時候？', '櫻花季（3-4月）和紅葉季（11月）最美，但人多價高。5-6月、9-10月避開梅雨季和颱風，價格較低，天氣也舒適。冬季（12-2月）適合滑雪和泡溫泉。'),
        ('日本交通怎麼省錢？', '建議購買JR Pass（全國版或地區版），新幹線自由席比指定席便宜。市內交通用地鐵一日券（Tokyo Subway Ticket、Osaka Amazing Pass）。巴士比地鐵便宜，但較慢。'),
        ('日本便利商店有哪些必買？', '7-11的飯糰、FamilyMart的炸雞、Lawson的霜淇淋都超推薦。還有各式便當、沙拉、飯店、甜點，品質不輸餐廳，價格只要1/3。'),
        ('日本插座需要變壓器嗎？', '日本電壓100V，台灣110V，大部分電器（手機、筆電）可直接使用。但吹風機、電棒捲可能需要變壓器。插座為兩頭扁腳，台灣插頭可直接使用。'),
        ('日本溫泉禮儀要注意什麼？', '入浴前要先沖洗身體。毛巾不可放入浴池，可放在頭上或旁邊。有刺青者可能被拒絕入場（可找允許刺青的溫泉或用貼布遮蓋）。'),
        ('日本怎麼上網？SIM卡還是WiFi機？', '推薦購買當地SIM卡（成田、羽田機場都有賣），價格約¥2,000-3,000/5天。WiFi機訊號穩但需歸還，適合多人分攤。Free WiFi熱點越來越多，但覆蓋率仍不足。'),
    ],
    'korea': [
        ('韓國簽證需要嗎？', '台灣護照免簽證，可停留90天。但需填寫「入境卡」和「健康狀態調查表」。建議準備來回機票和住宿證明，海關可能查驗。'),
        ('韓國上網怎麼辦？', '推薦在台灣先買好eSIM（Korea Telecom、SK Telecom），下飛機就有網路。也可在仁川機場租WiFi機（約₩3,000/天），多人分攤較划算。'),
        ('韓國插座是什麼規格？需要變壓器嗎？', '韓國電壓220V，插座為兩頭圓腳（歐規）。台灣插頭需要轉接頭，建議在台灣先買好。變壓器大多不需要，手機、筆電都支援110-240V。'),
        ('韓國 T-money 卡怎麼用？', 'T-money卡可在便利商店購買（₩2,500），地鐵、公車都能用，比現金便宜₩100。也可在便利商店消費。退卡可退押金，但需手續費，不常用建議直接留作紀念。'),
        ('韓國夜生活安全嗎？', '首爾弘大、明洞、江南都算安全，但建議避開偏僻小巷。女性單獨旅行建議22:00前回住宿。計程車安全，但需注意酒後亂說話的司機（可裝假翻譯App應付）。'),
        ('韓國购物退稅怎麼辦？', '單店消費₩30,000以上可退稅（約7-8%）。結帳時出示護照，離開韓國時在海關退稅櫃檯辦理。建議集中在樂天、現代免稅店購買，可當場折扣。'),
    ],
    'taiwan': [
        ('台灣旅遊最佳時間？', '春秋（3-5月、9-11月）天氣最舒適。夏季（6-8月）炎熱多雨，但適合海邊活動。冬季（12-2月）北部濕冷，南部仍溫暖。颱風季（7-9月）需注意天氣預報。'),
        ('台灣交通怎麼安排？', '台鐵（火車）和高鐵（高鐵）連接主要城市。市區以大眾運輸為主（台北捷運、高雄捷運）。租機車/汽車適合東部、離島自由行。推薦下載「台灣交通」App查詢時刻表。'),
        ('台灣夜市必吃什麼？', '士林夜市（台北）：豪大大雞排、大餅包小餅。逢甲夜市（台中）：黃金右腿、整隻章魚。六合夜市（高雄）：鄭老牌木瓜牛奶、臭豆腐。花園夜市（台南）：正是茶飲、阿美綠豆湯。'),
        ('台灣住宿推薦哪裡？', '台北：西門町（交通方便）、中山區（文青咖啡廳多）。台中：逢甲附近（夜市美食）。台南：老城區（古蹟民宿）。花蓮：火車站附近（交通方便）。墾丁：大街附近（海邊活動）。'),
        ('台灣有什麼特色體驗？', '泡湯（北投、陽明山）、自行車道（河濱公園、日月潭）、茶園採茶（阿里山、梨山）、原住民文化（花蓮、台東）、夜市美食團購（適合多人）。'),
    ],
    'southeast_asia': [
        ('東南亞旅遊最佳季節？', '乾季（11-2月）最舒適，雨水少、溫度適中。雨季（5-10月）雖然下雨但機票住宿便宜，適合預算有限的旅客。4月最熱（35°C+），需做好防曬。'),
        ('東南亞需要打疫苗嗎？', '建議接種日本腦炎、A型肝炎、破傷風疫苗。瘧疾藥物視目的地而定（城市不需要，深山叢林建議）。出發前2個月諮詢旅遊醫學門診。'),
        ('東南亞上網怎麼辦？', '推薦在台灣買好當地eSIM（Airalo、Nomad），或購買當地SIM卡（7-11、全家都有賣）。WiFi機多人分攤較划算，但需歸還。Free WiFi覆蓋率城市較高，鄉村較差。'),
        ('東南亞飲食要注意什麼？', '避免生水和未剝皮的水果。街邊攤選擇熱食、現煮的較安全。自備益生菌預防水土不服。路邊冰塊若用不潔水製作可能會拉肚子，建議觀察店家衛生狀況。'),
        ('東南亞交通怎麼安排？', '城市內用Grab（東南亞版Uber）最方便。長途移動可搭廉航（AirAsia、Lion Air）。火車適合慢活旅行（泰國、越南）。租機車需國際駕照，戴安全帽。'),
        ('東南亞貨幣怎麼處理？', '大多數國家可用美元，但匯率較差。建議在當地換錢所換成當地貨幣（匯率較好）。信用卡在大型商場可用，夜市、小吃攤只收現金。'),
    ],
    'general': [
        ('旅行保險需要買嗎？', '強烈建議購買旅遊不便險和醫療險。海外醫療費用昂貴，有保險可減輕負擔。推薦比較「富邦」、「國泰」、「新光」的旅平險方案。'),
        ('出國前要準備什麼？', '檢查護照有效期（需6個月以上）。準備來回機票和住宿證明。兌換少量當地貨幣備用。下載離線地圖和翻譯App。通知銀行信用卡將出國使用。'),
        ('怎麼找便宜機票？', '使用Skyscanner、Google Flights比價。設定價格通知，價格下降會自動通知。避開週末出發，週二週三較便宜。提前2-3個月購買，最後一刻訂票通常較貴。'),
        ('行李怎麼打包最聰明？', '使用打包清單App（如PackPoint）。穿搭以層次穿搭為主，適應溫差。重要文件（護照、保險卡）拍照備份。攜帶萬用插頭和行動電源。'),
    ],
}

def get_article_topic(filename):
    """判斷文章主題，返回對應的 FAQ 模板類別"""
    name = filename.lower()
    if any(k in name for k in ['japan', 'tokyo', 'kyoto', 'osaka', 'hokkaido', 'okinawa', 'kansai']):
        return 'japan'
    elif any(k in name for k in ['korea', 'seoul', 'busan', 'jeju']):
        return 'korea'
    elif any(k in name for k in ['taiwan', 'taipei', 'tainan', 'jiufen', 'kenting', 'hualien']):
        return 'taiwan'
    elif any(k in name for k in ['bangkok', 'chiang', 'vietnam', 'danang', 'southeast', 'seasia']):
        return 'southeast_asia'
    else:
        return 'general'

def count_faqs(content):
    """計算現有 FAQ 數量"""
    return len(re.findall(r'<div class="faq-item">', content))

def generate_faq_html(questions_answers):
    """生成 FAQ HTML 區塊"""
    html = '<div class="faq-section">\n'
    html += '  <h2>❓ 常見問題 FAQ</h2>\n'
    html += '  <div class="faq-list">\n'
    
    for q, a in questions_answers:
        html += '    <div class="faq-item">\n'
        html += f'      <h3>{q}</h3>\n'
        html += f'      <p>{a}</p>\n'
        html += '    </div>\n'
    
    html += '  </div>\n'
    html += '</div>\n'
    return html

def fix_article_faq(filepath, target_count):
    """修復單篇文章的 FAQ"""
    try:
        content = filepath.read_text(encoding='utf-8')
        
        current_count = count_faqs(content)
        
        if current_count >= target_count:
            print(f"✅ {filepath.name} FAQ 已充足 ({current_count}>={target_count})")
            return False
        
        # 獲取主題
        topic = get_article_topic(filepath.name)
        
        # 取得模板
        templates = FAQ_TEMPLATES.get(topic, FAQ_TEMPLATES['general'])
        
        # 隨機選取問題（避免重複）
        import random
        selected = random.sample(templates, min(target_count, len(templates)))
        
        # 生成 FAQ HTML
        faq_html = generate_faq_html(selected)
        
        # 找到插入位置：在 </body> 或 </article> 之前
        # 優先在 related-posts 之後插入
        insert_pos = -1
        
        # 方法1: 在 related-posts 之後
        related_end = content.rfind('</div>\n</div>', content.find('<div class="related-posts">'))
        if related_end > 0:
            insert_pos = related_end + len('</div>\n</div>')
        
        # 方法2: 在 </body> 之前
        if insert_pos == -1:
            body_end = content.rfind('</body>')
            if body_end > 0:
                insert_pos = body_end
        
        if insert_pos == -1:
            print(f"❌ {filepath.name} 找不到合適的 FAQ 插入位置")
            return False
        
        # 插入 FAQ
        new_content = content[:insert_pos] + '\n' + faq_html + '\n' + content[insert_pos:]
        
        # 寫回檔案
        filepath.write_text(new_content, encoding='utf-8')
        print(f"✅ {filepath.name} 已補充 FAQ ({current_count}->{len(selected)})")
        return True
        
    except Exception as e:
        print(f"❌ {filepath.name} 處理失敗: {e}")
        return False

def main():
    print("=" * 60)
    print("P2-2 修復：補充 FAQ 數量")
    print("=" * 60)
    
    # 讀取檢查結果
    try:
        with open(WORK_DIR / 'p2_check_result.json', 'r', encoding='utf-8') as f:
            result = json.load(f)
        faq_issues = result['faq_issues']
    except:
        print("❌ 無法讀取檢查結果，使用預設列表")
        faq_issues = [
            ['bangkok-3days.html', 0, 4],
            ['busan-capsule.html', 0, 4],
            ['chiang-mai.html', 0, 4],
            ['esim-comparison.html', 0, 4],
            ['hokkaido-winter.html', 0, 4],
            ['hualien-taitung.html', 0, 4],
            ['jeju-island.html', 0, 4],
            ['kansai-pass.html', 0, 4],
            ['kenting.html', 0, 4],
            ['korea-budget-travel-guide.html', 0, 4],
            ['korea-travel.html', 0, 4],
            ['kyoto-temples.html', 0, 4],
            ['okinawa.html', 0, 4],
            ['osaka-food.html', 0, 4],
            ['seasia-budget-travel-guide.html', 0, 4],
            ['seoul-food.html', 0, 4],
            ['southeast-asia.html', 0, 4],
            ['tainan-food.html', 0, 6],
            ['taiwan-travel-guide.html', 0, 4],
            ['taiwan-travel.html', 0, 4],
            ['tokyo-5days.html', 0, 4],
        ]
    
    fixed = 0
    skipped = 0
    
    for filename, current, target in faq_issues:
        filepath = WORK_DIR / filename
        if not filepath.exists():
            print(f"⚠️  {filename} 不存在，跳過")
            skipped += 1
            continue
        
        if fix_article_faq(filepath, target):
            fixed += 1
        else:
            skipped += 1
    
    print("\n" + "=" * 60)
    print(f"修復完成：{fixed} 篇成功，{skipped} 篇跳過")
    print("=" * 60)

if __name__ == '__main__':
    main()
