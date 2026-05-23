"""Embed Trip.com promo banners directly into HTML pages."""
import os, re

REPO = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab"

# Map filename keyword → (image, alt, link)
BANNER_MAP = {
    "tokyo":       ("trip-japan.webp",    "Trip.com 日本旅遊優惠", "https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n"),
    "kansai":      ("trip-japan.webp",    "Trip.com 關西機票酒店優惠", "https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n"),
    "hokkaido":    ("trip-japan.webp",    "Trip.com 北海道機票酒店優惠", "https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n"),
    "okinawa":     ("trip-okinawa.webp",  "Trip.com 快閃沖繩 機+酒折$1000", "https://tw.trip.com/sale/w/17859/okinawapromotion.html?locale=zh-TW&promo_referer=3952_17859_2&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011395"),
    "kyoto":       ("trip-japan.webp",    "Trip.com 京都機票酒店優惠", "https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n"),
    "osaka":       ("trip-japan.webp",    "Trip.com 大阪機票酒店優惠", "https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n"),
    "japan":       ("trip-japan.webp",    "Trip.com 日本旅遊優惠", "https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n"),
    "seoul":       ("trip-korea.webp",    "Trip.com 暢遊韓國五折起", "https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&promo_referer=3952_4337_8&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011353"),
    "busan":       ("trip-busan.webp",    "Trip.com 釜山遊 機+酒$999起", "https://tw.trip.com/sale/w/31376/superbusan-promotion.html?locale=zh-TW&promo_referer=3952_31376_3&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011416"),
    "jeju":        ("trip-korea.webp",    "Trip.com 暢遊韓國五折起", "https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&promo_referer=3952_4337_8&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011353"),
    "korea":       ("trip-korea.webp",    "Trip.com 暢遊韓國五折起", "https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&promo_referer=3952_4337_8&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011353"),
    "hualien":     ("trip-taiwan.webp",   "Trip.com 台灣飯店五折起", "https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507"),
    "tainan":      ("trip-taiwan.webp",   "Trip.com 台灣飯店五折起", "https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507"),
    "kenting":     ("trip-taiwan.webp",   "Trip.com 台灣飯店五折起", "https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507"),
    "taipei":      ("trip-taiwan.webp",   "Trip.com 台灣飯店五折起", "https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507"),
    "taiwan":      ("trip-taiwan.webp",   "Trip.com 台灣飯店五折起", "https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507"),
    "chiang-mai":  ("trip-thailand.webp", "Trip.com 泰國五折優惠", "https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"),
    "bangkok":     ("trip-thailand.webp", "Trip.com 曼谷五折優惠", "https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"),
    "southeast":   ("trip-thailand.webp", "Trip.com 東南亞機票優惠", "https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"),
    "vietnam":     ("trip-thailand.webp", "Trip.com 泰國五折優惠", "https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"),
    "hongkong":    ("trip-hongkong.webp", "Trip.com 港澳快閃優惠", "https://tw.trip.com/sale/w/5025/cn-hk-mo-promotion.html?locale=zh_tw&promo_referer=3952_5025_10&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17079001"),
}

# Skip these pages
SKIP = {"index.html", "about.html", "contact.html", "privacy.html", "terms.html", "disclaimer.html", "travel-tools.html"}

# CSS to inject once
BANNER_CSS = """
<style>
.trip-promo-inline {
  margin: 32px 0;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  transition: transform 0.2s, box-shadow 0.2s;
}
.trip-promo-inline:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 24px rgba(0,0,0,0.12);
}
.trip-promo-inline a { display: block; }
.trip-promo-inline img { width: 100%; height: auto; display: block; }
</style>
"""

def get_banner(filename):
    """Match filename to banner, most specific first."""
    name = filename.lower().replace(".html", "")
    # Check specific keywords first (longer matches)
    for key in sorted(BANNER_MAP.keys(), key=len, reverse=True):
        if key in name:
            return BANNER_MAP[key]
    return None

def process_file(filepath):
    filename = os.path.basename(filepath)
    if filename in SKIP:
        return False
    
    banner = get_banner(filename)
    if not banner:
        return False
    
    img, alt, link = banner
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Skip if already embedded
    if "trip-promo-inline" in html:
        print(f"  SKIP (already embedded): {filename}")
        return False
    
    # Build the inline HTML block
    banner_html = f'''
<div class="trip-promo-inline">
  <a href="{link}" target="_blank" rel="noopener sponsored" data-affiliate="trip">
    <img src="images/{img}" alt="{alt}" loading="lazy" />
  </a>
</div>
'''
    
    # Insert after first </h2> closing tag
    h2_close = html.find("</h2>")
    if h2_close == -1:
        # Try after first <hr> or before article-bottom-cta
        insert_pos = html.find('<div class="article-bottom-cta">')
        if insert_pos == -1:
            insert_pos = html.find("</article>") or html.find("</div>", html.find("article-container"))
            if insert_pos == -1:
                print(f"  SKIP (no insert point): {filename}")
                return False
    else:
        insert_pos = h2_close + len("</h2>")
    
    html = html[:insert_pos] + banner_html + html[insert_pos:]
    
    # Add CSS before </head> if not already there
    if "trip-promo-inline" not in html[:html.find("</head>")]:
        html = html.replace("</head>", BANNER_CSS + "\n</head>", 1)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"  OK: {filename} → {img}")
    return True

count = 0
for fn in os.listdir(REPO):
    if fn.endswith(".html") and fn not in SKIP:
        result = process_file(os.path.join(REPO, fn))
        if result:
            count += 1

print(f"\nDone: {count} pages updated")
