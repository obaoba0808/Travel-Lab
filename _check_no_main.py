import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# These 6 files don't have </main> - need to find their content structure
no_main_files = [
    'korea-budget-travel-guide.html',
    'live-japan-budget.html', 
    'packing-list-online.html',
    'packing-list.html',
    'seasia-budget-travel-guide.html',
    'taiwan-travel-guide.html',
]

for fname in no_main_files:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Find structural markers in the last half of the file
    half = len(c) // 2
    tail = c[half:]
    
    markers = ['</article>', '</section>', '<footer', '<div class="footer"', '<div class="hub-content"']
    results = []
    for m in markers:
        idx = tail.find(m)
        if idx >= 0:
            abs_idx = half + idx
            results.append((abs_idx, m))
    
    results.sort()
    
    with open(os.path.join(base, f'_struct_{fname}'), 'w', encoding='utf-8') as out:
        out.write(f"File: {fname} ({len(c)} chars)\n")
        out.write(f"Half point: {half}\n\n")
        for abs_idx, m in results:
            ctx = c[max(0,abs_idx-40):abs_idx+60]
            out.write(f"@{abs_idx}: {m}\n  context: ...{ctx}\n\n")
    
    print(f"{fname}: {len(results)} markers found")
