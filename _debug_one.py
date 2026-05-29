import os, re, sys, subprocess
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
fname = 'taiwan-travel.html'

# Get clean version
result = subprocess.run(['git', 'show', f'HEAD~2:{fname}'], cwd=base, capture_output=True)
c = result.stdout.decode('utf-8')
print(f"Clean version: {len(c)} chars")
print(f"Has </main>: {'</main>' in c} at {c.rfind('</main>')}")
print(f"Has lead-inline before: {'lead-inline' in c}")

# Now do the replacement step by step
FORM_HTML = '<section class="lead-inline">TEST_FORM</section>'

if '</main>' in c:
    c2 = c.replace('</main>', '\n' + FORM_HTML + '\n</main>')
    idx = c2.find('lead-inline')
    print(f"\nAfter insert: {len(c2)} chars")
    print(f"lead-inline at: {idx}")
    print(f"Before: ...{c2[max(0,idx-80):idx]}")
    print(f"After: ...{c2[idx:idx+50]}")
