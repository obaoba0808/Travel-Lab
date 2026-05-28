# -*- coding: utf-8 -*-
# Pure ASCII generator - reads pdf_data.json (base64-encoded Chinese) and generates PDFs
import os, json, base64
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Chinese font
CF = None
for fp in ["C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simhei.ttf", "C:/Windows/Fonts/simsun.ttc"]:
    if os.path.exists(fp):
        try:
            pdfmetrics.registerFont(TTFont("CF", fp))
            CF = "CF"
            break
        except:
            continue
if not CF:
    print("ERROR: No Chinese font found!")
    exit(1)

BRAND = colors.HexColor("#0ABAB5")
DARK = colors.HexColor("#1a1a2e")
LIGHT = colors.HexColor("#f0fafa")
GRAY = colors.HexColor("#666666")
OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
os.makedirs(OUTDIR, exist_ok=True)

def d(s):
    return base64.b64decode(s).decode("utf-8")

def make_styles():
    s = getSampleStyleSheet()
    kw = dict(fontName=CF)
    s.add(ParagraphStyle(name="CT", fontSize=26, leading=34, textColor=colors.white, alignment=1, spaceAfter=8*mm, **kw))
    s.add(ParagraphStyle(name="CS", fontSize=13, leading=18, textColor=colors.HexColor("#b0e8e4"), alignment=1, **kw))
    s.add(ParagraphStyle(name="H1", fontSize=17, leading=24, textColor=BRAND, spaceBefore=10*mm, spaceAfter=4*mm, **kw))
    s.add(ParagraphStyle(name="H2", fontSize=13, leading=18, textColor=DARK, spaceBefore=5*mm, spaceAfter=3*mm, **kw))
    s.add(ParagraphStyle(name="BD", fontSize=10, leading=16, textColor=DARK, spaceAfter=3*mm, **kw))
    s.add(ParagraphStyle(name="BL", fontSize=10, leading=15, textColor=DARK, leftIndent=8*mm, spaceAfter=2*mm, **kw))
    s.add(ParagraphStyle(name="TP", fontSize=9, leading=14, textColor=colors.HexColor("#d35400"), leftIndent=5*mm, rightIndent=5*mm, spaceBefore=2*mm, spaceAfter=2*mm, **kw))
    s.add(ParagraphStyle(name="FT", fontSize=8, leading=11, textColor=GRAY, alignment=1, **kw))
    return s

def mk_table(data, st):
    if not data or len(data) < 2:
        return None
    t = Table(data)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BRAND),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,-1), CF),
        ("FONTSIZE", (0,0), (-1,0), 9),
        ("FONTSIZE", (0,1), (-1,-1), 8),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    return t

def gen_pdf(fname, title, subtitle, sections):
    fpath = os.path.join(OUTDIR, fname)
    doc = SimpleDocTemplate(fpath, pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=18*mm, bottomMargin=18*mm)
    st = make_styles()
    story = []
    story.append(Spacer(1, 70*mm))
    story.append(Paragraph(title, st["CT"]))
    story.append(Paragraph(subtitle, st["CS"]))
    story.append(Spacer(1, 18*mm))
    story.append(Paragraph(d("5ZG95pyA6L+R5LiW"), st["CS"]))
    story.append(PageBreak())
    for sec in sections:
        tp = sec.get("tp", "")
        if tp == "h1":
            story.append(Paragraph(d(sec["tx"]), st["H1"]))
        elif tp == "h2":
            story.append(Paragraph(d(sec["tx"]), st["H2"]))
        elif tp == "body":
            story.append(Paragraph(d(sec["tx"]), st["BD"]))
        elif tp == "bullet":
            story.append(Paragraph("\u2022 " + d(sec["tx"]), st["BL"]))
        elif tp == "tip":
            story.append(Paragraph(d(sec["tx"]), st["TP"]))
        elif tp == "table":
            tdata = [[d(c) for c in r] for r in sec.get("dt", [])]
            tbl = mk_table(tdata, st)
            if tbl:
                story.append(tbl)
                story.append(Spacer(1, 4*mm))
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("- " + d("5ZG95pyA6L+R5LiW") + " golightly.fun -", st["FT"]))
    story.append(Paragraph(d("5pu05aS55pyD5YiG5qih5bCE56eH5L2c57WQ5Zy6"), st["FT"]))
    doc.build(story)
    sz = os.path.getsize(fpath)
    print("  OK " + fname + " (" + str(sz) + " bytes)")

if __name__ == "__main__":
    jpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf_data.json")
    with open(jpath, "r", encoding="utf-8") as f:
        pdfs = json.load(f)
    print("=" * 50)
    print("Generating " + str(len(pdfs)) + " PDFs for golightly.fun...")
    print("=" * 50)
    for p in pdfs:
        try:
            gen_pdf(p["f"], d(p["t"]), d(p["s"]), p["sec"])
        except Exception as e:
            print("  ERROR " + p["f"] + ": " + str(e))
    print("=" * 50)
    print("Done!")
    print("=" * 50)
