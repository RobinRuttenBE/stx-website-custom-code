# -*- coding: utf-8 -*-
"""Leest de distri-huisstijlen map en bouwt brands.json + uitgeknipte logo's in assets/logos/."""
import os, re, json, colorsys, subprocess
from PIL import Image, ImageChops

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Distri huisstijlen")
ROOT = os.path.dirname(os.path.abspath(__file__))
LOGOS = f"{ROOT}/assets/logos"
os.makedirs(LOGOS, exist_ok=True)

COUNTRY_LANG = {"Netherlands": "nl", "United Kingdom": "en", "Ireland": "en", "Malta": "en",
                "Germany": "de", "Switzerland": "de", "France": "fr", "Poland": "pl", "Greece": "el",
                "Hungary": "hu", "Lithuania": "lt", "Italy": "it"}
FONT_MAP = {  # websitefont -> (fontsource family, head weight) ; None = systeemfont
    "Montserrat": ("Montserrat", 800), "Lato": ("Lato", 900), "Albert Sans": ("Albert Sans", 800),
    "Quicksand": ("Quicksand", 700), "Inter": ("Inter", 800), "Open Sans": ("Open Sans", 800),
    "Comfortaa": ("Comfortaa", 700), "Poppins": ("Poppins", 800), "Kaushan Script": ("Kaushan Script", 400),
    "RobotoSerif-Regular": ("Roboto Serif", 800), "Karla-Regular": ("Karla", 700), "Abril Fatface": ("Abril Fatface", 400),
    "Figtree": ("Figtree", 700), "Fredoka": ("Fredoka", 700), "Kanit": ("Kanit", 800), "Nunito Sans": ("Nunito Sans", 700),
    "Playfair Display": ("Playfair Display", 800), "Catamaran": ("Catamaran", 800), "Rethink Sans": ("Rethink Sans", 800),
    "gothambold1": ("Montserrat", 800), "Gotham Book": ("Montserrat", 400),
}
LOGO_PICK = {  # map -> bestand (beste versie), anders logo-website.*
    "Balloon Service Basel": "logo-partnerpagina.png",
    "Datta's wholesale": "Logo's/DATTAS.png",
    "Dm Balloon Company": "Neues-Logo-21_1-2048x526 (1).png",
    "Euro Party": "Logo/logo-europarty-by-BF.jpg",
    "Go International": "Logo/goint hi res (2).jpg",
    "Irish Party Supplies": "Logo.png",
    "Mooideco": "Logo's/Original on Transparent.png",
    "Northwest Greetings": "New logo.png",
    "Pro Balloon Shop": "PBS-Logo.png",
    "Sempertex France": "logo-1746117907 (1).jpg",
    "Tons of Fun": "tons-of-fun-logo (1).jpg",
    "Crosswear Trading LTD": "logo-familytree.png",
    "Cut Price Wholesaler": "logo-familytree.png",
}
SKIP = {"STX EU"}

def slug(name):
    s = re.sub(r"[^a-z0-9]+", "", name.lower().replace("&", "and"))
    return s

def hexes(line):
    return re.findall(r"#[0-9a-fA-F]{6}", line)

def h2rgb(h): h = h.lstrip("#"); return tuple(int(h[i:i+2], 16)/255 for i in (0, 2, 4))
def rgb2h(r, g, b): return "#%02X%02X%02X" % (round(r*255), round(g*255), round(b*255))
def hls(h): r, g, b = h2rgb(h); return colorsys.rgb_to_hls(r, g, b)
def from_hls(hh, l, s): return rgb2h(*colorsys.hls_to_rgb(hh, l, s))
def lum(h):
    r, g, b = h2rgb(h)
    f = lambda c: c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def contrast(a, b):
    la, lb = lum(a), lum(b); hi, lo = max(la, lb), min(la, lb); return (hi+0.05)/(lo+0.05)

def parse_md(path):
    d = {"logo": [], "accent": [], "text": None, "darkp": None, "head": None, "body": None, "country": None, "site": None, "official": []}
    if not os.path.exists(path): return d
    for line in open(path, encoding="utf-8"):
        if "**Land:**" in line: d["country"] = line.split("**Land:**")[1].strip()
        elif "**Website:**" in line: d["site"] = line.split("**Website:**")[1].strip()
        elif line.startswith("- **Titels") : d["head"] = line.split(":**")[1].strip()
        elif line.startswith("- **Tekst:**"): d["body"] = line.split(":**")[1].strip()
        elif "**Uit het logo:**" in line: d["logo"] = hexes(line)
        elif "**Accentkleuren" in line: d["accent"] = hexes(line)
        elif "**Tekstkleur:**" in line: d["text"] = (hexes(line) or [None])[0]
        elif "**Donkere vlakken:**" in line: d["darkp"] = (hexes(line) or [None])[0]
        elif line.startswith("Officiele"): d["official"] = hexes(line)
    return d

def font_of(s, default="Inter"):
    if not s or "systeemfont" in s: return default
    for k, v in FONT_MAP.items():
        if k.lower() in s.lower(): return v[0]
    return default

def head_weight(fam):
    for k, v in FONT_MAP.items():
        if v[0] == fam: return v[1]
    return 800

