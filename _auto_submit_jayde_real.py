#!/usr/bin/env python3
"""
使用 Python requests 模擬真實瀏覽器提交表單到 Jayde
加入完整的 headers 和 cookie 處理，模擬真人行為
"""

import requests
from bs4 import BeautifulSoup
import time
import json

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

# 完整 headers（模擬真實 Chrome 瀏覽器）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.jayde.com',
    'Referer': 'https://www.jayde.com/submit.html',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0'
}

print('[AUTO] 開始自動提交到 Jayde（模擬真實瀏覽器）...')
print('=' * 70)

try:
    # 步驟 1: 建立 Session（保持 cookies）
    session = requests.Session()
    
    # 步驟 2: 取得提交頁面（取得初始 cookies）
    print('\n[STEP 1] 取得提交頁面（建立 session）...')
    response = session.get(submit_url, headers=headers, timeout=15)
    
    if response.status_code != 200:
        print(f'[錯誤] 無法取得頁面，HTTP {response.status_code}')
        exit(1)
    
    print(f'[成功] 頁面取得成功 (HTTP {response.status_code})')
    print(f'[Cookies] 取得 {len(session.cookies)} 個 cookies')
    
    # 步驟 3: 分析表單結構
    print('\n[STEP 2] 分析表單結構...')
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    
    if not forms:
        print('[錯誤] 找不到表單')
        exit(1)
    
    # 找到 POST 方法且欄位數 > 5 的表單
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
    
    # 步驟 4: 準備提交資料
    print('\n[STEP 3] 準備提交資料...')
    
    # 取得所有欄位
    inputs = target_form.find_all(['input', 'textarea', 'select'])
    
    # 建立欄位對應
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
            form_data[name] = website_data['contact_name']
        elif 'desc' in name_lower or 'about' in name_lower or 'summary' in name_lower or 'detail' in name_lower:
            form_data[name] = website_data['description']
        elif 'industry' in name_lower or 'category' in name_lower or 'type' in name_lower:
            form_data[name] = website_data['category']
        elif 'address' in name_lower:
            form_data[name] = ''
        elif 'phone' in name_lower or 'tel' in name_lower:
            form_data[name] = ''
        elif 'zip' in name_lower or 'postal' in name_lower:
            form_data[name] = ''
        elif 'country' in name_lower:
            form_data[name] = 'Taiwan'
        elif 'state' in name_lower or 'province' in name_lower:
            form_data[name] = ''
        elif 'facebook' in name_lower or 'fb' in name_lower:
            form_data[name] = ''
        elif 'twitter' in name_lower or 'x' in name_lower:
            form_data[name] = ''
        elif 'youtube' in name_lower or 'yt' in name_lower:
            form_data[name] = ''
        elif 'logo' in name_lower or 'image' in name_lower:
            form_data[name] = ''
        elif 'map' in name_lower or 'gmap' in name_lower:
            form_data[name] = ''
        elif 'form_id' in name_lower or 'id' in name_lower:
            # 隱藏欄位，保留原值
            value = inp.get('value', '')
            form_data[name] = value
        else:
            form_data[name] = ''
    
    print(f'準備了 {len(form_data)} 個欄位')
    print('\n[表單資料預覽]')
    for i, (key, value) in enumerate(list(form_data.items())[:10], 1):
        display_value = value[:50] + '...' if len(str(value)) > 50 else value
        print(f'  {i}. {key}: {display_value}')
    
    # 步驟 5: 檢查是否有 CAPTCHA
    print('\n[STEP 4] 檢查 CAPTCHA...')
    page_text = response.text.lower()
    
    has_captcha = False
    if 'captcha' in page_text:
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
    
    # 步驟 6: 提交表單
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
    
    # 模擬真人延遲（2-5 秒）
    delay = 3
    print(f'\n[延遲] 等待 {delay} 秒（模擬真人填寫時間）...')
    time.sleep(delay)
    
    # 發送請求
    try:
        if form_method == 'post':
            submit_response = session.post(
                submit_action_url,
                data=form_data,
                headers=headers,
                timeout=20,
                allow_redirects=True,
                verify=True
            )
        else:
            submit_response = session.get(
                submit_action_url,
                params=form_data,
                headers=headers,
                timeout=20,
                allow_redirects=True,
                verify=True
            )
        
        print(f'\n[結果] HTTP {submit_response.status_code}')
        print(f'最終 URL: {submit_response.url}')
        print(f'[Cookies] 現在共有 {len(session.cookies)} 個 cookies')
        
        if submit_response.status_code == 200:
            response_text = submit_response.text.lower()
            
            # 檢查是否成功
            success_keywords = ['success', 'thank', 'submitted', 'received', 'approved', 'pending', 'confirmation']
            error_keywords = ['error', 'invalid', 'failed', 'captcha', 'spam', 'blocked', 'sorry']
            
            is_success = any(keyword in response_text for keyword in success_keywords)
            is_error = any(keyword in response_text for keyword in error_keywords)
            
            if is_success and not is_error:
                print('\n[成功] 提交成功！')
                print('[注意] 大多數目錄需要人工審核，請耐心等待 1-4 週')
                
                # 嘗試從回應中提取確認訊息
                soup_response = BeautifulSoup(submit_response.text, 'html.parser')
                confirmation = soup_response.find('div', class_=lambda x: x and 'confirm' in x.lower())
                if confirmation:
                    print(f'[確認訊息] {confirmation.text.strip()[:200]}')
                
            elif is_error:
                print('\n[失敗] 提交失敗，可能被檢測為垃圾郵件或需要 CAPTCHA')
                print('建議手動提交')
                
                # 顯示部分回應內容
                soup_response = BeautifulSoup(submit_response.text, 'html.parser')
                error_text = soup_response.get_text(separator=' ', strip=True)[:500]
                print(f'回應內容: {error_text}')
            else:
                print('\n[不確定] 無法確認提交狀態，請手動檢查')
                print(f'回應長度: {len(submit_response.text)} 字元')
                
                # 顯示部分回應
                snippet = submit_response.text[:1000]
                print(f'\n[回應前 1000 字元]')
                print(snippet)
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
