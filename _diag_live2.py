import urllib.request, sys, re
sys.stdout.reconfigure(encoding='utf-8')

for url, label in [
    ('https://golightly.fun/korea-budget-travel-guide', 'korea-budget-travel-guide'),
    ('https://golightly.fun/live-japan-budget', 'live-japan-budget'),
    ('https://golightly.fun/seasia-budget-travel-guide', 'seasia-budget-travel-guide'),
    ('https://golightly.fun/taiwan-travel-guide', 'taiwan-travel-guide'),
    ('https://golightly.fun/tokyo-5days', 'tokyo-5days (ref)'),
]:
    try:
        html = urllib.request.urlopen(
            urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        ).read().decode('utf-8')
        faqs = [(m.start(), m.group()) for m in re.finditer(r'faq-item[^-"\s]*', html)]
        body_start = html.find('<body')
        form = html.find('class="lead-inline"')
        foot = html.find('<footer')
        print(f'\n=== {label} ({len(html)} chars) ===')
        print(f'FAQ positions: {[p for p,_ in faqs]}')
        print(f'Body start: {body_start}')
        print(f'Form: {form}, Footer: {foot}')
        
        # Show context around last FAQ
        if faqs:
            last_pos = faqs[-1][0]
            print(f'Last faq context: ...{html[max(0,last_pos-30):last_pos+100]}...')
            
            # Find closing div from last FAQ
            remainder = html[last_pos:]
            closes = [(m.start(), m.group()) for m in re.finditer(r'</div>', remainder[:500])]
            print(f'Closing divs from last FAQ: {closes[:8]}')
    except Exception as e:
        print(f'ERROR {label}: {e}')
