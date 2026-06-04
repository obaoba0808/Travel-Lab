import sys
import os

# 检查 reportlab 和字体
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    print("✅ reportlab 已安装")
except ImportError as e:
    print(f"❌ reportlab 未安装: {e}")
    sys.exit(1)

# 注册中文字体
font_path = "C:/Windows/Fonts/msjh.ttc"
try:
    pdfmetrics.registerFont(TTFont('MSJH', font_path, subfontIndex=0))
    pdfmetrics.registerFont(TTFont('MSJH-Bold', font_path, subfontIndex=1))
    print("✅ MS JhengHei 字体已注册")
except Exception as e:
    print(f"❌ 字体注册失败: {e}")
    sys.exit(1)

# 创建测试 PDF
output = "pdfs/chinese-test.pdf"
c = canvas.Canvas(output, pagesize=A4)
width, height = A4

# 使用中文字体
c.setFont("MSJH", 16)
c.drawString(50, height - 50, "測試中文顯示：旅行實驗室")
c.setFont("MSJH", 12)
c.drawString(50, height - 80, "這是一個測試 PDF，驗證中文是否可以正常顯示。")
c.drawString(50, height - 110, "Tokyo Metro Map - 東京地鐵圖")
c.drawString(50, height - 140, "Osaka Food Map - 大阪美食地圖")

c.save()
print(f"✅ 测试 PDF 已生成: {output}")
print(f"   文件大小: {os.path.getsize(output)} bytes")
