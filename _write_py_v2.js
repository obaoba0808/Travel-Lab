// _write_py_v2.js - Generates Python PDF script (fixed encoding)
const fs = require('fs');

let py = '';
function L(s) { py += s + '\n'; }

// Python script header
L('# -*- coding: utf-8 -*-');
L('import sys; sys.stdout.reconfigure(encoding="utf-8")');
L('from reportlab.lib.pagesizes import A4');
L('from reportlab.lib.styles import ParagraphStyle');
L('from reportlab.lib.units import mm');
L('from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak');
L('from reportlab.lib import colors');
L('from reportlab.pdfbase import pdfmetrics');
L('from reportlab.pdfbase.ttfonts import TTFont');
L('from reportlab.lib.enums import TA_CENTER, TA_LEFT');
L('import os');
L('');

// Font registration
L('pdfmetrics.registerFont(TTFont("MSJH", "C:/Windows/Fonts/msjh.ttc", subfontIndex=0))');
L('pdfmetrics.registerFont(TTFont("MSJHB", "C:/Windows/Fonts/msjh.ttc", subfontIndex=1))');
L('');

// Color constants
L('TEAL = colors.HexColor("#0ABAB5")');
L('DARK = colors.HexColor("#1a1a2e")');
L('LIGHT_BG = colors.HexColor("#e8f8f7")');
L('');

// Styles
L('h1 = ParagraphStyle("H1", fontName="MSJHB", fontSize=18, leading=24, textColor=DARK, spaceAfter=12, alignment=TA_CENTER)');
L('h2 = ParagraphStyle("H2", fontName="MSJHB", fontSize=14, leading=20, textColor=TEAL, spaceBefore=16, spaceAfter=8)');
L('h3 = ParagraphStyle("H3", fontName="MSJHB", fontSize=11, leading=16, textColor=DARK, spaceBefore=10, spaceAfter=6)');
L('body = ParagraphStyle("Body", fontName="MSJH", fontSize=9.5, leading=15, textColor=colors.HexColor("#333333"), spaceAfter=6)');
L('tip = ParagraphStyle("Tip", fontName="MSJH", fontSize=9, leading=14, textColor=colors.HexColor("#d35400"), leftIndent=15, spaceAfter=4)');
L('center = ParagraphStyle("Center", fontName="MSJH", fontSize=9, leading=14, alignment=TA_CENTER)');
L('sc = ParagraphStyle("SC", fontName="MSJH", fontSize=8, leading=12, textColor=colors.HexColor("#888888"), alignment=TA_CENTER)');
L('');

// Table helper
L('def tbl(headers, rows, widths):');
L('    d = [[Paragraph("<b>"+h+"</b>", body) for h in headers]');
L('    for r in rows: d.append([Paragraph(str(c), body) for c in r])');
L('    t = Table(d, colWidths=widths)');
L('    t.setStyle(TableStyle([');
L('        ("BACKGROUND", (0,0), (-1,0), TEAL),');
L('        ("TEXTCOLOR", (0,0), (-1,0), colors.white),');
L('        ("ALIGN", (0,0), (-1,-1), "CENTER"),');
L('        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),');
L('        ("FONTNAME", (0,0), (-1,-1), "MSJH"),');
L('        ("FONTSIZE", (0,0), (-1,-1), 8),');
L('        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),');
L('        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT_BG]),');
L('        ("TOPPADDING", (0,0), (-1,-1), 6),');
L('        ("BOTTOMPADDING", (0,0), (-1,-1), 6),');
L('    ]))');
L('    return t');
L('');

// CTA function
L('def cta(story):');
L('    story.append(Spacer(1, 20))');
L('    bd = [');
L('        [Paragraph("<b>[ 更多完整攻略 ]</b>", center)],');
L('        [Paragraph("golightly.fun - 均在路上的旅游实验室", center)],');
L('        [Paragraph("<b>[ 即时旅游咨询 ]</b>", center)],');
L('        [Paragraph("加入 LINE 群组，免费获得行程建议", center)],');
L('    ]');
L('    b = Table(bd, [380])');
L('    b.setStyle(TableStyle([');
L('        ("BOX", (0,0), (-1,-1), 2, TEAL),');
L('        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#f0fffe")),');
L('        ("ALIGN", (0,0), (-1,-1), "CENTER"),');
L('        ("TOPPADDING", (0,0), (-1,-1), 10),');
L('        ("BOTTOMPADDING", (0,0), (-1,-1), 10),');
L('    ]))');
L('    story.append(b)');
L('    story.append(Spacer(1, 15))');
L('    story.append(Paragraph("均在路上 Travel Lab (c) 2026 | golightly.fun", sc))');
L('    story.append(Paragraph("价格与资讯可能随时变动，出发前请再次确认", sc))');
L('');

// Build function
L('def build(fn, title, sub, secs):');
L('    p = "downloads/" + fn + ".pdf"');
L('    doc = SimpleDocTemplate(p, pagesize=A4, leftMargin=25*mm, rightMargin=25*mm, topMargin=20*mm, bottomMargin=20*mm)');
L('    s = []');
L('    s.append(Paragraph(title, h1))');
L('    s.append(Paragraph(sub, center))');
L('    s.append(Spacer(1, 8))');
L('    for sec in secs: sec(s)');
L('    cta(s)');
L('    doc.build(s)');
L('    return os.path.getsize(p)');
L('');

// Safe markers (NO unicode symbols)
L('OK = "[OK] "');
L('WRN = "[!] "');
L('STAR = "* "');
L('ARROW = "> "');
L('CROSS = "X "');
L('');

fs.writeFileSync('C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab/_fix_pdf_garble.py', py, 'utf-8');
console.log('Part 1 written: ' + py.length + ' bytes');
