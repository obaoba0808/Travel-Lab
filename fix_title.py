import os
import re

def fix_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix corrupted title: <title>><title><meta ...>真實標題</title>
    # Extract real title from og:title as fallback
    og_match = re.search(r'<meta property="og:title" content="(.*?)"', content)
    if not og_match:
        print(f"  SKIP (no og:title): {os.path.basename(filepath)}")
        return False
    
    real_title = og_match.group(1)
    
    # Replace any corrupted title tag with clean one
    new_content = re.sub(
        r'<title>.*?</title>',
        '<title>' + real_title + '</title>',
        content,
        flags=re.DOTALL
    )
    
    # Also fix Worker URL if present
    wrong1 = 'https://https://golightly-email.8107e1de.workers.dev.workers.dev'
    wrong2 = 'https://golightly-email.8107e1de.workers.dev.workers.dev'
    right = 'https://golightly-email.8107e1de.workers.dev'
    new_content = new_content.replace(wrong1, right).replace(wrong2, right)
    
    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

os.chdir(os.path.dirname(os.path.abspath(__file__)))

fixed = 0
for f in os.listdir('.'):
    if not f.endswith('.html'):
        continue
    try:
        if fix_html(f):
            print('FIXED: ' + f)
            fixed += 1
        else:
            print('OK: ' + f)
    except Exception as e:
        print('ERROR ' + f + ': ' + str(e))

print('\nTotal fixed: ' + str(fixed))
