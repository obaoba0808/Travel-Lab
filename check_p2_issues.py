#!/usr/bin/env python3
"""
檢查 P2 問題 - 延伸閱讀區塊和 FAQ 數量
"""

import os
import re
from pathlib import Path

# 工作目錄
WORK_DIR = Path("C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab")

# 排除的檔案
EXCLUDE_FILES = {
    'index.html', 'about.html', 'contact.html', 'privacy.html',
    'terms.html', 'disclaimer.html', 'travel-tools.html', '404.html',
    '_live_index.html'
}

def get_html_files():
    """獲取所有文章 HTML 檔案"""
    html_files = []
    for f in WORK_DIR.glob("*.html"):
        if f.name not in EXCLUDE_FILES:
            html_files.append(f)
    return sorted(html_files)

def check_related_posts(filepath):
    """檢查是否有延伸閱讀區塊"""
    try:
        content = filepath.read_text(encoding='utf-8')
        has_related = '<div class="related-posts">' in content
        return has_related
    except Exception as e:
        print(f"❌ 讀取失敗 {filepath.name}: {e}")
        return False

def count_faqs(filepath):
    """計算 FAQ 數量"""
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # 找 FAQ 區塊
        faq_match = re.search(r'<div class="faq-item">', content)
        if not faq_match:
            return 0
        
        # 計算 faq-item 數量
        faq_count = len(re.findall(r'<div class="faq-item">', content))
        return faq_count
    except Exception as e:
        print(f"❌ 讀取失敗 {filepath.name}: {e}")
        return 0

def get_article_category(filepath):
    """從 HTML 中提取文章分類"""
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # 嘗試從 cat-tag 或 title 判斷分類
        cat_match = re.search(r'<span class="cat-tag">([^<]+)</span>', content)
        if cat_match:
            return cat_match.group(1)
        
        # 從檔名判斷
        name = filepath.stem
        if 'japan' in name or 'tokyo' in name or 'kyoto' in name or 'osaka' in name or 'hokkaido' in name or 'okinawa' in name:
            return '日本自由行'
        elif 'korea' in name or 'seoul' in name or 'busan' in name or 'jeju' in name:
            return '韓國自由行'
        elif 'taiwan' in name or 'taipei' in name or 'tainan' in name or 'jiufen' in name or 'kenting' in name or 'hualien' in name:
            return '台灣自由行'
        elif 'bangkok' in name or 'chiang' in name or 'vietnam' in name or 'southeast' in name or 'seasia' in name:
            return '東南亞自由行'
        
        return '其他'
    except Exception as e:
        return '其他'

def main():
    print("=" * 60)
    print("P2 問題檢查")
    print("=" * 60)
    
    html_files = get_html_files()
    
    print(f"\n📁 找到 {len(html_files)} 個文章檔案\n")
    
    # 檢查延伸閱讀
    print("=" * 60)
    print("P2-1: 檢查「延伸閱讀」區塊")
    print("=" * 60)
    
    missing_related = []
    for f in html_files:
        has_related = check_related_posts(f)
        if not has_related:
            category = get_article_category(f)
            missing_related.append((f.name, category))
            print(f"❌ {f.name} - 缺少延伸閱讀 [{category}]")
    
    if not missing_related:
        print("\n✅ 所有文章都有延伸閱讀區塊")
    else:
        print(f"\n⚠️  共有 {len(missing_related)} 篇文章缺少延伸閱讀")
    
    # 檢查 FAQ 數量
    print("\n" + "=" * 60)
    print("P2-2: 檢查 FAQ 數量")
    print("=" * 60)
    
    faq_issues = []
    
    # 特別檢查的檔案
    special_check = {
        'tainan-food.html': 6,
        'jiufen.html': 6,
        'packing-list.html': 5
    }
    
    for f in html_files:
        faq_count = count_faqs(f)
        target = special_check.get(f.name)
        
        if target:
            if faq_count < target:
                faq_issues.append((f.name, faq_count, target))
                print(f"❌ {f.name} - FAQ {faq_count}/{target}")
        elif faq_count < 4:
            faq_issues.append((f.name, faq_count, 4))
            print(f"⚠️  {f.name} - FAQ 偏少 ({faq_count})")
        else:
            print(f"✅ {f.name} - FAQ {faq_count}")
    
    if not faq_issues:
        print("\n✅ 所有文章 FAQ 數量充足")
    else:
        print(f"\n⚠️  共有 {len(faq_issues)} 篇文章需要補充 FAQ")
    
    # 輸出結果供後續使用
    print("\n" + "=" * 60)
    print("檢查結果摘要")
    print("=" * 60)
    
    if missing_related:
        print(f"\n缺少延伸閱讀的檔案 ({len(missing_related)}):")
        for name, cat in missing_related:
            print(f"  - {name} [{cat}]")
    
    if faq_issues:
        print(f"\nFAQ 不足的文章 ({len(faq_issues)}):")
        for name, current, target in faq_issues:
            print(f"  - {name}: {current} -> {target}")
    
    # 寫入檢查結果
    result = {
        'missing_related': missing_related,
        'faq_issues': faq_issues
    }
    
    import json
    with open(WORK_DIR / 'p2_check_result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print("\n✅ 檢查結果已保存到 p2_check_result.json")

if __name__ == '__main__':
    main()
