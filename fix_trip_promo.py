# -*- coding: utf-8 -*-
import os
import re

# 目的地對應圖片和連結
TRIP_PROMOS = {
    # 日本
    'japan-budget-guide': {'img': 'trip-japan.webp', 'url': 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n', 'alt': 'Trip 日本自由行優惠'},
    'japan-travel': {'img': 'trip-japan.webp', 'url': 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n', 'alt': 'Trip 日本自由行優惠'},
    'tokyo-5days': {'img': 'trip-japan.webp', 'url': 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n', 'alt': 'Trip 日本自由行優惠'},
    'kansai-pass': {'img': 'trip-japan.webp', 'url': 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n', 'alt': 'Trip 日本自由行優惠'},
    'hokkaido-winter': {'img': 'trip-japan.webp', 'url': 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n', 'alt': 'Trip 日本自由行優惠'},
    'okinawa': {'img': 'trip-okinawa.webp', 'url': 'https://tw.trip.com/sale/w/17859/okinawapromotion.html?locale=zh-TW&promo_referer=3952_17859_2&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011395', 'alt': 'Trip 沖繩機加酒優惠'},
    'kyoto-temples': {'img': 'trip-japan.webp', 'url': 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n', 'alt': 'Trip 日本自由行優惠'},
    'osaka-usj': {'img': 'trip-japan.webp', 'url': 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n', 'alt': 'Trip 日本自由行優惠'},
    'osaka-food': {'img': 'trip-japan.webp', 'url': 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n', 'alt': 'Trip 日本自由行優惠'},
    # 韓國
    'korea-travel': {'img': 'trip-korea.webp', 'url': 'https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&promo_referer=3952_4337_8&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011353', 'alt': 'Trip 韓國自由行優惠'},
    'korea-budget': {'img': 'trip-korea.webp', 'url': 'https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&promo_referer=3952_4337_8&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011353', 'alt': 'Trip 韓國自由行優惠'},
    'seoul-food': {'img': 'trip-korea.webp', 'url': 'https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&promo_referer=3952_4337_8&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011353', 'alt': 'Trip 韓國自由行優惠'},
    'busan-capsule': {'img': 'trip-busan.webp', 'url': 'https://tw.trip.com/sale/w/31376/superbusan-promotion.html?locale=zh-TW&promo_referer=3952_31376_3&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011416', 'alt': 'Trip 釜山機加酒優惠'},
    'jeju-island': {'img': 'trip-korea.webp', 'url': 'https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&promo_referer=3952_4337_8&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011353', 'alt': 'Trip 韓國自由行優惠'},
    # 台灣
    'taiwan-travel': {'img': 'trip-taiwan.webp', 'url': 'https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507', 'alt': 'Trip 台灣旅遊優惠'},
    'taipei-food': {'img': 'trip-taiwan.webp', 'url': 'https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507', 'alt': 'Trip 台灣旅遊優惠'},
    'hualien-taitung': {'img': 'trip-taiwan.webp', 'url': 'https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507', 'alt': 'Trip 台灣旅遊優惠'},
    'tainan-food': {'img': 'trip-taiwan.webp', 'url': 'https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507', 'alt': 'Trip 台灣旅遊優惠'},
    'kenting': {'img': 'trip-taiwan.webp', 'url': 'https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507', 'alt': 'Trip 台灣旅遊優惠'},
    # 東南亞
    'southeast-asia': {'img': 'trip-thailand.webp', 'url': 'https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987', 'alt': 'Trip 東南亞自由行優惠'},
    'chiang-mai': {'img': 'trip-thailand.webp', 'url': 'https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987', 'alt': 'Trip 泰國自由行優惠'},
    'bangkok-3days': {'img': 'trip-thailand.webp', 'url': 'https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987', 'alt': 'Trip 泰國自由行優惠'},
    'bangkok-massage': {'img': 'trip-thailand.webp', 'url': 'https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987', 'alt': 'Trip 泰國自由行優惠'},
    'hongkong-3days': {'img': 'trip-hongkong.webp', 'url': 'https://tw.trip.com/sale/w/5025/cn-hk-mo-promotion.html?locale=zh_tw&promo_referer=3952_5025_10&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17079001', 'alt': 'Trip 港澳自由行優惠'},
    'vietnam-danang': {'img': 'trip-thailand.webp', 'url': 'https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987', 'alt': 'Trip 東南亞自由行優惠'},
}

# 匹配 iframe 的正則
IFRAME_PATTERN = re.compile(r'<iframe[^>]*src="https://tw\.trip\.com/partners/ad/DB[^"]*"[^>]*></iframe>', re.IGNORECASE)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 獲取文件名（不含路徑和擴展名）
    basename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(basename)[0]
    
    # 查找對應的推廣信息
    promo = TRIP_PROMOS.get(name_without_ext)
    if not promo:
        print(f"  [SKIP] {basename}: 無對應推廣配置")
        return False
    
    # 檢查是否已經有圖片
    if 'trip-' in content and '.webp' in content and promo['img'] in content:
        print(f"  [SKIP] {basename}: 已經是圖片")
        return False
    
    # 替換 iframe 為圖片
    def replace_iframe(match):
        return f'''<a href="{promo['url']}" target="_blank" rel="noopener sponsored" class="trip-promo-inline">
          <img src="images/{promo['img']}" alt="{promo['alt']}" style="width:100%;height:auto;display:block;">
        </a>'''
    
    new_content = IFRAME_PATTERN.sub(replace_iframe, content)
    
    if new_content == content:
        print(f"  [SKIP] {basename}: 未找到 iframe")
        return False
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  [OK] {basename} -> {promo['img']}")
    return True

# 處理所有 HTML 文件
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
count = 0

print(f"處理 {len(html_files)} 個 HTML 文件...")

for html_file in html_files:
    if process_file(html_file):
        count += 1

print(f"\n完成！共修改 {count} 個文件")
