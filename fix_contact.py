import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('contact.html', 'rb') as f:
    raw = f.read()

head_end = raw.find(b'<body>')
head_bytes = raw[:head_end]
body_bytes = raw[head_end:]

# Head: decode as UTF-8
try:
    head_text = head_bytes.decode('utf-8', errors='replace')
    print('Head: UTF-8 OK')
except Exception as e:
    print('Head ERROR:', e)
    head_text = head_bytes.decode('latin-1')

# Body: decode as CP950 (Windows Traditional Chinese)
try:
    body_text = body_bytes.decode('cp950', errors='replace')
    print('Body: CP950 OK')
except Exception as e:
    print('Body CP950 ERROR:', e)
    body_text = body_bytes.decode('latin-1')

# Count real CJK chars in body
cjk_count = sum(1 for c in body_text if 0x4e00 <= ord(c) <= 0x9fff)
print(f'CJK chars in body: {cjk_count}')

# Rebuild as UTF-8
new_content = head_text + body_text

# Write back as UTF-8
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('contact.html rebuilt as UTF-8')

# Verify
with open('contact.html', 'r', encoding='utf-8') as f:
    verify = f.read()
cjk_verify = sum(1 for c in verify if 0x4e00 <= ord(c) <= 0x9fff)
print(f'Verification - CJK chars in file: {cjk_verify}')
title_m = __import__('re').search(r'<title>(.*?)</title>', verify)
if title_m:
    print(f'Title: {title_m.group(1)}')