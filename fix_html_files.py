import os
import re

def fix_html_file(filepath):
    """修復HTML文件的<title>標籤和Worker URL"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    modified = content
    
    # 修復1: 損壞的title標籤
    # 從og:title提取正確標題
    og_match = re.search(r'<meta property="og:title" content="(.*?)"', modified)
    if og_match:
        real_title = og_match.group(1)
        # 替換任何損壞的title標籤
        modified = re.sub(
            r'<title>.*?</title>',
            '<title>' + real_title + '</title>',
            modified,
            flags=re.DOTALL
        )
        print(f'  Fixed title: {os.path.basename(filepath)}')
    
    # 修復2: Worker URL錯誤
    wrong_urls = [
        'https://https://golightly-email.8107e1de.workers.dev.workers.dev',
        'https://golightly-email.8107e1de.workers.dev.workers.dev',
        'YOUR-WORKER-URL',
    ]
    correct_url = 'https://golightly-email.8107e1de.workers.dev'
    
    for wrong in wrong_urls:
        if wrong in modified:
            modified = modified.replace(wrong, correct_url)
            print(f'  Fixed Worker URL: {os.path.basename(filepath)}')
    
    # 檢查是否需要寫入
    if modified != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False

# 主程序
if __name__ == '__main__':
    # 切換到腳本所在目錄
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print('Starting HTML repair...')
    print('=' * 50)
    
    fixed_count = 0
    error_count = 0
    
    # 處理所有HTML文件
    for filename in os.listdir('.'):
        if not filename.endswith('.html'):
            continue
        
        try:
            if fix_html_file(filename):
                fixed_count += 1
                print(f'✓ {filename}')
            else:
                print(f'  {filename} (no changes needed)')
        except Exception as e:
            error_count += 1
            print(f'✗ {filename}: {str(e)}')
    
    print('=' * 50)
    print(f'Repair complete!')
    print(f'Fixed: {fixed_count} files')
    print(f'Errors: {error_count} files')
    
    # 顯示幾個修復後的標題示例
    print('\nSample fixed titles:')
    for filename in ['tokyo-5days.html', 'osaka-food.html', 'kyoto-temples.html']:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read(2000)
            title_match = re.search(r'<title>(.*?)</title>', content)
            if title_match:
                print(f'  {filename}: {title_match.group(1)[:50]}...')
