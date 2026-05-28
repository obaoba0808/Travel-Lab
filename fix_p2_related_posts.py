#!/usr/bin/env python3
"""
P2-1 修復：為缺少「延伸閱讀」的文章補上
"""

import re
import json
from pathlib import Path

WORK_DIR = Path("C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab")

# 文章分類映射（根據檔名判斷）
CATEGORY_ARTICLES = {
    '日本自由行': [
        ('japan-travel.html', 'images/japan-hero.webp', '日本旅遊完全指南｜第一次去日本就上手'),
        ('japan-budget-guide.html', 'images/japan-budget-hero.webp', '日本預算攻略｜10天9夜花費明細'),
        ('tokyo-5days.html', 'images/tokyo-hero.webp', '東京5天4夜行程｜地鐵教學×景點推薦'),
        ('kyoto-temples.html', 'images/kyoto-hero.webp', '京都寺廟散步地圖｜清水寺、金閣寺、伏見稻荷'),
        ('osaka-food.html', 'images/osaka-food-hero.webp', '大阪2天1夜美食攻略｜道頓堀必吃小吃'),
        ('osaka-usj.html', 'images/usj-hero.webp', '大阪環球影城攻略｜任天堂世界搶先玩'),
        ('hokkaido-winter.html', 'images/hokkaido-hero.webp', '北海道冬日幻想曲｜札幌小樽5天行程'),
        ('okinawa.html', 'images/okinawa-hero.webp', '沖繩攻略｜美麗海水族館×美國村'),
        ('kansai-pass.html', 'images/kansai-pass-hero.webp', '關西交通券攻略｜ICOCA×KTP×關西周遊券'),
    ],
    '韓國自由行': [
        ('korea-travel.html', 'images/korea-hero.webp', '韓國旅遊完全指南｜第一次去韓國就上手'),
        ('korea-budget.html', 'images/korea-budget-hero.webp', '韓國10天9夜預算明細｜人均3000元行程'),
        ('korea-budget-travel-guide.html', 'images/korea-budget-guide-hero.webp', '韓國窮遊攻略｜學生黨必看省錢技巧'),
        ('seoul-food.html', 'images/seoul-food-hero.webp', '首爾美食地圖｜明洞×弘大×聖水洞'),
        ('busan-capsule.html', 'images/busan-hero.webp', '釜山海雲台×藍色線路膠囊｜2天1夜行程'),
        ('jeju-island.html', 'images/jeju-hero.webp', '濟州島4天3夜｜牛島×涉地可支'),
    ],
    '台灣自由行': [
        ('taiwan-travel.html', 'images/taiwan-hero.webp', '台灣旅遊完全指南｜熱門景點×美食推薦'),
        ('taiwan-travel-guide.html', 'images/taiwan-guide-hero.webp', '台灣自由行攻略｜交通×住宿×景點一次看'),
        ('taipei-food.html', 'images/taipei-food-hero.webp', '台北美食地圖｜夜市×老店×咖啡廳'),
        ('tainan-food.html', 'images/tainan-food-hero.webp', '台南美食攻略｜牛肉湯×擔仔麵×中式點心'),
        ('jiufen.html', 'images/jiufen-hero.webp', '九份老街散步｜侯孝賢電影場景×茶樓夜景'),
        ('hualien-taitung.html', 'images/east-coast-hero.webp', '花蓮台東走跳｜太魯閣×伯朗大道×三仙台'),
        ('kenting.html', 'images/kenting-hero.webp', '墾丁玩水攻略｜南灣×白沙灣×鵝鑾鼻'),
    ],
    '東南亞自由行': [
        ('southeast-asia.html', 'images/seasia-hero.webp', '東南亞旅遊完全指南｜第一次去東南亞就上手'),
        ('seasia-budget-travel-guide.html', 'images/seasia-budget-hero.webp', '東南亞窮遊攻略｜月均3000元長期旅行'),
        ('bangkok-3days.html', 'images/bangkok-hero.webp', '曼谷3天2夜｜四面佛×恰圖恰×考山路'),
        ('bangkok-massage.html', 'images/massage-hero.webp', '曼谷按摩攻略｜正宗泰式按摩推薦'),
        ('chiang-mai.html', 'images/chiang-mai-hero.webp', '清邁古城慢活｜雙龍寺×週末夜市×咖啡廳'),
        ('vietnam-danang.html', 'images/danang-hero.webp', '峴港4天3夜｜會安古城×巴拿山×美溪沙灘'),
    ],
}

def get_article_category(filename):
    """判斷文章所屬分類"""
    for category, articles in CATEGORY_ARTICLES.items():
        if any(article[0] == filename for article in articles):
            return category
    return None

def get_related_articles(filename, category):
    """獲取同分類的其他文章（排除自己）"""
    if not category or category not in CATEGORY_ARTICLES:
        return []
    
    related = []
    for article in CATEGORY_ARTICLES[category]:
        if article[0] != filename:
            related.append(article)
    
    # 最多返回 3 篇
    return related[:3]

