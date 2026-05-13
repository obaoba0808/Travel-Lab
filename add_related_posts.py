import re, os

articles_info = {
    'tokyo-5days.html': {
        'category': '日本自由行', 'category_url': 'japan-travel.html',
        'related_title': '關西交通票券指南｜JR Pass、周遊卡、ICOCA 省錢決策樹',
        'related_url': 'kansai-pass.html',
        'related_img': 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '去完東京想順遊關西？JR Pass 值不值得買、大阪周遊卡怎麼用最省、ICOCA 搭配技巧，一次搞懂日本關西交通。',
    },
    'kansai-pass.html': {
        'category': '日本自由行', 'category_url': 'japan-travel.html',
        'related_title': '北海道冬季賞雪攻略｜5大必去景點、禦寒穿搭、溫泉推薦',
        'related_url': 'hokkaido-winter.html',
        'related_img': 'https://images.unsplash.com/photo-1491002052546-bf38f186af56?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '冬天最值得一去的日本目的地！札幌雪祭、函館百萬夜景、登別雪景露天風呂，北海道冬季完整攻略。',
    },
    'hokkaido-winter.html': {
        'category': '日本自由行', 'category_url': 'japan-travel.html',
        'related_title': '沖繩自駕4天3夜攻略｜美麗海水族館到古宇利島',
        'related_url': 'okinawa.html',
        'related_img': 'https://images.unsplash.com/photo-1598866594230-a7c12756260f?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '不想受凍？沖繩一年四季都暖和！自駕環島路線、美麗海水族館、古宇利大橋，亞熱帶海島度假完整規劃。',
    },
    'okinawa.html': {
        'category': '日本自由行', 'category_url': 'japan-travel.html',
        'related_title': '京都寺廟與楓紅散步地圖｜清水寺、金閣寺、伏見稻荷',
        'related_url': 'kyoto-temples.html',
        'related_img': 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '千年古都的靜謐之美，清水寺木造舞台、金閣寺金色倒影、伏見稻荷千本鳥居，3條散步路線帶你走進京都。',
    },
    'kyoto-temples.html': {
        'category': '日本自由行', 'category_url': 'japan-travel.html',
        'related_title': '東京5天4夜省錢行程攻略｜地鐵教學、住宿推薦',
        'related_url': 'tokyo-5days.html',
        'related_img': 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '第一次去東京？5天4夜行程規劃、地鐵搭到會、新宿/淺草/秋葉原住宿推薦，新手也能輕鬆上手。',
    },
    'seoul-food.html': {
        'category': '韓國自由行', 'category_url': 'korea-travel.html',
        'related_title': '釜山膠囊列車預約教學｜海景咖啡、住宿推薦',
        'related_url': 'busan-capsule.html',
        'related_img': 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '首爾吃飽了想去海邊？釜山膠囊列車、海雲台海景咖啡、甘川文化村，韓國第二大城市完整攻略。',
    },
    'busan-capsule.html': {
        'category': '韓國自由行', 'category_url': 'korea-travel.html',
        'related_title': '濟州島自駕環島3天2夜｜城山日出峰、牛島、漢拏山',
        'related_url': 'jeju-island.html',
        'related_img': 'https://images.unsplash.com/photo-1551818255-e6e10975bc17?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '韓國免簽蜜月勝地！自駕環島路線、城山日出峰日出、牛島海岸公路，濟州島3天2夜全記錄。',
    },
    'jeju-island.html': {
        'category': '韓國自由行', 'category_url': 'korea-travel.html',
        'related_title': '首爾必吃美食攻略｜5大必吃、換錢攻略、T-money教學',
        'related_url': 'seoul-food.html',
        'related_img': 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '首爾不只是烤肉和炸鸡！從明洞街頭小吃到傳統市場，5大必吃美食、換錢技巧、交通卡使用完整指南。',
    },
    'hualien-taitung.html': {
        'category': '台灣旅遊', 'category_url': 'taiwan-travel.html',
        'related_title': '台南美食牛肉湯攻略｜5家老店、國華街地圖、老屋咖啡',
        'related_url': 'tainan-food.html',
        'related_img': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '台灣美食之都！5家必吃牛肉湯老店、國華街採買攻略、老屋咖啡廳巡禮，台南一日遊路線規劃。',
    },
    'tainan-food.html': {
        'category': '台灣旅遊', 'category_url': 'taiwan-travel.html',
        'related_title': '墾丁三天兩夜海景與夜市攻略｜南灣戲水、鵝鑾鼻打卡',
        'related_url': 'kenting.html',
        'related_img': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '國境之南的陽光沙灘！南灣戲水、龍磐公園看海、鵝鑾鼻燈塔打卡、墾丁大街夜市吃爆，墾丁3天2夜全攻略。',
    },
    'kenting.html': {
        'category': '台灣旅遊', 'category_url': 'taiwan-travel.html',
        'related_title': '花東三天兩夜｜太魯閣步道、七星潭、民宿推薦',
        'related_url': 'hualien-taitung.html',
        'related_img': 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '台灣最美的一條公路！太魯閣峽谷步道、七星潭鵝卵石海岸、花蓮/台東溫泉民宿，花東3天2夜深度之旅。',
    },
    'chiang-mai.html': {
        'category': '東南亞自由行', 'category_url': 'southeast-asia.html',
        'related_title': '曼谷3天2夜吃貨攻略｜洽圖洽、唐人街、10大美食',
        'related_url': 'bangkok-3days.html',
        'related_img': 'https://images.unsplash.com/photo-1524413840807-0c3cb6fa808d?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '從清邁飛曼谷只要1.5小時！洽圖洽周末市集、唐人街美食、昭披耶河夜景，曼谷吃貨完整攻略。',
    },
    'bangkok-3days.html': {
        'category': '東南亞自由行', 'category_url': 'southeast-asia.html',
        'related_title': '清邁7天數位遊牧指南｜咖啡廳、長租公寓、簽證攻略',
        'related_url': 'chiang-mai.html',
        'related_img': 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=600&q=80',
        'related_excerpt': '數位遊牧人的天堂！月租NT$5000起、優質咖啡廳推薦、長期簽證申請，清邁7天深度生活體驗。',
    },
}

