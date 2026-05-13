import os

base_chiang = "https://images.unsplash.com/photo-1528181304800-259b08848526"
base_kyoto = "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e"
base_osaka = "https://images.unsplash.com/photo-1480796927426-f609979314bd"
base_taiwan_food = "https://images.unsplash.com/photo-1555939594-58d7cb561ad1"
base_bangkok = "https://images.unsplash.com/photo-1508009603885-50cf7c579365"
base_tokyo = "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf"
base_seoul = "https://images.unsplash.com/photo-1538681105587-85640961bf8b"
base_winter = "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1"
base_beach = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"

def fix_hero(fn, old_base, new_base):
    txt = open(fn, encoding='utf-8').read()
    n = txt.replace(old_base, new_base)
    if n != txt:
        open(fn, 'w', encoding='utf-8').write(n)
        print(f'Fixed hero in {fn}: {old_base[:60]} -> {new_base[:60]}')
    else:
        print(f'No change in {fn} (hero)')

def fix_meta(fn, old_base, new_base, props):
    txt = open(fn, encoding='utf-8').read()
    n = txt
    for prop in props:
        n = n.replace(f'<meta property="{prop}" content="{old_base}', f'<meta property="{prop}" content="{new_base}')
        n = n.replace(f'<meta name="{prop}" content="{old_base}', f'<meta name="{prop}" content="{new_base}')
    if n != txt:
        open(fn, 'w', encoding='utf-8').write(n)
        print(f'Fixed meta in {fn}: {old_base[:60]} -> {new_base[:60]}')
    else:
        print(f'No change in {fn} (meta)')

# 1. chiang-mai Hero: Kyoto -> Chiang Mai temple
fix_hero('chiang-mai.html', base_kyoto, base_chiang)

# 2. kansai-pass Hero: Kyoto -> Osaka/Kansai
fix_hero('kansai-pass.html', base_kyoto, base_osaka)

# 3. tainan-food Hero: Bangkok -> Taiwan food
fix_hero('tainan-food.html', base_bangkok, base_taiwan_food)

# 4. tokyo-5days Hero: Seoul -> Tokyo
fix_hero('tokyo-5days.html', base_seoul, base_tokyo)

# 5. hokkaido-winter og:image: Bangkok -> Winter scenery
fix_meta('hokkaido-winter.html', base_bangkok, base_winter, ['og:image', 'twitter:image'])

# 6. hualien-taitung og:image: Winter -> Taiwan beach
fix_meta('hualien-taitung.html', base_winter, base_beach, ['og:image', 'twitter:image'])

print('\nAll fixes done!')
