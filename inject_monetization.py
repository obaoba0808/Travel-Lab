import os, re

folder = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'

# Pages that should get monetization (all content pages, NOT legal pages)
TARGET_PAGES = [
    'index.html', 'japan-travel.html', 'korea-travel.html', 'taiwan-travel.html',
    'southeast-asia.html', 'travel-tools.html', 'about.html', 'contact.html',
    'tokyo-5days.html', 'kansai-pass.html', 'hokkaido-winter.html',
    'okinawa.html', 'kyoto-temples.html', 'seoul-food.html',
    'busan-capsule.html', 'jeju-island.html', 'hualien-taitung.html',
    'tainan-food.html', 'kenting.html', 'chiang-mai.html',
    'bangkok-3days.html'
]

SCRIPT_TAG = '<script src="js/monetization.js" defer></script>'

# Also update the GA script to track affiliate clicks
GA_ENHANCE = '''
<script>
  // Track affiliate link clicks via GA4
  document.addEventListener('click', function(e) {
    var link = e.target.closest('[data-affiliate]');
    if (link) {
      if (typeof gtag === 'function') {
        gtag('event', 'affiliate_click', {
          affiliate: link.getAttribute('data-affiliate'),
          page: window.location.pathname
        });
      }
    }
  });
</script>'''

changed = 0
for fname in TARGET_PAGES:
    path = os.path.join(folder, fname)
    if not os.path.exists(path):
        print(f'SKIP (not found): {fname}')
        continue

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'monetization.js' in content:
        print(f'SKIP (already has): {fname}')
        continue

    # Insert before </body>
    if '</body>' in content:
        new_content = content.replace('</body>', GA_ENHANCE + '\n' + SCRIPT_TAG + '\n</body>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        changed += 1
        print(f'OK: {fname}')
    else:
        print(f'WARNING (no </body>): {fname}')

print(f'\nDone: {changed} files updated')
