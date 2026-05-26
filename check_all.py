import re, os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print('Checking Chinese character counts for all HTML files:\n')
results = []
for f in sorted(html_files):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', content)
    count = len(chinese_chars)
    status = 'PASS' if count >= 2500 else 'FAIL'
    results.append((f, count, status))

# Sort by count
results.sort(key=lambda x: x[1])
for f, count, status in results:
    mark = '[OK]' if status == 'PASS' else '[XX]'
    print(f'{mark} {f}: {count}')
    
pass_count = sum(1 for _,_,s in results if s=='PASS')
fail_count = sum(1 for _,_,s in results if s=='FAIL')
print(f'\n[OK] Pass: {pass_count}/{len(results)} files')
print(f'[XX] Fail: {fail_count}/{len(results)} files')
