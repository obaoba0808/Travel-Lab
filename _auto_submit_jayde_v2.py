#!/usr/bin/env python3
"""
自動提交到 Jayde 目錄（正確版本）
針對表單 2（19 個欄位，POST 到 ientry.com）
"""

import requests
from bs4 import BeautifulSoup
import re

# 提交頁面 URL
submit_url = 'https://www.jayde.com/submit.html'

# 網站資訊
website_data = {
    'url': 'https://golightly.fun',
    'title': '均在路上 Travel Lab',
    'description': '實戰旅遊攻略：日本、韓國、台灣、東南亞自由行指南，附 PDF 下載。',
    'email': 'travel.lab@golightly.fun',
    'category': 'Travel/Asia_Travel',
    'keywords': '旅遊攻略, 自由行, 日本旅遊, 韓國旅遊, 台灣旅遊',
    'business_name': '均在路上 Travel Lab',
    'contact_name': 'Travel Lab Team',
    'industry': 'Travel/Asia_Travel'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.jayde.com/submit.html'
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
    
    # 步驟 2: 分析表單結構，找到正確的提交表單
    print('\n[STEP 2] 分析表單結構...')
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    
    # 尋找 POST 方法且欄位數 > 5 的表單（真正的提交表單）
    target_form = None
    for form in forms:
        method = form.get('method', '').lower()
        inputs = form.find_all(['input', 'textarea', 'select'])
        
        if method == 'post' and len(inputs) > 5:
            target_form = form
            break
    
    if not target_form:
        print('[錯誤] 找不到正確的提交表單')
        exit(1)
    
    form_action = target_form.get('action', '')
    form_method = target_form.get('method', 'post').lower()
    
    print(f'找到目標表單:')
    print(f'  action: {form_action}')
    print(f'  method: {form_method}')
    
    # 步驟 3: 準備提交資料
    print('\n[STEP 3] 準備提交資料...')
    
    # 取得所有欄位
    inputs = target_form.find_all(['input', 'textarea', 'select'])
    
    # 建立欄位對應（根據欄位名稱推測）
    form_data = {}
    
    for inp in inputs:
        name = inp.get('name', '')
        if not name:
            continue
        
        inp_type = inp.get('type', inp.name).lower()
        
        # 跳過提交按鈕
        if inp_type == 'submit' or inp_type == 'button':
            continue
        
        # 根據欄位名稱對應資料
        name_lower = name.lower()
        
        if 'url' in name_lower or 'website' in name_lower or 'link' in name_lower:
            form_data[name] = website_data['url']
        elif 'email' in name_lower or 'mail' in name_lower:
            form_data[name] = website_data['email']
        elif 'business' in name_lower or 'company' in name_lower:
            form_data[name] = website_data['business_name']
        elif 'name' in name_lower and 'business' not in name_lower and 'user' not in name_lower:
            # 可能是聯絡人姓名
            form_data[name] = website_data['contact_name']
        elif 'desc' in name_lower or 'about' in name_lower or 'summary' in name_lower or 'detail' in name_lower:
            form_data[name] = website_data['description']
        elif 'industry' in name_lower or 'category' in name_lower or 'type' in name_lower:
            form_data[name] = website_data['category']
        elif 'address' in name_lower:
            form_data[name] = ''  # 留空
        elif 'phone' in name_lower or 'tel' in name_lower:
            form_data[name] = ''  # 留空
        elif 'zip' in name_lower or 'postal' in name_lower:
            form_data[name] = ''  # 留空
        elif 'country' in name_lower:
            form_data[name] = 'Taiwan'
        elif 'state' in name_lower or 'province' in name_lower:
            form_data[name] = ''  # 留空
        elif 'facebook' in name_lower or 'fb' in name_lower:
            form_data[name] = ''  # 留空
        elif 'twitter' in name_lower or 'x' in name_lower:
            form_data[name] = ''  # 留空
        elif 'youtube' in name_lower or 'yt' in name_lower:
            form_data[name] = ''  # 留空
        elif 'logo' in name_lower or 'image' in name_lower:
            form_data[name] = ''  # 留空
        elif 'map' in name_lower or 'gmap' in name_lower:
            form_data[name] = ''  # 留空
        elif 'form_id' in name_lower or 'id' in name_lower:
            # 隱藏欄位，保留原值
            value = inp.get('value', '')
            form_data[name] = value
        else:
            # 其他欄位留空
            form_data[name] = ''
    
    print(f'準備了 {len(form_data)} 個欄位')
    print('\n[表單資料預覽]')
    for key, value in list(form_data.items())[:10]:
        display_value = value[:50] + '...' if len(str(value)) > 50 else value
        print(f'  {key}: {display_value}')
    
    # 步驟 4: 檢查是否有 CAPTCHA
    print('\n[STEP 4] 檢查 CAPTCHA...')
    page_text = response.text.lower()
    
    has_captcha = False
    if 'captcha' in page_text:
        # 檢查是否在表單中
        form_html = str(target_form).lower()
        if 'captcha' in form_html:
            has_captcha = True
            print('[警告] 發現 CAPTCHA！無法自動提交')
    
    if not has_captcha:
        print('[OK] 未發現 CAPTCHA，可以嘗試自動提交')
    
    if has_captcha:
        print('\n[結果] 需要手動提交')
        print('請開啟: https://www.jayde.com/submit.html')
        print('並手動填寫表單')
        exit(0)
    
    # 步驟 5: 提交表單
    print('\n[STEP 5] 提交表單...')
    
    # 確定提交 URL
    if form_action and form_action.startswith('http'):
        submit_action_url = form_action
    elif form_action and form_action.startswith('/'):
        submit_action_url = 'https://www.jayde.com' + form_action
    elif form_action:
        submit_action_url = 'https://www.jayde.com/' + form_action
    else:
        submit_action_url = submit_url
    
    print(f'提交到: {submit_action_url}')
    print(f'方法: {form_method}')
    
    # 發送請求
    try:
        if form_method == 'post':
            submit_response = requests.post(
                submit_action_url,
                data=form_data,
                headers=headers,
                timeout=15,
                allow_redirects=True
            )
        else:
            submit_response = requests.get(
                submit_action_url,
                params=form_data,
                headers=headers,
                timeout=15,
                allow_redirects=True
            )
        
        print(f'\n[結果] HTTP {submit_response.status_code}')
        print(f'最終 URL: {submit_response.url}')
        
        if submit_response.status_code == 200:
            response_text = submit_response.text.lower()
            
            # 檢查是否成功
            success_keywords = ['success', 'thank', 'submitted', 'received', 'approved', 'pending']
            error_keywords = ['error', 'invalid', 'failed', 'captcha', 'spam', 'blocked']
            
            is_success = any(keyword in response_text for keyword in success_keywords)
            is_error = any(keyword in response_text for keyword in error_keywords)
            
            if is_success and not is_error:
                print('\n[成功] 提交成功！')
                print('[注意] 大多數目錄需要人工審核，請耐心等待 1-4 週')
                
                # 更新追蹤檔案
                print('\n[追蹤] 請更新 directory_submission_tracking.md:')
                print('  狀態: submitted')
                print('  日期: ' + '2026-06-04')
                
            elif is_error:
                print('\n[失敗] 提交失敗，可能被檢測為垃圾郵件或需要 CAPTCHA')
                print('建議手動提交')
                
                # 顯示部分回應內容
                soup_response = BeautifulSoup(submit_response.text, 'html.parser')
                error_text = soup_response.get_text(separator=' ', strip=True)[:300]
                print(f'回應內容: {error_text}')
            else:
                print('\n[不確定] 無法確認提交狀態，請手動檢查')
                print(f'回應長度: {len(submit_response.text)} 字元')
        else:
            print(f'\n[失敗] 提交失敗，HTTP {submit_response.status_code}')
            
    except Exception as e:
        print(f'\n[錯誤] 提交時發生錯誤: {e}')
        print('建議手動提交')
    
except Exception as e:
    print(f'\n[錯誤] {e}')
    print('\n[建議] 請手動提交到: https://www.jayde.com/submit.html')

print('\n' + '=' * 70)
print('[完成] Jayde 自動提交嘗試完成')
print('\n[下一步]')
print('1. 如果自動提交成功 → 更新 directory_submission_tracking.md')
print('2. 如果需要手動提交 → 參考 directory_submission_guide.md')
