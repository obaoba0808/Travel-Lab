#!/usr/bin/env python3
"""
P2-3 修復：去除重複內容
根據檢查結果，修復重複的段落
"""

import re
import json
from pathlib import Path

WORK_DIR = Path("C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab")

def read_file_safe(filepath):
    """安全讀取檔案"""
    try:
        return filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"❌ 讀取失敗 {filepath.name}: {e}")
        return None

def write_file_safe(filepath, content):
    """安全寫入檔案"""
    try:
        filepath.write_text(content, encoding='utf-8')
        return True
    except Exception as e:
        print(f"❌ 寫入失敗 {filepath.name}: {e}")
        return False

def fix_transportation_duplicates():
    """修復交通攻略重複（tokyo-5days.html 和 kansai-pass.html）"""
    print("\n" + "=" * 60)
    print("修復交通攻略重複")
    print("=" * 60)
    
    # 讀取檢查結果
    try:
        with open(WORK_DIR / 'p2_duplicate_check.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        transport_dups = [d for d in data['duplicates'] 
                         if d['file1'] in ['tokyo-5days.html', 'kansai-pass.html'] 
                         or d['file2'] in ['tokyo-5days.html', 'kansai-pass.html']]
    except:
        print("⚠️  無法讀取檢查結果，使用預設值")
        transport_dups = []
    
    # 定義替換內容（為每篇文章準備獨特的版本）
    replacements = {
        'tokyo-5days.html': {
            '建議購買JR Pass（全國版或地區版），新幹線自由席比指定席便宜。市內交通用地鐵一日券（Tokyo Subway Ticket、Osaka Amazing Pass）。巴士比地鐵便宜，但較慢。': 
            '東京地鐵一日券（Tokyo Subway Ticket）24小時券僅₹800，比單程票便宜。JR Pass如計劃去多個城市才划算，單在東京使用的話不推薦。巴士（Toei Bus）僅₹210/次，適合短距離移動。',
            
            '入浴前要先沖洗碗體。毛巾不可放入浴池，可放在頭上或旁邊。有刺青者可能被拒絕入場（可找允許刺青的溫泉或用貼布遮蓋）。':
            '東京有超過30家溫泉設施，推薦「大江戶溫泉物語」和「兩國湯屋」。部分溫泉允許刺青（需遮蓋），但大多數傳統溫泉仍禁止。入浴前務必先沖洗。',
            
            '推薦購買當地SIM卡（成田、羽田機場都有賣），價格約¥2,000-3,000/5天。WiFi機訊號穩但需歸還，適合多人分攤。Free WiFi熱點越來越多，但覆蓋率仍不足。':
            '成田機場和羽田機場都有SIM卡自動販賣機，推薦購買SoftBank或NTT Docomo的卡。也可在便利商店（7-11、Lawson）購買預付SIM。WiFi機適合3人以上分攤，每日約¥500。'
        },
        'kansai-pass.html': {
            '建議購買JR Pass（全國版或地區版），新幹線自由席比指定席便宜。市內交通用地鐵一日券（Tokyo Subway Ticket、Osaka Amazing Pass）。巴士比地鐵便宜，但較慢。':
            '關西地區推薦購買ICOCA卡（可搭地鐵、JR、私鐵）或關西周遊券（KTP）。KTP分為1日（₹2,800）、2日（₹4,600）、3日（₹5,800），適合遊覽大阪、京都、奈良。',
            
            '入浴前要先沖洗碗體。毛巾不可放入浴池，可放在頭上或旁邊。有刺青者可能被拒絕入場（可找允許刺青的溫泉或用貼布遮蓋）。':
            '關西有悠久的溫泉文化，推薦「有馬溫泉」（神戶）、「城崎溫泉」（豐岡）。部分溫泉有「刺青OK」的時段或專用浴池。入浴前先沖洗，毛巾不可放入浴池。',
            
            '推薦購買當地SIM卡（成田、羽田機場都有賣），價格約¥2,000-3,000/5天。WiFi機訊號穩但需歸還，適合多人分攤。Free WiFi熱點越來越多，但覆蓋率仍不足。':
            '關西機場（KIX）有SIM卡販賣機，推薦購買「日本手機」或「SoftBank」的卡。也可在關西機場的租借服務台租借WiFi機，每日約¥700。大阪市內Free WiFi覆蓋率高。'
        }
    }
    
    fixed = 0
    for filename, repl_dict in replacements.items():
        filepath = WORK_DIR / filename
        content = read_file_safe(filepath)
        
        if not content:
            continue
        
        modified = False
        for old_text, new_text in repl_dict.items():
            if old_text in content:
                content = content.replace(old_text, new_text)
                modified = True
                print(f"✅ {filename}: 已替換重複段落")
        
        if modified:
            if write_file_safe(filepath, content):
                fixed += 1
    
    print(f"\n✅ 交通攻略重複修復完成：{fixed} 篇")
    return fixed

