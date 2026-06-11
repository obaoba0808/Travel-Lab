# -*- coding: utf-8 -*-
import re
f = open("downloads.html", "r", encoding="utf-8").read()
m = re.findall(r'href=["\x27][^\x27"]*\.pdf["\x27]', f)
for x in m[:5]:
    print(x)
