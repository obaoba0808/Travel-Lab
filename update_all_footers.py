#!/usr/bin/env python3
"""Update footer bottom on all 21 HTML pages to add terms + disclaimer links"""
import os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

old_link = ('    <div style="margin-top:8px;font-size:12px;">\n'
            '      <a href="about.html" style="color:inherit;margin-right:12px;">關於我們</a>\n'
            '      <a href="contact.html" style="color:inherit;margin-right:12px;">聯絡我們</a>\n'
            '      <a href="privacy.html" style="color:inherit;">隱私權政策</a>\n'
            '    </div>')

new_link = ('    <div style="margin-top:8px;font-size:12px;">\n'
            '      <a href="about.html" style="color:inherit;margin-right:12px;">關於我們</a>\n'
            '      <a href="privacy.html" style="color:inherit;margin-right:12px;">隱私權政策</a>\n'
            '      <a href="terms.html" style="color:inherit;margin-right:12px;">使用條款</a>\n'
            '      <a href="disclaimer.html" style="color:inherit;">免責聲明</a>\n'
            '    </div>')

count = 0
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    if old_link in content:
        content = content.replace(old_link, new_link)
        with open(f, 'w', encoding='utf-8', newline='\r\n') as fh:
            fh.write(content)
        count += 1
        print(f'{f}: updated')
    else:
        # Check what footer bottom looks like
        idx = content.find('margin-top:8px;font-size:12px')
        if idx > 0:
            snippet = content[idx-5:idx+300]
            print(f'{f}: different pattern - {snippet[:150]!r}')
        else:
            print(f'{f}: no footer bottom found')

print(f'\nUpdated {count} pages')