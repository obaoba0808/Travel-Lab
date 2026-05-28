import sys
import os

html_path = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\kyoto-temples.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 東山路線
h3_higashiyama = '<h3>東山路线：清水寺 → 二年坂三年坂 → 八坂神社 → 祇園</h3>'
fig_higashiyama = '''<h3>東山路线：清水寺 → 二年坂三年坂 → 八坂神社 → 祇園</h3>
    <figure style="margin:24px 0;text-align:center;">
      <img src="images/kyoto-higashiyama-route.webp" alt="京都東山路線：清水寺、二年坂、祇園｜均在路上" style="width:100%;max-width:900px;border-radius:28px;box-shadow:0 4px 12px rgba(0,0,0,0.10);" width="900" height="675" loading="lazy">
      <figcaption style="margin-top:10px;color:#888;font-size:13px;font-style:italic;">📷 小編體悟：清水寺早上8點前到，遊客還沒湧入，木造舞台在晨光裡特別莊嚴。走下二年坂石板路，兩旁和菓子店飄出甜味，這段路是京都最有「古都感」的散步路線。</figcaption>
    </figure>'''

# 北山路線
h3_kitayama = '<h3>北山路線：金閣寺 → 龍安寺 → 仁和寺 → 嵐山</h3>'
fig_kitayama = '''<h3>北山路線：金閣寺 → 龍安寺 → 仁和寺 → 嵐山</h3>
    <figure style="margin:24px 0;text-align:center;">
      <img src="images/kyoto-kitayama-route.webp" alt="京都北山路線：金閣寺、龍安寺、嵐山竹林｜均在路上" style="width:100%;max-width:900px;border-radius:28px;box-shadow:0 4px 12px rgba(0,0,0,0.10);" width="900" height="675" loading="lazy">
      <figcaption style="margin-top:10px;color:#888;font-size:13px;font-style:italic;">📷 小編體悟：金閣寺的耀眼金色在上午順光時最美，鏡湖池倒映出的畫面一輩子忘不了。龍安寺枯山水15塊石頭怎麼看都湊不齊，禪意就在這種「看不盡」裡。</figcaption>
    </figure>'''

# 南邊路線
h3_minamiji = '<h3>南邊路線：伏見稻荷 → 東福寺 → 宇治</h3>'
fig_minamiji = '''<h3>南邊路線：伏見稻荷 → 東福寺 → 宇治</h3>
    <figure style="margin:24px 0;text-align:center;">
      <img src="images/kyoto-minamiji-route.webp" alt="京都南邊路線：伏見稻荷千本鳥居、東福寺、宇治抹茶｜均在路上" style="width:100%;max-width:900px;border-radius:28px;box-shadow:0 4px 12px rgba(0,0,0,0.10);" width="900" height="675" loading="lazy">
      <figcaption style="margin-top:10px;color:#888;font-size:13px;font-style:italic;">📷 小編體悟：伏見稻荷清晨5點去幾乎包場，千本鳥居一個人走下去超有電影感。下午搭JR去宇治，中村藤吉的抹茶聖代一定要點，苦甜交織的滋味是京都行最棒的結尾。</figcaption>
    </figure>'''

if h3_higashiyama in content:
    content = content.replace(h3_higashiyama, fig_higashiyama, 1)
    print('OK: 東山路線')
else:
    print('MISS: 東山路線 H3')

if h3_kitayama in content:
    content = content.replace(h3_kitayama, fig_kitayama, 1)
    print('OK: 北山路線')
else:
    print('MISS: 北山路線 H3')

if h3_minamiji in content:
    content = content.replace(h3_minamiji, fig_minamiji, 1)
    print('OK: 南邊路線')
else:
    print('MISS: 南邊路線 H3')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('DONE: kyoto-temples.html updated')