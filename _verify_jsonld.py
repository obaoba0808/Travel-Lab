import re
import json

with open('tainan-food.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all JSON-LD blocks
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
print(f'Found {len(blocks)} JSON-LD blocks')

for i, block in enumerate(blocks):
    block = block.strip()
    print(f'\nBlock {i+1}:')
    print(f'  Length: {len(block)} chars')
    print(f'  First 80 chars: {block[:80]}')
    print(f'  Last 50 chars: {block[-50:]}')
    
    try:
        parsed = json.loads(block)
        print(f'  Status: VALID')
    except json.JSONDecodeError as e:
        print(f'  Status: INVALID - {e.msg}')
        pos = e.pos
        start = max(0, pos - 50)
        end = min(len(block), pos + 50)
        print(f'  Context around error: ...{block[start:end]}...')
