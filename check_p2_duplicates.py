#!/usr/bin/env python3
"""
P2-3 內容去重複檢查
檢查多篇文章是否有段落重複
"""

import re
import difflib
from pathlib import Path
from collections import defaultdict

WORK_DIR = Path("C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab")

def read_file_safe(filepath):
    """安全讀取檔案"""
    try:
        return filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"❌ 讀取失敗 {filepath.name}: {e}")
        return None

def extract_paragraphs(content):
    """提取文章中的主要段落（去除HTML標籤）"""
    # 移除 script 和 style 標籤內容
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    
    # 移除 HTML 標籤
    text = re.sub(r'<[^>]+>', ' ', content)
    
    # 解碼 HTML 實體
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')
    text = text.replace('&quot;', '"')
    
    # 分割為段落
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    
    # 過濾太短的段落（可能是選單、版權宣告等）
    paragraphs = [p for p in paragraphs if len(p) > 50]
    
    return paragraphs

def find_similar_paragraphs(files_to_check):
    """找出相似段落"""
    print("\n" + "=" * 60)
    print("檢查相似段落")
    print("=" * 60)
    
    # 讀取所有檔案內容
    file_paragraphs = {}
    for filepath in files_to_check:
        content = read_file_safe(filepath)
        if content:
            paragraphs = extract_paragraphs(content)
            file_paragraphs[filepath.name] = paragraphs
    
    # 比對段落相似度
    duplicates = []
    
    files = list(file_paragraphs.keys())
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1 = files[i]
            file2 = files[j]
            
            paras1 = file_paragraphs[file1]
            paras2 = file_paragraphs[file2]
            
            for idx1, p1 in enumerate(paras1):
                for idx2, p2 in enumerate(paras2):
                    # 計算相似度
                    ratio = difflib.SequenceMatcher(None, p1, p2).ratio()
                    
                    if ratio > 0.7:  # 相似度超過 70%
                        duplicates.append({
                            'file1': file1,
                            'para1_idx': idx1,
                            'para1': p1[:100] + '...' if len(p1) > 100 else p1,
                            'file2': file2,
                            'para2_idx': idx2,
                            'para2': p2[:100] + '...' if len(p2) > 100 else p2,
                            'similarity': ratio
                        })
    
    return duplicates

def check_transportation_guide():
    """檢查交通攻略說明是否有重複"""
    print("\n" + "=" * 60)
    print("P2-3-1: 檢查交通攻略說明重複")
    print("=" * 60)
    
    files = [
        WORK_DIR / 'tokyo-5days.html',
        WORK_DIR / 'kansai-pass.html',
        WORK_DIR / 'japan-budget-guide.html'
    ]
    
    # 只檢查存在的檔案
    files = [f for f in files if f.exists()]
    
    if len(files) < 2:
        print("⚠️  檔案不足，跳過檢查")
        return []
    
    duplicates = find_similar_paragraphs(files)
    
    if duplicates:
        print(f"\n⚠️  發現 {len(duplicates)} 處可能重複")
        for dup in duplicates[:5]:  # 只顯示前5處
            print(f"\n相似度: {dup['similarity']:.2%}")
            print(f"  {dup['file1']} (段落 {dup['para1_idx']}): {dup['para1']}")
            print(f"  {dup['file2']} (段落 {dup['para2_idx']}): {dup['para2']}")
    else:
        print("\n✅ 未發現明顯重複")
    
    return duplicates

