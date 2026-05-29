import subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')

commits = ['4f1bffa', '1e4ce20', '7a200b2', 'b11fd3f', '933dbb2']
for c in commits:
    result = subprocess.run(['git', 'show', f'{c}:kansai-pass.html'], 
                          capture_output=True, text=True, encoding='utf-8')
    html = result.stdout
    form = html.find('class="lead-inline"')
    foot = html.find('<footer')
    print(f'{c}: form@{form}, footer@{foot}, form<footer={form < foot}')
