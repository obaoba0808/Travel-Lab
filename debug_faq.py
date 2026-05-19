import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for f in ['busan-capsule.html', 'hokkaido-winter.html', 'seoul-food.html', 'tainan-food.html', 'kansai-pass.html', 'hualien-taitung.html']:
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    # Find FAQ section
    idx = c.find('faq-section')
    if idx < 0:
        idx = c.find('常見問題')
    if idx < 0:
        continue
    chunk = c[idx:idx+800]
    # Count faq-item occurrences in this section
    fi_count = chunk.count('faq-item')
    print(f'=== {f}: faq-item in first 800 chars of FAQ section = {fi_count} ===')
    print(chunk[:500])
    print()
