import re
import json

with open('tainan-food.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all JSON-LD blocks
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
print(f'Found {len(blocks)} JSON-LD blocks')
for i, block in enumerate(blocks):
    try:
        json.loads(block.strip())
        print(f'Block {i+1}: VALID')
    except json.JSONDecodeError as e:
        print(f'Block {i+1}: INVALID - {e}')
        # Show context around error
        pos = e.pos
        start = max(0, pos - 80)
        end = min(len(block), pos + 80)
        print(f'  Around error position {pos}:')
        print(f'  ...{repr(block[start:end])}...')