def check_taxfree_content():
    """檢查免稅提醒是否有重複"""
    print("\n" + "=" * 60)
    print("P2-3-2: 檢查免稅提醒重複")
    print("=" * 60)
    
    # 找出所有包含「小編真心話」或「免稅」的文章
    html_files = list(WORK_DIR.glob("*.html"))
    
    taxfree_paragraphs = []
    for filepath in html_files:
        if filepath.name.startswith('_') or filepath.name in ['index.html', 'about.html']:
            continue
        
        content = read_file_safe(filepath)
        if not content:
            continue
        
        # 搜尋免稅相關段落
        paras = extract_paragraphs(content)
        for idx, para in enumerate(paras):
            if '免税' in para or '小編真心話' in para or 'tax' in para.lower():
                taxfree_paragraphs.append({
                    'file': filepath.name,
                    'para_idx': idx,
                    'content': para[:150]
                })
    
    # 比對相似度
    duplicates = []
    for i in range(len(taxfree_paragraphs)):
        for j in range(i + 1, len(taxfree_paragraphs)):
            p1 = taxfree_paragraphs[i]
            p2 = taxfree_paragraphs[j]
            
            ratio = difflib.SequenceMatcher(None, p1['content'], p2['content']).ratio()
            
            if ratio > 0.6:  # 相似度超過 60%
                duplicates.append({
                    'file1': p1['file'],
                    'para1_idx': p1['para_idx'],
                    'content1': p1['content'],
                    'file2': p2['file'],
                    'para2_idx': p2['para_idx'],
                    'content2': p2['content'],
                    'similarity': ratio
                })
    
    if duplicates:
        print(f"\n⚠️  發現 {len(duplicates)} 處可能重複的免稅提醒")
        for dup in duplicates[:3]:
            print(f"\n相似度: {dup['similarity']:.2%}")
            print(f"  {dup['file1']} (段落 {dup['para1_idx']}): {dup['content1']}")
            print(f"  {dup['file2']} (段落 {dup['para2_idx']}): {dup['content2']}")
    else:
        print("\n✅ 未發現明顯重複的免稅提醒")
    
    return duplicates

def check_convenience_store_content():
    """檢查便利店推薦是否有重複"""
    print("\n" + "=" * 60)
    print("P2-3-3: 檢查便利店推薦重複")
    print("=" * 60)
    
    # 找出所有提到 7-11 或 FamilyMart 的文章
    html_files = list(WORK_DIR.glob("*.html"))
    
    convenience_paragraphs = []
    for filepath in html_files:
        if filepath.name.startswith('_') or filepath.name in ['index.html', 'about.html']:
            continue
        
        content = read_file_safe(filepath)
        if not content:
            continue
        
        # 搜尋便利店相關段落
        paras = extract_paragraphs(content)
        for idx, para in enumerate(paras):
            if '7-11' in para or 'FamilyMart' in para or '便利商店' in para or '便利店' in para:
                convenience_paragraphs.append({
                    'file': filepath.name,
                    'para_idx': idx,
                    'content': para[:150]
                })
    
    # 比對相似度
    duplicates = []
    for i in range(len(convenience_paragraphs)):
        for j in range(i + 1, len(convenience_paragraphs)):
            p1 = convenience_paragraphs[i]
            p2 = convenience_paragraphs[j]
            
            ratio = difflib.SequenceMatcher(None, p1['content'], p2['content']).ratio()
            
            if ratio > 0.6:  # 相似度超過 60%
                duplicates.append({
                    'file1': p1['file'],
                    'para1_idx': p1['para_idx'],
                    'content1': p1['content'],
                    'file2': p2['file'],
                    'para2_idx': p2['para_idx'],
                    'content2': p2['content'],
                    'similarity': ratio
                })
    
    if duplicates:
        print(f"\n⚠️  發現 {len(duplicates)} 處可能重複的便利店推薦")
        for dup in duplicates[:3]:
            print(f"\n相似度: {dup['similarity']:.2%}")
            print(f"  {dup['file1']} (段落 {dup['para1_idx']}): {dup['content1']}")
            print(f"  {dup['file2']} (段落 {dup['para2_idx']}): {dup['content2']}")
    else:
        print("\n✅ 未發現明顯重複的便利店推薦")
    
    return duplicates

def save_results(duplicates, filename):
    """儲存檢查結果"""
    import json
    
    output = {
        'check_time': str(Path(__file__).stat().st_mtime),
        'duplicates_count': len(duplicates),
        'duplicates': duplicates
    }
    
    with open(WORK_DIR / filename, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 檢查結果已保存到 {filename}")

def main():
    print("=" * 60)
    print("P2-3 內容去重複檢查")
    print("=" * 60)
    
    all_duplicates = []
    
    # P2-3-1: 交通攻略說明
    transport_dup = check_transportation_guide()
    all_duplicates.extend(transport_dup)
    
    # P2-3-2: 免稅提醒
    taxfree_dup = check_taxfree_content()
    all_duplicates.extend(taxfree_dup)
    
    # P2-3-3: 便利店推薦
    convenience_dup = check_convenience_store_content()
    all_duplicates.extend(convenience_dup)
    
    # 儲存結果
    save_results(all_duplicates, 'p2_duplicate_check.json')
    
    print("\n" + "=" * 60)
    print(f"檢查完成：發現 {len(all_duplicates)} 處可能重複")
    print("=" * 60)

if __name__ == '__main__':
    main()
