#!/usr/bin/env python
"""Travel Lab SEO Batch Fix Script
- Convert PNG hero images to WebP
- Rename images to English filenames
- Update all HTML references
- Remove lazy loading from hero images, add fetchpriority="high"
- Fix OG image to full URLs
- Add width/height to images
- Add rel="sponsored" to affiliate links
- Add favicon
- Delete unused ChatGPT images
"""

import os, re, glob
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE, "images")
HTML_DIR = BASE

# ========== 1. Image mapping: Chinese filename → English filename ==========
IMAGE_MAP = {
    "東京.png": "tokyo-hero.webp",
    "京都.png": "kyoto-hero.webp",
    "北海道.png": "hokkaido-hero.webp",
    "沖繩.png": "okinawa-hero.webp",
    "花東.png": "hualien-hero.webp",
    "台南.png": "tainan-hero.webp",
    "墾丁.png": "kenting-hero.webp",
    "首爾.png": "seoul-hero.webp",
    "釜山.png": "busan-hero.webp",
    "濟州島.png": "jeju-hero.webp",
    "清邁.png": "chiangmai-hero.webp",
    "曼谷.png": "bangkok-hero.webp",
    "關西.png": "kansai-hero.webp",
    "台灣.png": "taiwan-hero.webp",
}

# Also map the JPG files
JPG_MAP = {
    "hokkaido-winter.jpg": "hokkaido-winter.webp",
    "okinawa.jpg": "okinawa-side.webp",
    "曼谷.jpg": "bangkok-side.webp",
    "tokyo-hero.jpg": "tokyo-hero-old.webp",
}

# Charter banner
BANNER_MAP = {
    "charter-banner.png": "charter-banner.webp",
}

# Logo
LOGO_MAP = {
    "logo.png": "logo.webp",
}

ALL_MAP = {}
ALL_MAP.update(IMAGE_MAP)
ALL_MAP.update(JPG_MAP)
ALL_MAP.update(BANNER_MAP)
ALL_MAP.update(LOGO_MAP)

# ========== 2. Convert images ==========
print("=== Converting images to WebP ===")
converted = 0
for old_name, new_name in ALL_MAP.items():
    old_path = os.path.join(IMG_DIR, old_name)
    new_path = os.path.join(IMG_DIR, new_name)
    if not os.path.exists(old_path):
        print(f"  SKIP (not found): {old_name}")
        continue
    if os.path.exists(new_path):
        print(f"  SKIP (already exists): {new_name}")
        continue
    try:
        img = Image.open(old_path)
        # Convert RGBA to RGB for WebP if needed
        if img.mode in ('RGBA', 'P'):
            bg = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            bg.paste(img, mask=img.split()[3])
            img = bg
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(new_path, 'WEBP', quality=80, method=6)
        old_size = os.path.getsize(old_path)
        new_size = os.path.getsize(new_path)
        pct = (1 - new_size/old_size) * 100
        print(f"  OK: {old_name} ({old_size//1024}KB) → {new_name} ({new_size//1024}KB, -{pct:.0f}%)")
        converted += 1
    except Exception as e:
        print(f"  ERROR: {old_name}: {e}")

print(f"\nConverted {converted} images\n")

# ========== 3. Delete unused ChatGPT images ==========
print("=== Deleting unused ChatGPT images ===")
deleted = 0
for f in os.listdir(IMG_DIR):
    if f.startswith("ChatGPT"):
        os.remove(os.path.join(IMG_DIR, f))
        print(f"  DEL: {f}")
        deleted += 1
print(f"Deleted {deleted} unused images\n")

# ========== 4. Fix HTML files ==========
SITE_URL = "https://obaoba0808.github.io/Travel-Lab"

html_files = glob.glob(os.path.join(HTML_DIR, "*.html"))

print("=== Fixing HTML files ===")
for html_path in html_files:
    fname = os.path.basename(html_path)
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 4a. Replace image filenames (Chinese → English, .png/.jpg → .webp)
    for old_name, new_name in ALL_MAP.items():
        # Match src="images/old" and content="images/old"
        content = content.replace(f'images/{old_name}', f'images/{new_name}')
    
    # 4b. Fix OG image: relative → full URL
    # Pattern: og:image" content="images/xxx.webp" → full URL
    content = re.sub(
        r'(og:image"\s+content=")images/([^"]+)(")',
        lambda m: f'{m.group(1)}{SITE_URL}/images/{m.group(2)}{m.group(3)}',
        content
    )
    # Same for twitter:image
    content = re.sub(
        r'(twitter:image"\s+content=")images/([^"]+)(")',
        lambda m: f'{m.group(1)}{SITE_URL}/images/{m.group(2)}{m.group(3)}',
        content
    )
    # Same for JSON-LD image field
    content = re.sub(
        r'("image"\s*:\s*")https://obaoba0808\.github\.io/Travel-Lab/images/([^"]+\.png)(")',
        lambda m: f'{m.group(1)}{SITE_URL}/images/{m.group(2).replace(".png", ".webp")}{m.group(3)}',
        content
    )
    
    # 4c. Hero images: remove loading="lazy", add fetchpriority="high"
    # Pattern: <img src="images/xxx-hero.webp" ... loading="lazy">
    content = re.sub(
        r'(<img\s[^>]*class="hero-img"[^>]*?)\s+loading="lazy"',
        r'\1 fetchpriority="high"',
        content
    )
    
    # 4d. Add rel="sponsored" to affiliate links (Agoda, Klook, Skyscanner, Airalo)
    content = re.sub(
        r'rel="noopener noreferrer"(?=.*?(?:agoda|klook|skyscanner|airalo))',
        r'rel="noopener noreferrer sponsored"',
        content,
        flags=re.IGNORECASE
    )
    
    # 4e. Add favicon before </head>
    if 'rel="icon"' not in content and 'rel="shortcut icon"' not in content:
        favicon_tag = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>✈️</text></svg>">'
        content = content.replace('</head>', f'{favicon_tag}\n</head>')
    
    if content != original:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  FIXED: {fname}")
    else:
        print(f"  OK: {fname} (no changes)")

print("\n=== Done! ===")
print("\nRemaining manual steps:")
print("1. Verify all pages render correctly in browser")
print("2. Delete old PNG/JPG files after confirming WebP works")
print("3. Add width/height attributes to <img> tags (needs dimension measurement)")
print("4. Create 404.html")
print("5. Submit updated sitemap to Google Search Console")
