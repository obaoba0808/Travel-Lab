#!/usr/bin/env python3
"""Update hero images for about.html and travel-tools.html"""
import os

os.chdir(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab')

# Update about.html
with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace(
    "background-image: url('images/tokyo-hero.webp');",
    "background-image: url('images/about-hero.webp');"
)
with open('about.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(content)
print('about.html: tokyo-hero -> about-hero')

# Update travel-tools.html
with open('travel-tools.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace(
    "background-image: url('images/tokyo-hero.webp');",
    "background-image: url('images/travel-tools-hero.webp');"
)
with open('travel-tools.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(content)
print('travel-tools.html: tokyo-hero -> travel-tools-hero')
