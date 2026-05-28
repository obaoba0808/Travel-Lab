import os

with open('kansai-pass.html', 'r', encoding='utf-8') as f:
    c = f.read()

with open('__js_check.txt', 'w', encoding='utf-8') as out:
    idx = c.find('function closeLeadPopup')
    end = c.find('}</script>', idx) + 11
    out.write('=== closeLeadPopup ===\n')
    out.write(c[idx:end])
    out.write('\n\n=== scroll listener ===\n')
    idx2 = c.find('addEventListener', c.find('scroll'))
    end2 = c.find('});', idx2) + 3
    out.write(c[idx2:end2+50])

print('Written to __js_check.txt')
