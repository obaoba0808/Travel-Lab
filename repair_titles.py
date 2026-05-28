import os
import re

def extract_correct_title(filepath):
    """從檔案中提取正確的標題（從 og:title 或 h1 標籤）"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 方法1: 從 og:title 提取
    og_match = re.search(r'<meta property="og:title" content="(.*?)"', content)
    if og_match:
        return og_match.group(1)
    
    # 方法2: 從 h1 提取
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if h1_match:
        return re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
    
    # 方法3: 從 description 提取
    desc_match = re.search(r'<meta name="description" content="(.*?)"', content)
    if desc_match:
        desc = desc_match.group(1)
        # 取前20個字元作為標題
        return desc[:20] + '...'
    
    return None

def fix_title_in_file(filepath):
    """修復檔案中的 <title> 標籤"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 提取正確標題
    correct_title = extract_correct_title(filepath)
    if not correct_title:
        print(f'  SKIP (no title found): {os.path.basename(filepath)}')
        return False
    
    # 修復標題標籤 - 替換整個損壞的 title 標籤
    # 模式1: <title>><title>...garbage...正確標題</title>
    # 模式2: <title>&gt;&lt;title&gt;...正確標題</title>
    # 模式3: 任何包含 ><title> 或 &gt; 的 title 標籤
    
    new_title_tag = f'<title>{correct_title}</title>'
    
    # 使用正則表達式替換整個 title 標籤
    pattern = r'<title>.*?</title>'
    replacement = new_title_tag
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print('HTML Title Tag Repair Tool')
    print('=' * 50)
    
    fixed = 0
    skipped = 0
    errors = 0
    
    for filename in os.listdir('.'):
        if not filename.endswith('.html'):
            continue
        
        try:
            if fix_title_in_file(filename):
                print(f'✓ FIXED: {filename}')
                fixed += 1
            else:
                print(f'  OK:    {filename}')
                skipped += 1
        except Exception as e:
            print(f'✗ ERROR: {filename} - {str(e)}')
            errors += 1
    
    print('=' * 50)
    print(f'Repair complete!')
    print(f'Fixed:   {fixed} files')
    print(f'Skipped: {skipped} files')
    print(f'Errors:  {errors} files')
    
    # 顯示幾個修復後的標題示例
    print('\nSample repaired titles:')
    for filename in ['tokyo-5days.html', 'osaka-food.html', 'kyoto-temples.html']:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read(2000)
            title_match = re.search(r'<title>(.*?)</title>', content)
            if title_match:
                print(f'  {filename}: {title_match.group(1)[:60]}')

if __name__ == '__main__':
    main()
