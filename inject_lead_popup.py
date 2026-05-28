import os

POPUP_CONFIGS = {
    "tokyo-5days.html": ("東京地鐵攻略免費送！", "東京5天地鐵全圖PDF免費下載，含所有景點標記與出口資訊", "tokyo-metro-map", "免費下載東京地鐵圖"),
    "kansai-pass.html": ("關西票券省錢秘籍！", "JR Pass + 京都巴士三日券省錢試算表免費送", "kansai-pass-calculator", "立即試算我能省多少"),
    "hokkaido-winter.html": ("北海道冬季穿搭攻略！", "免費下載冬季穿搭清單 + 防寒裝備檢查表", "hokkaido-packing-list", "下載冬季穿搭清單"),
    "okinawa.html": ("沖繩自駕必備地圖！", "免費下載沖繩自駕路線圖PDF，含停車場位置", "okinawa-driving-map", "下載自駕路線圖"),
    "kyoto-temples.html": ("京都賞楓時間表2026！", "京都賞楓最佳觀測點+預測時間表PDF", "kyoto-momiji-schedule", "免費下載賞楓時間表"),
    "osaka-food.html": ("大阪美食地圖免費送！", "20家道頓堀美食位置圖PDF，含排隊時間與必吃理由", "osaka-food-map", "下載大阪美食地圖"),
    "osaka-usj.html": ("USJ快速通關攻略！", "免費下載FP抽籤攻略+刺激設施排行", "usj-quick-pass", "下載快速通關攻略"),
    "japan-budget-guide.html": ("日本預算試算表！", "免費下載日本7天預算表，含餐費/交通/門票", "japan-budget-sheet", "下載預算表"),
    "seoul-food.html": ("首爾美食地圖免費送！", "明洞/弘大/江南三大區美食地圖PDF", "seoul-food-map", "下載首爾美食地圖"),
    "busan-capsule.html": ("釜山膠囊列車預約攻略！", "免費下載預約時間表+乘車攻略", "busan-capsule-guide", "下載預約攻略"),
    "jeju-island.html": ("濟州島自駕路線圖！", "免費下載環島路線圖PDF，含每站停留時間", "jeju-driving-route", "下載環島路線圖"),
    "korea-budget.html": ("韓國5天預算表！", "免費下載韓國5天預算表，含餐費/交通/門票", "korea-budget-sheet", "下載預算表"),
    "hualien-taitung.html": ("花東三天行程表！", "免費下載花東三天兩夜行程表PDF", "hualien-itinerary", "下載行程表"),
    "tainan-food.html": ("台南牛肉湯地圖！", "免費下載台南牛肉湯地圖PDF，含營業時間", "tainan-food-map", "下載牛肉湯地圖"),
    "kenting.html": ("墾丁夜市美食清單！", "免費下載墾丁夜市美食清單PDF", "kenting-night-market", "下載夜市美食清單"),
    "taipei-food.html": ("台北美食地圖！", "免費下載台北美食地圖PDF", "taipei-food-map", "下載台北美食地圖"),
    "jiufen.html": ("九份老街攻略！", "免費下載九份老街攻略PDF", "jiufen-guide", "下載老街攻略"),
    "chiang-mai.html": ("清邁數位遊牧指南！", "免費下載清邁簽證攻略+共享空間清單", "chiang-mai-guide", "下載簽證攻略"),
    "bangkok-3days.html": ("曼谷美食地圖！", "免費下載曼谷美食地圖PDF", "bangkok-food-map", "下載美食地圖"),
    "bangkok-massage.html": ("曼谷按摩地圖！", "免費下載22家合法按摩店位置圖PDF", "bangkok-massage-map", "下載按摩地圖"),
    "vietnam-danang.html": ("峴港景點地圖！", "免費下載巴拿山+美溪沙灘路線圖PDF", "danang-map", "下載景點地圖"),
}

