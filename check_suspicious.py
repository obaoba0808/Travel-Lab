import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

suspicious = ['busan-capsule.html','hokkaido-winter.html','hualien-taitung.html','kansai-pass.html','seoul-food.html','tainan-food.html','japan-travel.html','southeast-asia.html','taiwan-travel.html','korea-budget.html','travel-tools.html']

for f in suspicious:
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    # Find ALL faq-related patterns
    patterns = re.findall(r'faq-[qa][^"]*"[^>]*>(.+?)</div>', c)
    questions = [p.strip()[:60] for p in patterns if len(p.strip()) > 5 and not p.strip().startswith('<')]
    print(f'{f}: {len(questions)} FAQ-Qs found')
    for q in questions:
        q_clean = re.sub(r'<[^>]+>', '', q).strip()
        if q_clean:
            print(f'  - {q_clean}')
    print()
