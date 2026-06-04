# -*- coding: utf-8 -*-
# Debug: Find where to insert SlideShare embed

with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for </article>
if '</article>' in content:
    idx = content.index('</article>')
    line_num = content[:idx].count('\n') + 1
    print(f'[PASS] Found </article> at line {line_num}')
    
    # Show context (50 chars before and after)
    start = max(0, idx - 100)
    end = min(len(content), idx + 100)
    context = content[start:end]
    print(f'\nContext around </article>:')
    print(context)
else:
    print('[FAIL] </article> NOT found in file')
    print('\nSearching for alternative closing tags...')
    
    # Check for other possible closing tags
    for tag in ['</main>', '</section>', '</div>', '</body>']:
        if tag in content:
            idx = content.index(tag)
            line_num = content[:idx].count('\n') + 1
            print(f'  [FOUND] {tag} at line {line_num}')
            
print('\n[INFO] Debug completed')
