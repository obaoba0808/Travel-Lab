const fs = require('fs');
const path = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab/_test_pdf.py';

const py = `# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register font
pdfmetrics.registerFont(TTFont('MSJH', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=0))

# Create PDF
doc = SimpleDocTemplate('downloads/test.pdf')
story = []

style = ParagraphStyle('h1', fontName='MSJH', fontSize=24, textColor=colors.HexColor('#26A69A'))
story.append(Paragraph('测试 PDF 生成', style))

style2 = ParagraphStyle('body', fontName='MSJH', fontSize=12, textColor=colors.black)
story.append(Paragraph('这是中文测试内容。Tokyo Metro Map 东京地铁线路图。', style2))

doc.build(story)
print('OK: downloads/test.pdf')
`;

fs.writeFileSync(path, py, 'utf-8');
console.log('Test script written to: ' + path);
