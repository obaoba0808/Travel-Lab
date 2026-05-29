import sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['esim-comparison.html', 'live-japan-budget.html']:
    c=open(f'C:\\Users\\FH01\\.qclaw\\workspace-cwapojim0yfmyvq8\\Travel-Lab\\{fname}','r',encoding='utf-8').read()
    footer=c.find('<footer')
    # Find the </div> that closes the page wrapper (just before <!-- FOOTER -->)
    foot_comment=c.find('<!-- FOOTER -->')
    if foot_comment>0:
        before_foot=c[:foot_comment]
    else:
        before_foot=c[:footer]
    last_div_before_foot=before_foot.rfind('</div>')
    print(f'\n=== {fname} ===')
    print(f'footer tag: @{footer}')
    print(f'<!-- FOOTER -->: @{foot_comment}')
    print(f'last </div> before footer: @{last_div_before_foot}')
    print(f'Context: {repr(c[last_div_before_foot-80:last_div_before_foot+50])}')
    print(f'After last div: {repr(c[last_div_before_foot:last_div_before_foot+50])}')
