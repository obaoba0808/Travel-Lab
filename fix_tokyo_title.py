import re

with open('tokyo-5days.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Extract actual title from the corrupted section
idx = content.find('</title>')
end_idx = idx
start_idx = content.rfind('>', 0, end_idx)
actual_title = content[start_idx+1:end_idx]
print('Actual title:', actual_title)

# Find all meta tags after </title>
rest = content[idx+8:]
meta_author = re.search(r'<meta name="author" content="([^"]+)"', rest)
meta_desc = re.search(r'<meta name="description" content="([^"]+)"', rest)
meta_keywords = re.search(r'<meta name="keywords" content="([^"]+)"', rest)

print('Author:', meta_author.group(1) if meta_author else 'N/A')
print('Desc preview:', (meta_desc.group(1)[:100] if meta_desc else 'N/A'))
print('Keywords:', meta_keywords.group(1)[:100] if meta_keywords else 'N/A')

# Now rebuild the head section
# The pattern from other clean files is:
# <head>
# <meta charset="UTF-8">
# <title>ACTUAL TITLE</title>
# <meta name="author" content="AUTHOR">
# <meta name="description" content="DESC">
# ...

# Find where <head> ends (after charset line)
head_start = content.find('<head>')
charset_end = content.find('</title>', head_start) + 8  # after </title>

# Replace everything from after <head><meta charset="UTF-8"> to before </title>
old_head_chunk = content[head_start:charset_end]
print('\n--- Old head chunk ---')
print(old_head_chunk[:500])
