import re

# 读取文件
with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 旧样式 (需要被替换)
old_style = 'margin:10px 0 0 0;font-size:13px;color:#666;line-height:1.6;font-style:italic;'

# 新样式 (Tiffany 绿 #0ABAB5 + 靠左)
new_style = 'margin:10px 0 0 0;font-size:13px;color:#0ABAB5;line-height:1.6;font-style:italic;text-align:left;'

# 替换所有 4 个图片区块的 p 标签样式
modified = content.replace(old_style, new_style)

# 统计替换次数
count = content.count(old_style)
print(f"[OK] Found {count} p tags to modify")

# 写回文件
with open('tokyo-5days.html', 'w', encoding='utf-8') as f:
    f.write(modified)

print(f"[SUCCESS] Modified tokyo-5days.html, {count} p tags updated")
print("  New style: color:#0ABAB5 + text-align:left")
