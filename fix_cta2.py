import re

f = 'kyoto-temples.html'
with open(f, 'r', encoding='utf-8') as fh:
    c = fh.read()

c2 = re.sub(
    r'<div class="article-bottom-cta">.*?</div>\s*\n</div><!-- /three-col-wrapper -->',
    '</div><!-- /three-col-wrapper -->',
    c,
    flags=re.DOTALL
)

with open(f, 'w', encoding='utf-8') as fh:
    fh.write(c2)

print('still has CTA:', 'article-bottom-cta' in c2)
