#!/usr/bin/env python3
"""Add 3-column sidebar card layout to all article pages (matching tokyo-5days pattern)."""
import re, os

WORKDIR = os.path.dirname(os.path.abspath(__file__))

# Article pages with their metadata
ARTICLES = {
    "tokyo-5days.html": {
        "title": "東京自由行<br>5天4夜行程表",
        "emoji": "🗼",
        "subtitle": "第一次去東京照著排！",
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "img": "tokyo-hero.webp",
        "highlights": [
            ("⛩️", "淺草寺雷門"),
            ("🏙️", "新宿歌舞伎町"),
            ("🗼", "東京鐵塔"),
            ("🛍️", "澀谷十字路口"),
            ("🍜", "拉麵一條街"),
        ],
    },
    "hokkaido-winter.html": {
        "title": "北海道冬季賞雪",
        "emoji": "❄️",
        "subtitle": "看完想換個地方？",
        "gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
        "img": "hokkaido-vertical.webp",
        "highlights": [
            ("🏔️", "小樽運河・雪燈路"),
            ("🌲", "富良野・美瑛樹冰"),
            ("🌋", "登別地獄谷溫泉"),
            ("🌃", "函館山百萬夜景"),
            ("⛄", "札幌雪祭・大通公園"),
        ],
    },
    "okinawa.html": {
        "title": "沖繩自駕<br>4天3夜攻略",
        "emoji": "🏝️",
        "subtitle": "下次改去海島度假？",
        "gradient": "linear-gradient(135deg, #11998e 0%, #38ef7d 100%)",
        "img": "okinawa-vertical.webp",
        "highlights": [
            ("🐋", "美麗海水族館"),
            ("🌉", "古宇利大橋"),
            ("🎡", "美國村"),
            ("☕", "瀨長島"),
            ("🏯", "首里城"),
        ],
    },
    "kansai-pass.html": {
        "title": "關西交通票券<br>省錢指南",
        "emoji": "🚄",
        "subtitle": "大阪京都交通全攻略",
        "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
        "img": "kansai-hero.webp",
        "highlights": [
            ("🎫", "JR Pass 全攻略"),
            ("🚌", "周遊卡比較"),
            ("💳", "ICOCA 教學"),
            ("🏯", "京都巴士一日券"),
            ("🍜", "道頓堀美食街"),
        ],
    },
    "kyoto-temples.html": {
        "title": "京都寺廟<br>楓紅散步地圖",
        "emoji": "🍁",
        "subtitle": "古都千年美學之旅",
        "gradient": "linear-gradient(135deg, #ee9ca7 0%, #ffdde1 100%)",
        "img": "kyoto-hero.webp",
        "highlights": [
            ("⛩️", "伏見稻荷大社"),
            ("🏛️", "金閣寺"),
            ("🏯", "清水寺"),
            ("🌿", "嵐山竹林"),
            ("🎎", "祇園花見小路"),
        ],
    },
    "seoul-food.html": {
        "title": "首爾必吃<br>美食攻略",
        "emoji": "🍖",
        "subtitle": "吃貨首爾5大必吃",
        "gradient": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)",
        "img": "seoul-hero.webp",
        "highlights": [
            ("🥩", "韓烤三層肉"),
            ("🍲", "部隊鍋"),
            ("🍗", "炸雞配啤酒"),
            ("🥟", "廣藏市場綠豆煎餅"),
            ("🍜", "明洞刀削麵"),
        ],
    },
    "busan-capsule.html": {
        "title": "釜山膠囊列車<br>預約教學",
        "emoji": "🚊",
        "subtitle": "海雲台藍線公園",
        "gradient": "linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)",
        "img": "busan-hero.webp",
        "highlights": [
            ("🎟️", "膠囊列車預約"),
            ("☕", "海景咖啡廳"),
            ("🏖️", "海雲台沙灘"),
            ("🌃", "廣安里夜景"),
            ("🦀", "札嘎其市場"),
        ],
    },
    "jeju-island.html": {
        "title": "濟州島自駕<br>環島3天2夜",
        "emoji": "🌋",
        "subtitle": "韓國最美海島",
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "img": "jeju-hero.webp",
        "highlights": [
            ("🌅", "城山日出峰"),
            ("🏝️", "牛島環島"),
            ("🏔️", "漢拏山"),
            ("🏖️", "翰林海灘"),
            ("🍊", "濟州柑橘"),
        ],
    },
    "hualien-taitung.html": {
        "title": "花東三天兩夜<br>縱谷漫遊",
        "emoji": "🌄",
        "subtitle": "台灣最美海岸線",
        "gradient": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
        "img": "hualien-hero.webp",
        "highlights": [
            ("🏔️", "太魯閣峽谷"),
            ("🌊", "七星潭"),
            ("稻田", "池上伯朗大道"),
            ("🏯", "瑞穗牧場"),
            ("🏝️", "綠島浮潛"),
        ],
    },
    "tainan-food.html": {
        "title": "台南美食<br>牛肉湯攻略",
        "emoji": "🍜",
        "subtitle": "國華街吃透透",
        "gradient": "linear-gradient(135deg, #f6d365 0%, #fda085 100%)",
        "img": "tainan-hero.webp",
        "highlights": [
            ("🥩", "5家必喝牛肉湯"),
            ("🍢", "國華街小吃"),
            ("☕", "老屋咖啡廳"),
            ("🏛️", "赤崁樓"),
            ("🌙", "神農街夜遊"),
        ],
    },
    "kenting.html": {
        "title": "墾丁三天兩夜<br>海景夜市攻略",
        "emoji": "🏖️",
        "subtitle": "南台灣陽光海灘",
        "gradient": "linear-gradient(135deg, #0fd850 0%, #f9f047 100%)",
        "img": "kenting-hero.webp",
        "highlights": [
            ("🌊", "南灣戲水"),
            ("🌅", "龍磐公園"),
            ("🏠", "鵝鑾鼻燈塔"),
            ("🌙", "墾丁夜市"),
            ("🛵", "機車環島"),
        ],
    },
    "chiang-mai.html": {
        "title": "清邁7天<br>數位遊牧指南",
        "emoji": "🛕",
        "subtitle": "泰北玫瑰城",
        "gradient": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
        "img": "chiangmai-hero.webp",
        "highlights": [
            ("☕", "Nomad 咖啡廳"),
            ("🛕", "古城寺廟群"),
            ("🏔️", "素帖山"),
            ("🌙", "週日夜市"),
            ("🏠", "長租公寓"),
        ],
    },
    "bangkok-3days.html": {
        "title": "曼谷3天2夜<br>吃貨攻略",
        "emoji": "🍛",
        "subtitle": "泰式街頭美食天堂",
        "gradient": "linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%)",
        "img": "bangkok-hero.webp",
        "highlights": [
            ("🛍️", "洽圖洽週末市集"),
            ("🏮", "唐人街耀華力路"),
            ("🥘", "10大必吃美食"),
            ("🚢", "昭披耶河遊船"),
            ("💆", "泰式按摩"),
        ],
    },
}

