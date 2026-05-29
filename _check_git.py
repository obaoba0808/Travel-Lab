import subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')

result = subprocess.run(['git', 'show', 'HEAD:kansai-pass.html'], 
                      capture_output=True, text=True, encoding='utf-8', 
                      cwd=r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab')
c = result.stdout
forms = [i for i in range(len(c)) if c[i:i+20]=='class="lead-inline"']
print(f'Found {len(forms)} forms in HEAD')
for i,pos in enumerate(forms):
    foot = c.find('<footer')
    print(f'Form {i+1} @{pos}, footer @{foot}, form<footer={pos<foot}')
