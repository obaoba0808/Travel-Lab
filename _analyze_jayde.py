#!/usr/bin/env python3
"""
分析 Jayde 目錄提交表單結構
嘗試找到提交表單的 URL 和欄位
"""

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.jayde.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

try:
    response = requests.get(url, headers=headers, timeout=10)
    print(f'HTTP Status: {response.status_code}')
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 尋找提交表單或連結
        forms = soup.find_all('form')
        links = soup.find_all('a', string=lambda text: text and ('submit' in text.lower() or 'add' in text.lower() or 'suggest' in text.lower() or 'submit url' in text.lower()))
        
        print(f'\n找到 {len(forms)} 個表單')
        for i, form in enumerate(forms[:3], 1):
            print(f'\n表單 {i}:')
            print(f'  action: {form.get("action", "N/A")}')
            print(f'  method: {form.get("method", "N/A")}')
            inputs = form.find_all(['input', 'textarea', 'select'])
            print(f'  欄位數: {len(inputs)}')
            for inp in inputs[:5]:
                print(f'    - {inp.get("name", inp.get("id", "N/A"))}: {inp.get("type", inp.name)}')
        
        print(f'\n找到 {len(links)} 個相關連結')
        for i, link in enumerate(links[:5], 1):
            href = link.get('href')
            text = link.text.strip()
            print(f'{i}. {href} - {text}')
        
        # 嘗試找到 "Submit URL" 或 "Add URL" 連結
        submit_links = soup.find_all('a', href=True, string=re.compile(r'submit|add.*url|suggest', re.I))
        if submit_links:
            print(f'\n*** 找到提交連結:')
            for link in submit_links[:3]:
                print(f'  {link.get("href")} - {link.text.strip()}')
        
except Exception as e:
    print(f'錯誤: {e}')
