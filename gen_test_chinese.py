# -*- coding: utf-8 -*-
# Test Chinese display in PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register font
pdfmetrics.registerFont(TTFont('MSJH', 'C:/Windows/Fonts/msjh.ttc', subfontIndex=0))

c = canvas.Canvas('pdfs/chinese-test.pdf', pagesize=A4)
c.setFont('MSJH', 16)
c.drawString(50, 800, '测试中文显示')
c.save()
print('OK')
