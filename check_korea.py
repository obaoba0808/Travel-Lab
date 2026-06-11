import os
f = 'korea-transport.html'
with open(f, 'r', encoding='utf-8') as fp:
    c = fp.read()
print('File size:', len(c), 'bytes')
ac_start = c.find('<div class="article-container">')
ac_end = c.find('<!-- /article-container -->')
if ac_start > 0 and ac_end > 0:
    print('article-container content length:', ac_end - ac_start - 48)
else:
    print('article-container markers: start=', ac_start, 'end=', ac_end)
# Check div balance
print('Opening divs:', c.count('<div'))
print('Closing divs:', c.count('</div>'))
