# -*- coding: utf-8 -*-
import re

# 1. 讀取 tokyo-5days.html
with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. 讀取 SlideShare 嵌入範例
with open('_example_slideshare_embed.html', 'r', encoding='utf-8') as f:
    slideshare_block = f.read()

# 3. 用正則表達式找到 </article> (允許前後空白和換行)
# 模式: 任意空白字元 + </article> + 任意空白字元
pattern = r'\s*</article>\s*'

match = re.search(pattern, content)
if match:
    # 在 </article> 之前插入 SlideShare 區塊
    matched_text = match.group(0)
    replacement = slideshare_block + '\n' + matched_text
    new_content = content[:match.start()] + replacement + content[match.end():]
    
    # 4. 寫回 tokyo-5days.html
    with open('tokyo-5days.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('SUCCESS: Inserted SlideShare embed BEFORE </article>')
    print(f'   Matched text: "{matched_text.strip()}"')
    print(f'   Inserted block size: {len(slideshare_block)} bytes')
    print(f'   New file size: {len(new_content)} bytes')
else:
    print('ERROR: </article> tag NOT found in tokyo-5days.html')
    print('   Please check the HTML structure')
