import sys; sys.stdout.reconfigure(encoding='utf-8')
c = open('japan-travel.html', 'r', encoding='utf-8').read()
# Replace only the 2nd occurrence (card thumbnail)
idx = c.find('images/japan-hero.png')
idx2 = c.find('images/japan-hero.png', idx + 1)
c = c[:idx2] + 'images/東京直版.png' + c[idx2+len('images/japan-hero.png'):]
open('japan-travel.html', 'w', encoding='utf-8').write(c)
print('OK - Tokyo card fixed to 東京直版.png')