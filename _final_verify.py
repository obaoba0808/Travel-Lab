import urllib.request, re

pages = [
    ('chiang-mai',    'https://obaoba0808.github.io/Travel-Lab/chiang-mai.html'),
    ('kyoto-temples', 'https://obaoba0808.github.io/Travel-Lab/kyoto-temples.html'),
    ('seoul-food',    'https://obaoba0808.github.io/Travel-Lab/seoul-food.html'),
    ('busan-capsule', 'https://obaoba0808.github.io/Travel-Lab/busan-capsule.html'),
    ('jeju-island',   'https://obaoba0808.github.io/Travel-Lab/jeju-island.html'),
    ('hualien-taitung','https://obaoba0808.github.io/Travel-Lab/hualien-taitung.html'),
    ('tainan-food',   'https://obaoba0808.github.io/Travel-Lab/tainan-food.html'),
    ('kenting',       'https://obaoba0808.github.io/Travel-Lab/kenting.html'),
    ('bangkok-3days', 'https://obaoba0808.github.io/Travel-Lab/bangkok-3days.html'),
    ('hokkaido-winter','https://obaoba0808.github.io/Travel-Lab/hokkaido-winter.html'),
    ('okinawa',       'https://obaoba0808.github.io/Travel-Lab/okinawa.html'),
    ('tokyo-5days',   'https://obaoba0808.github.io/Travel-Lab/tokyo-5days.html'),
    ('kansai-pass',   'https://obaoba0808.github.io/Travel-Lab/kansai-pass.html'),
]
for name, url in pages:
    try:
        req = urllib.request.urlopen(url, timeout=10)
        html = req.read().decode('utf-8', errors='ignore')
        idx = html.find('class="hero"')
        chunk = html[idx:idx+400] if idx >= 0 else ''
        m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', chunk)
        src = m.group(1) if m else 'NOT FOUND'
        print(f'[OK] {name:20s} HTTP {req.status} | {src[:70]}')
    except Exception as e:
        print(f'[FAIL] {name:20s} {e}')