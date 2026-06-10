import glob, re

# Check all HTML files for footer inside article-container pattern
problems = []

for f in sorted(glob.glob('*.html')):
    if f in ['404.html', 'disclaimer.html', 'terms.html']:
        continue
        
    c = open(f, 'r', encoding='utf-8').read()
    
    # Skip if no three-col-wrapper (not an article page)
    if 'three-col-wrapper' not in c:
        continue
    
    # Find footer position
    footer_pos = c.find('<footer class="site-footer">')
    if footer_pos == -1:
        continue
    
    # Check what's before footer
    before = c[footer_pos-100:footer_pos]
    
    # Check if proper closing structure exists
    has_proper_close = '/three-col-wrapper' in before or '/col-center' in before or '/article-container' in before
    
    if not has_proper_close:
        # Check if it's just </div>\n<footer (missing closing comments)
        if '</div>\n<footer' in c or '</div> \n<footer' in c or '</div>\n\n<footer' in c:
            problems.append(f)
            print(f'❌ {f}: Footer missing proper closing structure')
            print(f'   Before footer: {repr(before[-50:])}')

print(f'\n=== 發現 {len(problems)} 個頁面有 Footer 結構問題 ===')
for p in problems:
    print(f'  - {p}')