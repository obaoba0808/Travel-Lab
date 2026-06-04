#!/usr/bin/env python3
"""
自動提交到 Jayde 目錄
嘗試自動填寫並提交表單
"""

import requests
from bs4 import BeautifulSoup
import time

# 提交頁面 URL
submit_url = 'https://www.jayde.com/submit.html'

# 網站資訊
website_data = {
    'title': '均在路上 Travel Lab',
    'url': 'https://golightly.fun',
    'description': '實戰旅遊攻略：日本、韓國、台灣、東南亞自由行指南，附 PDF 下載。',
    'category': 'Travel/Asia_Travel',
    'email': 'travel.lab@golightly.fun',
    'keywords': '旅遊攻略, 自由行, 日本旅遊, 韓國旅遊'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}

print('[AUTO] 開始自動提交到 Jayde...')
print('=' * 70)

try:
    # 步驟 1: 取得提交頁面
    print('\n[STEP 1] 取得提交頁面...')
    response = requests.get(submit_url, headers=headers, timeout=10)
    
    if response.status_code != 200:
        print(f'[錯誤] 無法取得頁面，HTTP {response.status_code}')
        exit(1)
    
    print(f'[成功] 頁面取得成功 (HTTP {response.status_code})')
    
    # 步驟 2: 分析表單結構
    print('\n[STEP 2] 分析表單結構...')
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    
    if not forms:
        print('[錯誤] 找不到表單')
        exit(1)
    
    # 使用第一個表單（通常是提交表單）
    form = forms[0]
    form_action = form.get('action', submit_url)
    form_method = form.get('method', 'post').lower()
    
    print(f'表單 action: {form_action}')
    print(f'表單 method: {form_method}')
    
    # 找出所有輸入欄位
    inputs = form.find_all(['input', 'textarea', 'select'])
    print(f'找到 {len(inputs)} 個欄位')
    
    # 準備提交資料
    form_data = {}
    
    for inp in inputs:
        name = inp.get('name', '')
        if not name:
            continue
        
        # 根據欄位名稱推測內容
        name_lower = name.lower()
        
        if 'title' in name_lower or 'name' in name_lower or 'site' in name_lower:
            form_data[name] = website_data['title']
        elif 'url' in name_lower or 'link' in name_lower or 'website' in name_lower:
            form_data[name] = website_data['url']
        elif 'desc' in name_lower or 'about' in name_lower or 'summary' in name_lower:
            form_data[name] = website_data['description']
        elif 'email' in name_lower or 'contact' in name_lower:
            form_data[name] = website_data['email']
        elif 'keyword' in name_lower or 'tag' in name_lower:
            form_data[name] = website_data['keywords']
        elif 'category' in name_lower:
            form_data[name] = website_data['category']
        elif inp.get('type') == 'submit' or inp.get('type') == 'button':
            # 跳過提交按鈕
            continue
        else:
            # 其他欄位留空或設為預設值
            if inp.name == 'input':
                form_data[name] = ''
    
    print('\n[表單資料]')
    for key, value in form_data.items():
        print(f'  {key}: {value[:50] if len(str(value)) > 50 else value}')
    
    # 步驟 3: 檢查是否有 CAPTCHA
    print('\n[STEP 3] 檢查 CAPTCHA...')
    page_text = response.text.lower()
    
    has_captcha = False
    if 'captcha' in page_text:
        has_captcha = True
        print('[警告] 發現 CAPTCHA！無法自動提交')
    else:
        print('[OK] 無 CAPTCHA，可以嘗試自動提交')
    
    if has_captcha:
        print('\n[結果] 需要手動提交')
        print('請開啟: https://www.jayde.com/submit.html')
        print('並手動填寫表單')
        exit(0)
    
    # 步驟 4: 提交表單
    print('\n[STEP 4] 提交表單...')
    
    # 確定提交 URL
    if form_action and form_action != '#' and not form_action.startswith('http'):
        submit_action_url = submit_url + '/' + form_action if not form_action.startswith('/') else submit_url[:submit_url.rfind('/')] + form_action
    elif form_action and form_action.startswith('http'):
        submit_action_url = form_action
    else:
        submit_action_url = submit_url
    
    print(f'提交到: {submit_action_url}')
    print(f'方法: {form_method}')
    
    # 發送請求
    if form_method == 'post':
        submit_response = requests.post(submit_action_url, data=form_data, headers=headers, timeout=10)
    else:
        submit_response = requests.get(submit_action_url, params=form_data, headers=headers, timeout=10)
    
    print(f'\n[結果] HTTP {submit_response.status_code}')
    
    if submit_response.status_code == 200:
        response_text = submit_response.text.lower()
        
        # 檢查是否成功
        success_keywords = ['success', 'thank', 'submitted', 'received', 'approved']
        error_keywords = ['error', 'invalid', 'failed', 'captcha', 'spam']
        
        is_success = any(keyword in response_text for keyword in success_keywords)
        is_error = any(keyword in response_text for keyword in error_keywords)
        
        if is_success and not is_error:
            print('[成功] 提交成功！')
            print('\n[注意] 大多數目錄需要人工審核，請耐心等待 1-4 週')
        elif is_error:
            print('[失敗] 提交失敗，可能被檢測為垃圾郵件或需要 CAPTCHA')
            print('建議手動提交')
        else:
            print('[不確定] 無法確認提交狀態，請手動檢查')
            print('回應長度: ' + str(len(submit_response.text)) + ' 字元')
    else:
        print('[失敗] 提交失敗，HTTP ' + str(submit_response.status_code))
    
except Exception as e:
    print(f'\n[錯誤] {e}')
    print('\n[建議] 請手動提交到: https://www.jayde.com/submit.html')

print('\n' + '=' * 70)
print('[完成] Jayde 自動提交嘗試完成')
