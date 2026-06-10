import re, glob

files = glob.glob('*.html')
bad = []

for f in files:
    c = open(f, 'r', encoding='utf-8').read()
    if '延伸閱讀' not in c:
        continue
    # Find the wrapper div before 延伸閱讀 (style="background:#f5f5f5...")
    wrapper_pat = r'<div\s+style="[^"]*background:#f5f5f5[^"]*"[^>]*>'
    m = re.search(wrapper_pat, c)
    if not m:
        # try class-based wrapper
        continue
    
    widx = m.start()
    footer_idx = c.find('<footer', widx)
    if footer_idx == -1:
        continue
    
    section = c[widx:footer_idx]
    opens = len(re.findall(r'<div\b', section))
    closes = len(re.findall(r'</div>', section))
    
    if opens > closes:
        bad.append((f, opens - closes))
        print(f"❌ {f}: {opens} opens, {closes} closes → {opens-closes} UNCLOSED div(s)")

print(f"\nTotal broken: {len(bad)} pages")
