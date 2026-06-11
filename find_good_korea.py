import subprocess, sys

commits = ['64456b4','cd60631','a52b817','7f3f503','a84ffd9','b7b1e95','004dde4','aaa4e63']
for c in commits:
    result = subprocess.run(['git','show', c+':korea-transport.html'], capture_output=True, encoding='utf-8', errors='ignore')
    content = result.stdout
    size = len(content)
    ac_start = content.find('<div class="article-container">')
    ac_end = content.find('<!-- /article-container -->')
    ac_len = ac_end - ac_start - 48 if ac_start > 0 and ac_end > 0 else -1
    div_open = content.count('<div')
    div_close = content.count('</div>')
    print(f'{c}: size={size}, article-container={ac_len}, div={div_open}/{div_close}')
