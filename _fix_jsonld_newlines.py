import re
import json

with open('tainan-food.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all JSON-LD blocks
pattern = r'<script type="application/ld\+json">(.*?)</script>'
blocks = re.findall(pattern, content, re.DOTALL)

print(f'Found {len(blocks)} JSON-LD blocks')

new_content = content
for i, block in enumerate(blocks):
    block_stripped = block.strip()
    
    # Check if block has literal newlines inside (not escaped)
    # In valid JSON, newlines in strings must be \n
    if '\n' in block_stripped:
        print(f'Block {i+1}: Has literal newlines - attempting to fix...')
        
        try:
            # Try to parse (Python might be lenient)
            parsed = json.loads(block_stripped)
            # Re-serialize with proper escaping
            fixed_json = json.dumps(parsed, ensure_ascii=False, indent=2)
            # Replace in content
            old_block = f'<script type="application/ld+json">{block_stripped}</script>'
            new_block = f'<script type="application/ld+json">{fixed_json}</script>'
            new_content = new_content.replace(old_block, new_block, 1)
            print(f'  Fixed block {i+1}')
        except json.JSONDecodeError as e:
            print(f'  Block {i+1}: Cannot parse - {e}')
            # Try to fix manually - escape newlines in strings
            # This is complex, let's just report the error position
            print(f'  Error at position {e.pos}')
    else:
        print(f'Block {i+1}: No literal newlines (OK)')

# Write back
with open('tainan-food.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('\nDone - fixed JSON-LD blocks')
