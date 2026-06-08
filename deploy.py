import os
import shutil

pdfs_dir = 'pdfs'
downloads_dir = 'downloads'

# 查找所有 -with-links.pdf
processed = [f for f in os.listdir(pdfs_dir) if f.endswith('-with-links.pdf')]

print(f'Found {len(processed)} processed PDFs')

copied = 0
for pdf in processed:
    # 还原原始文件名（移除 -with-links）
    original_name = pdf.replace('-with-links', '')
    src = os.path.join(pdfs_dir, pdf)
    dst = os.path.join(downloads_dir, original_name)
    
    # 复制并覆盖
    shutil.copy2(src, dst)
    copied += 1
    print(f'  Copied: {pdf} -> {original_name}')

print(f'Done. Copied {copied} files.')
