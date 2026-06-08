# -*- coding: utf-8 -*-
import re

with open('okinawa.html', 'r', encoding='utf-8') as f:
    raw = f.read()

# Step 1: Remove castle-twilight block (whatever location)
pattern = r'<!-- \u5be6\u6230\u63a8\u85a6\u914d\u5716 -->\s*<div[^>]*>\s*<img[^>]*castle-twilight[^>]*>\s*<p[^>]*>.*?</p>\s*</div>'
raw = re.sub(pattern, '', raw, flags=re.DOTALL)
print('[OK] Removed castle-twilight block')

# Step 2: Insert after Day 1 </div>, before Day 2 starts
# Correct anchor: </div> then blank line then <div class="day-card"> then <span class="day-tag">Day 2</span>
castle_html = '''

<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0;transition:transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
  <img src="images/castle-twilight.webp" alt="首里城公園金色城牆暮光" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);cursor:pointer;" loading="lazy">
  <p style="margin:10px 0 0 0;font-size:13px;color:#0ABAB5;line-height:1.6;font-style:italic;text-align:left;">📝 小編個人體驗：首里城的日落真的很美！金色城牆配上晚霞，拍照超有fu。建議傍晚4-5點到，既能看到白天的城牆，又能等到日落的magic hour。登城費用 ¥820，但很值得！</p>
</div>
'''

# Target: the </div> that ends Day 1, followed by whitespace, then Day 2 card
# Day 1 ends with: </div>\n\n  <div class="day-card">\n    <span class="day-tag">Day 2</span>
anchor_match = re.search(
    r'(</div>)\s*\n\s*<div class="day-card">\s*\n\s*<span class="day-tag">Day 2</span>',
    raw
)
if anchor_match:
    end_div_pos = anchor_match.end(1)  # position right after </div>
    raw = raw[:end_div_pos] + castle_html + raw[end_div_pos:]
    print('[OK] Inserted castle-twilight after Day 1 (correct location)')
else:
    print('[FAIL] Could not find Day 1 end anchor')

with open('okinawa.html', 'w', encoding='utf-8') as f:
    f.write(raw)

print('[DONE]')
