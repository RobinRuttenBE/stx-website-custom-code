# -*- coding: utf-8 -*-
"""Bundelt alle gerenderde carousels: zip per land (UK in 2 delen), preview.html, overzicht."""
import os, io, json, base64, zipfile, re, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build  # laadt BRANDS + make_copy

ROOT = os.path.dirname(os.path.abspath(__file__)); OUT = f"{ROOT}/out"; DEL = f"{ROOT}/deliver"
os.makedirs(DEL, exist_ok=True)
B = build.BRANDS
STYLES = {1: "Stijl 1 · Studio", 2: "Stijl 2 · Studio Dark", 3: "Stijl 3 · Bold"}
LANGNAME = {"nl": "Nederlands", "en": "English (UK)", "de": "Deutsch", "fr": "Français", "it": "Italiano", "pl": "Polski", "el": "Ελληνικά", "hu": "Magyar", "lt": "Lietuvių"}

README = """Carousel: "Hoe kies je kleurencombinaties voor ballondecoratie" (bron: sempertexeurope.com/blog)
Distributeur: {name} ({country}, taal: {lang})

Inhoud
- stijl1/ … stijl3/: 7 slides per stijl, PNG 1080x1350 (Instagram 4:5), slide-01 = cover, slide-07 = CTA.
- caption.txt: voorgestelde caption voor de post.

Opmerkingen
- Fonts, kleuren en logo komen uit de huisstijl van {name} (map "Distri huisstijlen"). Sempertex staat op elke slide (naam in titel + logo).
- De ballonnen zijn de echte R12 productfoto's van sempertexeurope.com.
- Paletten (Meadow Glow, Sage Whisper, Spring Daisies, Kickoff Communion) komen van sempertexeurope.com/inspiration.
"""

