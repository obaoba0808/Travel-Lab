import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# 读取 tokyo-5days.html 的完整内容作为骨架
with open(os.path.join(BASE, 'tokyo-5days.html'), 'r', encoding='utf-8') as f:
    tokyo = f.read()

print('tokyo-5days.html 长度:', len(tokyo))

# 对于 thailand-sim.html 和 vietnam-hochiminh.html，
# 策略：直接用 tokyo-5days.html 的内容，
# 替换其中的文章内容部分为各自的内容
#
# 文章内容 = HER0 后面到 FAQ 之前（简化：替换 <h2> 到 <section class="faq-section"> 之前）
#
# 但这样很复杂。更简单的方法：
# 直接用 tokyo-5days.html 作为基础，只改：
#   1. <title> 和 meta
#   2. HER0 图片和标题
#   3. 文章主体（从 H2 第一个到 FAQ 前）
#   4. related-posts 内部链接
#   5. Footer 中的当前页高亮
#
# 这需要精确提取每个文件的"文章主体"。
# 暂时先手动操作，写辅助脚本来帮助。

print('此脚本为辅助工具，请手动操作。')
print('建议步骤：')
print('1. 用浏览器打开 tokyo-5days.html（本地），确认页面正常')
print('2. 将该文件 <body> 到 </body> 的内容复制')
print('3. 粘贴到 thailand-sim.html，然后修改其中的文章内容')
print('4. 对 vietnam-hochiminh.html 重复步骤2-3')
