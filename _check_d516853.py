import subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')

result = subprocess.run(['git', 'show', 'd516853:kansai-pass.html'], 
                      capture_output=True, text=True, encoding='utf-8',
                      cwd=r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab')
c = result.stdout
print(f'Total length: {len(c)}')
print(f'lead-inline count: {c.count("lead-inline")}')
forms = [i for i in range(len(c)) if c[i:i+20]=='class="lead-inline"']
print(f'Forms found: {len(forms)} at positions {forms}')
