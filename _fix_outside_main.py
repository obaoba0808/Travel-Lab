import re, glob

problem_files = [
    'angkor-wat-2days.html',
    'korea-travel.html', 
    'kualalumpur-3days.html',
    'singapore-3days.html',
    'southeast-asia.html',
    'taiwan-travel.html',
]

for f in problem_files:
    c = open(f, 'r', encoding='utf-8').read()
    
    main_end = c.find('</main>')
    footer_start = c.find('<footer')
    
    if main_end == -1 or footer_start == -1:
        print(f"⚠️  {f}: skipping, can't find markers")
        continue
    
    # Get the orphaned content
    orphaned = c[main_end + len('</main>'):footer_start]
    
    # The fix: move </main> to just before <footer>
    # This puts all content back inside <main>
    new_c = c[:main_end] + orphaned + '\n</main>\n' + c[footer_start:]
    
    open(f, 'w', encoding='utf-8').write(new_c)
    print(f"✅ {f}: moved {len(orphaned)} chars of content back inside <main>")

print(f"\nDone! Fixed {len(problem_files)} pages.")
