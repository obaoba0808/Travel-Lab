import os
os.chdir(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab')
with open('japan-travel.html', 'rb') as f:
    html = f.read()
with open('style.css', 'rb') as f:
    css = f.read()
print('hero-title-block in HTML:', b'hero-title-block' in html)
print('overlay in HTML:', b'class="overlay"' in html)
print('hero-title-block in CSS:', b'hero-title-block' in css)
print('.overlay in CSS:', b'.category-hero .overlay' in css)