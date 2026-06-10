#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接查看 kenting.html 的 FAQ 結尾到 related-posts 之間的原始內容
寫入 debug_kenting.txt（UTF-8）
"""
import re

fpath = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\kenting.html"
with open(fpath, "r", encoding="utf-8") as f:
    content = f.read()

# 找 </section> 的位置
pos_end = content.find("</section>")
if pos_end < 0:
    with open("debug_kenting.txt", "w", encoding="utf-8") as f:
        f.write("找不到 </section>\n")
    print("找不到 </section>")
else:
    # 取 </section> 後 500 字元
    after = content[pos_end:pos_end+500]
    with open("debug_kenting.txt", "w", encoding="utf-8") as f:
        f.write("</section> 位置: " + str(pos_end) + "\n\n")
        f.write("後面 500 字元（原始）:\n")
        f.write(after)
        f.write("\n\n===== 逐字元 =====\n")
        for i, ch in enumerate(after[:300]):
            f.write("pos " + str(i) + ": " + repr(ch) + "\n")
    print("已寫入 debug_kenting.txt")
