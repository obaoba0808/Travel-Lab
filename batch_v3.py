#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch process PDFs - pure ASCII source, Chinese loaded from JSON"""

import fitz
import json
import os
import sys

# Tiffany Green color
TIFFANY = (0.3, 0.71, 0.67)
TIFFANY_DARK = (0.15, 0.65, 0.6)

# Load link mapping
with open('link_mapping.json', 'r', encoding='ascii') as f:
    LINK_MAP = json.load(f)

# Load Chinese texts (stored as unicode escapes in JSON)
with open('pdf_texts.json', 'r', encoding='ascii') as f:
    TEXTS = json.load(f)

FOOTER_TEXT = TEXTS['footer']
TIP_TEXT = TEXTS['tip']

def add_links(pdf_path, output_path, klook_links):
    doc = fitz.open(pdf_path)
    for page_num in range(doc.page_count):
        page = doc[page_num]
        rect = page.rect
        
        # Footer
        footer_rect = fitz.Rect(rect.x0 + 50, rect.y1 - 40, rect.x1 - 50, rect.y1 - 10)
        page.insert_textbox(footer_rect, FOOTER_TEXT, fontsize=8.5, color=TIFFANY, align=fitz.TEXT_ALIGN_CENTER)
        
        # Links (4 regions)
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