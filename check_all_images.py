import os, re, urllib.request

workspace = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'
article_pages = ['tokyo-5days.html','kansai-pass.html','hokkaido-winter.html',
                 'okinawa.html','kyoto-temples.html','seoul-food.html',
                 'busan-capsule.html','jeju-island.html','hualien-taitung.html',
                 'tainan-food.html','kenting.html','chiang-mai.html','bangkok-3days.html']

all_urls = {}  # url -> [list of pages using it]

for fname in article_pages:
    path = os.path.join(workspace, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    imgs = re.findall(r'https://images\.unsplash\.com/photo-[^"\']+', content)
    for img in imgs:
        base_url = img.split('?')[0]
        if base_url not in all_urls:
            all_urls[base_url] = []
        all_urls[base_url].append(fname)

# Find duplicates and broken
print('=== URLs used by multiple pages ===')
for url, pages in sorted(all_urls.items(), key=lambda x: -len(x[1])):
    if len(pages) > 1:
        print(f'{url} -> {pages}')

print()
print('=== Testing all unique URLs ===')
for url in sorted(all_urls.keys()):
    # Extract photo ID
    photo_id = url.split('/')[-1]
    test_url = url + '?auto=format&fit=crop&w=600&q=80'
    try:
        req = urllib.request.Request(test_url, headers={'User-Agent':'Mozilla/5.0'})
        r = urllib.request.urlopen(req, timeout=10)
        status = r.status
    except Exception as e:
        status = 'FAIL:' + str(e)[:30]
    print(f'{photo_id}: {status}')