def thumb_b64(path, w=240, q=66):
    im = Image.open(path).convert("RGB"); im = im.resize((w, int(w*im.height/im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

def done(key): return all(os.path.exists(f"{OUT}/{key}_stijl{s}/slide-07.png") for s in (1, 2, 3))

keys = [k for k in sorted(B) if done(k)]
print(len(keys), "distri's gerenderd")

# ---------- zips per land
groups = {}
for k in keys:
    c = B[k]["country"]
    if c == "United Kingdom":
        c = "United Kingdom A-L" if B[k]["name"][0].upper() <= "L" else "United Kingdom M-Z"
    groups.setdefault(c, []).append(k)
zips = []
for country, ks in sorted(groups.items()):
    zpath = f"{DEL}/Carousels_{country.replace(' ', '_')}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for k in ks:
            b = B[k]; c = build.make_copy(k); folder = b["name"].replace(" ", "_").replace("/", "-")
            for s in (1, 2, 3):
                for i in range(1, 8):
                    z.write(f"{OUT}/{k}_stijl{s}/slide-{i:02d}.png", f"{folder}/stijl{s}/slide-{i:02d}.png")
            z.writestr(f"{folder}/caption.txt", c["caption"])
            z.writestr(f"{folder}/README.txt", README.format(name=b["name"], country=b["country"], lang=LANGNAME[b["lang"]]))
    zips.append((zpath, round(os.path.getsize(zpath)/1e6, 1), [B[k]["name"] for k in ks]))
    print(zpath, round(os.path.getsize(zpath)/1e6, 1), "MB", len(ks))

# ---------- preview
by_lang = {}
for k in keys: by_lang.setdefault(B[k]["lang"], []).append(k)
nav = "".join(f'<a href="#lang-{l}">{LANGNAME[l]} <span>{len(ks)}</span></a>' for l, ks in by_lang.items())
sections = ""
for l, ks in by_lang.items():
    sections += f'<h2 class="lang-h" id="lang-{l}">{LANGNAME[l]} <span class="lang">{len(ks)} distri\'s</span></h2>'
    for k in ks:
        b = B[k]; c = build.make_copy(k)
        blocks = ""
        for s in (1, 2, 3):
            slides = "".join(f'<figure><img src="{thumb_b64(f"{OUT}/{k}_stijl{s}/slide-{i:02d}.png")}" alt="" loading="lazy"><figcaption>{i}</figcaption></figure>' for i in range(1, 8))
            blocks += f'<div class="style"><h3>{STYLES[s]}</h3><div class="strip">{slides}</div></div>'
        cap = c["caption"].replace("\n", "<br>")
        sections += f"""
  <section id="{k}">
    <header class="sec-head"><h2>{b['name']}</h2><span class="lang">{b['country']}</span><span class="dom">{b['domain']}</span></header>
    {blocks}
    <details class="caption"><summary>Caption</summary><p>{cap}</p></details>
  </section>"""

html = f"""<title>Distri Carousels Kleurencombinaties</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
:root{{--bg:#F3F1EE;--fg:#1B1A17;--muted:#6E6A62;--line:#DAD6CF;--card:#FFFFFF;--accent:#6B3FB9;--chip:#EEE8F7}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#17161A;--fg:#F1EFEA;--muted:#A49F96;--line:#2E2C33;--card:#1F1E24;--accent:#B99BF0;--chip:#2A2440;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#17161A;--fg:#F1EFEA;--muted:#A49F96;--line:#2E2C33;--card:#1F1E24;--accent:#B99BF0;--chip:#2A2440;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:'Lato',system-ui,sans-serif;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 48px}}
.wrap{{max-width:1180px;margin:0 auto}}
.top{{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:16px;padding-block:36px 20px;border-bottom:1px solid var(--line)}}
h1{{font-family:'Rethink Sans','Lato',sans-serif;font-size:clamp(26px,3.4vw,38px);margin:0;letter-spacing:-.02em;text-wrap:balance}}
.sub{{color:var(--muted);font-size:15px;margin:6px 0 0;max-width:62ch}}
nav{{display:flex;gap:8px;flex-wrap:wrap}}
nav a{{text-decoration:none;color:var(--fg);background:var(--card);border:1px solid var(--line);border-radius:999px;padding:8px 14px;font-size:14px;font-weight:700}}
nav a span{{color:var(--muted);font-weight:400;margin-left:6px}}
nav a:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
.lang-h{{font-family:'Rethink Sans','Lato',sans-serif;font-size:22px;margin:40px 0 0;padding-top:24px;border-top:3px solid var(--accent);display:flex;gap:12px;align-items:baseline}}
section{{padding-block:28px 8px;border-bottom:1px solid var(--line)}}
.sec-head{{display:flex;align-items:baseline;gap:12px;margin-bottom:6px;flex-wrap:wrap}}
h2{{font-family:'Rethink Sans','Lato',sans-serif;font-size:24px;margin:0;letter-spacing:-.01em}}
.lang{{background:var(--chip);color:var(--accent);border-radius:6px;padding:2px 8px;font-size:12px;font-weight:700;letter-spacing:.08em}}
.dom{{color:var(--muted);font-size:14px}}
.style{{margin-top:14px}}
h3{{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:0 0 8px;font-weight:700}}
.strip{{display:flex;gap:10px;overflow-x:auto;padding-bottom:8px;scroll-snap-type:x mandatory}}
.strip figure{{margin:0;flex:0 0 auto;width:min(200px,60vw);scroll-snap-align:start;position:relative}}
.strip img{{width:100%;height:auto;display:block;border-radius:8px;border:1px solid var(--line);background:var(--card)}}
.strip figcaption{{position:absolute;left:6px;top:6px;background:rgba(0,0,0,.55);color:#fff;font-size:11px;font-weight:700;border-radius:5px;padding:1px 7px;font-variant-numeric:tabular-nums}}
.caption{{margin-top:14px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 14px}}
.caption summary{{cursor:pointer;font-weight:700;font-size:14px}}
.caption p{{margin:10px 0 2px;font-size:14px;line-height:1.5;max-width:70ch}}
.note{{color:var(--muted);font-size:14px;line-height:1.5;max-width:70ch;margin-top:28px}}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Rethink+Sans:wght@600;800&display=swap">
<div class="wrap">
  <header class="top">
    <div><h1>Distri carousels: kleurencombinaties kiezen</h1>
    <p class="sub">Eén blog, {len(keys)} distributeurs, 3 stijlen per distri, 7 slides per carousel (1080 × 1350). Gegroepeerd per taal. Scroll elke strip horizontaal.</p></div>
    <nav>{nav}</nav>
  </header>
  {sections}
  <p class="note">Ballonnen zijn de echte R12 productfoto's uit de webshop. Distri's met dezelfde taal krijgen een andere hook, klantvraag, tweede palet en gespiegelde lay-out, zodat geen twee posts identiek zijn. Sempertex staat op elke slide in de titel en als logo.</p>
</div>
"""
with open(f"{DEL}/preview_all.html", "w", encoding="utf-8") as f: f.write(html)
print("preview_all.html", round(os.path.getsize(f"{DEL}/preview_all.html")/1e6, 1), "MB")
json.dump({"zips": zips}, open(f"{DEL}/zips.json", "w"), indent=1)
