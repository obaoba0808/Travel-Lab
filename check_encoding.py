import os
issues = []
clean = []
for f in os.listdir('.'):
    if f.endswith('.html'):
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                content = fh.read()
            bad = sum(1 for c in content if ord(c) == 0xfffd)
            if bad > 0:
                issues.append(f'{f}: {bad} bad chars')
            else:
                clean.append(f)
        except Exception as e:
            issues.append(f'{f}: ERROR {str(e)[:50]}')

print('ENCODING ISSUES:')
for i in issues:
    print(' ', i)
print()
print(f'Clean files: {len(clean)}')
