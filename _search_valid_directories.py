#!/usr/bin/env python3
"""
搜尋並驗證有效的旅遊目錄網站
取代之前失效的 8 個目錄
"""

import requests
import json
import time
from datetime import datetime

# 候選目錄清單（經過篩選，可能有效的網站）
candidates = [
    # 一般網站目錄（可能包含旅遊分類）
    {"name": "Astronomy Directory", "url": "https://www.astronomy-directory.com/", "type": "general", "difficulty": "medium"},
    {"name": "Directory Journal", "url": "https://www.directoryjournal.com/", "type": "general", "difficulty": "medium"},
    {"name": "Jayde", "url": "https://www.jayde.com/", "type": "general", "difficulty": "easy"},
    {"name": "Gimpsy", "url": "https://www.gimpsy.com/", "type": "general", "difficulty": "easy"},
    {"name": "Scrub The Web", "url": "https://www.scrubtheweb.com/", "type": "general", "difficulty": "easy"},
    {"name": "Site Promotion", "url": "https://www.sitepromotion.com/", "type": "seo", "difficulty": "medium"},
    {"name": "Marketing Internet Directory", "url": "https://www.marketinginternetdirectory.com/", "type": "marketing", "difficulty": "medium"},
    {"name": "Text Link Directory", "url": "https://www.textlinkdirectory.com/", "type": "seo", "difficulty": "easy"},
    {"name": "Directory Critic", "url": "https://www.directorycritic.com/", "type": "general", "difficulty": "medium"},
    {"name": "Free Directory", "url": "https://www.freedirectory.com/", "type": "general", "difficulty": "easy"},
    
    # 旅遊相關目錄
    {"name": "Travel Comm", "url": "https://www.travelcomm.net/", "type": "travel", "difficulty": "medium"},
    {"name": "Tourism Directory", "url": "https://www.tourismdirectory.com/", "type": "travel", "difficulty": "hard"},
    {"name": "World Travel Guide", "url": "https://www.worldtravelguide.net/", "type": "travel", "difficulty": "hard"},
    {"name": "Travel and Tourism", "url": "https://www.travel-and-tourism.net/", "type": "travel", "difficulty": "medium"},
    {"name": "Asia Travel", "url": "https://www.asiatravel.com/", "type": "travel", "difficulty": "medium"},
]

print("[SEARCH] 開始搜尋有效的旅遊目錄網站...")
print("=" * 70)

valid_directories = []

for i, candidate in enumerate(candidates, 1):
    name = candidate['name']
    url = candidate['url']
    diff = candidate['difficulty']
    dtype = candidate['type']
    
    print(f"\n[{i}/{len(candidates)}] 檢查: {name}")
    print(f"  URL: {url}")
    
    try:
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        if response.status_code == 200:
            print(f"  [成功] HTTP {response.status_code} - 網站可訪問")
            candidate['status'] = 'valid'
            candidate['http_status'] = response.status_code
            valid_directories.append(candidate)
        else:
            print(f"  [警告] HTTP {response.status_code} - 網站回應異常")
            
    except Exception as e:
        print(f"  [錯誤] {e}")
    
    time.sleep(0.5)  # 避免請求過快

# 產生報告
print("\n" + "=" * 70)
print(f"[報告] 找到 {len(valid)} 個有效目錄")
print("=" * 70)

if valid_directories:
    print("\n有效目錄清單：")
    for i, d in enumerate(valid_directories, 1):
        print(f"{i}. {d['name']} ({d['type']}, {d['difficulty']})")
        print(f"   URL: {d['url']}")
    
    # 儲存到 JSON
    output_file = 'valid_directories_found.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'found_count': len(valid_directories),
            'found_at': datetime.now().isoformat(),
            'directories': valid_directories
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n[完成] 結果已儲存到: {output_file}")
    
    # 顯示後續步驟
    print("\n" + "=" * 70)
    print("[下一步] 如何將這些目錄加入提交清單：")
    print("=" * 70)
    print("1. 開啟 valid_directories_found.json")
    print("2. 複製 'directories' 陣列內容")
    print("3. 貼到 directory_submission_data.json 的 'directories' 陣列")
    print("4. 移除失效的 8 個目錄")
    print("5. 重新執行 _auto_submit_directories.py")
    
else:
    print("\n[警告] 未找到任何有效目錄，建議改用社群媒體外鏈策略")

print("\n[提示] 如果需要更多目錄，可以：")
print("  - 搜尋 'travel directory submit' 或 'free web directory'")
print("  - 嘗試旅遊論壇或部落格的友情連結交換")
print("  - 改用社群媒體（Reddit, Plurk, PTT）分享內容")