count = 0
for filename, info in articles_info.items():
    filepath = os.path.join('.', filename)
    if not os.path.exists(filepath):
        print(f'SKIP: {filename} not found')
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'article-related' in content:
        print(f'SKIP: {filename} already has related section')
        continue

    html = (
        '\n<!-- RELATED POST -->\n'
        '<div class="article-related">\n'
        f'  <a href="{info["category_url"]}" class="cat-tag">{info["category"]}</a>\n'
        '  <div class="related-card">\n'
        f'    <a href="{info["related_url"]}" class="post-thumb"><img src="{info["related_img"]}" alt="{info["related_title"]}"></a>\n'
        '    <div class="post-body">\n'
        f'      <h3><a href="{info["related_url"]}">{info["related_title"]}</a></h3>\n'
        '      <div class="post-meta"><span class="author">Travel Lab</span><span class="date">2026-05-13</span></div>\n'
        f'      <p class="post-excerpt">{info["related_excerpt"]}</p>\n'
        f'      <a href="{info["related_url"]}" class="read-more">繼續閱讀 &rarr;</a>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>'
    )

    # Insert before <!-- FOOTER --> or <footer
    pattern = r'(</section>\s*</div>\s*)(<!-- FOOTER -->|<footer)'
    new_content = re.sub(pattern, r'\1' + html + r'\n\2', content)

    if new_content == content:
        pattern2 = r'(</section>\s*</div>\s*)<footer'
        new_content = re.sub(pattern2, r'\1' + html + r'\n<footer', content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'OK: {filename}')
    else:
        print(f'FAIL: {filename}')

print(f'\nDone! Updated {count}/{len(articles_info)} files')
