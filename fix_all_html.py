import os
import re

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    modified = content
    
    # Fix 1: Corrupted title tag
    # Extract real title from og:title
    og_match = re.search(r'<meta property="og:title" content="(.*?)"', modified)
    if og_match:
        real_title = og_match.group(1)
        # Replace any corrupted title with clean one
        modified = re.sub(
            r'<title>.*?</title>',
            '<title>' + real_title + '</title>',
            modified,
            flags=re.DOTALL
        )
    
    # Fix 2: Worker URL - wrong patterns
    wrong_patterns = [
        'https://https://golightly-email.8107e1de.workers.dev.workers.dev',
        'https://golightly-email.8107e1de.workers.dev.workers.dev',
        'https://YOUR-WORKER-URL.workers.dev',
        'YOUR-WORKER-URL',
    ]
    correct_url = 'https://golightly-email.8107e1de.workers.dev'
    
    for wrong in wrong_patterns:
        if wrong in modified:
            modified = modified.replace(wrong, correct_url)
    
    # Also fix any malformed URL that has extra https://
    modified = re.sub(
        r'https://https://golightly-email\.8107e1de\.workers\.dev',
        'https://golightly-email.8107e1de.workers.dev',
        modified
    )
    
    if modified != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False

# Process all HTML files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

fixed = 0
for f in os.listdir('.'):
    if not f.endswith('.html'):
        continue
    try:
        if fix_html_file(f):
            print('FIXED: ' + f)
            fixed += 1
        else:
            print('OK:     ' + f)
    except Exception as e:
        print('ERROR:  ' + f + ' - ' + str(e))

print('\nTotal fixed: ' + str(fixed))
