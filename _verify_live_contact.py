import urllib.request
import re
import time

# 1. 抓取線上 contact.html (添加 cache-busting 參數)
url = 'https://golightly.fun/contact.html?v=' + str(int(time.time()))
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req, timeout=15)
content = response.read().decode('utf-8')

# 2. 擷取 ContactPage JSON-LD 區塊
pattern_contact = r'<script type="application/ld\+json">\s*\{[^}]*"@type": "ContactPage"[^}]*\}[^<]*</script>'
match_contact = re.search(pattern_contact, content, re.DOTALL)

if match_contact:
    json_ld = match_contact.group(0)
    print('✅ 成功擷取 ContactPage JSON-LD：')
    # 檢查關鍵中文字串
    if '"聯絡窗口 | 均在路上 Travel Lab"' in json_ld:
        print('   ✅ ContactPage name 正確')
    else:
        print('   ❌ ContactPage name 錯誤或亂碼')
    if '"聯絡窗口均在路上 Travel Lab"' in json_ld:
        print('   ✅ ContactPage description 正確')
    else:
        print('   ❌ ContactPage description 錯誤或亂碼')
else:
    print('❌ 找不到 ContactPage JSON-LD')

# 3. 擷取 BreadcrumbList JSON-LD 區塊
pattern_breadcrumb = r'<script type="application/ld\+json">\s*\{[^}]*"@type": "BreadcrumbList"[^}]*\}[^<]*</script>'
match_breadcrumb = re.search(pattern_breadcrumb, content, re.DOTALL)

if match_breadcrumb:
    json_ld_b = match_breadcrumb.group(0)
    print('\n✅ 成功擷取 BreadcrumbList JSON-LD：')
    if '"首頁"' in json_ld_b:
        print('   ✅ BreadcrumbList 首頁 正確')
    else:
        print('   ❌ BreadcrumbList 首頁 錯誤或亂碼')
    if '"聯絡窗口"' in json_ld_b:
        print('   ✅ BreadcrumbList 聯絡窗口 正確')
    else:
        print('   ❌ BreadcrumbList 聯絡窗口 錯誤或亂碼')
else:
    print('\n❌ 找不到 BreadcrumbList JSON-LD')

# 4. 檢查 OG 標籤
if 'property="og:site_name" content="均在路上 Travel Lab"' in content:
    print('\n✅ og:site_name 正確')
else:
    print('\n❌ og:site_name 錯誤或亂碼')

print('\n✅ 線上 contact.html 驗證完成')
