# -*- coding: utf-8 -*-

with open('okinawa.html', 'r', encoding='utf-8') as f:
    content = f.read()

images_config = [
    {
        'keyword': '古宇利島',
        'image': 'castle-twilight.webp',
        'alt': '古宇利島海洋之心古堡暮光',
        'experience': '古宇利的「海洋之心」愛心形狀窗戶超夯！建議早上先去，人少又好拍照。旁边就是古宇利海灘，情人橋夕陽超美。我去的時候剛好遇到有人在這裡求婚，浪漫爆表!'
    },
    {
        'keyword': '海中道路',
        'image': 'kai-chu-doro.webp',
        'alt': '沖繩海上道路drive-thru',
        'experience': '海中道路开车可以直接停在海上!旁边就是浅滩，可以下去玩水。记得带换洗衣服，夏天超多人在这裡戏水。这里也是电影「女友男友」的取景地!'
    },
    {
        'keyword': '瀨長島',
        'image': 'senganna.webp',
        'alt': '瀨長島龍捲風觀景台',
        'experience': '瀨長島的「龍捲風」觀景台可以看飛機起降的超最近距離!旁邊的瀨長海灘也很棒，夕陽時分超級療癒。建議预留1-2小时慢慢逛!'
    }
]

def create_image_block(config):
    return f'''<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0;transition:transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
  <img src="images/{config['image']}" alt="{config['alt']}" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);cursor:pointer;" loading="lazy">
  <p style="margin:10px 0 0 0;font-size:13px;color:#0ABAB5;line-height:1.6;font-style:italic;text-align:left;">📝 小編個人體驗：{config['experience']}</p>
</div>'''

inserted_count = 0

for config in images_config:
    if config['keyword'] in content and config['image'] not in content:
        # 找到 keyword 後的第一個 </div> 閉標籤（day-card 結束）
        import re
        pattern = f'{config["keyword"]}.*?</div>'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            # 在 day-card 結束後插入圖片
            end_pos = match.end()
            insert_html = create_image_block(config)
            content = content[:end_pos] + insert_html + content[end_pos:]
            inserted_count += 1
            print("[OK] Inserted: %s" % config['image'])
    elif config['image'] in content:
        print("[SKIP] Already exists: %s" % config['image'])
    else:
        print("[WARN] Not found: %s" % config['keyword'])

with open('okinawa.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[SUCCESS] Inserted %d images to okinawa.html" % inserted_count)