# Sidebar pairings: each article gets (left_sidebar, right_sidebar)
PAIRINGS = {
    "hokkaido-winter.html":  ("tokyo-5days.html", "okinawa.html"),
    "okinawa.html":          ("hokkaido-winter.html", "kansai-pass.html"),
    "kansai-pass.html":      ("kyoto-temples.html", "okinawa.html"),
    "kyoto-temples.html":    ("kansai-pass.html", "tokyo-5days.html"),
    "seoul-food.html":       ("busan-capsule.html", "jeju-island.html"),
    "busan-capsule.html":    ("seoul-food.html", "jeju-island.html"),
    "jeju-island.html":      ("busan-capsule.html", "seoul-food.html"),
    "hualien-taitung.html":  ("tainan-food.html", "kenting.html"),
    "tainan-food.html":      ("hualien-taitung.html", "kenting.html"),
    "kenting.html":          ("hualien-taitung.html", "tainan-food.html"),
    "chiang-mai.html":       ("bangkok-3days.html", "kenting.html"),
    "bangkok-3days.html":    ("chiang-mai.html", "kenting.html"),
}


def build_sidebar_card(page_key, position):
    """Build sidebar card HTML for a given article."""
    art = ARTICLES[page_key]
    use_circle = position == "right"  # right sidebar uses circle list style like tokyo
    img_src = f"images/{art['img']}"
    
    html_parts = []
    html_parts.append(f'<div class="sidebar-card">')
    html_parts.append(f'  <a href="{page_key}">')
    html_parts.append(f'    <img class="sb-hero-img" src="{img_src}" alt="{art["emoji"]} {art["title"].replace("<br>","")}" loading="lazy">')
    style_attr = f' style="background:{art["gradient"]};"' if position == "right" else ""
    html_parts.append(f'    <div class="sb-header"{style_attr}>')
    html_parts.append(f'      <div class="sb-title">{art["emoji"]} {art["title"]}</div>')
    html_parts.append(f'      <div class="sb-subtitle">{art["subtitle"]}</div>')
    html_parts.append(f'    </div>')
    
    if use_circle:
        html_parts.append(f'    <div class="sb-circle-list">')
    else:
        html_parts.append(f'    <div class="sb-thumb-list">')
    
    for emoji, label in art["highlights"]:
        if use_circle:
            html_parts.append(f'      <a href="{page_key}" class="sb-circle-item">')
            html_parts.append(f'        <img src="{img_src}" alt="{label}" loading="lazy">')
            html_parts.append(f'        <span class="sb-circle-label">{emoji} {label}</span>')
            html_parts.append(f'      </a>')
        else:
            html_parts.append(f'      <a href="{page_key}" class="sb-thumb-item">')
            html_parts.append(f'        <img src="{img_src}" alt="{label}" loading="lazy">')
            html_parts.append(f'        <span class="sb-thumb-label">{emoji} {label}</span>')
            html_parts.append(f'      </a>')
    
    html_parts.append(f'    </div>')
    html_parts.append(f'  </a>')
    html_parts.append(f'</div>')
    return "\n".join(html_parts)


