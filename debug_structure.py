#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
除錯：查看 FAQ </section> 和 related-posts 之間的實際內容
輸出到 debug_output.txt（UTF-8），避免 Windows 終端機編碼問題
"""
import re
import os

BASE = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab"
files = ["kenting.html", "kansai-pass.html", "seoul-food.html"]

out_lines = []

for fname in files:
    fpath = os.path.join(BASE, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    out_lines.append("=" * 60)
    out_lines.append("檔案: " + fname)
    out_lines.append("=" * 60)

    # 找 faq-section 的範圍
    faq_match = re.search(r'<section class="faq-section">.*?</section>', content, re.DOTALL)
    if faq_match:
        faq_text = faq_match.group(0)
        out_lines.append("[OK] 找到 faq-section，長度=" + str(len(faq_text)))
        # 顯示尾部 300 字（去除換行）
        tail = faq_text[-300:]
        tail_clean = tail.replace("\n", "\\n").replace("\r", "\\r")
        out_lines.append("FAQ 尾部 300 字:")
        out_lines.append(tail_clean)
    else:
        out_lines.append("[WARN] 找不到 faq-section")

    # 找所有 </section>
    end_positions = [m.start() for m in re.finditer(r'</section>', content)]
    out_lines.append("檔案中共有 " + str(len(end_positions)) + " 個 </section>")

    # 找 related-posts
    rel_match = re.search(r'<div class="related-posts">', content)
    if rel_match:
        rpos = rel_match.start()
        out_lines.append("related-posts 位置: " + str(rpos))
        before = content[max(0, rpos - 150):rpos]
        before_clean = before.replace("\n", "\\n")
        out_lines.append("  前 150 字: " + before_clean)
    else:
        out_lines.append("[WARN] 找不到 related-posts")

    out_lines.append("")

# 寫入檔案（UTF-8）
out_path = os.path.join(BASE, "debug_output.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print("除錯完成，請查看 debug_output.txt（UTF-8 編碼）")
