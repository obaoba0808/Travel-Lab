# -*- coding: utf-8 -*-
"""Fix hero images with working Unsplash IDs"""

import re

# Test each location and replace with known working IDs
fixes = [
    ('okinawa.html', 'photo-1507525428034-b723cf961d3e'),  # Beach/kenting - use working one
    ('seoul-food.html', 'photo-1517154421773-0529f29ea451'),  # Seoul - try different
    ('jeju-island.html', 'photo-1556434570-39d4a95d75f0'),  # Jeju 
    ('hualien-taitung.html', 'photo-1559032880-b0c3e526c33a'),  # Taiwan
    ('bangkok-3days.html', 'photo-1508009603885-50cf7c579365'),  # Bangkok
    ('chiang-mai.html', 'photo-1528181304800-259b08848526'),  # Chiang Mai
]

for filename, img_id in fixes:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace background-image URL
        pattern = r"(background-image:url\()https://images\.unsplash\.com/[^)]+(\))"
        replacement = f"\\1https://images.unsplash.com/{img_id}?auto=format&fit=crop&w=1920&q=80\\2"
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed: {filename}')
        else:
            print(f'No change: {filename}')
    except Exception as e:
        print(f'Error {filename}: {e}')