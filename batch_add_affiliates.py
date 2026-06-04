#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch process PDFs with destination-specific affiliate links"""

import fitz
import sys
import os
from urllib.parse import quote

# Tiffany Green 配色
TIFFANY = (0.3, 0.71, 0.67)  # #4DB6AC
TIFFANY_DARK = (0.15, 0.65, 0.6)  # #26A69A

# 目的地 → Klook 联盟链接映射
LINK_MAP = {
    'tokyo-metro-map': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283447&k_site=' + quote('https://www.klook.com/zh-TW/activity/1552-subway-ticket-tokyo/', safe=''),
    ],
    'japan-budget-sheet': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=' + quote('https://www.klook.com/zh-HK/activity/3277-5-day-kansai-wide-area-jr-pass/', safe=''),
    ],
    'okinawa-driving-map': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=' + quote('https://www.klook.com/zh-TW/activity/46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry/', safe=''),
    ],
    'kyoto-momiji-schedule': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282006&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E4%BA%AC%E9%83%BD', safe=''),
    ],
    'osaka-food-map': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282013&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E5%A4%A7%E9%98%AA%E7%BE%8E%E9%A3%9F', safe=''),
    ],
    'seoul-food-map': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282023&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E9%A6%96%E7%88%BE%E7%BE%8E%E9%A3%9F', safe=''),
    ],
    'korea-budget-sheet': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282023&k_site=' + quote('https://www.klook.com/zh-TW/activity/1938-korea-rail-pass-korail-pass/', safe=''),
    ],
    'busan-capsule-guide': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282009&k_site=' + quote('https://www.klook.com/zh-TW/activity/65663-busan-air-cruise-capsule-train/', safe=''),
    ],
    'jeju-driving-route': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282026&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E6%B5%8E%E5%B7%9E%E5%B3%B6', safe=''),
    ],
    'taipei-food-map': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282378&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E5%8F%B0%E5%8C%97%E5%A4%9C%E5%B8%82', safe=''),
    ],
    'tainan-food-map': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282376&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E5%8F%B0%E5%8D%97%E7%BE%8E%E9%A3%9F', safe=''),
    ],
    'hualien-itinerary': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282375&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E8%8A%B1%E7%BE%8E', safe=''),
    ],
    'kenting-night-market': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282377&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E8%82%AF%E4%B8%81%E5%A4%9C%E5%B8%82', safe=''),
    ],
    'jiufen-guide': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282378&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E4%B9%9D%E4%BB%BD', safe=''),
    ],
    'bangkok-food-map': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282013&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E6%9B%BC%E8%B0%B7%E7%BE%8E%E9%A3%9F', safe=''),
    ],
    'bangkok-massage-map': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282013&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E6%9B%BC%E8%B0%B7%E6%8C%89%E6%91%A9', safe=''),
    ],
    'chiang-mai-guide': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282031&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E6%B8%85%E8%BF%88', safe=''),
    ],
    'danang-map': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282013&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E5%B4%94%E6%98%8E', safe=''),
    ],
    'hokkaido-packing-list': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282007&k_site=' + quote('https://www.klook.com/zh-TW/search/?q=%E5%8C%97%E6%B5%B7%E9%81%93', safe=''),
    ],
    'kansai-pass-calculator': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=' + quote('https://www.klook.com/zh-HK/activity/3277-5-day-kansai-wide-area-jr-pass/', safe=''),
    ],
    'usj-quick-pass': [
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=' + quote('https://www.klook.com/zh-TW/activity/46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry/', safe=''),
        'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=' + quote('https://www.klook.com/zh-TW/activity/3407-universal-studios-japan-express-pass-osaka/', safe=''),
    ],
}

def add_affiliate_links(pdf_path, output_path, klook_links):
    \"\"\"为 PDF 添加联盟链接（页脚 + 贴心提示）\"\"\"
    doc = fitz.open(pdf_path)
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        rect = page.rect
        
        # 1. 页脚链接（底部居中）
        footer_rect = fitz.Rect(rect.x0 + 50, rect.y1 - 40, rect.x1 - 50, rect.y1 - 10)
        
        # 添加页脚文字
        footer_text = '📌 更多旅遊攻略 👉 golightly.fun   |   LINE 群組   |   Klook 優惠   |   Trip.com 優惠'
        page.insert_textbox(footer_rect, footer_text, fontsize=8.5, color=TIFFANY, align=fitz.TEXT_ALIGN_CENTER)
        
        # 添加可点击链接
        page.insert_link({
            'kind': fitz.LINK_URI,
            'uri': 'https://golightly.fun',
            'from': fitz.Rect(rect.x0 + 50, rect.y1 - 40, rect.x0 + 200, rect.y1 - 10)
        })
        
        page.insert_link({
            'kind': fitz.LINK_URI,
            'uri': 'https://line.me/ti/g/NbNGnW4Eh6',
            'from': fitz.Rect(rect.x0 + 250, rect.y1 - 40, rect.x0 + 350, rect.y1 - 10)
        })
        
        # Klook 优惠链接（使用定制的链接）
        if klook_links:
            page.insert_link({
                'kind': fitz.LINK_URI,
                'uri': klook_links[0],
                'from': fitz.Rect(rect.x0 + 400, rect.y1 - 40, rect.x0 + 500, rect.y1 - 10)
            })
        
        page.insert_link({
            'kind': fitz.LINK_URI,
            'uri': 'https://tw.trip.com/partners/ad/DB17138130?Allianceid=8237671&SID=312406690&trip_sub1=',
            'from': fitz.Rect(rect.x0 + 550, rect.y1 - 40, rect.x1 - 50, rect.y1 - 10)
        })
        
        # 2. 贴心提示（第1页右上角）
        if page_num == 0:
            tip_rect = fitz.Rect(rect.x1 - 250, rect.y0 + 20, rect.x1 - 20, rect.y0 + 60)
            tip_text = '💡 推薦：Klook 上有更多當地體驗，點此查看優惠'
            page.insert_textbox(tip_rect, tip_text, fontsize=9, color=TIFFANY_DARK)
            
            if klook_links:
                page.insert_link({
                    'kind': fitz.LINK_URI,
                    'uri': klook_links[0],
                    'from': tip_rect
                })
    
    doc.save(output_path)
    doc.close()
    return True

def main():
    pdf_dir = 'downloads'
    output_dir = 'pdfs'
    
    # 获取所有 PDF（排除已处理的）
    pdfs = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf') and not f.endswith('-with-links.pdf')]
    
    print(f'📋 找到 {len(pdfs)} 个 PDF 需要处理')
    print('')
    
    success = 0
    failed = 0
    
    for pdf_name in pdfs:
        # 提取基础名称（不含 .pdf）
        base_name = pdf_name.replace('.pdf', '')
        
        # 获取对应的 Klook 链接
        klook_links = LINK_MAP.get(base_name, [])
        
        input_path = os.path.join(pdf_dir, pdf_name)
        output_name = pdf_name.replace('.pdf', '-with-links.pdf')
        output_path = os.path.join(output_dir, output_name)
        
        print(f'Processing: {pdf_name}')
        if klook_links:
            print(f'  Klook links: {len(klook_links)} 个')
        else:
            print('  ⚠️  无定制链接，使用默认')
        
        try:
            add_affiliate_links(input_path, output_path, klook_links)
            print(f'  ✅ 已保存到: {output_name}')
            success += 1
        except Exception as e:
            print(f'  ❌ 失败: {e}')
            failed += 1
        
        print('')
    
    print('=== 处理完成 ===')
    print(f'成功: {success}')
    print(f'失败: {failed}')

if __name__ == '__main__':
    main()
