# -*- coding: utf-8 -*-
import re

# 讀取 index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 讀取 SlideShare 區塊
with open('_slideshare_section.html', 'r', encoding='utf-8') as f:
    slideshare_block = f.read()

# 在 </main> 之前插入 SlideShare 區塊
new_content = content.replace('</main>', slideshare_block + '\n</main>')

# 寫回 index.html (UTF-8 無 BOM)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('✅ 已成功將 SlideShare 資源區塊插入 index.html')
print(f'   插入位置: 在 </main> 之前')
print(f'   區塊大小: {len(slideshare_block)} 字節')
