#!/usr/bin/env python3
"""
重新分析 Jayde 提交頁面
找到正確的「提交網站」表單（而非搜尋表單）
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
        
        # 分析每個表單，找到「提交網站」的那個
        for i, form in enumerate(forms, 1):
            print('\n' + '=' * 70)
            print('表單 ' + str(i) + ':')
            print('  action: ' + str(form.get('action', 'N/A')))
            print('  method: ' + str(form.get('method', 'N/A')))
            
            # 找出所有輸入欄位
            inputs = form.find_all(['input', 'textarea', 'select'])
            print('  欄位數: ' + str(len(inputs)))
            
            # 列出所有欄位名稱
            field_names = []
            for inp in inputs:
                name = inp.get('name', inp.get('id', ''))
                if name:
                    field_names.append(name)
            
            if field_names:
                print('  欄位清單: ' + ', '.join(field_names))
            
            # 檢查是否包含「提交網站」的關鍵欄位
            has_url = any('url' in name.lower() or 'link' in name.lower() or 'site' in name.lower() for name in field_names)
            has_title = any('title' in name.lower() or 'name' in name.lower() for name in field_names)
            
            if has_url:
                print('  [可能的提交表單] 包含 URL 欄位')
            if has_title:
                print('  [可能的提交表單] 包含 Title 欄位')
            
            # 顯示前 5 個欄位的詳細資訊
            print('\n  前 5 個欄位:')
            for j, inp in enumerate(inputs[:5], 1):
                name = inp.get('name', inp.get('id', 'N/A'))
                inp_type = inp.get('type', inp.name)
                print(f'    {j}. {name}: {inp_type}')
        
        # 嘗試找到「Submit Your Site」的連結或按鈕
        print('\n' + '=' * 70)
        print('尋找「Submit Your Site」連結...')
        
        submit_links = soup.find_all('a', string=lambda text: text and 'submit' in text.lower())
        if submit_links:
            print(f'找到 {len(submit_links)} 個提交連結:')
            for link in submit_links[:3]:
                print(f'  - {link.get("href")} - {link.text.strip()}')
        
        # 檢查頁面主要內容
        print('\n' + '=' * 70)
        print('頁面主要內容（前 500 字元）:')
        main_content = soup.get_text(separator=' ', strip=True)[:500]
        print(main_content)
        
except Exception as e:
    print('錯誤: ' + str(e))
