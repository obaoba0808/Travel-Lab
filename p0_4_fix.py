# -*- coding: utf-8 -*-
"""
P0-4: Replace Unsplash og:image URLs with self-hosted cropped WebP images.
"""
import os, re, glob, subprocess

BASE = r'G:\aistudio-travel-lab'
os.chdir(BASE)

# Article → og_image_id → source image filename in public/images/
OG_IMAGES = [
    ('angkor-wat-2days.html',            'angkor-og',              'angkor.webp'),
    ('chiang-mai.html',                  'chiangmai-og',           'chiangmai-hero.webp'),
    ('fukuoka-5days.html',               'fukuoka-og',            'Fukuoka.webp'),
    ('hokkaido-winter.html',             'hokkaido-og',            'hokkaido-hero.webp'),
    ('japan-budget-guide.html',          'japan-budget-og',       'japan-budget-hero.webp'),
    ('japan-cherry-blossom-season.html', 'japan-cherry-og',       'Cherry blossom and autumn foliage viewing in Japan.webp'),
    ('japan-drugstore-checklist.html',   'japan-drugstore-og',    'Japanese drugstore cosmetics.webp'),
    ('kualalumpur-3days.html',          'kualalumpur-og',        'kualalumpur-3days.webp'),
    ('singapore-3days.html',            'singapore-og',          'singapore.webp'),
    ('tokyo-accommodation.html',         'tokyo-accommodation-og','Tokyo-Accommodation-hero.webp'),
]

IMAGES_DIR = os.path.join(BASE, 'public', 'images')
SHARP_MODULE = os.path.join(BASE, 'node_modules', 'sharp')

# Step 1: Generate cropped 1200x630 WebP og:image files
print("=== Step 1: Generating og:image WebP files ===")
generated = []
for html_file, og_id, src_img in OG_IMAGES:
    src_path = os.path.join(IMAGES_DIR, src_img)
    out_path = os.path.join(IMAGES_DIR, f'{og_id}.webp')

    if not os.path.exists(src_path):
        print(f"  [SKIP] {src_img}: NOT FOUND")
        continue

    try:
        # Use sharp via Node.js inline script
        script = f"""
const sharp = require('{SHARP_MODULE.replace(chr(92), chr(92)+chr(92))}');
sharp('{src_path}')
  .resize(1200, 630, {{ fit: 'cover', position: 'center' }})
  .webp({{ quality: 80 }})
  .toFile('{out_path}', (err, info) => {{
    if (err) {{ console.error('ERROR:', err); process.exit(1); }}
    console.log('OK: {og_id}.webp', info.width+'x'+info.height, info.size+'B');
  }});
"""
        result = subprocess.run(['node', '--input-type=module', '-e', script],
                              capture_output=True, text=True, timeout=60,
                              cwd=BASE)
        if result.returncode == 0:
            size = os.path.getsize(out_path)
            print(f"  [OK] {og_id}.webp ({size:,}B) <- {src_img}")
            generated.append((html_file, og_id))
        else:
            print(f"  [ERR] {og_id}: {result.stderr[:100]}")
    except Exception as e:
        print(f"  [ERR] {og_id}: {e}")

print(f"\nGenerated {len(generated)} og:image files")
print()

# Step 2: Update physical HTML files
print("=== Step 2: Updating HTML og:image tags ===")
BASE_URL = 'https://golightly.fun'
for html_file, og_id in generated:
    fpath = os.path.join(BASE, html_file)
    if not os.path.exists(fpath):
        print(f"  [SKIP] {html_file}: NOT FOUND")
        continue

    with open(fpath, encoding='utf-8', errors='replace') as f:
        html = f.read()

    new_url = f'{BASE_URL}/images/{og_id}.webp'

    # Replace og:image content
    def replace_og(m):
        return f'<meta property="og:image" content="{new_url}"/>'

    new_html, count = re.subn(
        r'<meta\s+property="og:image"\s+content="[^"]*"(\s*/)?>',
        replace_og,
        html
    )

    if count > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"  [OK] {html_file}: replaced og:image -> {og_id}.webp")
    else:
        print(f"  [SKIP] {html_file}: no og:image tag found")

print("\nDone.")
