import re, glob

files = [
    'budget-airline-guide.html',
    'busan-4days.html',
    'credit-card-miles-guide.html',
    'japan-drugstore-checklist.html',
    'japan-money-saving-tips.html',
    'korea-money-saving-tips.html',
    'miles-calculator.html',
    'tax-refund-calculator.html',
]

for f in files:
    c = open(f, 'r', encoding='utf-8').read()
    
    # Find the pattern: </a> (last related-card) followed by </div> (related-list)
    # then missing the wrapper </div> before <footer or <p>©
    
    # Pattern: last </a> of related-card → </div> (related-list) → should have another </div> (wrapper) → footer
    # Find: last </div> before <footer that comes after 延伸閱讀
    ext_idx = c.find('延伸閱讀')
    if ext_idx == -1:
        print(f"⚠️  {f}: no 延伸閱讀 found")
        continue
    
    footer_idx = c.find('<footer', ext_idx)
    before_footer = c[:footer_idx]
    
    # We need to insert </div> right before <footer>
    # The structure should be: ... </div>(related-list) </div>(wrapper) <footer ...
    # Currently it's: ... </div>(related-list) <footer ...(missing wrapper close)
    
    # Check what's immediately before <footer
    chunk = c[footer_idx-50:footer_idx+10]
    
    # Insert </div>\n before <footer
    c_new = c[:footer_idx] + '</div>\n' + c[footer_idx:]
    
    open(f, 'w', encoding='utf-8').write(c_new)
    print(f"✅ {f}: inserted missing </div> before <footer>")

print(f"\nDone! Fixed {len(files)} pages.")
