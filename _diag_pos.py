import urllib.request, sys, re
sys.stdout.reconfigure(encoding='utf-8')

# Check current LIVE site positions for ALL 11 pages
TARGET_PAGES = [
    ('https://golightly.fun/esim-comparison', 'esim-comparison'),
    ('https://golightly.fun/japan-travel', 'japan-travel'),
    ('https://golightly.fun/korea-budget-travel-guide', 'korea-budget-travel-guide'),
    ('https://golightly.fun/korea-travel', 'korea-travel'),
    ('https://golightly.fun/live-japan-budget', 'live-japan-budget'),
    ('https://golightly.fun/packing-list-online', 'packing-list-online'),
    ('https://golightly.fun/packing-list', 'packing-list'),
    ('https://golightly.fun/seasia-budget-travel-guide', 'seasia-budget-travel-guide'),
    ('https://golightly.fun/southeast-asia', 'southeast-asia'),
    ('https://golightly.fun/taiwan-travel-guide', 'taiwan-travel-guide'),
    ('https://golightly.fun/taiwan-travel', 'taiwan-travel'),
]

print('LIVE SITE FORM POSITION CHECK')
print('='*70)
for url, label in TARGET_PAGES:
    html = urllib.request.urlopen(
        urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    ).read().decode('utf-8')
    
    form = html.find('class="lead-inline"')
    foot = html.find('<footer')
    body = html.find('<body')
    
    # Find content FAQ items (in <body>, excluding JS)
    body_html = html[body:]
    faqs = [m.start() for m in re.finditer(r'faq-item', body_html)]
    last_faq_in_body = max(faqs) if faqs else -1
    last_faq_abs = body + last_faq_in_body if last_faq_in_body >= 0 else -1
    
    has_faq = last_faq_abs > 0
    after_faq = form > last_faq_abs if has_faq else False
    before_footer = form < foot
    
    # Determine status
    if not has_faq:
        status = '✅ (no FAQ, before footer)' if before_footer else '❌ (no FAQ, after footer!)'
    else:
        status = '✅ (after FAQ)' if after_faq else '❌ (BEFORE FAQ!)'
    
    print(f'{label:40s} {status}')
    if has_faq:
        print(f'  form@{form}, last_faq@{last_faq_abs}, footer@{foot}')
