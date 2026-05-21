import re
with open('taiwan-travel.html','r',encoding='utf-8') as f:
    c = f.read()

# Find ALL tables and their context (which section they're in)
tables = re.finditer(r'<table[^>]*>.*?</table>', c, re.DOTALL)
for i, t in enumerate(tables):
    start = t.start()
    # Find nearest section before this table
    sec_match = re.search(r'<(section|div)[^>]*class="[^"]*"[^>]*>', c[:start])
    if sec_match:
        # Get last 2 section/div tags before this table
        all_tags = list(re.finditer(r'<(section|div)[^>]*class="[^"]*"[^>]*>', c[:start]))
        if all_tags:
            parent = all_tags[-1].group()[:80]
            print(f'Table {i+1}: inside {parent}')
            print(f'  Position: {start}')
            # Show first 60 chars of table content
            print(f'  Content preview: {t.group()[:100]}')
            print()
