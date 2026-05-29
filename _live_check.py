import urllib.request, sys
sys.stdout.reconfigure(encoding='utf-8')

def check_page(url, label):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req, timeout=10)
    html = resp.read().decode('utf-8')
    fi = html.find('class="lead-inline"')
    foot = html.find('<footer')
    faq = html.rfind('faq-item')
    main = html.rfind('</main>')
    head_end = html.find('</head>')
    body_start = html.find('<body')
    print(f'=== {label} ===')
    print(f'  form@{fi}, </head>@{head_end}, <body@{body_start}')
    print(f'  last faq@{faq}, </main>@{main}, <footer@{foot}')
    print(f'  in_body={fi>body_start}, in_head={fi<head_end}, after_faq={fi>faq}, before_footer={fi<foot}')
    if fi >= 0:
        print(f'  context_before: ...{html[max(0,fi-100):fi]}')
        print(f'  context_after: {html[fi:fi+150]}...')
    print()

pages = [
    ('https://golightly.fun/esim-comparison', 'esim-comparison (BROKEN)'),
    ('https://golightly.fun/taiwan-travel', 'taiwan-travel (BROKEN)'),
    ('https://golightly.fun/tokyo-5days', 'tokyo-5days (WORKS)'),
    ('https://golightly.fun/packing-list-online', 'packing-list-online'),
]

for url, label in pages:
    try:
        check_page(url, label)
    except Exception as e:
        print(f'ERROR {label}: {e}')
