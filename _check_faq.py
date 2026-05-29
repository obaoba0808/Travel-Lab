import urllib.request, sys, re
sys.stdout.reconfigure(encoding='utf-8')

for url, label in [
    ('https://golightly.fun/tokyo-5days', 'tokyo-5days WORKS'),
    ('https://golightly.fun/esim-comparison', 'esim-comparison'),
    ('https://golightly.fun/korea-travel', 'korea-travel'),
    ('https://golightly.fun/packing-list-online', 'packing-list-online'),
]:
    html = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
    form = html.find('class="lead-inline"')
    foot = html.find('<footer')
    faqs = [m.start() for m in re.finditer('faq-item', html)]
    last_faq = faqs[-1] if faqs else -1
    print(f'{label}: form@{form}, last_faq@{last_faq}, footer@{foot}')
    print(f'  after_last_faq={form>last_faq}, before_footer={form<foot}')
    if form > 0 and last_faq > 0:
        print(f'  faq->form gap: {form-last_faq} chars')
        print(f'  between: ...{html[last_faq+30:last_faq+120]}...')
    print()
