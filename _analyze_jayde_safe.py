#!/usr/bin/env python3
"""
分析 Jayde 提交頁面的表單結構（純文字輸出，避免編碼錯誤）
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.jayde.com/submit.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

try:
    response = requests.get(url, headers=headers, timeout=10)
    print('HTTP Status: ' + str(response.status_code))
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 尋找所有表單
        forms = soup.find_all('form')
        print('\n找到 ' + str(len(forms)) + ' 個表單')
        
        for i, form in enumerate(forms, 1):
            print('\n表單 ' + str(i) + ':')
            print('  action: ' + str(form.get('action', 'N/A')))
            print('  method: ' + str(form.get('method', 'N/A')))
            
            # 找出所有輸入欄位
            inputs = form.find_all(['input', 'textarea', 'select'])
            print('  欄位數: ' + str(len(inputs)))
            
            for inp in inputs:
                name = inp.get('name', inp.get('id', 'N/A'))
                inp_type = inp.get('type', inp.name)
                required = inp.get('required', False)
                req_text = ' [必填]' if required else ''
                print('    - ' + str(name) + ': ' + str(inp_type) + req_text)
            
            # 檢查是否有 CAPTCHA
            page_text = soup.get_text().lower()
            if 'captcha' in page_text:
                print('  [警告] 發現 CAPTCHA!')
            else:
                print('  [OK] 無 CAPTCHA')
        
        # 尋找提交按鈕
        submit_buttons = soup.find_all(['input', 'button'], {'type': 'submit'})
        if submit_buttons:
            print('\n找到 ' + str(len(submit_buttons)) + ' 個提交按鈕:')
            for btn in submit_buttons[:3]:
                print('  - ' + str(btn.get('value', btn.text.strip()[:20])))
        
except Exception as e:
    print('錯誤: ' + str(e))
