import re

files = ['kyoto-temples.html', 'tokyo-5days.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    c2 = re.sub(
        r'<div class="article-bottom-cta">.*?</div>\s*</div><!-- /col-center -->',
        '</div><!-- /col-center -->',
        c,
        flags=re.DOTALL
    )
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c2)
    
    remaining = 'article-bottom-cta' in c2
    print(f'{f}: still has CTA = {remaining}')
