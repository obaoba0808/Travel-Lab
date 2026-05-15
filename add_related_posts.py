import os

base = os.path.dirname(os.path.abspath(__file__))

articles = [
    {'file':'tokyo-5days.html','cat':'日本','region':'japan','title':'東京5天4夜行程｜地鐵教學×景點推薦','img':'tokyo-hero.webp','alt':'東京自由行'},
    {'file':'kansai-pass.html','cat':'日本','region':'japan','title':'關西交通票券指南｜JR Pass省錢攻略','img':'kansai-hero.webp','alt':'關西交通票券'},
    {'file':'hokkaido-winter.html','cat':'日本','region':'japan','title':'北海道冬季賞雪｜5大景點+溫泉推薦','img':'hokkaido-hero.webp','alt':'北海道冬季'},
    {'file':'okinawa.html','cat':'日本','region':'japan','title':'沖繩自駕4天3夜｜美麗海水族館+古宇利島','img':'okinawa-hero.webp','alt':'沖繩自駕'},
    {'file':'kyoto-temples.html','cat':'日本','region':'japan','title':'京都寺廟與楓紅散步地圖','img':'kyoto-hero.webp','alt':'京都寺廟'},
    {'file':'seoul-food.html','cat':'韓國','region':'korea','title':'首爾必吃美食攻略｜換錢+地鐵教學','img':'seoul-hero.webp','alt':'首爾美食'},
    {'file':'busan-capsule.html','cat':'韓國','region':'korea','title':'釜山膠囊列車預約教學','img':'busan-hero.webp','alt':'釜山膠囊列車'},
    {'file':'jeju-island.html','cat':'韓國','region':'korea','title':'濟州島自駕環島3天2夜','img':'jeju-hero.webp','alt':'濟州島環島'},
    {'file':'hualien-taitung.html','cat':'台灣','region':'taiwan','title':'花東三天兩夜行程｜太魯閣步道+民宿','img':'hualien-hero.webp','alt':'花東行程'},
    {'file':'tainan-food.html','cat':'台灣','region':'taiwan','title':'台南美食牛肉湯攻略','img':'tainan-hero.webp','alt':'台南美食'},
    {'file':'kenting.html','cat':'台灣','region':'taiwan','title':'墾丁三天兩夜海景攻略','img':'kenting-hero.webp','alt':'墾丁攻略'},
    {'file':'chiang-mai.html','cat':'東南亞','region':'sea','title':'清邁7天數位遊牧指南','img':'chiangmai-hero.webp','alt':'清邁遊牧'},
    {'file':'bangkok-3days.html','cat':'東南亞','region':'sea','title':'曼谷3天2夜吃貨攻略','img':'bangkok-hero.webp','alt':'曼谷美食'},
]

cat_links = {'日本':'japan-travel.html','韓國':'korea-travel.html','台灣':'taiwan-travel.html','東南亞':'southeast-asia.html'}

def get_related(current):
    related = [a for a in articles if a['file'] != current['file'] and a['region'] == current['region']]
    if len(related) < 3:
        others = [a for a in articles if a['file'] != current['file'] and a['region'] != current['region']]
        related.extend(others)
    return related[:3]

def make_related_html(current):
    related = get_related(current)
    lines = ['<div class="related-posts">', '  <h2 class="section-title">📖 延伸閱讀</h2>', '  <div class="related-list">']
    for r in related:
        lines.append(f'    <a href="{r["file"]}" class="related-card">')
        lines.append(f'      <div class="post-thumb"><img loading="lazy" src="images/{r["img"]}" alt="{r["alt"]}" width="1536" height="1024"></div>')
        lines.append(f'      <div class="post-body">')
        lines.append(f'        <span class="cat-tag">{r["cat"]}自由行</span>')
        lines.append(f'        <h3>{r["title"]}</h3>')
        lines.append(f'      </div>')
        lines.append(f'    </a>')
    lines.append('  </div>')
    lines.append('</div>')
    return '\n'.join(lines)

marker = '<div class="article-bottom-cta">'
for a in articles:
    fp = os.path.join(base, a['file'])
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    if marker in c:
        rh = make_related_html(a)
        c = c.replace(marker, rh + '\n' + marker)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'OK: {a["file"]}')
    else:
        print(f'SKIP: {a["file"]} (no CTA)')
