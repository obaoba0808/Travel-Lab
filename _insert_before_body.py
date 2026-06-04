# -*- coding: utf-8 -*-
import re

# 1. 讀取 tokyo-5days.html
with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. 讀取 SlideShare 嵌入範例
with open('_example_slideshare_embed.html', 'r', encoding='utf-8') as f:
    slideshare_block = f.read()

# 3. 在 </body> 之前插入 SlideShare 區塊
# 使用正則表達式，允許 </body> 前後有空白和換行
pattern = r'\s*</body>\s*'
match = re.search(pattern, content)

if match:
    matched_text = match.group(0)
    replacement = slideshare_block + '\n' + matched_text
    new_content = content[:match.start()] + replacement + content[match.end():]
    
    # 4. 寫回 tokyo-5days.html
    with open('tokyo-5days.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('SUCCESS: Inserted SlideShare embed BEFORE </body>')
    print(f'   Matched text: "{matched_text.strip()}"')
    print(f'   Inserted block size: {len(slideshare_block)} bytes')
    print(f'   New file size: {len(new_content)} bytes')
    print(f'   Location: ~line {content[:match.start()].count(chr(10)) + 1}')
else:
    print('ERROR: </body> tag NOT found in tokyo-5days.html')
    print('   Please check the HTML structure')
