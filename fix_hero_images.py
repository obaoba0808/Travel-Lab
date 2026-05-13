# -*- coding: utf-8 -*-
"""Batch update article pages with hero background images"""

import re
import os

# Map articles to their background images
articles = {
    'tokyo-5days.html': 'photo-1540959733332-eab4deabeeaf',  # Tokyo
    'kansai-pass.html': 'photo-1493976040374-85c8e12f0c0e',  # Kyoto
    'hokkaido-winter.html': 'photo-1491002052546-bf38f186af56',  # Hokkaido snow
    'okinawa.html': 'photo-1559124563-d1c8db88f720',  # Okinawa
    'kyoto-temples.html': 'photo-1528360983277-13d401cdc186',  # Kyoto temple
    'seoul-food.html': 'photo-1517154421779-a02d5b3a00f0',  # Seoul
    'busan-capsule.html': 'photo-1552832230-c0197dd311b5',  # Busan
    'jeju-island.html': 'photo-1556434570-39d4a95d75f0',  # Jeju
    'hualien-taitung.html': 'photo-1559032880-b0c3e526c33a',  # Hualien
    'tainan-food.html': 'photo-1508009603885-50cf7c579365',  # Tainan
    'kenting.html': 'photo-1507525428034-b723cf961d3e',  # Kenting
    'chiang-mai.html': 'photo-1556056763-9a5aff2fa7b2',  # Chiang Mai
    'bangkok-3days.html': 'photo-1526506118085-60ce8154c605',  # Bangkok
}

for filename, img_id in articles.items():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace hero section to add background image
        old_hero = r'<div class="hero">\s*<h2>([^<]+)</h2>\s*<p>([^<]+)</p>\s*</div>'
        new_hero = f'''<div class="hero" style="background-image:url('https://images.unsplash.com/{img_id}?auto=format&fit=crop&w=1920&q=80');">
  <h2>\\1</h2>
  <p>\\2</p>
</div>'''
        
        new_content = re.sub(old_hero, new_hero, content, flags=re.MULTILINE)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
        else:
            print(f'No change for {filename}')
    except Exception as e:
        print(f'Error {filename}: {e}')