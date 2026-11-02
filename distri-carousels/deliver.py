# -*- coding: utf-8 -*-
import os, base64, io, zipfile, shutil
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = f"{ROOT}/out"
DEL = f"{ROOT}/deliver"
os.makedirs(DEL, exist_ok=True)

DISTRIS = [
 ("mooideco", "Mooideco", "NL", "nl"),
 ("gointernational", "Go International", "UK", "en"),
 ("segelken", "RS Segelken", "DE", "de"),
]
STYLES = {1: "Stijl 1 · Studio (licht, kaders, cursor-pills)",
          2: "Stijl 2 · Studio Dark (donker, dot-grid, fotolijsten)",
          3: "Stijl 3 · Bold (felle achtergrond, oud vs. nieuw)"}

CAPTIONS = {
 "nl": """Zo kies je een kleurencombinatie die klopt, in 3 stappen: basiskleur, steunkleur, accent. In deze carousel: de regel van 4 of 5 kleuren, waarom textuur diepte geeft, en het voorbeeldpalet Meadow Glow met Sempertex codes.

Bestel je Sempertex kleuren op mooideco.nl.

#ballondecoratie #sempertex #mooideco #ballonartiest #kleurenpalet #ballonnen""",
 "en": """Choosing colours for a balloon decor in 3 steps: base, support, accent. Swipe for the 4 or 5 colour rule, why texture adds depth, and the Meadow Glow example palette with Sempertex codes.

Trade customers: order your Sempertex colours at gointernational.co.uk.

#balloondecor #sempertex #gointernational #balloonartist #colourpalette #balloons""",
 "de": """Farbkombinationen für Ballondeko in 3 Schritten: Basisfarbe, Begleitfarbe, Akzent. Im Carousel: die Regel von 4 oder 5 Farben, warum Textur Tiefe bringt, und die Beispielpalette Meadow Glow mit Sempertex Codes.

Bestell deine Sempertex Farben auf rs-segelken.de.

#ballondeko #sempertex #rssegelken #ballonkünstler #farbpalette #ballons""",
}

README = """Carousel: "Hoe kies je kleurencombinaties voor ballondecoratie" (bron: sempertexeurope.com/blog)
Distributeur: {name} ({lang})

Inhoud
- stijl1/ … stijl3/: 7 slides per stijl, PNG 1080x1350 (Instagram 4:5), slide-01 = cover, slide-07 = CTA.
- caption.txt: voorgestelde caption voor de post.

Opmerkingen
- Fonts, kleuren en logo komen uit de huisstijl van {name}. Sempertex flor staat op elke slide.
- De ballonnen zijn de echte R12 productfoto's van sempertexeurope.com (Rosewood 010, Eucalyptus 027,
  Pastel Dusk Green Tea 126, Silk Gold Dust 870, enz.), uitgeknipt uit de webshop.
- Paletten (Meadow Glow, Sage Whisper) komen van sempertexeurope.com/inspiration.
"""

def thumb_b64(path, w=540):
    im = Image.open(path).convert("RGB")
    im = im.resize((w, int(w * im.height / im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=80, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

# ---------- zips
for key, name, lang, lc in DISTRIS:
    zpath = f"{DEL}/{name.replace(' ', '_')}_carousels.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for s in (1, 2, 3):
            d = f"{OUT}/{key}_stijl{s}"
            for i in range(1, 8):
                z.write(f"{d}/slide-{i:02d}.png", f"stijl{s}/slide-{i:02d}.png")
        z.writestr("caption.txt", CAPTIONS[lc])
        z.writestr("README.txt", README.format(name=name, lang=lang))
    print(zpath, round(os.path.getsize(zpath)/1e6, 1), "MB")

# ---------- preview html
sections = ""
nav = ""
for key, name, lang, lc in DISTRIS:
    nav += f'<a href="#{key}">{name} <span>{lang}</span></a>'
    blocks = ""
    for s in (1, 2, 3):
        slides = "".join(
            f'<figure><img src="{thumb_b64(f"{OUT}/{key}_stijl{s}/slide-{i:02d}.png")}" alt="{name} stijl {s} slide {i}" loading="lazy"><figcaption>{i}</figcaption></figure>'
            for i in range(1, 8))
        blocks += f"""
      <div class="style">
        <h3>{STYLES[s]}</h3>
        <div class="strip">{slides}</div>
      </div>"""
    cap = CAPTIONS[lc].replace("\n", "<br>")
    sections += f"""
  <section id="{key}">
    <header class="sec-head"><h2>{name}</h2><span class="lang">{lang}</span></header>
    {blocks}
    <details class="caption"><summary>Caption ({lang})</summary><p>{cap}</p></details>
  </section>"""

html = f"""<title>Distri Carousels Kleurencombinaties</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
/* Layout: review board. Eén kolom, per distri drie horizontale slide-strips. Neutraal canvas zodat de huisstijlen zelf spreken. */
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
section{{padding-block:32px 8px;border-bottom:1px solid var(--line)}}
.sec-head{{display:flex;align-items:baseline;gap:12px;margin-bottom:8px}}
h2{{font-family:'Rethink Sans','Lato',sans-serif;font-size:26px;margin:0;letter-spacing:-.01em}}
.lang{{background:var(--chip);color:var(--accent);border-radius:6px;padding:2px 8px;font-size:12px;font-weight:700;letter-spacing:.08em}}
.style{{margin-top:18px}}
h3{{font-size:14px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:0 0 10px;font-weight:700}}
.strip{{display:flex;gap:12px;overflow-x:auto;padding-bottom:10px;scroll-snap-type:x mandatory}}
.strip figure{{margin:0;flex:0 0 auto;width:min(270px,70vw);scroll-snap-align:start;position:relative}}
.strip img{{width:100%;height:auto;display:block;border-radius:10px;border:1px solid var(--line);background:var(--card)}}
.strip figcaption{{position:absolute;left:8px;top:8px;background:rgba(0,0,0,.55);color:#fff;font-size:12px;font-weight:700;border-radius:6px;padding:2px 8px;font-variant-numeric:tabular-nums}}
.caption{{margin-top:18px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px}}
.caption summary{{cursor:pointer;font-weight:700;font-size:14px}}
.caption p{{margin:10px 0 2px;font-size:15px;line-height:1.5;max-width:70ch}}
.note{{color:var(--muted);font-size:14px;line-height:1.5;max-width:70ch;margin-top:28px}}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Rethink+Sans:wght@600;800&display=swap">
<div class="wrap">
  <header class="top">
    <div><h1>Distri carousels: kleurencombinaties kiezen</h1>
    <p class="sub">Eén blog, drie distributeurs, drie stijlen. 7 slides per carousel, 1080 × 1350. Scroll elke strip horizontaal.</p></div>
    <nav>{nav}</nav>
  </header>
  {sections}
  <p class="note">De ballonnen zijn de echte R12 productfoto's uit de webshop (Rosewood 010, Eucalyptus 027, Pastel Dusk Green Tea 126, Silk Gold Dust 870 en de andere kleuren in de post). De paletten Meadow Glow en Sage Whisper komen van sempertexeurope.com/inspiration. De Sempertex flor staat op elke slide.</p>
</div>
"""
with open(f"{DEL}/preview.html", "w", encoding="utf-8") as f:
    f.write(html)
print("preview", round(os.path.getsize(f"{DEL}/preview.html")/1e6, 1), "MB")
