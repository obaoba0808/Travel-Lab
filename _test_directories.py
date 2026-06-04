#!/usr/bin/env python3
"""
測試已知的旅遊目錄網站是否仍然存在
"""

import requests
import time
from datetime import datetime

# 已知的旅遊目錄網站清單
travel_directories = [
    # 通用網站目錄（包含旅遊分類）
    "https://www.jayde.com/submit.html",
    "https://www.dmoz.org/",  # 已關站，但 Curlie 是繼承者
    "https://curlie.org/",
    "https://www.botw.org/",
    
    # 旅遊專門目錄
    "https://www.traveldirectory.com/",
    "https://www.worldtravelguide.net/",
    "https://www.tripadvisor.com/",  # 雖然是評論網站，但也是目錄
    
    # 免費目錄提交
    "https://www.free-web-directory.com/",
    "https://www.all-free-directories.com/",
    "https://www.directoryvault.com/",
    
    # 地區性旅遊目錄
    "https://www.asiatravel.com/",
    "https://www.tourism-of-asia.com/",
    
    # SEO 目錄（接受旅遊網站）
    "https://www.best-of-the-web.com/",
    "https://www.highrankings.com/",
    "https://www.avivadirectory.com/",
    
    # 新興目錄
    "https://www.insanelycool.com/",
    "https://www.topsites.net/",
    "https://www.top100sites.com/",
]

print('[TEST] 測試旅遊目錄網站可訪問性...')
print('=' * 70)

results = {
    'accessible': [],
    'broken': [],
    'timeout': [],
    'error': []
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for i, url in enumerate(travel_directories, 1):
    print(f'\n[{i}/{len(travel_directories)}] 測試: {url[:60]}...')
    
    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10,
            allow_redirects=True
        )
        
        if response.status_code == 200:
            print(f'  [OK] 可訪問 (HTTP {response.status_code})')
            results['accessible'].append({
                'url': url,
                'status': response.status_code,
                'final_url': response.url
            })
        else:
            print(f'  [WARN] HTTP {response.status_code}')
            results['broken'].append({
                'url': url,
                'status': response.status_code
            })
    
    except requests.exceptions.Timeout:
        print(f'  [FAIL] 連線超時')
        results['timeout'].append({'url': url})
    except requests.exceptions.ConnectionError:
        print(f'  [FAIL] 連線錯誤')
        results['error'].append({'url': url, 'error': 'ConnectionError'})
    except Exception as e:
        print(f'  [FAIL] 錯誤: {type(e).__name__}')
        results['error'].append({'url': url, 'error': str(e)})
    
    time.sleep(0.5)

# 輸出結果
print('\n' + '=' * 70)
print('[結果總結]')
print('=' * 70)

print(f'\n[OK] 可訪問 ({len(results["accessible"])} 個):')
for item in results['accessible']:
    print(f'  • {item["url"]}')
    if item['url'] != item['final_url']:
        print(f'    -> 重定向到: {item["final_url"]}')

if results['broken']:
    print(f'\n[WARN] HTTP 錯誤 ({len(results["broken"])} 個):')
    for item in results['broken']:
        print(f'  • {item["url"]} (HTTP {item["status"]})')

if results['timeout']:
    print(f'\n[FAIL] 連線超時 ({len(results["timeout"])} 個):')
    for item in results['timeout']:
        print(f'  • {item["url"]}')

if results['error']:
    print(f'\n[FAIL] 其他錯誤 ({len(results["error"])} 個):')
    for item in results['error']:
        print(f'  • {item["url"]}: {item["error"]}')

# 儲存結果
import json
output_file = 'directory_test_results.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f'\n[輸出] 結果已儲存到: {output_file}')
print('\n[下一步]')
print('1. 檢查可訪問的目錄網站')
print('2. 準備提交資料（如果網站接受免費提交）')
print('3. 執行自動化提交（如果遇到 CAPTCHA 則改為手動）')