def process_file(filename):
    """Add 3-column layout to an article page."""
    filepath = os.path.join(WORKDIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Skip if already has sidebar
    if "sidebar-card" in content:
        print(f"  SKIP (already has sidebar): {filename}")
        return False
    
    left_key, right_key = PAIRINGS.get(filename, (None, None))
    if not left_key or not right_key:
        print(f"  SKIP (no pairing): {filename}")
        return False
    
    left_card = build_sidebar_card(left_key, "left")
    right_card = build_sidebar_card(right_key, "right")
    
    # Find the article-container div and wrap it
    # Strategy: find "<div class="article-container">" and wrap from before it
    
    # Find where article-container starts
    ac_match = re.search(r'(<div\s+class="article-container">)', content)
    if not ac_match:
        # Try finding hero section end + charter banner
        # Look for the main content start after hero/banner
        print(f"  SKIP (no article-container): {filename}")
        return False
    
    # Find where article-container closes (last </div> before footer)
    # We need to find the closing </div> that matches article-container
    # Simple approach: find footer and work backwards
    
    # Find the article-container opening position
    ac_start = ac_match.start()
    
    # Strategy: find footer, then find the </div> just before it
    # That closing </div> should be the article-container close
    footer_match = re.search(r'(<!--\s*FOOTER\s*-->\s*<footer|<footer\s+class="site-footer")', content)
    if not footer_match:
        print(f"  SKIP (no footer found): {filename}")
        return False
    
    # Find the last </div> before footer
    pre_footer_text = content[:footer_match.start()]
    last_close_div = pre_footer_text.rfind('</div>')
    if last_close_div == -1:
        print(f"  SKIP (no closing div before footer): {filename}")
        return False
    
    ac_end = last_close_div + 6  # length of "</div>"
    
    # Build new content
    before = content[:ac_start]
    article_block = content[ac_start:ac_end]
    after = content[ac_end:]
    
    new_content = before
    new_content += "<div class=\"three-col-wrapper\">\n"
    new_content += left_card + "\n"
    new_content += "<div class=\"col-center\">\n"
    new_content += article_block
    new_content += "\n</div><!-- /col-center -->\n"
    new_content += right_card + "\n"
    new_content += "</div><!-- /three-col-wrapper -->\n"
    new_content += after
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"  DONE: {filename} (left={left_key}, right={right_key})")
    return True


def main():
    os.chdir(WORKDIR)
    
    article_files = [
        "hokkaido-winter.html",
        "okinawa.html",
        "kansai-pass.html",
        "kyoto-temples.html",
        "seoul-food.html",
        "busan-capsule.html",
        "jeju-island.html",
        "hualien-taitung.html",
        "tainan-food.html",
        "kenting.html",
        "chiang-mai.html",
        "bangkok-3days.html",
    ]
    
    success = 0
    for f in article_files:
        if process_file(f):
            success += 1
    
    print(f"\nProcessed {success}/{len(article_files)} files")


if __name__ == "__main__":
    main()
