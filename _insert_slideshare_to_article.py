# -*- coding: utf-8 -*-
import re

# 1. 讀取 tokyo-5days.html
with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. 讀取 SlideShare 嵌入範例
with open('_example_slideshare_embed.html', 'r', encoding='utf-8') as f:
    slideshare_block = f.read()

# 3. 在 </article> 之前插入 SlideShare 區塊
# 使用正則表達式，保留 </article> 標籤
new_content = content.replace('</article>', slideshare_block + '\n</article>')

# 4. 寫回 tokyo-5days.html (UTF-8 無 BOM)
with open('tokyo-5days.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Success: Inserted SlideShare embed before </article> in tokyo-5days.html')
print(f'Inserted block size: {len(slideshare_block)} bytes')
