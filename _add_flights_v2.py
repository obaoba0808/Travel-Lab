import sys
from pathlib import Path

BASE = Path("C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/travel-lab")
f = BASE / "travel-tools.html"
c = f.read_bytes()

CTA = b"<!-- CTA BANNER -->"
INSERT = b"""
<!-- TRIP.COM FLIGHTS CTA -->
<div style="max-width:900px;margin:40px auto;padding:0 20px;">
  <a href="https://tw.trip.com/sale/w/4823/flight-deals.html?locale=zh-TW&promo_referer=3952_4823_6&affiliateid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078938" target="_blank" rel="noopener">
    <img loading="lazy" src="images/trip-flights.webp" alt="Trip.com 機票優惠" style="width:100%;border-radius:12px;display:block;">
  </a>
</div>
"""

idx = c.find(CTA)
if idx >= 0:
    new = c[:idx+len(CTA)] + INSERT + c[idx+len(CTA):]
    f.write_bytes(new)
    print("OK: flights CTA added")
else:
    print("SKIP: CTA BANNER not found")
