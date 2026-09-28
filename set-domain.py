#!/usr/bin/env python3
"""Fill in the production domain everywhere.  Usage: python3 set-domain.py https://your-real-domain.in"""
import sys, pathlib
if len(sys.argv) != 2 or not sys.argv[1].startswith("http"):
    sys.exit("Usage: python3 set-domain.py https://your-real-domain.in")
url = sys.argv[1].rstrip("/")
root = pathlib.Path(__file__).parent
for name in ("index.html", "robots.txt", "sitemap.xml"):
    f = root / name
    text = f.read_text(encoding="utf-8").replace("https://YOUR-DOMAIN.example", url)
    if name == "index.html":
        text = text.replace("SITE_URL: ''", f"SITE_URL: '{url}'", 1)
    f.write_text(text, encoding="utf-8")
print("Domain set to", url)
left = [n for n in ("index.html", "robots.txt", "sitemap.xml") if "YOUR-DOMAIN" in (root / n).read_text(encoding="utf-8")]
print("Placeholders left:", left or "none")
if not (root / "assets" / "og-image.jpg").exists():
    print("REMINDER: add assets/og-image.jpg (1200x630) or link previews will be blank.")
