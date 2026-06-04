import re
import urllib.request

# 1. 檢查本地 index.html 的 og:image 標籤
print("[CHECK] Checking index.html OG image tags...")
print("=" * 60)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到所有 og:image 相關標籤
patterns = [
    'og:image',
    'og:image:secure_url',
    'og:image:type',
    'og:image:width',
    'og:image:height',
    'og:image:alt'
]

for pattern in patterns:
    matches = re.findall(rf'<meta property="{pattern}"[^>]*>', content)
    if matches:
        for match in matches:
            print(f"[FOUND] {match}")
    else:
        print(f"[MISSING] {pattern}")

# 特別檢查 og:image 是否指向 .webp
print("\n" + "=" * 60)
print("[CHECK] Checking if og:image points to .webp or .jpg...")

og_image_match = re.search(r'<meta property="og:image" content="([^"]+)"', content)
if og_image_match:
    og_url = og_image_match.group(1)
    print(f"[CURRENT] og:image = {og_url}")
    
    if '.webp' in og_url:
        print("[ISSUE] og:image still points to .webp (should be .jpg)")
    elif '.jpg' in og_url:
        print("[OK] og:image correctly points to .jpg")
else:
    print("[ERROR] Could not find og:image tag")

# 2. 檢查線上版本（看看 Cloudflare 是否有快取）
print("\n" + "=" * 60)
print("[ONLINE] Checking online version (may be cached)...")

try:
    url = 'https://golightly.fun/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req, timeout=10) as response:
        online_content = response.read().decode('utf-8')
        
        # 檢查線上版本的 og:image
        online_og_match = re.search(r'<meta property="og:image" content="([^"]+)"', online_content)
        if online_og_match:
            online_og_url = online_og_match.group(1)
            print(f"[ONLINE] og:image = {online_og_url}")
            
            if '.webp' in online_og_url:
                print("[ISSUE] Online version still shows .webp")
                print("   -> May need to clear Cloudflare cache")
            elif '.jpg' in online_og_url:
                print("[OK] Online version shows .jpg")
        else:
            print("[ERROR] Could not find og:image in online version")
            
except Exception as e:
    print(f"[ERROR] {e}")

# 3. 檢查是否有 .jpg 檔案存在
print("\n" + "=" * 60)
print("[CHECK] Checking if JPG files exist...")

import os

if os.path.exists('images/og/og-home-hero.jpg'):
    print("[OK] images/og/og-home-hero.jpg exists")
else:
    print("[MISSING] images/og/og-home-hero.jpg not found")

if os.path.exists('images/og/og-tokyo-hero.jpg'):
    print("[OK] images/og/og-tokyo-hero.jpg exists")
else:
    print("[MISSING] images/og/og-tokyo-hero.jpg not found")