def generate_related_posts_html(filename, category):
    """生成延伸閱讀 HTML"""
    related = get_related_articles(filename, category)
    
    if not related:
        return None
    
    html = '<div class="related-posts">\n'
    html += '  <h2 class="section-title">📖 延伸閱讀</h2>\n'
    html += '  <div class="related-list">\n'
    
    for href, img, title in related:
        html += f'    <a href="{href}" class="related-card">\n'
        html += f'      <div class="post-thumb"><img loading="lazy" src="{img}" alt="{title}" width="1536" height="1024"></div>\n'
        html += f'      <div class="post-body">\n'
        html += f'        <span class="cat-tag">{category}</span>\n'
        html += f'        <h3>{title}</h3>\n'
        html += f'      </div>\n'
        html += f'    </a>\n'
    
    html += '  </div>\n'
    html += '</div>\n'
    
    return html

def fix_article(filepath):
    """修復單篇文章：添加延伸閱讀"""
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # 檢查是否已有延伸閱讀
        if '<div class="related-posts">' in content:
            print(f"✅ {filepath.name} 已有延伸閱讀，跳過")
            return False
        
        # 判斷分類
        category = get_article_category(filepath.name)
        if not category:
            print(f"⚠️  {filepath.name} 無法判斷分類，跳過")
            return False
        
        # 生成延伸閱讀 HTML
        related_html = generate_related_posts_html(filepath.name, category)
        if not related_html:
            print(f"⚠️  {filepath.name} 找不到相關文章，跳過")
            return False
        
        # 找到插入位置：在 FAQ 之後、Klook/Trip banner 之前
        # 優先找 </div> <!-- end .faq-item --> 後的面 Klook banner
        # 如果沒有 FAQ，就找 </article> 或 </main> 之前
        
        insert_pos = -1
        
        # 方法1: 找 Klook/Trip banner 前面插入
        klook_pattern = re.search(r'<div class="cta-banner">', content)
        if klook_pattern:
            # 往前找 </div> 或 </section> 作為插入點
            pos = klook_pattern.start()
            # 找最後一個 </div> 或 </section>
            last_div = content.rfind('</div>', 0, pos)
            last_section = content.rfind('</section>', 0, pos)
            insert_pos = max(last_div, last_section)
            if insert_pos > 0:
                insert_pos += len('</div>')  # 在結束標籤後插入
        
        # 方法2: 如果沒找到 Klook banner，找 </article>
        if insert_pos == -1:
            article_end = content.rfind('</article>')
            if article_end > 0:
                insert_pos = article_end
        
        # 方法3: 如果還是沒找到，找 </main>
        if insert_pos == -1:
            main_end = content.rfind('</main>')
            if main_end > 0:
                insert_pos = main_end
        
        if insert_pos == -1:
            print(f"❌ {filepath.name} 找不到合適的插入位置")
            return False
        
        # 插入延伸閱讀
        new_content = content[:insert_pos] + '\n' + related_html + '\n' + content[insert_pos:]
        
        # 寫回檔案
        filepath.write_text(new_content, encoding='utf-8')
        print(f"✅ {filepath.name} 已添加延伸閱讀 [{category}]")
        return True
        
    except Exception as e:
        print(f"❌ {filepath.name} 處理失敗: {e}")
        return False

def main():
    print("=" * 60)
    print("P2-1 修復：添加「延伸閱讀」區塊")
    print("=" * 60)
    
    # 讀取檢查結果
    try:
        with open(WORK_DIR / 'p2_check_result.json', 'r', encoding='utf-8') as f:
            result = json.load(f)
        missing_related = result['missing_related']
    except:
        print("❌ 無法讀取檢查結果，使用預設列表")
        missing_related = [
            ['esim-comparison.html', '其他'],
            ['japan-travel.html', '日本自由行'],
            ['korea-budget-travel-guide.html', '韓國自由行'],
            ['korea-travel.html', '韓國自由行'],
            ['packing-list-online.html', '其他'],
            ['packing-list.html', '其他'],
            ['seasia-budget-travel-guide.html', '東南亞自由行'],
            ['southeast-asia.html', '東南亞自由行'],
            ['taiwan-travel-guide.html', '台灣自由行'],
            ['taiwan-travel.html', '台灣自由行'],
        ]
    
    fixed = 0
    skipped = 0
    
    for filename, category in missing_related:
        filepath = WORK_DIR / filename
        if not filepath.exists():
            print(f"⚠️  {filename} 不存在，跳過")
            skipped += 1
            continue
        
        if fix_article(filepath):
            fixed += 1
        else:
            skipped += 1
    
    print("\n" + "=" * 60)
    print(f"修復完成：{fixed} 篇成功，{skipped} 篇跳過")
    print("=" * 60)

if __name__ == '__main__':
    main()
