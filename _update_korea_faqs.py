# -*- coding: utf-8 -*-

# ===== Seoul Food - Update JSON-LD FAQ to 8 questions =====
with open('seoul-food.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = '{"@type":"Question","name":"韓國餐廳一個人可以吃嗎？","acceptedAnswer":{"@type":"Answer","text":"烤肉類通常2人起點，但越來越多一人烤肉店。部隊鍋、湯飯類、拌飯等本來就是一人份。建議避開標示「2人起」的餐廳即可。"}}]}</script>'

new = '{"@type":"Question","name":"韓國餐廳一個人可以吃嗎？","acceptedAnswer":{"@type":"Answer","text":"烤肉類通常2人起點，但越來越多一人烤肉店。部隊鍋、湯飯類、拌飯等本來就是一人份。建議避開標示「2人起」的餐廳即可。"}},{"@type":"Question","name":"首爾哪裡可以吃到正宗韓式烤肉？","acceptedAnswer":{"@type":"Answer","text":"弘大「Maple Tree House」平價好吃、江南「Potful」豬五花肉專賣、明洞「姜虎東烤肉」連鎖品質穩定。預算每人₩15,000-30,000，建議提前用APP排隊。"}},{"@type":"Question","name":"首爾咖啡廳推薦？","acceptedAnswer":{"@type":"Answer","text":"弘大和聖水洞是咖啡廳聚集區。推薦：①聖水洞Cafe Onion ②弘大Born Coffee ③漢南洞Cheetah Electric。韓國咖啡廳氛圍感極強，拍照打卡必去。"}},{"@type":"Question","name":"首爾街頭小吃必吃？","acceptedAnswer":{"@type":"Answer","text":"①辣炒年糕（₩3,000）②魚糕串（₩1,000）③韓式煎餅（₩5,000）④紫菜包飯（₩2,000）⑤旋轉烤雞（₩8,000）。廣藏市場和明洞街頭小吃最多最集中。"}},{"@type":"Question","name":"首爾冬天會下雪嗎？","acceptedAnswer":{"@type":"Answer","text":"12-2月都有可能下雪，但近年暖化雪量減少。想要看雪景建議1月去，機率最高。雪中的景福宮和北村韓屋超美，記得穿保暖衣物。"}}]}</script>'

if old in c:
    c = c.replace(old, new, 1)
    with open('seoul-food.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('seoul-food: JSON-LD FAQ updated to 8 questions')
else:
    print('seoul-food: pattern not found')

# ===== Korea Budget - Update JSON-LD FAQ to 6 questions =====
with open('korea-budget.html', 'r', encoding='utf-8') as f:
    c = f.read()

old2 = '{"@type":"Question","name":"T-money卡怎麼省錢？","acceptedAnswer":{"@type":"Answer","text":"T-money卡地鐵單程₩1,400-2,000（比現金購票便宜₩100），還可在便利店消費。全程交通費約₩30,000-50,000/5天。建議預先加值₩50,000。"}}]}]}</script>'

new2 = '{"@type":"Question","name":"T-money卡怎麼省錢？","acceptedAnswer":{"@type":"Answer","text":"T-money卡地鐵單程₩1,400-2,000（比現金購票便宜₩100），還可在便利店消費。全程交通費約₩30,000-50,000/5天。建議預先加值₩50,000。"}},{"@type":"Question","name":"首爾哪裡換錢最划算？","acceptedAnswer":{"@type":"Answer","text":"明洞大使館前的換錢所匯率最好，比銀行高約2-3%。携帶現金換匯，不要用信用卡刷外幣（匯率差）。"}},{"@type":"Question","name":"退稅怎麼申請？","acceptedAnswer":{"@type":"Answer","text":"消費滿₩50,000可申請退稅（10%）。貼有「Tax Free」標誌的商店消費後，向店家拿退稅單，在機場海關出示退稅物品辦理。電子退稅更方便。"}},{"@type":"Question","name":"韓國機票最便宜什麼時候買？","acceptedAnswer":{"@type":"Answer","text":"提前2-3個月、選週二週三出發、廉航（德威、易斯達、釜山航空）比大航便宜30-50%。避開農曆新年、中秋連假和暑假旺季。用Skyscanner設價格提醒抓低價。"}},{"@type":"Question","name":"韓國住宿怎麼選最划算？","acceptedAnswer":{"@type":"Answer","text":"首爾：弘大和東大門的Guest House最平價（NT$500-1,500/晚），明洞位置好但較貴。釜山：海雲塔附近民宿CP值高。用Agoda或HotelsCombined比價，韓國住宿比日本便宜不少。"}}]}]}</script>'

if old2 in c:
    c = c.replace(old2, new2, 1)
    with open('korea-budget.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('korea-budget: JSON-LD FAQ updated to 6 questions')
else:
    print('korea-budget: pattern not found')

print('Done.')