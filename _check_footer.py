f = 'tokyo-accommodation.html'
c = open(f, 'r', encoding='utf-8').read()

# Find structural markers
markers = ['related-posts', '<footer', 'site-footer', '/article-container', '/col-center', '/three-col-wrapper']
for m in markers:
    pos = c.find(m)
    print(f'{m}: position {pos}')

# Show the area around footer
footer_pos = c.find('<footer')
if footer_pos > 0:
    chunk = c[footer_pos-300:footer_pos+300]
    print(f'\n=== Footer 周圍 300 字元 ===')
    print(chunk.replace('\n', ' '))
    
# Check if footer is inside any container
# Find the div that contains footer
lines = c[:footer_pos].split('\n')
open_divs = 0
for i, line in enumerate(reversed(lines)):
    if '</div>' in line:
        open_divs += line.count('</div>')
    if '<div' in line:
        open_divs -= line.count('<div')
    if open_divs < 0:
        print(f'\n⚠️ Footer 可能在第 {len(lines)-i} 行的 div 內部')
        break