import re

# === Fix 1: Delete packing-list-online.html ===
import os
if os.path.exists('packing-list-online.html'):
    os.remove('packing-list-online.html')
    print("DELETED: packing-list-online.html")
else:
    print("SKIP: packing-list-online.html already gone")

# === Fix 2: Add content to terms.html ===
with open('terms.html', 'r', encoding='utf-8') as f:
    terms = f.read()

legal_content = '''
        <div class="legal-content">
          <div class="legal-meta-bar">
            <span style="font-size:20px;">📄</span>
            <span class="meta-text">最後更新：<strong>2026年6月</strong> ｜ 適用於 <a href="https://golightly.fun/">golightly.fun</a></span>
          </div>

          <div class="legal-section open">
            <div class="legal-section-header">
              <span class="section-num-badge">1</span>
              <div class="section-title-wrap"><h2>服務說明</h2><p>Service Overview</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>本網站（golightly.fun，以下簡稱「均在路上 Travel Lab」）提供日本、韓國、台灣、東南亞自由行旅遊攻略、行程建議、預算分析等資訊內容。所有內容僅供參考，使用者應根據自身情況做出判斷。</p>
              <p>本網站保留隨時修改、暫停或終止任何服務之權利，恕不另行通知。</p>
            </div>
          </div>

          <div class="legal-section">
            <div class="legal-section-header">
              <span class="section-num-badge">2</span>
              <div class="section-title-wrap"><h2>智慧財產權</h2><p>Intellectual Property</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>本網站所有內容，包括但不限於文字、圖片、圖表、版面設計、原始碼等，均為均在路上 Travel Lab 所有，受著作權法及相關智慧財產權法律保護。</p>
              <p>未經本網站書面授權，禁止以任何形式複製、轉載、改寫、散布或使用於其他商業用途。</p>
              <p>若欲引用本網站內容（如部落格分享、媒體報導），請註明出處：「均在路上 Travel Lab（golightly.fun）」並附上原文連結。</p>
            </div>
          </div>

          <div class="legal-section">
            <div class="legal-section-header">
              <span class="section-num-badge">3</span>
              <div class="section-title-wrap"><h2>使用者責任</h2><p>User Responsibilities</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>使用本網站即表示您同意：</p>
              <ul>
                <li>✅ 不利用本網站從事任何違反法令之行為</li>
                <li>✅ 不干擾或破壞本網站之正常運作</li>
                <li>✅ 不未經授權存取本網站之系統或資料</li>
                <li>✅ 不對本網站進行任何可能造成過度負載的操作</li>
              </ul>
            </div>
          </div>

          <div class="legal-section">
            <div class="legal-section-header">
              <span class="section-num-badge">4</span>
              <div class="section-title-wrap"><h2>外部連結</h2><p>External Links</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>本網站可能包含第三方網站連結（如 Booking.com、Klook、Trip.com 等聯盟行銷連結）。這些連結僅為方便使用者參考而提供，不代表本網站對該第三方網站的內容、產品或服務背書。</p>
              <p>使用者透過聯盟連結進行消費時，本網站可能獲得少量佣金，但不會影響您的購買價格。所有聯盟合作關係均已依法揭露。</p>
            </div>
          </div>

          <div class="legal-section">
            <div class="legal-section-header">
              <span class="section-num-badge">5</span>
              <div class="section-title-wrap"><h2>條款修改</h2><p>Modifications</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>本網站保留隨時修改本使用條款之權利。修改後的條款將公布於本頁面，並於公布時立即生效。建議使用者定期查閱本條款以了解最新內容。</p>
              <p>若修改後繼續使用本網站，即視為您已接受修改後的條款。</p>
            </div>
          </div>

          <div class="legal-section">
            <div class="legal-section-header">
              <span class="section-num-badge">6</span>
              <div class="section-title-wrap"><h2>聯絡我們</h2><p>Contact</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>如對本使用條款有任何疑問，請透過以下方式聯絡我們：</p>
              <p>📧 <a href="mailto:hi@golightly.fun">hi@golightly.fun</a></p>
              <p>💬 LINE：<a href="https://line.me/R/ti/p/@938nzmjr" target="_blank">@938nzmjr</a></p>
            </div>
          </div>

        </div>
'''

# Insert legal content after <div class="legal-main">
terms = terms.replace('<div class="legal-main">', '<div class="legal-main">' + legal_content)

