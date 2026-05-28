import re

with open('tokyo-5days.html', 'rb') as f:
    raw = f.read()

# Decode for inspection
content = raw.decode('utf-8', errors='replace')

# Find the actual title content: after the last > before </title>
title_end = raw.find(b'</title>')
title_start = raw.rfind(b'>', 0, title_end)
actual_title_bytes = raw[title_start+1:title_end]

print('Actual title bytes:', actual_title_bytes)
print('Decoded:', actual_title_bytes.decode('utf-8', errors='replace'))

# Find author bytes
author_match = re.search(b'<meta name="author" content="([^"]+)"', raw)
author_bytes = author_match.group(1) if author_match else b''
print('Author bytes:', author_bytes)
print('Author decoded:', author_bytes.decode('utf-8', errors='replace'))

# Find where <head> is
head_idx = raw.find(b'<head>')
charset_end = raw.find(b'</title>') + 8

# Build the fixed head section
# Pattern in <head>: <head><meta charset="UTF-8"><title>><title><meta author...>TITLE</title>...
old_head = raw[head_idx:charset_end]
print('\nOld head (raw bytes):')
print(old_head[:200])

# Fixed version: <head><meta charset="UTF-8"><title>TITLE</title><meta name="author" content="AUTHOR">
fixed_head = (
    b'<head><meta charset="UTF-8"><title>'
    + actual_title_bytes
    + b'</title><meta name="author" content="'
    + author_bytes
    + b'">'
)

print('\nFixed head:')
print(fixed_head.decode('utf-8', errors='replace'))

# Now reconstruct
new_raw = raw[:head_idx] + fixed_head + raw[charset_end:]

# Also fix the double > issue: after description we have >>meta keywords
# The pattern: content="...">><meta
double_dquote = b'">><meta name="keywords"'
if double_dquote in new_raw:
    new_raw = new_raw.replace(double_dquote, b'"><meta name="keywords"')
    print('\nFixed double >> before meta keywords')

with open('tokyo-5days.html', 'wb') as f:
    f.write(new_raw)

# Verify
with open('tokyo-5days.html', 'r', encoding='utf-8', errors='replace') as f:
    verify = f.read()
titles = re.findall(r'<title>.*?</title>', verify, re.DOTALL)
for t in titles:
    print('\nVerified title tag:', repr(t[:120]))
    print('Clean?', '<' not in t[7:-8])

# Check for double >> in description
desc_match = re.search(r'<meta name="description" content="[^"]*">>[^<]', verify)
print('Double >> still present?', bool(desc_match))
