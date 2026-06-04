# -*- coding: utf-8 -*-
"""
Remove <meta name="keywords" ...> tags from all HTML files
"""
import os
import re

# 1. Find all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f'[INFO] Found {len(html_files)} HTML files')

files_modified = 0

# 2. Process each file
for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 3. Check if file contains meta keywords tag
    # Pattern matches: <meta name="keywords" content="..."> (case insensitive, allows whitespace)
    pattern = r'<\s*meta\s+name\s*=\s*["\']keywords["\'][^>]*>'
    
    if re.search(pattern, content, re.IGNORECASE):
        print(f'[FOUND] {filename}')
        
        # 4. Remove the meta keywords tag (and any surrounding whitespace/newlines)
        new_content = re.sub(pattern, '', content, flags=re.IGNORECASE)
        
        # 5. Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        files_modified += 1
        print(f'   -> Removed meta keywords tag')
    else:
        # print(f'[SKIP ] {filename} (no keywords tag)')
        pass

print(f'\n[SUCCESS] Modified {files_modified} files')
print(f'[INFO] Ready to commit and push')
