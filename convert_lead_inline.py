"""Convert lead popup to inline form after last FAQ item"""
import os
import re

HTML_FILES = [
    'tokyo-5days.html', 'kansai-pass.html', 'hokkaido-winter.html', 'okinawa.html',
    'kyoto-temples.html', 'osaka-food.html', 'osaka-usj.html', 'japan-budget-guide.html',
    'seoul-food.html', 'busan-capsule.html', 'jeju-island.html', 'korea-budget.html',
    'hualien-taitung.html', 'tainan-food.html', 'kenting.html', 'taipei-food.html',
    'jiufen.html', 'chiang-mai.html', 'bangkok-3days.html', 'bangkok-massage.html',
    'vietnam-danang.html'
]

INLINE_FORM_html = '''
    <div class="lead-inline">
      <div class="lead-inline-icon">📘</div>
      <h3>小編獨家攻略，限時免費送</h3>
      <p>填Email立即收到PDF下載連結和最新旅遊資訊</p>
      <form onsubmit="submitLeadForm(this,event)">
        <input type="email" placeholder="輸入你的Email" required id="leadEmail">
        <button type="submit" id="leadSubmitBtn">免費下載攻略</button>
      </form>
      <p class="lead-note">🔒 尊重隱秘，隨時可取消訂閱</p>
    </div>
'''

# CSS for inline form
INLINE_CSS = '''
/* Inline Lead Form */
.lead-inline {
  background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
  border-radius: 16px;
  padding: 32px;
  text-align: center;
  margin: 48px auto;
  max-width: 600px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  border: 2px solid #81c784;
}
.lead-inline-icon {
  font-size: 48px;
  margin-bottom: 12px;
}
.lead-inline h3 {
  color: #2e7d32;
  margin: 0 0 12px;
  font-size: 22px;
}
.lead-inline > p {
  color: #558b2f;
  margin: 0 0 20px;
  font-size: 15px;
}
.lead-inline form {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
}
.lead-inline input[type="email"] {
  padding: 14px 18px;
  border: 2px solid #81c784;
  border-radius: 10px;
  font-size: 16px;
  width: 240px;
  transition: border-color 0.3s;
}
.lead-inline input[type="email"]:focus {
  outline: none;
  border-color: #43a047;
  box-shadow: 0 0 0 3px rgba(67, 160, 71, 0.15);
}
.lead-inline button {
  background: linear-gradient(135deg, #43a047 0%, #2e7d32 100%);
  color: white;
  border: none;
  padding: 14px 28px;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}
.lead-inline button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(46, 125, 50, 0.35);
}
.lead-inline button:disabled {
  background: #9e9e9e;
  cursor: not-allowed;
  transform: none;
}
.lead-note {
  font-size: 13px;
  color: #78909c;
  margin: 16px 0 0;
}
'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Add inline CSS to style.css if not exists
    style_path = os.path.join(os.path.dirname(filepath), 'style.css')
    if os.path.exists(style_path):
        with open(style_path, 'r', encoding='utf-8') as f:
            style_content = f.read()
        if '.lead-inline' not in style_content:
            with open(style_path, 'a', encoding='utf-8') as f:
                f.write('\n' + INLINE_CSS)
            print(f"Added CSS to style.css")

    # 2. Insert inline form AFTER last FAQ item, before </section>
    # Find the last </div> inside faq-section before </section>
    faq_pattern = r'(<section class="faq-section">.*?)(<div class="faq-item"[^>]*>.*?</div>\s*</div>\s*)(</section>)'
    
    def replace_faq(m):
        header = m.group(1)
        last_faq_item = m.group(2)
        closing = m.group(3)
        return header + last_faq_item + INLINE_FORM_html.strip() + '\n  ' + closing

    new_content = re.sub(faq_pattern, replace_faq, content, flags=re.DOTALL)
    
    if new_content == content:
        print(f"  [WARN] Could not find FAQ pattern in {filepath}")
        return False

    # 3. Remove popup overlay HTML (lead-popup-overlay)
    popup_pattern = r'\s*<div class="lead-popup-overlay" id="leadPopup">.*?</div>\s*</div>\s*'
    new_content = re.sub(popup_pattern, '', new_content, flags=re.DOTALL)

    # 4. Disable scroll trigger in JS (comment out)
    js_scroll_pattern = r"window\.addEventListener\('scroll',function\(\)\{[^}]+}\);"
    new_content = re.sub(js_scroll_pattern, "// window.addEventListener('scroll',...) // disabled - using inline form", new_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  [OK] {filepath}")
    return True

def main():
    base_dir = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab"
    
    success_count = 0
    for html_file in HTML_FILES:
        filepath = os.path.join(base_dir, html_file)
        if os.path.exists(filepath):
            if process_file(filepath):
                success_count += 1
        else:
            print(f"  [NOT FOUND] {html_file}")
    
    print(f"\nDone: {success_count}/{len(HTML_FILES)} files processed")

if __name__ == '__main__':
    main()