with open('terms.html', 'w', encoding='utf-8') as f:
    f.write(terms)
print("UPDATED: terms.html with proper legal content")

# === Fix 3: Add content to disclaimer.html ===
with open('disclaimer.html', 'r', encoding='utf-8') as f:
    disc = f.read()

disclaimer_content = '''
        <div class="legal-content">
          <div class="legal-meta-bar">
            <span style="font-size:20px;">📜</span>
            <span class="meta-text">最後更新：<strong>2026年6月</strong> ｜ 適用於 <a href="https://golightly.fun/">golightly.fun</a></span>
          </div>

          <div class="legal-section open">
            <div class="legal-section-header">
              <span class="section-num-badge">1</span>
              <div class="section-title-wrap"><h2>資訊僅供參考</h2><p>Information Purpose Only</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>本網站（golightly.fun，以下簡稱「均在路上 Travel Lab」）所提供之所有資訊，包括但不限於行程建議、預算分析、交通指南、住宿推薦等，僅供一般參考用途。</p>
              <p>我們盡力確保資訊的準確性與時效性，但不對資訊的完整性、正確性或即時性作任何明示或默示之保證。</p>
            </div>
          </div>

          <div class="legal-section">
            <div class="legal-section-header">
              <span class="section-num-badge">2</span>
              <div class="section-title-wrap"><h2>個人決策責任</h2><p>Personal Responsibility</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>本網站上的旅遊資訊（如票價、營業時間、交通時刻表等）可能隨時變動。使用者應在出發前自行查閱官方網站或與相關業者確認最新資訊。</p>
              <p>對於因使用或依賴本網站資訊而產生的任何直接或間接損失，均在路上 Travel Lab 概不負責。</p>
            </div>
          </div>

          <div class="legal-section">
            <div class="legal-section-header">
              <span class="section-num-badge">3</span>
              <div class="section-title-wrap"><h2>聯盟行銷揭露</h2><p>Affiliate Disclosure</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>本網站部分連結為聯盟行銷連結（包含 Booking.com、Klook、Trip.com 等合作夥伴）。當您透過這些連結進行消費時，本網站可能獲得少量佣金。</p>
              <p>這不會增加您的購買成本。所有聯盟收入用於維持網站營運，讓團隊能夠持續產出優質的旅遊內容。</p>
            </div>
          </div>

          <div class="legal-section">
            <div class="legal-section-header">
              <span class="section-num-badge">4</span>
              <div class="section-title-wrap"><h2>第三方內容</h2><p>Third-Party Content</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>本網站可能包含第三方提供的內容或外部網站連結。均在路上 Travel Lab 對這些第三方內容的準確性、合法性或可用性不承擔任何責任。</p>
              <p>使用者點擊外部連結即離開本網站，應自行承擔相關風險。</p>
            </div>
          </div>

          <div class="legal-section">
            <div class="legal-section-header">
              <span class="section-num-badge">5</span>
              <div class="section-title-wrap"><h2>免責範圍</h2><p>Limitation of Liability</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>在法律允許的最大範圍內，均在路上 Travel Lab 不對以下情況承擔責任：</p>
              <ul>
                <li>📌 因使用或無法使用本網站而產生的任何損害</li>
                <li>📌 本網站內容中的任何錯誤或遺漏</li>
                <li>📌 因不可抗力因素導致網站無法正常運作</li>
                <li>📌 使用者之間的糾紛或第三方索賠</li>
              </ul>
            </div>
          </div>

          <div class="legal-section">
            <div class="legal-section-header">
              <span class="section-num-badge">6</span>
              <div class="section-title-wrap"><h2>準據法</h2><p>Governing Law</p></div>
              <span class="section-chevron">▼</span>
            </div>
            <div class="legal-section-body">
              <p>本免責聲明以中華民國（台灣）法律為準據法。如發生爭議，雙方同意以台灣台北地方法院為第一審管轄法院。</p>
            </div>
          </div>

        </div>
'''

# Insert disclaimer content after <div class="legal-main">
disc = disc.replace('<div class="legal-main">', '<div class="legal-main">' + disclaimer_content)

with open('disclaimer.html', 'w', encoding='utf-8') as f:
    f.write(disc)
print("UPDATED: disclaimer.html with proper legal content")

print("\nDONE: All fixes applied")
