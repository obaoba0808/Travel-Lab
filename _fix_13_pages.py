import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# 13 pages with form AFTER footer (need to move form before footer)
BROKEN_PAGES = [
    'bangkok-massage.html',
    'busan-capsule.html',
    'hualien-taitung.html',
    'japan-budget-guide.html',
    'jeju-island.html',
    'jiufen.html',
    'kansai-pass.html',
    'korea-budget.html',
    'osaka-usj.html',
    'tainan-food.html',
    'taipei-food.html',
    'vietnam-danang.html',
]

PDF_MAP = {
    'bangkok-massage.html': 'bangkok-massage-map',
    'busan-capsule.html': 'busan-capsule-guide',
    'hualien-taitung.html': 'hualien-itinerary',
    'japan-budget-guide.html': 'japan-budget-sheet',
    'jeju-island.html': 'jeju-driving-route',
    'jiufen.html': 'jiufen-guide',
    'kansai-pass.html': 'kansai-pass-calculator',
    'korea-budget.html': 'korea-budget-sheet',
    'osaka-usj.html': 'usj-quick-pass',
    'tainan-food.html': 'tainan-food-map',
    'taipei-food.html': 'taipei-food-map',
    'vietnam-danang.html': 'danang-map',
}

FORM_HTML = '''<section class="lead-inline">
  <div class="lead-inline-icon">&#128236;</div>
  <h3>小編獨家攻略，限時免費送</h3>
  <p>填Email立即收到PDF下載連結和最新旅遊資訊</p>
  <form onsubmit="submitLeadForm(event);return false">
    <input type="email" placeholder="輸入你的Email" required id="leadEmail">
    <button type="submit" id="leadSubmitBtn">免費下載攻略</button>
  </form>
  <div id="leadMsg" style="font-size:13px;margin-top:8px;min-height:20px;"></div>
  <p class="lead-note">&#128274; 尊重隱私，隨時可取消訂閱</p>
</section>'''

def extract_form_section(html):
    """Extract the lead-inline form HTML from the file."""
    start = html.find('<section class="lead-inline">')
    if start == -1:
        start = html.find('<div class="lead-inline">')
    if start == -1:
        return None
    end = html.find('</section>', start)
    if end == -1:
        end = html.find('</div>', start)
        end = html.find('</div>', end + 6)  # find second </div>
    if end != -1:
        end += len('</section>')
    return html[start:end]

def remove_form_and_js(html, fname):
    """Remove the old form HTML and inline JS from body."""
    # Remove form section
    form_start = html.find('<section class="lead-inline">')
    if form_start == -1:
        form_start = html.find('<div class="lead-inline">')
    if form_start != -1:
        form_end = html.find('</section>', form_start)
        if form_end != -1:
            form_end += len('</section>')
            html = html[:form_start] + html[form_end:]
    
    # Remove inline JS (the submitLeadForm script)
    # Pattern: <script>const WORKER_URL=...submitLeadForm...</script>
    js_pattern = r'<script>const WORKER_URL=.*?</script>'
    html = re.sub(js_pattern, '', html, flags=re.DOTALL)
    
    return html

for fname in BROKEN_PAGES:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check current state
    form_pos = html.find('class="lead-inline"')
    foot_pos = html.find('<footer')
    
    if form_pos == -1:
        print(f'NO FORM: {fname}')
        continue
    
    if form_pos < foot_pos:
        print(f'ALREADY OK: {fname}')
        continue
    
    # Remove old form and JS
    html = remove_form_and_js(html, fname)
    
    # Find insertion point: before <!-- FOOTER --> or <footer
    foot_comment = html.find('<!-- FOOTER -->')
    foot_tag = html.find('<footer')
    
    if foot_comment != -1:
        insert_pos = foot_comment
    elif foot_tag != -1:
        insert_pos = foot_tag
    else:
        print(f'NO FOOTER: {fname}')
        continue
    
    # Insert form
    html = html[:insert_pos] + FORM_HTML + '\n' + html[insert_pos:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Verify
    new_form = html.find('class="lead-inline"')
    new_foot = html.find('<footer')
    print(f'{"OK" if new_form < new_foot else "FAIL"}: {fname} (form@{new_form}, footer@{new_foot})')
