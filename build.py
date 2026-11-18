#!/usr/bin/env python3
"""Builds index.html from src/template.html + assets/. Run: python3 build.py
Images are embedded as base64 so index.html is one self-contained file."""
import base64, json, os
R = os.path.dirname(os.path.abspath(__file__))
def uri(path, mime):
    return "data:%s;base64,%s" % (mime, base64.b64encode(open(path, "rb").read()).decode())
s = open(os.path.join(R, "src/template.html"), encoding="utf-8").read()
photos = sorted(os.listdir(os.path.join(R, "assets/photos")), key=lambda n: int(n.split("-")[1].split(".")[0]))
s = s.replace("{{PHOTOS}}", json.dumps([uri(os.path.join(R, "assets/photos", p), "image/jpeg") for p in photos]))
fm = json.load(open(os.path.join(R, "assets/headshots/_formats.json")))
s = s.replace("{{HS}}", json.dumps({k: uri(os.path.join(R, "assets/headshots", "%s.%s" % (k, e)), "image/png" if e == "png" else "image/jpeg") for k, e in fm.items()}))
L = os.path.join(R, "assets/logos")
s = s.replace("{{LOGO}}", uri(os.path.join(L, "logo.png"), "image/png"))
for k, f in (("LI", "ic_li"), ("IG", "ic_ig"), ("GM", "ic_gm"), ("LT", "ic_lt")):
    s = s.replace("{{IC_%s}}" % k, uri(os.path.join(L, f + ".png"), "image/png"))
for i in range(10):
    s = s.replace("{{LG%d}}" % i, uri(os.path.join(L, "lg_%d.png" % i), "image/png"))
assert "{{" not in s
open(os.path.join(R, "index.html"), "w", encoding="utf-8").write(s)
print("Built index.html (%d KB)" % (len(s) // 1024))
