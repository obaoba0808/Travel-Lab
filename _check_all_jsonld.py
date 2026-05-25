import os
import re
import json

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f'Checking {len(html_files)} HTML files for JSON-LD issues...\n')

issues = []
for fname in sorted(html_files):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    for i, block in enumerate(blocks):
        try:
            json.loads(block.strip())
        except json.JSONDecodeError as e:
            issues.append((fname, i+1, str(e)))
            print(f'  ISSUE: {fname} - Block {i+1}: {e.msg} at pos {e.pos}')

if not issues:
    print('All JSON-LD blocks are valid!')
else:
    print(f'\nTotal issues found: {len(issues)}')
    for fname, block_num, error in issues:
        print(f'  {fname} Block {block_num}: {error}')
