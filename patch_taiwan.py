# -*- coding: utf-8 -*-
with open('taiwan-travel.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = '台灣最棒的地方在於：它對預算有限的旅客超級友善，而且交通超級方便。NT$2,000 可以從台北搭高鐵到墾丁、NT$500 可以在台南吃三頓牛肉麵、NT$1,500 可以在花蓮住一晚有海景的民宿。加上台灣人超熱情（「你有吃飽嗎？」是全世界最暖的問候語），這就是為什麼我每年至少深度旅遊台灣 3-4 次。</p>'

new = '台灣最棒的地方在於：它對預算有限的旅客超級友善，而且交通超級方便。NT$2,000 可以從台北搭高鐵到墾丁、NT$500 可以在台南吃三頓牛肉麵、NT$1,500 可以在花蓮住一晚有海景的民宿。加上台灣人超熱情（「你有吃飽嗎？」是全世界最暖的問候語），這就是為什麼我每年至少深度旅遊台灣 3-4 次。</p>\n  <p style="line-height:1.9;margin-bottom:16px;color:#555;font-size:14px;"><strong>💡 個人真心話：</strong>我以前覺得「台北有什麼好玩的？」——直到我帶日本朋友去台北，才發現「我們每天經過的地方，原來這麼有趣！」象山看101、士林夜市吃大餅包、西門町逛潮流小店…… 台北其實是「重遊率最高」的城市，因為它一直在變。</p>'

if old in c:
    c = c.replace(old, new)
    open('taiwan-travel.html', 'w', encoding='utf-8').write(c)
    print('OK')
else:
    print('NOT FOUND')
