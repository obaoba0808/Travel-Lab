# -*- coding: utf-8 -*-
# Pure ASCII Python script - no encoding issues
import sys
sys.stdout.reconfigure(encoding="utf-8")
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER
import os
import shutil

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

def clean_text(text):
    """Remove null bytes and replace Unicode symbols with ASCII"""
    # Remove null bytes
    text = text.replace('\x00', '')
    # Replace Unicode symbols with ASCII markers
    text = text.replace('\u2705', '[OK]')  # ✓
    text = text.replace('\u26A0', '[!]')   # ⚠
    text = text.replace('\u2708', '[FLIGHT]')  # ✈
    text = text.replace('\u2715', '[X]')  # ✕
    text = text.replace('\u25A1', '[ ]')  # □
    # Replace common bullets/arrows
    text = text.replace('\u2022', '*')  # •
    text = text.replace('\u2192', '>')  # →
    return text

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using PyPDF2"""
    try:
        reader = PdfReader(pdf_path)
        full_text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                full_text += t + "\n"
        return full_text
    except Exception as e:
        print(f"[ERROR] Extract failed: {e}")
        return ""

def rebuild_pdf(pdf_path):
    """Rebuild a single PDF with cleaned text"""
    # Extract
    raw_text = extract_text_from_pdf(pdf_path)
    if not raw_text:
        print(f"[SKIP] No text extracted from {os.path.basename(pdf_path)}")
        return 0
    
    # Clean
    cleaned = clean_text(raw_text)
    
    # Backup original
    backup_path = pdf_path + ".bak"
    if not os.path.exists(backup_path):
        shutil.copy2(pdf_path, backup_path)
    
    # Build story
    story = []
    
    # Split into lines
    lines = [l.strip() for l in cleaned.split('\n') if l.strip()]
    
    if not lines:
        print(f"[SKIP] No content after cleaning: {os.path.basename(pdf_path)}")
        return 0
    
    # Title = first line
    title = lines[0]
    story.append(Paragraph(title, h1))
    
    # Remaining lines as body
    for line in lines[1:]:
        # Skip very short lines that might be decorative
        if len(line) < 2:
            continue
        story.append(Paragraph(line, body))
    
    # Add spacing
    story.append(Spacer(1, 15))
    
    # CTA
    story.append(Paragraph("[ More Guides Available ]", center))
    story.append(Paragraph("golightly.fun - Travel Lab", center))
    
    # Save (overwrite original)
    try:
        doc = SimpleDocTemplate(pdf_path, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm)
        doc.build(story)
        size = os.path.getsize(pdf_path)
        return size
    except Exception as e:
        print(f"[ERROR] Build failed: {e}")
        # Restore from backup
        shutil.copy2(backup_path, pdf_path)
        return 0

# Main
pdf_dir = "downloads"
pdfs = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf') and not f.startswith('test_')]

print(f"[INFO] Found {len(pdfs)} PDFs to process")
print(f"[INFO] Output directory: {pdf_dir}\n")

success = 0
failed = 0

for pdf in pdfs:
    pdf_path = os.path.join(pdf_dir, pdf)
    print(f"Processing: {pdf}")
    
    size = rebuild_pdf(pdf_path)
    
    if size > 0:
        print(f"  [OK] Rebuilt: {size} bytes")
        success += 1
    else:
        print(f"  [FAILED]")
        failed += 1
    print()

print("=" * 60)
print(f"[SUMMARY] Success: {success}/{len(pdfs)}")
print(f"[SUMMARY] Failed: {failed}")
print("=" * 60)
print("\n[INFO] Originals backed up as .bak files")
print("[INFO] Verify results, then commit and push")
