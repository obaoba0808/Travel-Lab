# -*- coding: utf-8 -*-
"""
為 kyoto-temples.html 和 esim-comparison.html 增加內部連結
提升 SEO 內部連結結構
"""

import re

def add_internal_links_kyoto():
    """為京都頁面增加內部連結"""
    with open('kyoto-temples.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定義要加入的內部連結（在適當位置）
    links_to_add = [
        # (搜尋模式, 替換為, 說明)
        (r'(關西交通票券完整比較)', r'<a href="kansai-pass.html" style="color:inherit;text-decoration:underline;">\1</a>'),
        (r'(大阪美食行程)', r'<a href="osaka-food.html" style="color:inherit;text-decoration:underline;">\1</a>'),
        (r'(日本機票省錢攻略)', r'<a href="japan-budget-guide.html" style="color:inherit;text-decoration:underline;">\1</a>'),
    ]
    
    modified = False
    for pattern, replacement, desc in links_to_add:
        if re.search(pattern, content) and not re.search(r'href=".*?"' + pattern, content):
            content = re.sub(pattern, replacement, content, count=1)
            modified = True
            print(f'Kyoto: Added link - {desc}')
    
    # 在合適位置手動加入內部連結推薦區塊
    h2_momiji = '<h2>🍁 京都賞楓攻略</h2>'
    if h2_momiji in content:
        pos = content.find(h2_momiji)
        if pos > 0 and 'class="related-posts"' not in content[pos:pos+500]:
        insert_pos = content.find('<h2>🍁 京都賞楓攻略</h2>')
        if insert_pos > 0:
            related_block = '''
<div style="background:#f5f5f5;padding:20px;border-radius:12px;margin:24px 0;">
  <h4 style="margin:0 0 12px;color:#333;">📖 相關文章推薦</h4>
  <ul style="margin:0;padding-left:20px;line-height:1.8;">
    <li><a href="kansai-pass.html" style="color:#078E8A;font-weight:600;">關西交通票券完整比較｜JR Pass vs ICOCA</a></li>
    <li><a href="osaka-food.html" style="color:#078E8A;font-weight:600;">大阪美食地圖｜道頓堀必吃清單</a></li>
    <li><a href="japan-budget-guide.html" style="color:#078E8A;font-weight:600;">日本旅遊預算指南｜機票+住宿+交通</a></li>
    <li><a href="tokyo-5days.html" style="color:#078E8A;font-weight:600;">東京5天4夜行程｜地鐵教學×景點推薦</a></li>
  </ul>
</div>
'''
            content = content[:insert_pos] + related_block + '\n' + content[insert_pos:]
            modified = True
            print('Kyoto: Added related posts block before 賞楓攻略')
    
    if modified:
        with open('kyoto-temples.html', 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def add_internal_links_esim():
    """為 eSIM 頁面增加內部連結"""
    with open('esim-comparison.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 在合適位置加入內部連結推薦區塊
    if '<h2>🌏 各地區 eSIM 方案詳細比較</h2>' in content:
        insert_pos = content.find('<h2>🌏 各地區 eSIM 方案詳細比較</h2>')
        if insert_pos > 0:
            related_block = '''
<div style="background:#e3f2fd;padding:20px;border-radius:12px;margin:24px 0;border-left:4px solid #1565C0;">
  <h4 style="margin:0 0 12px;color:#1565C0;">📱 出國前必看攻略</h4>
  <ul style="margin:0;padding-left:20px;line-height:1.8;">
    <li><a href="japan-budget-guide.html" style="color:#1565C0;font-weight:600;">日本旅遊預算表｜機票+住宿+交通+美食</a></li>
    <li><a href="korea-budget.html" style="color:#1565C0;font-weight:600;">韓國旅遊預算解析｜首爾+釜山花費指南</a></li>
    <li><a href="travel-tools.html" style="color:#1565C0;font-weight:600;">旅遊工具推薦｜eSIM、換匯、行李秤</a></li>
    <li><a href="packing-list.html" style="color:#1565C0;font-weight:600;">各國旅遊打包清單｜照著勾就對了</a></li>
  </ul>
</div>
'''
            content = content[:insert_pos] + related_block + '\n' + content[insert_pos:]
            modified = True
            print('eSIM: Added related posts block before 各地區方案比較')
    
    if modified:
        with open('esim-comparison.html', 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

if __name__ == '__main__':
    print('Adding internal links...')
    
    k_modified = add_internal_links_kyoto()
    e_modified = add_internal_links_esim()
    
    if k_modified or e_modified:
        print('\nDone! Internal links added successfully.')
    else:
        print('\nNo changes needed or already exists.')
