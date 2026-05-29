import os, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
for f in ['tokyo-5days.html', 'esim-comparison.html', 'taiwan-travel.html',
          'packing-list-online.html', 'live-japan-budget.html']:
    c = open(os.path.join(base, f), 'r', encoding='utf-8').read()
    fi = c.find('class="lead-inline"')
    faq = c.rfind('faq-item')
    main = c.rfind('</main>')
    foot = c.find('<footer')
    head = c.find('</head>')
    body = c.find('<body')
    print(f'=== {f} ===')
    print(f'  form@{fi}, </head>@{head}, <body@{body}')
    print(f'  last faq@{faq}, </main>@{main}, <footer@{foot}')
    print(f'  in_body={fi>body}, in_head={fi<head}, after_faq={fi>faq}, before_footer={fi<foot}')
    print(f'  context_before: ...{c[max(0,fi-80):fi]}')
    print(f'  context_after: {c[fi:fi+120]}...')
    print()
