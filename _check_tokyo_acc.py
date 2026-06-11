import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
path = os.path.join(BASE, 'tokyo-accommodation.html')

with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# div 平衡检查
opens = len(re.findall(r'<div[\s>]', c))
closes = c.count('</div>')
print(f'div: opens={opens}, closes={closes}, diff={opens-closes}')

# 找 article-container 开始和结束
ac_start = c.find('class="article-container"')
ac_end = c.find('<!-- /article-container -->')
print(f'\narticle-container: start={ac_start}, end={ac_end}')
if ac_start != -1 and ac_end != -1:
    ac_content = c[ac_start:ac_end+25]
    # 检查这个区域内的 div 平衡
    ac_opens = len(re.findall(r'<div[\s>]', ac_content))
    ac_closes = ac_content.count('</div>')
    print(f'  内部 div: opens={ac_opens}, closes={ac_closes}, diff={ac_opens-ac_closes}')

# 检查 col-center
cc_start = c.find('class="col-center"')
# 找对应的关闭
cc_search = c.find('col-center', cc_start + 10)
print(f'\ncol-center first at: {cc_start}')

# 检查 three-col-wrapper 到 FOOTER 之间的结构
tcw = c.find('three-col-wrapper')
foot = c.find('<!-- FOOTER -->')
section = c[tcw:foot]
s_opens = len(re.findall(r'<div[\s>]', section))
s_closes = section.count('</div>')
print(f'\nthree-col-wrapper → FOOTER 区段:')
print(f'  div: opens={s_opens}, closes={s_closes}, diff={s_opens-s_closes}')
print(f'  长度: {len(section)} 字符')

# 打印最后 500 字符看关闭结构
print('\n=== 区段末尾 600 字符 ===')
print(section[-600:])
