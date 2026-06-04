#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate batch_final.py with correct UTF-8 encoding"""

import json

# 1. 生成 link_mapping.json (纯 ASCII URL)
link_mapping = {
    'tokyo-metro-map': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283447&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F1552-subway-ticket-tokyo%2F'],
    'japan-budget-sheet': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-HK%2Factivity%2F3277-5-day-kansai-wide-area-jr-pass%2F'],
    'okinawa-driving-map': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry%2F'],
    'kyoto-momiji-schedule': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282006&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E4%25BA%25AC%25E9%2583%25BD'],
    'osaka-food-map': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282013&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E5%25A4%25A7%25E9%2598%25AA%25E7%25BE%258E%25E9%25A3%259F'],
    'seoul-food-map': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282023&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E9%25A6%2596%25E7%2588%25BE%25E7%25BE%258E%25E9%25A3%259F'],
    'korea-budget-sheet': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282023&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F1938-korea-rail-pass-korail-pass%2F'],
    'busan-capsule-guide': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282009&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F65663-busan-air-cruise-capsule-train%2F'],
    'jeju-driving-route': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282026&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E6%25B5%258E%25E5%25B7%259E%25E5%25B3%25B6'],
    'taipei-food-map': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282378&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E5%258F%25B0%25E5%258C%2597%25E5%25A4%259C%25E5%25B8%2582'],
    'tainan-food-map': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282376&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E5%258F%25B0%25E5%258D%2597%25E7%25BE%258E%25E9%25A3%259F'],
    'hualien-itinerary': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282375&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E8%258A%25B1%25E7%25BE%258E'],
    'kenting-night-market': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282377&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E8%2582%25AF%25E4%25B8%2581%25E5%25A4%259C%25E5%25B8%2582'],
    'jiufen-guide': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282378&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E4%25B9%259D%25E4%25BB%25BD'],
    'bangkok-food-map': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282013&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E6%259B%25BC%25E8%25B0%25B7%25E7%25BE%258E%25E9%25A3%259F'],
    'bangkok-massage-map': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282013&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E6%259B%25BC%25E8%25B0%25B7%25E6%258C%2589%25E6%2591%25A9'],
    'chiang-mai-guide': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282031&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E6%25B8%2585%25E8%25BF%2588'],
    'danang-map': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282013&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E5%25B4%25C5%25E6%2598%258E'],
    'hokkaido-packing-list': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282007&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Fsearch%2F%3Fq%3D%25E5%258C%2597%25E6%25B5%25B7%25E9%2581%2593'],
    'kansai-pass-calculator': ['https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-HK%2Factivity%2F3277-5-day-kansai-wide-area-jr-pass%2F'],
    'usj-quick-pass': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry%2F',
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F3407-universal-studios-japan-express-pass-osaka%2F'
    ]
}

with open('link_mapping.json', 'w', encoding='ascii') as f:
    json.dump(link_mapping, f, ensure_ascii=True, indent=2)

print('✅ Created link_mapping.json')

# 2. 生成 batch_final.py (UTF-8 with Chinese text)
batch_script = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch process PDFs with destination-specific affiliate links"""

import fitz
import json
import os

# Tiffany Green color
TIFFANY = (0.3, 0.71, 0.67)
TIFFANY_DARK = (0.15, 0.65, 0.6)

# Load link mapping
with open('link_mapping.json', 'r', encoding='ascii') as f:
    LINK_MAP = json.load(f)

# Chinese texts
FOOTER_TEXT = '📌 更多旅遊攻略 👉 golightly.fun   |   LINE 群組   |   Klook 優惠   |   Trip.com 優惠'
TIP_TEXT = '💡 推薦：Klook 上有更多當地體驗，點此查看優惠'

def add_links(pdf_path, output_path, klook_links):
    doc = fitz.open(pdf_path)
    for page_num in range(doc.page_count):
        page = doc[page_num]
        rect = page.rect
        
        # Footer
        footer_rect = fitz.Rect(rect.x0 + 50, rect.y1 - 40, rect.x1 - 50, rect.y1 - 10)
        page.insert_textbox(footer_rect, FOOTER_TEXT, fontsize=8.5, color=TIFFANY, align=fitz.TEXT_ALIGN_CENTER)
        
        y0 = rect.y1 - 40
        y1 = rect.y1 - 10
        
        page.insert_link({'kind': fitz.LINK_URI, 'uri': 'https://golightly.fun',
                         'from': fitz.Rect(rect.x0 + 50, y0, rect.x0 + 200, y1)})
        page.insert_link({'kind': fitz.LINK_URI, 'uri': 'https://line.me/ti/g/NbNGnW4Eh6',
                         'from': fitz.Rect(rect.x0 + 250, y0, rect.x0 + 350, y1)})
        if klook_links:
            page.insert_link({'kind': fitz.LINK_URI, 'uri': klook_links[0],
                             'from': fitz.Rect(rect.x0 + 400, y0, rect.x0 + 500, y1)})
        page.insert_link({'kind': fitz.LINK_URI, 'uri': 'https://tw.trip.com/partners/ad/DB17138130?Allianceid=8237671&SID=312406690&trip_sub1=',
                         'from': fitz.Rect(rect.x0 + 550, y0, rect.x1 - 50, y1)})
        
        # Tip on page 1
        if page_num == 0 and klook_links:
            tip_rect = fitz.Rect(rect.x1 - 250, rect.y0 + 20, rect.x1 - 20, rect.y0 + 60)
            page.insert_textbox(tip_rect, TIP_TEXT, fontsize=9, color=TIFFANY_DARK)
            page.insert_link({'kind': fitz.LINK_URI, 'uri': klook_links[0], 'from': tip_rect})
    
    doc.save(output_path)
    doc.close()

def main():
    pdf_dir = 'downloads'
    output_dir = 'pdfs'
    
    pdfs = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf') and not f.endswith('-with-links.pdf')]
    print(f'Found {len(pdfs)} PDFs to process')
    
    ok = 0
    fail = 0
    
    for pdf in pdfs:
        base = pdf.replace('.pdf', '')
        klook = LINK_MAP.get(base, [])
        out = os.path.join(output_dir, pdf.replace('.pdf', '-with-links.pdf'))
        
        print(f'Processing: {pdf}')
        try:
            add_links(os.path.join(pdf_dir, pdf), out, klook)
            print(f'  -> Saved: {os.path.basename(out)}')
            ok += 1
        except Exception as e:
            print(f'  ERROR: {e}')
            fail += 1
    
    print(f'Done. Success: {ok}, Failed: {fail}')

if __name__ == '__main__':
    main()
'''

with open('batch_final.py', 'w', encoding='utf-8') as f:
    f.write(batch_script)

print('✅ Created batch_final.py')
print('   Size:', len(batch_script), 'bytes')
