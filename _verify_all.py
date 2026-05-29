import os, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

for f in ['korea-budget-travel-guide.html','packing-list-online.html','taiwan-travel-guide.html',
          'seasia-budget-travel-guide.html','packing-list.html','live-japan-budget.html']:
    c = open(os.path.join(base, f), 'r', encoding='utf-8').read()
    fi = c.find('class="lead-inline"')
    faq = c.rfind('faq-item')
    foot = c.find('<footer')
    head_end = c.find('</head>')
    body_start = c.find('<body')
    print(f'{f}:')
    print(f'  form@{fi}, last_faq@{faq}, footer@{foot}')
    print(f'  </head>@{head_end}, <body@{body_start}')
    print(f'  in_head={fi<head_end}, after_faq={fi>faq}, before_footer={fi<foot}')
    print()
