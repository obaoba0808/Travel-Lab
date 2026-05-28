import os, re

# Old popup HTML
old_popup = '''<div class="lead-popup-overlay" id="leadPopup">
  <div class="lead-popup">
    <button class="lead-popup-close" onclick="closeLeadPopup()">&times;</button>
    <h3>📘 小編獨家攻略，限時免費送</h3>
    <p id="leadDesc">填Email立即收到PDF下載連結<br>和最新日本自由行資訊</p>
    <form onsubmit="submitLeadForm(this,event)">
      <input type="email" placeholder="輸入你的Email" required id="leadEmail">
      <button type="submit" id="leadSubmitBtn">免費下載攻略</button>
    </form>
    <p class="lead-note">🔒 尊重隱私，隨時可取消訂閱</p>
  </div>
</div>'''

# New popup HTML with header/body structure
new_popup = '''<div class="lead-popup-overlay" id="leadPopup">
  <div class="lead-popup">
    <div class="lead-popup-header">
      <button class="lead-popup-close" onclick="closeLeadPopup()">&times;</button>
      <h3>📘 小編獨家攻略，限時免費送</h3>
    </div>
    <div class="lead-popup-body">
      <p id="leadDesc">填Email立即收到PDF下載連結<br>和最新日本自由行資訊</p>
      <form onsubmit="submitLeadForm(this,event)">
        <input type="email" placeholder="輸入你的Email" required id="leadEmail">
        <button type="submit" id="leadSubmitBtn">免費下載攻略</button>
      </form>
      <p class="lead-note">🔒 尊重隱私，隨時可取消訂閱</p>
    </div>
  </div>
</div>'''

count = 0
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8', errors='replace') as fp:
        content = fp.read()
    if old_popup in content:
        content = content.replace(old_popup, new_popup)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)
        count += 1

print(f'Updated {count} files with new popup HTML structure')
