import os

with open('kansai-pass.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function closeLeadPopup')
end = c.find('</script>', idx)
print('=== closeLeadPopup ===')
print(c[idx:end])

print('\n=== scroll listener ===')
idx2 = c.find('addEventListener', c.find('scroll'))
end2 = c.find('});', idx2) + 3
print(c[idx2:end2+50])
