import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('contact.html', 'rb') as f:
    raw = f.read()

body_start = raw.find(b'<body>')
# Try cp950 decode with replace
body_cp950 = raw[body_start:].decode('cp950', errors='replace')

# Find lines with real CJK characters
lines = body_cp950.split('\n')
found = 0
for i, l in enumerate(lines):
    cjk_chars = [c for c in l if 0x4e00 <= ord(c) <= 0x9fff or 0x3000 <= ord(c) <= 0x303f]
    if len(cjk_chars) > 3:
        print(f'Line {i}: {repr(l[:120])}')
        found += 1
        if found > 30:
            break

print(f'\nTotal lines with Chinese: {found}')
