#!/usr/bin/env python3
"""
分析 Jayde 提交頁面的表單結構
檢查是否有 CAPTCHA，並嘗試自動化提交
"""

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.jayde.com/submit.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

try:
    response = requests.get(url, headers=headers, timeout=10)
    print(f'HTTP Status: {response.status_code}')
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 尋找所有表單
        forms = soup.find_all('form')
        print(f'\n找到 {len(forms)} 個表單')
        
        for i, form in enumerate(forms, 1):
            print(f'\n表單 {i}:')
            print(f'  action: {form.get("action", "N/A")}')
            print(f'  method: {form.get("method", "N/A")}')
            
            # 找出所有輸入欄位
            inputs = form.find_all(['input', 'textarea', 'select'])
            print(f'  欄位數: {len(inputs)}')
            
            for inp in inputs:
                name = inp.get('name', inp.get('id', 'N/A'))
                inp_type = inp.get('type', inp.name)
                required = inp.get('required', False)
                print(f'    - {name}: {inp_type}' + (' [必填]' if required else ''))
            
            # 檢查是否有 CAPTCHA
            page_text = soup.get_text().lower()
            if 'captcha' in page_text or form.find('img', alt=lambda x: x and 'captcha' in x.lower()):
                print(f'  ⚠️  發現 CAPTCHA!')
            else:
                print(f'  ✅ 無 CAPTCHA')
        
        # 尋找提交按鈕
        submit_buttons = soup.find_all(['input', 'button'], {'type': 'submit'})
        if submit_buttons:
            print(f'\n找到 {len(submit_buttons)} 個提交按鈕:')
            for btn in submit_buttons[:3]:
                print(f'  - {btn.get("value", btn.text.strip()[:20])}')
        
except Exception as e:
    print(f'錯誤: {e}')
