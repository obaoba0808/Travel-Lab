#!/usr/bin/env python3
import os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

legal_div = (
    '    <div style="margin-top:8px;font-size:12px;">\r\n'
    '      <a href="about.html" style="color:inherit;margin-right:12px;">關於我們</a>\r\n'
    '      <a href="privacy.html" style="color:inherit;margin-right:12px;">隱私權政策</a>\r\n'
    '      <a href="terms.html" style="color:inherit;margin-right:12px;">使用條款</a>\r\n'
    '      <a href="disclaimer.html" style="color:inherit;">免責聲明</a>\r\n'
    '    </div>'
)

COPYRIGHT = '\u00a9 2026 均在路上 Travel Lab. All Rights Reserved.'
old_bytes = ('<p>' + COPYRIGHT + '</p>\r\n  </div>\r\n</footer>').encode('utf-8')

pages = [f for f in sorted(os.listdir('.')) if f.endswith('.html')]
updated = []

for f in pages:
    with open(f, 'rb') as fh:
        raw = fh.read()
    
    if b'\xe5\x85\x8d\xe8\xb2\xac\xe8\x81\xb2\xe6\x98\x8e' in raw:
        print(f + ': already has legal links')
        continue
    
    if old_bytes in raw:
        new_bytes = raw.replace(old_bytes, (old_bytes[:-26] + '\r\n' + legal_div + '\r\n  </div>\r\n</footer>').encode('utf-8'), 1)
        with open(f, 'wb') as fh:
            fh.write(new_bytes)
        updated.append(f)
        print(f + ': legal div added')
    else:
        if b'footer-bottom' in raw:
            print(f + ': footer-bottom exists but pattern differs')
        else:
            print(f + ': no footer-bottom')

print('Updated: ' + str(updated))