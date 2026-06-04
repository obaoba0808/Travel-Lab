#!/usr/bin/env python3
"""
嘗試自動提交 golightly.fun 到 Jayde.com 目錄
"""

import requests
from bs4 import BeautifulSoup
import time

# 提交資料
submit_data = {
    'url': 'https://golightly.fun',
    'email': 'noreply@golightly.fun',  # 先使用測試 Email
    'name': 'Travel Lab',
    'business_name': 'Travel Lab',
    'description': 'AI-powered travel planning platform providing free downloadable PDF travel guides for Asia destinations including Japan, Korea, Taiwan, Thailand.',
    'category': 'Travel/Asia',
    'phone': '+886-926-656666',
    'address': 'Taipei, Taiwan',
    'facebook': 'https://www.facebook.com/golightly.fun',
    'twitter': '@golightlyfun',
    'logo': 'https://golightly.fun/images/og-image.jpg'
}

print('[SUBMIT] 嘗試自動提交到 Jayde.com...')
print('=' * 70)

# 步驟 1: 取得提交頁面（檢查是否有 CAPTCHA）
print('\n[步驟 1] 取得提交頁面...')
try:
    session = requests.Session()
    response = session.get('https://www.jayde.com/submit.html', timeout=15)
    
    if response.status_code != 200:
        print(f'  [FAIL] 無法取得頁面 (HTTP {response.status_code})')
        exit(1)
    
    print('  [OK] 頁面取得成功')
    
    # 解析 HTML，檢查是否有 CAPTCHA
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 檢查常見的 CAPTCHA 指標
    has_captcha = False
    captcha_indicators = [
        'captcha',
        'recaptcha',
        'g-recaptcha',
        'hcaptcha',
        'cf-turnstile',
        'challenge'
    ]
    
    page_text = response.text.lower()
    for indicator in captcha_indicators:
        if indicator in page_text:
            has_captcha = True
            print(f'  [WARN] 偵測到 CAPTCHA: {indicator}')
            break
    
    if not has_captcha:
        print('  [OK] 未偵測到 CAPTCHA')
    
except Exception as e:
    print(f'  [FAIL] 錯誤: {e}')
    exit(1)

# 步驟 2: 嘗試提交表單
print('\n[步驟 2] 嘗試提交表單...')

# 檢查表單結構
form = soup.find('form')
if not form:
    print('  [FAIL] 未找到表單')
    exit(1)

print(f'  [OK] 找到表單: {form.get("action", "无 action")}')

# 取得所有表單欄位
inputs = form.find_all(['input', 'textarea', 'select'])
form_data = {}

for input_tag in inputs:
    name = input_tag.get('name')
    if name:
        if input_tag.get('type') == 'submit':
            continue
        form_data[name] = input_tag.get('value', '')

print(f'  [INFO] 表單欄位: {list(form_data.keys())}')

# 填入我們的資料
# 注意：這裡需要根據實際表單欄位名稱調整
field_mapping = {
    'url': 'url',
    'email': 'email',
    'name': 'name',
    'business_name': 'business_name',
    'description': 'description',
    'category': 'category',
    'phone': 'phone',
    'address': 'address',
    'facebook': 'facebook_url',
    'twitter': 'twitter_account',
    'logo': 'logo_url'
}

for key, value in submit_data.items():
    form_field = field_mapping.get(key)
    if form_field and form_field in form_data:
        form_data[form_field] = value

print('  [INFO] 已填入提交資料')

# 提交表單
try:
    submit_url = form.get('action')
    if not submit_url or submit_url == '':
        submit_url = 'https://www.jayde.com/submit.html'
    elif not submit_url.startswith('http'):
        submit_url = 'https://www.jayde.com/' + submit_url.lstrip('/')
    
    print(f'  [INFO] 提交到: {submit_url}')
    
    # 如果有 CAPTCHA，則無法自動提交
    if has_captcha:
        print('  [WARN] 偵測到 CAPTCHA，無法自動提交')
        print('\n[結果] 需要手動提交')
        print('=' * 70)
        print('Jayde.com 有 CAPTCHA 驗證，無法自動化提交。')
        print('\n請依照以下步驟手動提交:')
        print('1. 開啟: https://www.jayde.com/submit.html')
        print('2. 填寫以下資料:')
        for key, value in submit_data.items():
            print(f'   {key}: {value}')
        print('3. 完成 CAPTCHA 驗證')
        print('4. 點擊提交按鈕')
        exit(0)
    
    # 如果沒有 CAPTCHA，則嘗試提交
    response = session.post(submit_url, data=form_data, timeout=15)
    
    if response.status_code == 200:
        print('  [OK] 提交成功！')
        print('\n[結果] 提交成功')
        print('=' * 70)
        print('Jayde.com 目錄提交成功！')
        print('請檢查 Email 收件匣以完成驗證。')
        print(f'使用 Email: {submit_data["email"]}')
    else:
        print(f'  [FAIL] 提交失敗 (HTTP {response.status_code})')
        print('\n[結果] 提交失敗')
        print('=' * 70)
        print(f'HTTP 狀態碼: {response.status_code}')
        print('可能需要手動提交或檢查表單欄位。')
        
except Exception as e:
    print(f'  [FAIL] 錯誤: {e}')
    print('\n[結果] 提交錯誤')
    print('=' * 70)
    print(f'錯誤訊息: {e}')
    print('請嘗試手動提交。')

print('\n[下一步]')
print('1. 如果自動提交成功，請檢查 Email 驗證')
print('2. 如果需要手動提交，請依照上述步驟執行')
print('3. 提交後約 1-2 週會審核通過')
