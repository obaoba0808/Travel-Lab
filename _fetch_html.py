import urllib.request, sys, re
sys.stdout.reconfigure(encoding='utf-8')

def analyze(url, label):
    html = urllib.request.urlopen(
        urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    ).read().decode('utf-8')
    print(f'\n=== {label} ({len(html)} chars) ===')
    
    # Find all major structural elements in the last 30%
    half = len(html) * 7 // 10
    tail = html[half:]
    
    structural = list(re.finditer(r'<(main|aside|section|footer|div)[^>]*/?>', tail))
    for m in structural[-15:]:
        abs_pos = half + m.start()
        print(f'  @{abs_pos}: {m.group()[:60]}')
    
    # Form position
    fi = html.find('class="lead-inline"')
    foot = html.find('<footer')
    faq = html.rfind('faq-item')
    print(f'\n  form@{fi}, faq@{faq}, footer@{foot}')
    print(f'  after_faq={fi>faq}, before_footer={fi<foot}')

pages = [
    ('https://golightly.fun/esim-comparison', 'esim-comparison'),
    ('https://golightly.fun/tokyo-5days', 'tokyo-5days (WORKS)'),
    ('https://golightly.fun/korea-travel', 'korea-travel'),
]
for url, label in pages:
    try:
        analyze(url, label)
    except Exception as e:
        print(f'ERROR {label}: {e}')
