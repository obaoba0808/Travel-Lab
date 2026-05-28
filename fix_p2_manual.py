#!/usr/bin/env python3
"""
手動修復 P2-1：替換自定義 related-articles 為標準 related-posts
"""

import re
from pathlib import Path

WORK_DIR = Path("C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab")

# 標準延伸閱讀 HTML 模板（根據分類）
RELATED_POSTS = {
    'korea-budget-travel-guide.html': '''
<div class="related-posts">
  <h2 class="section-title">📖 延伸閱讀</h2>
  <div class="related-list">
    <a href="korea-travel.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/korea-hero.webp" alt="韓國自由行" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">韓國自由行</span>
        <h3>韓國旅遊完全指南｜第一次去韓國就上手</h3>
      </div>
    </a>
    <a href="korea-budget.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/korea-budget-hero.webp" alt="韓國預算" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">韓國自由行</span>
        <h3>韓國10天9夜預算明細｜人均3000元行程</h3>
      </div>
    </a>
    <a href="seoul-food.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/seoul-food-hero.webp" alt="首爾美食" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">韓國自由行</span>
        <h3>首爾美食地圖｜明洞×弘大×聖水洞</h3>
      </div>
    </a>
  </div>
</div>
''',
    'seasia-budget-travel-guide.html': '''
<div class="related-posts">
  <h2 class="section-title">📖 延伸閱讀</h2>
  <div class="related-list">
    <a href="southeast-asia.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/seasia-hero.webp" alt="東南亞旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">東南亞自由行</span>
        <h3>東南亞旅遊完全指南｜第一次去東南亞就上手</h3>
      </div>
    </a>
    <a href="bangkok-3days.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/bangkok-hero.webp" alt="曼谷旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">東南亞自由行</span>
        <h3>曼谷3天2夜｜四面佛×恰圖恰×考山路</h3>
      </div>
    </a>
    <a href="chiang-mai.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/chiang-mai-hero.webp" alt="清邁旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">東南亞自由行</span>
        <h3>清邁古城慢活｜雙龍寺×週末夜市×咖啡廳</h3>
      </div>
    </a>
  </div>
</div>
''',
    'taiwan-travel-guide.html': '''
<div class="related-posts">
  <h2 class="section-title">📖 延伸閱讀</h2>
  <div class="related-list">
    <a href="taiwan-travel.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/taiwan-hero.webp" alt="台灣旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">台灣自由行</span>
        <h3>台灣旅遊完全指南｜熱門景點×美食推薦</h3>
      </div>
    </a>
    <a href="taipei-food.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/taipei-food-hero.webp" alt="台北美食" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">台灣自由行</span>
        <h3>台北美食地圖｜夜市×老店×咖啡廳</h3>
      </div>
    </a>
    <a href="tainan-food.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/tainan-food-hero.webp" alt="台南美食" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">台灣自由行</span>
        <h3>台南美食攻略｜牛肉湯×擔仔麵×中式點心</h3>
      </div>
    </a>
  </div>
</div>
''',
    'esim-comparison.html': '''
<div class="related-posts">
  <h2 class="section-title">📖 延伸閱讀</h2>
  <div class="related-list">
    <a href="japan-travel.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/japan-hero.webp" alt="日本旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">旅遊工具</span>
        <h3>日本旅遊完全指南｜第一次去日本就上手</h3>
      </div>
    </a>
    <a href="korea-travel.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/korea-hero.webp" alt="韓國旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">旅遊工具</span>
        <h3>韓國旅遊完全指南｜第一次去韓國就上手</h3>
      </div>
    </a>
    <a href="southeast-asia.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/seasia-hero.webp" alt="東南亞旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">旅遊工具</span>
        <h3>東南亞旅遊完全指南｜第一次去東南亞就上手</h3>
      </div>
    </a>
  </div>
</div>
''',
    'packing-list.html': '''
<div class="related-posts">
  <h2 class="section-title">📖 延伸閱讀</h2>
  <div class="related-list">
    <a href="japan-travel.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/japan-hero.webp" alt="日本旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">旅遊準備</span>
        <h3>日本旅遊完全指南｜第一次去日本就上手</h3>
      </div>
    </a>
    <a href="korea-travel.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/korea-hero.webp" alt="韓國旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">旅遊準備</span>
        <h3>韓國旅遊完全指南｜第一次去韓國就上手</h3>
      </div>
    </a>
    <a href="packing-list-online.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/packing-hero.webp" alt="打包清單" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">旅遊準備</span>
        <h3>線上打包清單｜自動產生專屬行李清單</h3>
      </div>
    </a>
  </div>
</div>
''',
    'packing-list-online.html': '''
<div class="related-posts">
  <h2 class="section-title">📖 延伸閱讀</h2>
  <div class="related-list">
    <a href="japan-travel.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/japan-hero.webp" alt="日本旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">旅遊準備</span>
        <h3>日本旅遊完全指南｜第一次去日本就上手</h3>
      </div>
    </a>
    <a href="korea-travel.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/korea-hero.webp" alt="韓國旅遊" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">旅遊準備</span>
        <h3>韓國旅遊完全指南｜第一次去韓國就上手</h3>
      </div>
    </a>
    <a href="packing-list.html" class="related-card">
      <div class="post-thumb"><img loading="lazy" src="images/packing-hero.webp" alt="打包清單" width="1536" height="1024"></div>
      <div class="post-body">
        <span class="cat-tag">旅遊準備</span>
        <h3>旅遊打包清單PDF｜50樣必備物品檢查表</h3>
      </div>
    </a>
  </div>
</div>
'''
}

