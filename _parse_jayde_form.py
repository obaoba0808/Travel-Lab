#!/usr/bin/env python3
"""
抓取 Jayde.com 提交表單的所有欄位
"""

import requests
import re

print('[FETCH] Downloading Jayde submit page...')
response = requests.get('https://www.jayde.com/submit.html', timeout=15)

if response.status_code != 200:
    print(f'FAIL: HTTP {response.status_code}')
    exit(1)

html = response.text
print(f'[OK] Downloaded {len(html)} bytes')

# 搜尋所有 form 標籤
forms = re.findall(r'<form[^>]*>(.*?)</form>', html, re.IGNORECASE | re.DOTALL)
print(f'\n[PARSE] Found {len(forms)} form(s)')

for i, form_html in enumerate(forms, 1):
    print(f'\n--- Form {i} ---')
    
    # 搜尋所有 input/textarea/select 的 name 屬性
    fields = re.findall(r'name=[\'"]([^\'"]+)[\'"]', form_html)
    print(f'Fields ({len(fields)}): {fields}')
    
    # 搜尋 action 屬性
    action_match = re.search(r'<form[^>]*action=[\'"]([^\'"]*)[\'"]', form_html, re.IGNORECASE)
    if action_match:
        print(f'Action: {action_match.group(1)}')
    else:
        print('Action: (empty)')

# 如果找不到 form，則直接搜尋所有 name= 屬性
if not forms:
    print('\n[WARN] No form found, searching all name= attributes...')
    all_fields = re.findall(r'name=[\'"]([^\'"]+)[\'"]', html)
    print(f'Found {len(all_fields)} name= attributes:')
    for field in all_fields[:20]:  # 只顯示前 20 個
        print(f'  - {field}')

print('\n[DONE]')
