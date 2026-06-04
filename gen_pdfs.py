# -*- coding: utf-8 -*-
# Tiffany Green beautified PDF generator for golightly.fun
# Primary color: #0ABABB (Tiffany Green)
import os, json, base64
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 Table, TableStyle, PageBreak)
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Register Chinese font ─────────────────────────────────────────
CF = None
for fp in ["C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simhei.ttf",
           "C:/Windows/Fonts/simsun.ttc"]:
    if os.path.exists(fp):
        try:
            pdfmetrics.registerFont(TTFont("CF", fp))
            CF = "CF"
            break
        except:
            continue
if not CF:
    print("ERROR: No Chinese font found!"); exit(1)

# ── Tiffany Green palette ────────────────────────────────────────
TGREEN      = colors.HexColor("#0ABABB")   # primary
TGREEN_DARK = colors.HexColor("#057A7A")   # dark accent
TGREEN_LT   = colors.HexColor("#E0F7F5")   # light bg
TGREEN_UL   = colors.HexColor("#0ABABB")   # underline
GRAY_DARK   = colors.HexColor("#1a1a2e")
GRAY_MID     = colors.HexColor("#555555")
GRAY_LT     = colors.HexColor("#cccccc")
WHITE       = colors.white
MARGIN      = 18 * mm

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
os.makedirs(OUTDIR, exist_ok=True)

def d(s):
    return base64.b64decode(s).decode("utf-8")

# ── Styles ───────────────────────────────────────────────────────
def make_styles():
    s = getSampleStyleSheet()
    kw = dict(fontName=CF)
    s.add(ParagraphStyle(name="CT", fontSize=26, leading=34,
                         textColor=WHITE, alignment=1,
                         spaceAfter=4*mm, **kw))
    s.add(ParagraphStyle(name="CS", fontSize=12, leading=18,
                         textColor=TGREEN_LT, alignment=1,
                         spaceAfter=2*mm, **kw))
    s.add(ParagraphStyle(name="CB", fontSize=10, leading=14,
                         textColor=GRAY_LT, alignment=1, **kw))
    s.add(ParagraphStyle(name="H1", fontSize=16, leading=22,
                         textColor=TGREEN_DARK, spaceBefore=8*mm,
                         spaceAfter=1*mm, **kw))
    s.add(ParagraphStyle(name="H2", fontSize=12, leading=17,
                         textColor=GRAY_DARK, spaceBefore=5*mm,
                         spaceAfter=2*mm, **kw))
    s.add(ParagraphStyle(name="BD", fontSize=10, leading=16,
                         textColor=GRAY_DARK, spaceAfter=3*mm, **kw))
    s.add(ParagraphStyle(name="BL", fontSize=10, leading=15,
                         textColor=GRAY_DARK, leftIndent=8*mm,
                         spaceAfter=2*mm, **kw))
    s.add(ParagraphStyle(name="TP", fontSize=9, leading=14,
                         textColor=TGREEN_DARK, leftIndent=6*mm,
                         rightIndent=6*mm, spaceBefore=2*mm,
                         spaceAfter=2*mm, **kw))
    s.add(ParagraphStyle(name="FT", fontSize=7.5, leading=10,
                         textColor=GRAY_MID, alignment=1, **kw))
    return s

# ── Table style (Tiffany Green header) ─────────────────────────
def mk_table(tdata):
    if not tdata or len(tdata) < 2:
        return None
    ncols = max(len(r) for r in tdata)
    for r in tdata:
        while len(r) < ncols:
            r.append("")
    col_w = (A4[0] - 2 * MARGIN) / ncols
    t = Table(tdata, colWidths=[col_w] * ncols)
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,0),  TGREEN),
        ("TEXTCOLOR",   (0,0), (-1,0),  WHITE),
        ("FONTNAME",    (0,0), (-1,-1), CF),
        ("FONTSIZE",   (0,0), (-1,0),  9),
        ("FONTSIZE",   (0,1), (-1,-1), 8.5),
        ("ALIGN",       (0,0), (-1,-1),  "CENTER"),
        ("VALIGN",      (0,0), (-1,-1),  "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, TGREEN_LT]),
        ("GRID",       (0,0), (-1,-1),  0.4, GRAY_LT),
        ("LINEABOVE",  (0,0), (-1,0),   1.2, TGREEN),
        ("LINEBELOW",  (0,-1), (-1,-1), 1.2, TGREEN),
        ("TOPPADDING", (0,0), (-1,-1),  4),
        ("BOTTOMPADDING",(0,0),(-1,-1), 4),
        ("LEFTPADDING",(0,0),(-1,-1),   4),
        ("RIGHTPADDING",(0,0),(-1,-1),  4),
    ]))
    return t

