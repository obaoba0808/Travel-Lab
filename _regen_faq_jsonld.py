import re
import json

with open('tainan-food.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Properly construct the FAQPage JSON-LD
faq_data = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "台南牛肉湯幾點去最好？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "溫體牛肉湯凌晨4-5點最新鮮！很多名店5點開門，7點前肉質最佳。不想早起也沒關係，大部分店家營業到下午。"
            }
        },
        {
            "@type": "Question",
            "name": "台南美食两天怎麼排？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Day1國華街+赤崁樓+神農街，Day2牛肉湯早餐+安平老街+安平古堡。每餐之間留2小時散步消化，台南節奏本來就慢。"
            }
        },
        {
            "@type": "Question",
            "name": "台南住哪裡最方便吃美食？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "中西區（赤崁樓/國華街附近）美食最密集，步行就能吃遍小吃。安平區適合想住海邊民宿的旅人。火車站附近選擇多但離小吃區稍遠。"
            }
        },
        {
            "@type": "Question",
            "name": "台南小吃一個人可以吃嗎？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "完全可以！台南小吃本來就是一人份為主，牛肉湯、碗粿、蝦捲、肉圓都是單人友善。有些店家沒有座位，站著吃是台南日常。"
            }
        },
        {
            "@type": "Question",
            "name": "台南咖啡廳推薦哪些？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "老屋咖啡推薦：Kadoya喫茶店、窄門咖啡、奉茶十八卯。文青風：StableNice、重慶寺、雙全紅茶。台南咖啡廳特色是老宅改建，每家都有自己的故事。"
            }
        }
    ]
}

# Generate minified JSON-LD (no newlines in strings)
faq_json = json.dumps(faq_data, ensure_ascii=False, separators=(',', ':'))

# Find and replace the FAQPage JSON-LD block
old_pattern = r'<script type="application/ld\+json">\{"@context":"https://schema\.org","@type":"FAQPage".*?\}</script>'
new_block = f'<script type="application/ld+json">{faq_json}</script>'

# Use re.DOTALL to match across lines
new_content = re.sub(old_pattern, new_block, content, flags=re.DOTALL)

if new_content == content:
    print('WARNING: No replacement made - pattern not matched')
    # Try a different approach - find by position
    # Find the FAQPage block
    start = content.find('{"@context":"https://schema.org","@type":"FAQPage"')
    if start > 0:
        end = content.find('}</script>', start) + len('}</script>')
        old_block = content[start-len('<script type="application/ld+json">'):end]
        print(f'Found FAQPage block: {old_block[:100]}...')
        new_content = content[:start-len('<script type="application/ld+json">')] + new_block + content[end:]
        print('Replaced using position-based approach')
else:
    print('Replacement successful using regex')

with open('tainan-food.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done - FAQPage JSON-LD regenerated')
