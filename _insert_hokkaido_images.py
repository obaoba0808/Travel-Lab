# -*- coding: utf-8 -*-
import re

# 读取文件
with open('hokkaido-winter.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义图片插入配置
images_config = [
    {
        'keyword': 'No.1</span>\n<h3>小樽運河',
        'image': 'otaru-canal.webp',
        'alt': '小樽運河雪景浪漫黃昏',
        'experience': '小樽運河的黃昏超級浪漫！瓦斯燈點亮時，搭配運河上的雪景氛圍，我站在運河邊看了半小時都不想走。推薦傍晚4點到，这样可以看到天色从蓝变成橘黄的渐变过程。'
    },
    {
        'keyword': 'No.2</span>\n<h3>札幌雪祭',
        'image': 'sapporo-snow.webp',
        'alt': '札幌雪祭大型雪雕夜間点灯',
        'experience': '札幌雪祭的规模真的很震撼！100多座雪雕，最夸张的一座高达15米。我在現場凍了3小時，但看到夜间点灯的那一刻，真的觉得一切都值得了。建议穿夠保暖衣物!'
    },
    {
        'keyword': 'No.4</span>\n<h3>旭山動物',
        'image': 'asahiyama-penguin.webp',
        'alt': '旭山动物园国王企鹅排队散步',
        'experience': '企鹅散步根本是北海道冬天的招牌！看企鹅摇摇晃晃走路，我笑到肚子痛。每天两场(11:00和14:30)，建议提早30分钟排队抢前面的位置，才能拍到近照!'
    },
    {
        'keyword': 'No.5</span>\n<h3>登別地獄谷',
        'image': 'noboriobuchi-onsen.webp',
        'alt': '登别地狱谷雪景露天温泉',
        'experience': '登别温泉的露天风吕太赞了！一边泡汤一边看雪花飘下来，周围都是白茫茫的雪，呼吸着冷空气却全身热腾腾，这种冰火体验终生难忘。注意头发会结冰!'
    }
]

def create_image_block(config):
    """创建图片区块 HTML"""
    return f'''<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0;transition:transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
  <img src="images/{config['image']}" alt="{config['alt']}" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);cursor:pointer;" loading="lazy">
  <p style="margin:10px 0 0 0;font-size:13px;color:#0ABAB5;line-height:1.6;font-style:italic;text-align:left;">📝 小編個人體驗：{config['experience']}</p>
</div>'''

inserted_count = 0

for config in images_config:
    search_pattern = config['keyword']
    insert_marker = f'<div class="day-card">\n<span class="day-tag">{search_pattern.split("</span>")[0]}</span>'
    
    if search_pattern in content:
        # 找到对应的 day-card 结束标签，在其后面插入图片
        # 替换策略：在 </div> 之后插入图片区块，找下一个 day-card 开始
        parts = content.split(search_pattern)
        if len(parts) > 1:
            # 找到包含这个 day-card 的部分
            target = parts[1].split('</div>')[0] + '</div>'
            
            # 检查是否已经插入过图片
            if config['image'] not in target:
                new_block = create_image_block(config)
                # 找到 </div> 闭标签，在其后插入图片
                content = content.replace(target, target + new_block, 1)
                inserted_count += 1
                print("[OK] Inserted: %s" % config['image'])
            else:
                print("[SKIP] Already exists: %s" % config['image'])
    else:
        # 尝试更宽松的匹配
        keyword_short = config['keyword'].split('\n')[0]
        print("[WARN] Keyword not found exactly: %s" % keyword_short)

# 写回文件
with open('hokkaido-winter.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[SUCCESS] Inserted %d images to hokkaido-winter.html" % inserted_count)