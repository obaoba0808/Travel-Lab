#!/usr/bin/env python3
"""Update all LINE links in Travel-Lab to https://line.me/ti/g/NbNGnW4Eh6"""
import os, re

os.chdir(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab')

NEW_LINK = 'https://line.me/ti/g/NbNGnW4Eh6'

# Pattern to match various LINE links
line_pattern = re.compile(
    r'https?://(line\.me|lin\.ee|line\.moe|lineapp\.me|page\.line\.me)[^\s"\'\\]*',
    re.IGNORECASE
)

updated_files = []
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    path = os.path.join('.', f)
    with open(path, 'rb') as fp:
        raw = fp.read()
    # Normalize line endings
    norm = raw.replace(b'\r\r\n', b'\n').replace(b'\r\n', b'\n')
    text = norm.decode('utf-8', errors='replace')
    
    matches = line_pattern.findall(text)
    if matches:
        print(f'[{f}] Found LINE links: {matches}')
        # Replace all LINE links with new link
        new_text = line_pattern.sub(NEW_LINK, text)
        # Write back with CRLF
        result = new_text.replace('\n', '\r\n').encode('utf-8')
        with open(path, 'wb') as fp:
            fp.write(result)
        updated_files.append(f)
        print(f'  -> Updated {f}')
    else:
        print(f'[{f}] No LINE links found')

print('\n=== Summary ===')
print(f'Updated {len(updated_files)} files:')
for f in updated_files:
    print(f'  - {f}')
