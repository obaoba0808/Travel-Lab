#!/usr/bin/env python3
"""Update OG images to match new hero images"""
import os

os.chdir(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab')

# Update about.html - OG + Twitter images
with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace(
    "og:image\" content=\"https://golightly.fun/images/tokyo-hero.webp\"",
    "og:image\" content=\"https://golightly.fun/images/about-hero.webp\""
)
content = content.replace(
    "twitter:image\" content=\"https://golightly.fun/images/tokyo-hero.webp\"",
    "twitter:image\" content=\"https://golightly.fun/images/about-hero.webp\""
)
with open('about.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(content)
print('about.html: og:image + twitter:image -> about-hero.webp')

# Update travel-tools.html - OG + Twitter images
with open('travel-tools.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace(
    "og:image\" content=\"https://golightly.fun/images/tokyo-hero.webp\"",
    "og:image\" content=\"https://golightly.fun/images/travel-tools-hero.webp\""
)
content = content.replace(
    "twitter:image\" content=\"https://golightly.fun/images/tokyo-hero.webp\"",
    "twitter:image\" content=\"https://golightly.fun/images/travel-tools-hero.webp\""
)
with open('travel-tools.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(content)
print('travel-tools.html: og:image + twitter:image -> travel-tools-hero.webp')
