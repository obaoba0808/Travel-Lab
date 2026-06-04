#!/usr/bin/env python3
"""
目錄網站自動提交腳本
自動化提交 golightly.fun 到旅遊相關目錄網站
"""

import json
import time
import requests
from datetime import datetime

# 讀取提交資料
with open('directory_submission_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

website = data['website']
directories = data['directories']
tracking = data['submission_tracking']

# 模擬提交函數（實際需要根據每個網站的表單結構調整）
def submit_to_directory(directory):
    """
    嘗試自動提交到目錄網站
    注意：大多數網站有 CAPTCHA，此腳本僅供參考
    """
    name = directory['name']
    url = directory['url']
    diff = directory['difficulty']
    
    print(f"\n[處理] {name} ({diff})")
    print(f"  URL: {url}")
    
    # 模擬送出 POST 請求（實際需要分析每個網站的表單）
    # 大多數免費目錄需要：
    # 1. 網站名稱
    # 2. 網站 URL
    # 3. 描述（短/中/長）
    # 4. 分類
    # 5. Email
    # 6. CAPTCHA 驗證
    
    try:
        # 嘗試 GET 請求檢查網站是否存在
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        if response.status_code == 200:
            print(f"  [成功] 網站可訪問 (HTTP {response.status_code})")
            print(f"  [資訊] 需要手動提交（大多數目錄有 CAPTCHA）")
            
            # 記錄到 pending
            tracking['pending'].append({
                'directory': name,
                'url': url,
                'date': datetime.now().isoformat(),
                'status': 'needs_manual_submission'
            })
            
            return 'pending'
        else:
            print(f"  [警告] 網站回應異常 (HTTP {response.status_code})")
            tracking['rejected'].append({
                'directory': name,
                'url': url,
                'date': datetime.now().isoformat(),
                'reason': f'HTTP {response.status_code}'
            })
            return 'rejected'
            
    except Exception as e:
        print(f"  [錯誤] {e}")
        tracking['rejected'].append({
            'directory': name,
            'url': url,
            'date': datetime.now().isoformat(),
            'reason': str(e)
        })
        return 'rejected'

# 主程式
def main():
    print("=" * 70)
    print("目錄網站自動提交工具")
    print("網站: golightly.fun")
    print("=" * 70)
    
    print("\n[資訊] 由於 CAPTCHA 限制，此腳本僅檢查網站可訪問性")
    print("[資訊] 實際提交需要手動完成或使用瀏覽器自動化工具\n")
    
    for directory in directories:
        result = submit_to_directory(directory)
        time.sleep(1)  # 避免請求過快
    
    # 更新追蹤資料
    data['submission_tracking'] = tracking
    data['last_update'] = datetime.now().isoformat()
    
    with open('directory_submission_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 產生報告
    print("\n" + "=" * 70)
    print("提交報告")
    print("=" * 70)
    print(f"待處理: {len(tracking['pending'])} 個")
    print(f"已拒絕: {len(tracking['rejected'])} 個")
    print(f"已提交: {len(tracking['submitted'])} 個")
    print(f"已批准: {len(tracking['approved'])} 個")
    
    # 產生手動提交清單
    print("\n" + "=" * 70)
    print("需要手動提交的目錄：")
    print("=" * 70)
    
    for item in tracking['pending']:
        print(f"\n• {item['directory']}")
        print(f"  URL: {item['url']}")
        print(f"  提交資料：")
        print(f"    - 網站名稱: {website['name']}")
        print(f"    - 網站網址: {website['url']}")
        print(f"    - 簡短描述: {website['description_short']}")
        print(f"    - 分類: {website['category']}")
        print(f"    - Email: {website['contact_email']}")
    
    print("\n[完成] 請手動訪問上述網站並完成提交")
    print("[提示] 提交後請編輯 directory_submission_data.json 更新狀態")

if __name__ == '__main__':
    main()
