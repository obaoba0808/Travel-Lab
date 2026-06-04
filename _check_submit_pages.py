#!/usr/bin/env python3
"""
檢查可訪問的目錄網站是否有「提交網址」頁面
"""

import requests
from bs4 import BeautifulSoup
import re

# 從測試結果中取得可訪問的目錄
accessible_directories = [
    "https://www.jayde.com/submit.html",
    "https://curlie.org/",
    "https://www.traveldirectory.com/",
    "https://www.worldtravelguide.net/",
    "https://directoryvault.com/",
    "https://www.avivadirectory.com/"
]

print('[CHECK] 檢查目錄網站的提交頁面...')
print('=' * 70)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

results = []

for i, url in enumerate(accessible_directories, 1):
    print(f'\n[{i}/{len(accessible_directories)}] 檢查: {url[:60]}...')
    
    try:
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        final_url = response.url
        
        if response.status_code != 200:
            print(f'  [WARN] HTTP {response.status_code}')
            continue
        
        # 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text().lower()
        
        # 檢查是否有「提交」相關關鍵字
        submit_keywords = [
            'submit', 'add url', 'add site', 'suggest', 'submit url',
            'add link', 'submit site', 'directory submission',
            '提交', '登錄', '加入', '建議'
        ]
        
        has_submit = any(keyword in page_text for keyword in submit_keywords)
        
        # 尋找「提交」相關連結
        submit_links = []
        for link in soup.find_all('a', href=True):
            link_text = link.get_text().lower()
            link_href = link['href']
            
            if any(keyword in link_text or keyword in link_href.lower() for keyword in submit_keywords):
                full_url = link_href if link_href.startswith('http') else final_url.rstrip('/') + '/' + link_href.lstrip('/')
                submit_links.append({
                    'text': link.get_text().strip()[:50],
                    'url': full_url
                })
        
        # 輸出結果
        if has_submit or submit_links:
            print(f'  [OK] 找到提交功能')
            result = {
                'url': url,
                'final_url': final_url,
                'has_submit': True,
                'submit_links': submit_links[:5]  # 只保留前 5 個
            }
            results.append(result)
            
            if submit_links:
                print(f'    找到 {len(submit_links)} 個提交連結:')
                for link in submit_links[:3]:
                    print(f'      - {link["text"]}: {link["url"][:80]}')
        else:
            print(f'  [WARN] 未找到提交功能')
            result = {
                'url': url,
                'final_url': final_url,
                'has_submit': False,
                'submit_links': []
            }
            results.append(result)
    
    except Exception as e:
        print(f'  [FAIL] 錯誤: {e}')
        results.append({
            'url': url,
            'error': str(e)
        })

# 輸出總結
print('\n' + '=' * 70)
print('[結果總結]')
print('=' * 70)

valid_directories = [r for r in results if r.get('has_submit')]
print(f'\n✅ 有提交功能的目錄 ({len(valid_directories)} 個):')
for r in valid_directories:
    print(f'  • {r["url"]}')
    if r.get('submit_links'):
        print(f'    → 提交頁面: {r["submit_links"][0]["url"][:80]}')

if len(valid_directories) < len(results):
    print(f'\n⚠️  無提交功能的目錄 ({len(results) - len(valid_directories)} 個):')
    for r in results:
        if not r.get('has_submit'):
            print(f'  • {r["url"]}')

# 儲存結果
import json
output_file = 'valid_directories.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f'\n[輸出] 結果已儲存到: {output_file}')
print('\n[下一步]')
print('1. 檢查 valid_directories.json 中的提交頁面')
print('2. 準備提交資料（網站標題、描述、Email 等）')
print('3. 嘗試自動化提交（如果遇到 CAPTCHA 則改為手動）')
