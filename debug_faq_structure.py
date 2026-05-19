#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
除錯：查看 FAQ </section> 和 related-posts 之間的實際內容
"""
import re

files = [
    "kenting.html",
    "kansai-pass.html",
    "seoul-food.html",
]

BASE = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab"

for fname in files:
    fpath = BASE + "\\" + fname
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    print("=" * 60)
    print("檔案: " + fname)
    print("=" * 60)

    # 找 faq-section 的 </section>
    faq_match = re.search(r'<section class="faq-section">(.*?)</section>', content, re.DOTALL)
    if faq_match:
        faq_full = faq_match.group(0)
        print("FAQ section 長度: " + str(len(faq_full)) + " 字元")
        # 顯示最後 300 字元
        tail = faq_full[-400:]
        print("FAQ section 尾部 400 字元:")
        print(repr(tail))
    else:
        print("找不到 faq-section")

    # 找所有 </section> 的位置
    all_ends = [m.start() for m in re.finditer(r'</section>', content)]
    print("\n檔案中共有 " + str(len(all_ends)) + " 個 </section>")
    for pos in all_ends:
        snippet = content[max(0,pos-30):pos+80]
        print("  位置 " + str(pos) + ": " + repr(snippet))

    # 找 <div class="related-posts"> 的位置
    rel_match = re.search(r'<div class="related-posts">', content)
    if rel_match:
        rel_pos = rel_match.start()
        print("\nrelated-posts 位置: " + str(rel_pos))
        # 看 related-posts 前 200 字元
        before_rel = content[max(0, rel_pos-200):rel_pos]
        print("related-posts 前 200 字元:")
        print(repr(before_rel))

    print("")