# ── Page header / footer (Tiffany Green) ───────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    # Header bar
    canvas.setFillColor(TGREEN)
    canvas.rect(0, h - 11*mm, w, 11*mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont(CF, 8.5)
    canvas.drawCentredString(w / 2, h - 7*mm, "均在路上 Travel Lab  —  golightly.fun")
    # Footer rule + page number
    canvas.setStrokeColor(TGREEN)
    canvas.setLineWidth(0.6)
    canvas.line(MARGIN, 12*mm, w - MARGIN, 12*mm)
    canvas.setFillColor(GRAY_MID)
    canvas.setFont(CF, 7.5)
    canvas.drawCentredString(w / 2, 7*mm, "—  %d  —" % doc.page)
    canvas.restoreState()

# ── H1 underline rule ───────────────────────────────────────────
def h1_rule():
    rule_data = [[""]]
    rule_tb = Table(rule_data, colWidths=[A4[0] - 2 * MARGIN])
    rule_tb.setStyle(TableStyle([
        ("LINEBELOW",    (0,0), (-1,-1), 2,   TGREEN_UL),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 2*mm),
    ]))
    return rule_tb

# ── Tip box (Tiffany Green left accent) ────────────────────────
def tip_box(text, st):
    inner = [[Paragraph(text, st["TP"])]]
    tb = Table(inner, colWidths=[A4[0] - 2*MARGIN - 10*mm])
    tb.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,-1), TGREEN_LT),
        ("LEFTPADDING",  (0,0), (-1,-1), 8*mm),
        ("RIGHTPADDING", (0,0), (-1,-1), 6*mm),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0),(-1,-1), 4),
        # Left accent bar (3mm wide, Tiffany Green)
        ("BACKGROUND",   (0,0), (0,0),    TGREEN),
        ("LEFTPADDING",  (0,0), (0,0),    3*mm),
    ]))
    return tb

# ── Generate one PDF ────────────────────────────────────────────
def gen_pdf(fname, title, subtitle, sections):
    fpath = os.path.join(OUTDIR, fname)
    doc = SimpleDocTemplate(
        fpath, pagesize=A4,
        rightMargin=MARGIN, leftMargin=MARGIN,
        topMargin=16*mm, bottomMargin=18*mm,
    )
    st = make_styles()
    story = []

    # ── Cover page ──────────────────────────────────────────────
    story.append(Spacer(1, 55*mm))
    # Title block (Tiffany Green bg)
    title_tb = Table([[Paragraph(title, st["CT"])]],
                     colWidths=[A4[0] - 2*MARGIN])
    title_tb.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,-1), TGREEN),
        ("TOPPADDING",   (0,0), (-1,-1), 10*mm),
        ("BOTTOMPADDING",(0,0),(-1,-1), 10*mm),
        ("LEFTPADDING",  (0,0), (-1,-1), 6*mm),
        ("RIGHTPADDING", (0,0), (-1,-1), 6*mm),
    ]))
    story.append(title_tb)
    story.append(Spacer(1, 4*mm))
    # Subtitle block (light green bg)
    sub_tb = Table([[Paragraph(subtitle, st["CS"])]],
                    colWidths=[A4[0] - 2*MARGIN])
    sub_tb.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,-1), TGREEN_LT),
        ("TOPPADDING",    (0,0), (-1,-1), 4*mm),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4*mm),
    ]))
    story.append(sub_tb)
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("-  均在路上 Travel Lab  -  golightly.fun  -", st["CB"]))
    story.append(PageBreak())

    # ── Content pages ──────────────────────────────────────────
    for sec in sections:
        tp = sec.get("tp", "")
        if tp == "h1":
            txt = d(sec["tx"])
            story.append(Paragraph(txt, st["H1"]))
            story.append(h1_rule())
        elif tp == "h2":
            story.append(Paragraph(d(sec["tx"]), st["H2"]))
        elif tp == "body":
            story.append(Paragraph(d(sec["tx"]), st["BD"]))
        elif tp == "bullet":
            story.append(Paragraph("• " + d(sec["tx"]), st["BL"]))
        elif tp == "tip":
            story.append(tip_box(d(sec["tx"]), st))
            story.append(Spacer(1, 2*mm))
        elif tp == "table":
            raw = [[d(c) for c in r] for r in sec.get("dt", [])]
            tbl = mk_table(raw)
            if tbl:
                story.append(tbl)
                story.append(Spacer(1, 4*mm))

    # ── Footer credit ──────────────────────────────────────────
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("-  均在路上 Travel Lab  -  golightly.fun  -", st["FT"]))
    story.append(Paragraph(d("5pu05aS55pyD5YiG5qih5bCE56eH5L2c57WQ5Zy6"), st["FT"]))

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    sz = os.path.getsize(fpath)
    print("  OK %s  (%d bytes)" % (fname, sz))

# ── Main ────────────────────────────────────────────────────────
if __name__ == "__main__":
    jpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf_data.json")
    with open(jpath, "r", encoding="utf-8") as f:
        pdfs = json.load(f)
    print("=" * 50)
    print("Generating %d beautified PDFs (Tiffany Green #0ABABB) ..." % len(pdfs))
    print("=" * 50)
    for p in pdfs:
        try:
            gen_pdf(p["f"], d(p["t"]), d(p["s"]), p["sec"])
        except Exception as e:
            print("  ERROR %s: %s" % (p["f"], e))
    print("=" * 50)
    print("Done!")
    print("=" * 50)
