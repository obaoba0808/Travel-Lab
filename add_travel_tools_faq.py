import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('travel-tools.html', encoding='utf-8') as f:
    c = f.read()

faq_html = '''
<section class="faq-section" style="max-width:900px;margin:40px auto;padding:0 40px;">
<h2 class="section-title">❓ 常見問題</h2>
<div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">出國旅行一定要帶什麼？</div><div class="faq-a">必帶：護照、機票住宿確認單（截圖備用）、海外旅遊保險、信用卡+少許現金、行動電源、轉換插頭。選帶：常備藥、防盜腰包、壓縮袋。最重要是保險，醫療費在國外可能天價。</div></div>
<div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">旅行保險怎麼選？</div><div class="faq-a">重點看三項：①海外醫療保額（建議NT$100萬以上）②緊急醫療轉送 ③行程取消/延誤理賠。富邦、國泰、安達的旅遊險都不錯，一週旅程保費約NT$500-1,200。</div></div>
<div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">海外上網最省錢的方式？</div><div class="faq-a">短期旅行推薦eSIM（日本5天NT$200起，韓國NT$250起），出發前裝好落地就有網。長期或多國：租行動Wi-Fi（每天NT$100-150）。</div></div>
<div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">機場免稅店比市區便宜嗎？</div><div class="faq-a">不一定！化妝品和香水通常便宜10-20%，但電子產品未必。韓國仁川免稅店化妝品最划算，日本成田免稅店巧克力便宜。先記好市區價格到免稅店再比。</div></div>
<div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">旅行行李怎麼打包最省空間？</div><div class="faq-a">①捲式收納比摺疊省30%空間 ②真空壓縮袋裝外套 ③鞋內塞襪子 ④貴重物品隨身帶 ⑤用旅行分裝瓶裝洗沐用品。手提行李7kg內盡量搞定，省托運費又省時間。</div></div>
</section>
'''

# Insert before <!-- FOOTER -->
c = c.replace('<!-- FOOTER -->', faq_html + '\n<!-- FOOTER -->')

with open('travel-tools.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("DONE travel-tools.html: added 5 FAQs")
