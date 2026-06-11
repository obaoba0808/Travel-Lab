with open('tokyo-accommodation.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

idx = content.find('charter-banner')
snippet = content[max(0, idx-300):idx+300]

with open('_banner_snippet.txt', 'w', encoding='utf-8') as f:
    f.write(f'charter-banner found at char {idx}\n')
    f.write('=== 300 chars before+after ===\n')
    f.write(snippet)
    f.write('\n')

# Also show the <a> tag structure
import re
a_match = re.search(r'<a[^>]+charter-banner[^>]*>', content)
if a_match:
    with open('_banner_snippet.txt', 'a', encoding='utf-8') as f:
        f.write('\n=== <a> tag ===\n')
        f.write(repr(a_match.group(0)))