def build_popup_html(title, subtitle, resource, button):
    # Build popup HTML using string concatenation to avoid f-string brace issues
    popup = (
        '<!-- Email Lead Magnet Popup -->\n'
        '<div id="lead-magnet-popup" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;z-index:9999;background:rgba(0,0,0,0.6);font-family:\'Noto Sans TC\',sans-serif;">\n'
        '  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);background:#fff;border-radius:20px;padding:40px;max-width:520px;width:90%;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,0.3);">\n'
        '    <button onclick="closeLeadPopup()" style="position:absolute;top:16px;right:20px;background:none;border:none;font-size:24px;cursor:pointer;color:#999;">&times;</button>\n'
        '    <div style="background:#0ABAB5;color:#fff;border-radius:50%;width:64px;height:64px;line-height:64px;font-size:32px;margin:0 auto 20px;">&#9992;&#65039;</div>\n'
        '    <h2 id="popup-title" style="color:#0ABAB5;margin:0 0 8px;font-size:22px;">' + title + '</h2>\n'
        '    <p id="popup-subtitle" style="color:#555;margin:0 0 24px;font-size:15px;line-height:1.6;">' + subtitle + '</p>\n'
        '    <form id="lead-form" onsubmit="submitLeadForm(event)">\n'
        '      <input type="email" id="lead-email" placeholder="輸入你的Email" required style="width:100%;padding:14px 16px;border:2px solid #0ABAB5;border-radius:10px;font-size:16px;margin-bottom:12px;box-sizing:border-box;">\n'
        '      <input type="hidden" id="lead-resource" value="' + resource + '">\n'
        '      <button type="submit" style="width:100%;padding:14px;background:#0ABAB5;color:#fff;border:none;border-radius:10px;font-size:16px;font-weight:700;cursor:pointer;">' + button + '</button>\n'
        '    </form>\n'
        '    <p style="margin:10px 0 0;font-size:12px;color:#aaa;">我們重視隱私，不會寄垃圾郵件，隨時可退訂</p>\n'
        '  </div>\n'
        '</div>\n'
        '<script>\n'
        'var leadPopupShown=false;\n'
        'window.addEventListener(\'scroll\',function(){\n'
        '  if(leadPopupShown)return;\n'
        '  var sh=document.documentElement.scrollHeight-window.innerHeight;\n'
        '  var sp=(window.scrollY/sh)*100;\n'
        '  if(sp>60){\n'
        '    leadPopupShown=true;\n'
        '    var p=document.getElementById(\'lead-magnet-popup\');\n'
        '    if(p){p.style.display=\'block\';p.style.animation=\'fadeInPopup 0.4s ease\';}\n'
        '  }\n'
        '});\n'
        'function closeLeadPopup(){\n'
        '  var p=document.getElementById(\'lead-magnet-popup\');\n'
        '  if(p)p.style.display=\'none\';\n'
        '  try{localStorage.setItem(\'leadShown_\'+location.pathname,\'1\');}catch(e){}\n'
        '}\n'
        'function submitLeadForm(e){\n'
        '  e.preventDefault();\n'
        '  var f=document.getElementById(\'lead-form\');\n'
        '  f.innerHTML=\'<div style="color:#0ABAB5;font-size:18px;font-weight:700;">&#10004;&#65039; 已收到！<br><span style="font-size:14px;color:#555;">請到 Email 收件匣確認，我們已發送下載連結給你！</span></div>\';\n'
        '  try{localStorage.setItem(\'leadShown_\'+location.pathname,\'1\');}catch(e){}\n'
        '  closeLeadPopup();\n'
        '}\n'
        '</script>\n'
        '<style>\n'
        '@keyframes fadeInPopup{from{opacity:0;transform:translate(-50%,-45%);}to{opacity:1;transform:translate(-50%,-50%);}}\n'
        '</style>'
    )
    return popup

workspace = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab"

results = []
for filename, cfg in POPUP_CONFIGS.items():
    filepath = os.path.join(workspace, filename)
    if not os.path.exists(filepath):
        results.append("SKIP: {} not found".format(filename))
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'id="lead-magnet-popup"' in content:
        results.append("EXISTS: {} already has popup".format(filename))
        continue

    popup_html = build_popup_html(cfg[0], cfg[1], cfg[2], cfg[3])

    if '</body>' in content:
        new_content = content.replace('</body>', popup_html + '\n</body>', 1)
    elif '</BODY>' in content:
        new_content = content.replace('</BODY>', popup_html + '\n</BODY>', 1)
    else:
        results.append("WARN: {} has no </body> tag".format(filename))
        continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    results.append("OK:   {}".format(filename))

print("=== LEAD MAGNET POPUP INJECTION RESULTS ===")
for r in results:
    print(r)
ok_count = len([r for r in results if r.startswith("OK:")])
print("\nTotal: {} files processed, {} updated".format(len(results), ok_count))