def pick_colours(d):
    cands = d["official"][:0] + d["logo"] + d["accent"]
    cands = [c.upper() for c in cands]
    sat = [c for c in cands if hls(c)[2] > 0.25 and 0.12 < hls(c)[1] < 0.85]   # verzadigd en niet te licht/donker
    neutral = [c for c in cands if c not in sat]
    primary = sat[0] if sat else (cands[0] if cands else "#444444")
    others = [c for c in sat if c != primary]
    c2 = others[0] if others else from_hls(hls(primary)[0], min(0.75, hls(primary)[1]+0.25), hls(primary)[2])
    c3 = others[1] if len(others) > 1 else from_hls(hls(primary)[0], max(0.2, hls(primary)[1]-0.18), hls(primary)[2])
    hh, l, s = hls(primary)
    # donker: eigen donker vlak als het niet neutraal zwart is, anders merk-donker uit de primaire tint
    dark = None
    if d["darkp"]:
        dh, dl, ds = hls(d["darkp"])
        if dl < 0.25 and ds > 0.15: dark = d["darkp"].upper()
    if not dark:
        dark = from_hls(hh, 0.12, min(0.55, max(0.3, s)))
    ink = dark
    paper = from_hls(hh, 0.975, min(0.6, s))
    tint = from_hls(hh, 0.90, min(0.5, s))
    # bright: primaire kleur als zwarte tekst erop leesbaar is, anders lichter
    bright = primary
    if contrast(bright, ink) < 4.5:
        for L in (0.55, 0.62, 0.68, 0.74):
            bright = from_hls(hh, L, max(0.45, s))
            if contrast(bright, ink) >= 4.5: break
    pill_text = from_hls(hh, 0.74, max(0.45, s))
    if contrast(pill_text, dark) < 4: pill_text = from_hls(hh, 0.82, max(0.4, s))
    return dict(c1=primary, c2=c2, c3=c3, dark=dark, ink=ink, paper=paper, tint=tint, bright=bright,
                bright_text=ink, pill_dark=dark, pill_dark_text=pill_text)

def knockout_white(im, lo=222, hi=250):
    im = im.convert("RGBA"); px = im.load(); w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]; m = min(r, g, b)
            if m >= hi: px[x, y] = (r, g, b, 0)
            elif m > lo: px[x, y] = (r, g, b, int(a*(1-(m-lo)/(hi-lo))))
    return im

def trim(im):
    bg = Image.new("RGBA", im.size, (0, 0, 0, 0)); bbox = ImageChops.difference(im, bg).getbbox()
    return im.crop(bbox) if bbox else im

def prep_logo(folder, key):
    pick = LOGO_PICK.get(folder)
    if pick: path = os.path.join(SRC, folder, pick)
    else:
        files = [f for f in os.listdir(os.path.join(SRC, folder)) if f.startswith("logo-website.")]
        if not files: return None
        path = os.path.join(SRC, folder, files[0])
    out = f"{LOGOS}/{key}.png"
    if path.lower().endswith(".svg"):
        subprocess.run(["python3", "-c", f"""
from playwright.sync_api import sync_playwright
svg=open({path!r},encoding='utf-8').read()
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={{'width':1600,'height':600}})
    pg.set_content('<html><body style="margin:0;background:transparent"><div id=w style="display:inline-block">'+svg+'</div></body></html>')
    pg.evaluate("document.querySelector('svg').setAttribute('width','1400');document.querySelector('svg').removeAttribute('height')")
    pg.query_selector('#w').screenshot(path={out!r}, omit_background=True); b.close()
"""], check=True)
        im = Image.open(out).convert("RGBA")
    else:
        im = Image.open(path).convert("RGBA")
    alpha = im.getchannel("A")
    if alpha.getextrema()[0] == 255:   # geen transparantie -> wit wegknippen
        im.thumbnail((1600, 1600)); im = knockout_white(im)
    else:
        im.thumbnail((1600, 1600))
    im = trim(im); im.save(out)
    return out, im.size

brands = {}
for folder in sorted(os.listdir(SRC)):
    if folder in SKIP or not os.path.isdir(os.path.join(SRC, folder)): continue
    d = parse_md(os.path.join(SRC, folder, "huisstijl.md"))
    key = slug(folder.split(" (")[0])
    name = folder.replace(" (STX DE)", "").replace(" (Balloon Fantasy)", "")
    if folder.startswith("Segelken"): name = "RS Segelken"
    head = font_of(d["head"], default="Inter"); body = font_of(d["body"], default="Inter")
    if head == "Kaushan Script" or head == "Abril Fatface" or head == "Playfair Display":
        body = body if body not in ("Inter",) else ("Lato" if head != "Kaushan Script" else "Open Sans")
    cols = pick_colours(d)
    logo = prep_logo(folder, key)
    domain = re.sub(r"^https?://(www\.)?", "", d["site"] or "").rstrip("/")
    brands[key] = dict(name=name, folder=folder, country=d["country"], lang=COUNTRY_LANG.get(d["country"], "en"),
                       site=d["site"], domain=domain, head=head, body=body, head_w=head_weight(head),
                       body_w=400, body_b=700, logo=logo[0] if logo else None, logo_white=None, logo_card=logo[0] if logo else None,
                       logo_ratio=(logo[1][0]/logo[1][1]) if logo else 3.0, **cols)
    print(f"{key:28s} {d['country']:14s} {head:16s}/{body:12s} c1={cols['c1']} dark={cols['dark']} bright={cols['bright']} logo={logo[1] if logo else None}")

json.dump(brands, open(f"{ROOT}/brands.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(brands), "brands")
