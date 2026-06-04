# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os
import re

# Register fonts
pdfmetrics.registerFont(TTFont("MSJH", "C:/Windows/Fonts/msjh.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("MSJHB", "C:/Windows/Fonts/msjh.ttc", subfontIndex=1))

# Colors
TEAL = colors.HexColor("#0ABAB5")
DARK = colors.HexColor("#1a1a2e")
LIGHT_BG = colors.HexColor("#e8f8f7")

# Styles
h1 = ParagraphStyle("H1", fontName="MSJHB", fontSize=18, leading=24, textColor=DARK, spaceAfter=12, alignment=TA_CENTER)
h2 = ParagraphStyle("H2", fontName="MSJHB", fontSize=14, leading=20, textColor=TEAL, spaceBefore=16, spaceAfter=8)
body = ParagraphStyle("Body", fontName="MSJH", fontSize=9.5, leading=15, textColor=colors.HexColor("#333333"), spaceAfter=6)
center = ParagraphStyle("Center", fontName="MSJH", fontSize=9, leading=14, alignment=TA_CENTER)
sc = ParagraphStyle("SC", fontName="MSJH", fontSize=8, leading=12, textColor=colors.HexColor("#888888"), alignment=TA_CENTER)

def clean_text(text):
    """Remove null bytes and replace Unicode symbols with ASCII markers"""
    # Remove null bytes
    text = text.replace('\x00', '')
    # Replace Unicode symbols with ASCII
    text = text.replace('✓', '[OK]')
    text = text.replace('✕', '[X]')
    text = text.replace('⚠', '[!]')
    text = text.replace('→', '>')
    text = text.replace('•', '*')
    # Keep Chinese characters, remove any remaining problematic Unicode
    return text

def extract_and_rebuild(pdf_path, output_path):
    """Extract text from PDF, clean it, and rebuild"""
    try:
        reader = PdfReader(pdf_path)
        print(f"[OK] Processing: {os.path.basename(pdf_path)}")
        print(f"  Pages: {len(reader.pages)}")
        
        # Extract all text
        full_text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                full_text += t + "\n"
        
        print(f"  Extracted: {len(full_text)} chars")
        
        # Clean text
        cleaned = clean_text(full_text)
        print(f"  Cleaned: {len(cleaned)} chars")
        
        # Split into sections (by double newline)
        sections = []
        current_section = {"h2": "Content", "body": ""}
        
        for line in cleaned.split('\n'):
            line = line.strip()
            if not line:
                if current_section["body"]:
                    sections.append(current_section)
                    current_section = {"h2": "Content", "body": ""}
            elif len(line) < 50 and ('攻略' in line or '指南' in line or '技巧' in line or '策略' in line or '分析' in line or '清單' in line):
                # This looks like a section header
                if current_section["body"]:
                    sections.append(current_section)
                current_section = {"h2": line, "body": ""}
            else:
                current_section["body"] += line + "\n"
        
        if current_section["body"]:
            sections.append(current_section)
        
        # If no sections detected, use whole text as one section
        if not sections:
            sections = [{"h2": "Content", "body": cleaned}]
        
        print(f"  Sections detected: {len(sections)}")
        
        # Build PDF
        story = []
        
        # Extract title from first line
        lines = cleaned.split('\n')
        title = lines[0] if lines else "Travel Guide"
        story.append(Paragraph(title, h1))
        
        # Add sections
        for sec in sections:
            if sec["h2"] != "Content":
                story.append(Paragraph(sec["h2"], h2))
            body_text = sec["body"].strip()
            if body_text:
                # Split by lines and add as paragraphs
                for para in body_text.split('\n'):
                    para = para.strip()
                    if para:
                        story.append(Paragraph(para, body))
                story.append(Spacer(1, 10))
        
        # CTA
        story.append(Spacer(1, 20))
        story.append(Paragraph("[ 更多完整攻略 ]", center))
        story.append(Paragraph("golightly.fun — 均在路上的旅游實驗室", center))
        story.append(Paragraph("即時旅遊諮詢", center))
        story.append(Paragraph("加入 LINE 群組，免費獲得行程建議", center))
        
        # Build
        doc = SimpleDocTemplate(output_path, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm)
        doc.build(story)
        
        size = os.path.getsize(output_path)
        print(f"  [SUCCESS] Rebuilt: {output_path}")
        print(f"  Size: {size} bytes")
        return size
        
    except Exception as e:
        print(f"  [ERROR] {e}")
        return 0

# Main
import os

pdf_dir = "downloads"
output_dir = "downloads_new"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get all PDFs
pdfs = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
print(f"\n[INFO] Found {len(pdfs)} PDFs to rebuild\n")

total_original = 0
total_new = 0
success_count = 0

for pdf in pdfs:
    pdf_path = os.path.join(pdf_dir, pdf)
    output_path = os.path.join(output_dir, pdf)
    
    original_size = os.path.getsize(pdf_path)
    total_original += original_size
    
    new_size = extract_and_rebuild(pdf_path, output_path)
    total_new += new_size
    
    if new_size > 0:
        success_count += 1
    
    print()

print("="*60)
print(f"[SUMMARY] Success: {success_count}/{len(pdfs)}")
print(f"[SUMMARY] Original total: {total_original} bytes ({total_original/1024:.1f} KB)")
print(f"[SUMMARY] New total: {total_new} bytes ({total_new/1024:.1f} KB)")
print(f"[SUMMARY] Avg size change: {(total_new/total_original*100)-100:.1f}%")
print("="*60)
print("\n[INFO] New PDFs in:", output_dir)
print("[INFO] Verify a few PDFs, then replace downloads/ with downloads_new/")