def fix_article(filename):
    """修復單篇文章"""
    filepath = WORK_DIR / filename
    
    if not filepath.exists():
        print(f"⚠️  {filename} 不存在")
        return False
    
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # 檢查是否已有標準 related-posts
        if '<div class="related-posts">' in content:
            print(f"✅ {filename} 已有標準延伸閱讀")
            return True
        
        # 檢查是否有自定義 related-articles
        if '<div class="related-articles"' in content:
            print(f"🔧 {filename} 發現自定義 related-articles，替換為標準結構")
            
            # 刪除舊的 related-articles 區塊
            pattern = r'<div class="related-articles"[^>]*>.*?</div>\s*</div>'
            new_content = re.sub(pattern, '', content, flags=re.DOTALL)
            
            # 在 </body> 前插入標準 related-posts
            related_html = RELATED_POSTS.get(filename)
            if not related_html:
                print(f"⚠️  {filename} 沒有對應的延伸閱讀內容")
                return False
            
            new_content = new_content.replace('</body>', related_html + '\n</body>')
            
            # 寫回檔案
            filepath.write_text(new_content, encoding='utf-8')
            print(f"✅ {filename} 已替換為標準延伸閱讀")
            return True
        
        # 如果都沒有，在 </body> 前插入
        related_html = RELATED_POSTS.get(filename)
        if not related_html:
            print(f"⚠️  {filename} 沒有對應的延伸閱讀內容")
            return False
        
        new_content = content.replace('</body>', related_html + '\n</body>')
        filepath.write_text(new_content, encoding='utf-8')
        print(f"✅ {filename} 已添加延伸閱讀")
        return True
        
    except Exception as e:
        print(f"❌ {filename} 處理失敗: {e}")
        return False

def main():
    print("=" * 60)
    print("手動修復 P2-1：6 篇失敗文章")
    print("=" * 60)
    
    files_to_fix = [
        'korea-budget-travel-guide.html',
        'seasia-budget-travel-guide.html',
        'taiwan-travel-guide.html',
        'esim-comparison.html',
        'packing-list.html',
        'packing-list-online.html'
    ]
    
    fixed = 0
    for filename in files_to_fix:
        if fix_article(filename):
            fixed += 1
    
    print("\n" + "=" * 60)
    print(f"修復完成：{fixed}/{len(files_to_fix)} 篇成功")
    print("=" * 60)

if __name__ == '__main__':
    main()