def fix_convenience_store_duplicates():
    """修復便利店推薦重複"""
    print("\n" + "=" * 60)
    print("修復便利店推薦重複")
    print("=" * 60)
    
    # 為每篇文章準備獨特的便利店推薦內容
    convenience_content = {
        'bangkok-3days.html': '泰國7-11有獨特的泰式奶茶、烤香蕉、便當。推薦試試「CP Meal」的泰式打拋豬飯（₿45）。FamilyMart的炸雞（₿25）和霜淇淋（₿19）也超值。便利商店是泰國旅行的救星！',
        'chiang-mai.html': '清邁的7-11比曼谷少，但古城區仍有幾家。推薦買「Thai-Danish」餅乾當伴手禮（₿89）。便利商店的椰子水（₿25）超解渴，比觀光區便宜一半。',
        'seasia-budget-travel-guide.html': '東南亞各國便利商店特色不同：泰國7-11有獨特泰式奶茶；越南有Circle K賣越式法包；新加坡7-11價格較高但有獨特商品；馬來西亞7-11有清真認證食品。',
        'southeast-asia.html': '東南亞便利商店是背包客的好朋友！泰國7-11密度極高，商品多樣；越南Circle K有便宜的越式法包；新加坡7-11價格較高但有特色商品；馬來西亞有清真認證選擇。',
        'japan-travel.html': '日本便利商店（7-11、FamilyMart、Lawson）是旅遊亮點！7-11的飯糰、FamilyMart的炸雞、Lawson的霜淇淋都必吃。還有各式便當、沙拉、甜點，品質不輸餐廳。',
        'korea-travel.html': '韓國便利商店（CU、GS25、7-11 Korea）有獨特商品：三角飯糰（₩1,200）、泡麵（₩1,500）、香蕉牛奶（₩1,500）。推荐試試「CU」的麻藥便當（₩4,500），CP值超高。',
        'taiwan-travel.html': '台灣便利商店（7-11、全家、萊爾富）是生活中心的。推薦7-11的「御飯糰」、全家的「關東煮」、萊爾富的「大亨堡」。還可以繳費、寄件、買票，超方便。',
        'hokkaido-winter.html': '北海道7-11有當地限定商品：北海道牛奶（¥198）、北海道薯條（¥248）、白色戀人餅乾。在寒冷天氣裡，便利商店的熱咖啡和關東煮（¥350）是救星。',
        'okinawa.html': '沖繩7-11有獨特的「沖繩紅豆餅乾」、「海鹽冰淇淋」和「苦瓜炒肉便當」。推薦試試當地限定的「沖繩可樂」（¥160），味道很特別。便利商店也是補給防曬用品的好地方。',
    }
    
    fixed = 0
    
    for filename, new_content in convenience_content.items():
        filepath = WORK_DIR / filename
        content = read_file_safe(filepath)
        
        if not content:
            continue
        
        # 找出舊的便利店段落並替換
        old_pattern = r'推薦在台灣買好當地eSIM（Airalo、Nomad），或購買當地SIM卡（7-11、全家都有賣）。WiFi機多人分攬較划算，但需歸還。Free WiFi覆蓋率城市較高，鄉村較差。'
        
        if re.search(old_pattern, content):
            content = re.sub(old_pattern, new_content, content)
            if write_file_safe(filepath, content):
                print(f"✅ {filename}: 已替換便利店推薦段落")
                fixed += 1
        else:
            print(f"⚠️  {filename}: 未找到重複段落")
    
    print(f"\n✅ 便利店推薦重複修復完成：{fixed} 篇")
    return fixed

def main():
    print("=" * 60)
    print("P2-3 修復：去除重複內容")
    print("=" * 60)
    
    fixed_transport = fix_transportation_duplicates()
    fixed_convenience = fix_convenience_store_duplicates()
    
    total_fixed = fixed_transport + fixed_convenience
    
    print("\n" + "=" * 60)
    print(f"修復完成：共 {total_fixed} 處重複內容")
    print("=" * 60)
    
    return total_fixed

if __name__ == '__main__':
    main()
