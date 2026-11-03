# -*- coding: utf-8 -*-
"""Genereert 9 carousels (3 distri's x 3 stijlen) als HTML, en rendert elke slide naar PNG 1080x1350."""
import os, sys, json, html
from carousel_copy import COPY, SX, PALETTES, MESSY, TEXTURE_DEMO

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = f"{ROOT}/fonts/node_modules/@fontsource"
ASSETS = f"{ROOT}/assets"
_topic_args = [a.split("=", 1)[1] for a in sys.argv if a.startswith("--topic=")]
TOPIC = _topic_args[0] if _topic_args else "colours"
TOPIC_TITLES = {"colours": "Kleurencombinaties kiezen", "artist": "Ballonartiest worden", "helium": "Helium voor ballonnen", "pricing": "Prijs voor ballondecoratie", "doublestuff": "Double stuffing", "storage": "Ballonnen bewaren", "releases": "Geen ballonoplatingen", "buyuk": "Waar koop je Sempertex in de UK", "startbiz": "Een ballonbusiness starten", "nozzleup": "Nozzle Up uitgelegd", "tying": "Ballonnen knopen zonder pijn", "spiral": "Spiraalboog bouwen", "flowers": "Ballonbloemen maken"}
OUT = f"{ROOT}/out" if TOPIC == "colours" else f"{ROOT}/out/{TOPIC}"
W, H = 1080, 1350

def esc(s): return html.escape(s, quote=False)
def hl(s):
    """Escape + het woord Sempertex highlighten in een merkpaarse pill."""
    return esc(s).replace("Sempertex", '<span class="sx">Sempertex</span>')
STX_WT = f"{ASSETS}/stx_full_whitetext.png"

# ---------------------------------------------------------------- BRANDS
import colorsys, glob
from copy_extra import VARIANTS, EXTRA, CAPTIONS_TPL
FLOR = f"{ASSETS}/stx_flor.png"
STX_FULL = f"{ASSETS}/stx_full.png"
STX_FULL_W = f"{ASSETS}/stx_full_white.png"

def _lum(h):
    h = h.lstrip("#"); r, g, b = (int(h[i:i+2], 16)/255 for i in (0, 2, 4))
    f = lambda c: c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def _contrast(a, b):
    la, lb = _lum(a), _lum(b); return (max(la, lb)+0.05)/(min(la, lb)+0.05)
def _text_on(bg, ink):
    return "#FFFFFF" if _contrast(bg, "#FFFFFF") >= 2.6 else ink

BRANDS = json.load(open(f"{ROOT}/brands.json", encoding="utf-8"))
# handmatig gefinetunede merken (eerste 3) + correcties
OVERRIDES = {
 "mooideco": dict(head="Montserrat", body="Lato", head_w=800, dark="#111424", ink="#111424", c1="#858CBC", c2="#DDACBB", c3="#5A6186",
                  paper="#FDF1F5", tint="#DED6F1", bright="#DDACBB", bright_text="#111424", pill_dark="#111424", pill_dark_text="#DDACBB",
                  logo=f"{ASSETS}/mooideco_color.png", logo_white=f"{ASSETS}/mooideco_white.png", logo_card=None, logo_ratio=2000/570, hero="duskrose",
                  cta_sub="Voor 15:00 besteld, vandaag verzonden. Gratis verzending vanaf €350."),
 "gointernational": dict(dark="#313147", ink="#1A1A2E", c1="#3084D5", c2="#6CBCE2", c3="#0C6EAF", paper="#F6F9FD", tint="#E3F0FA",
                  bright="#6CBCE2", bright_text="#111827", pill_dark="#313147", pill_dark_text="#6CBCE2", hero="caribbean",
                  cta_sub="Trade accounts only. Sales team on 01438 745746, Mon to Fri, 9 to 5."),
 "segelken": dict(dark="#0F2D57", ink="#0B1F3F", c1="#2563AD", c2="#0A9FE1", c3="#4D7DB4", paper="#F1F7FB", tint="#CEE1ED",
                  bright="#0A9FE1", bright_text="#0B1F3F", pill_dark="#0B1F3F", pill_dark_text="#5CC6F5", hero="caribbean",
                  cta_sub="We deliver. You create. All celebrate!"),
 "sempertexfrance": dict(c1="#6B3FB9", c2="#CD0B5C", c3="#1B073D", dark="#1B073D", ink="#1B073D", paper="#F7F2FC", tint="#F1D9FF",
                  bright="#B388F0", bright_text="#1B073D", pill_dark="#1B073D", pill_dark_text="#F1D9FF"),
 "premioloongermany": dict(c1="#6C625E", c2="#F4DCD3", c3="#2F170E", bright="#F4DCD3", pill_dark_text="#F4DCD3"),
 "balionaisumeile": dict(c1="#B6935E", c2="#921044", c3="#723434"),
 "northwestgreetings": dict(c1="#292B33", c2="#7B7E82", c3="#A6B3B4", bright="#A6B3B4", pill_dark_text="#C9D2D3"),
}
for k, o in OVERRIDES.items():
    if k in BRANDS: BRANDS[k].update(o)

# ballonkeys op kleurtoon, voor de 'hero'-ballon per merk
_HERO = {"rosewood": 350, "duskrose": 355, "mattepink": 340, "fuchsia": 330, "red": 0, "orange": 25, "yellow": 55, "matteyellow": 52,
         "limegreen": 85, "eucalyptus": 110, "greentea": 75, "caribbean": 190, "matteblue": 205, "royalblue": 225, "violet": 275,
         "golddust": 40, "reflexgold": 42, "whitesand": 38}
def _hue(h):
    h = h.lstrip("#"); r, g, b = (int(h[i:i+2], 16)/255 for i in (0, 2, 4)); hh, l, s = colorsys.rgb_to_hls(r, g, b); return hh*360, s, l
for k, b in BRANDS.items():
    b.setdefault("body_w", 400); b.setdefault("body_b", 700)
    for key in ("logo", "logo_card", "logo_white"):
        if b.get(key) and not os.path.isabs(b[key]): b[key] = os.path.join(ROOT, b[key])
    if not b.get("hero"):
        hh, s, l = _hue(b["c1"])
        if s < 0.2: b["hero"] = "whitesand"
        else: b["hero"] = min(_HERO, key=lambda n: min(abs(_HERO[n]-hh), 360-abs(_HERO[n]-hh)))
    b["ui"] = b["body"] if b["head"] in ("Kaushan Script", "Abril Fatface", "Playfair Display", "Roboto Serif") else b["head"]
    b["c1t"] = _text_on(b["c1"], b["ink"]); b["c2t"] = _text_on(b["c2"], b["ink"]); b["c3t"] = _text_on(b["c3"], b["ink"])
    r = b.get("logo_ratio", 3)
    b["footer_h"] = 130 if r < 1.0 else (110 if r < 1.3 else (84 if r < 2.2 else 64))
    b["cta_logo_h"] = 190 if r < 1.3 else (120 if r < 2.2 else 92)
    if k == "gointernational": b["footer_h"] = 74

# variatie: index binnen taalgroep bepaalt hook, vraag, 2e palet en 'flip' van de layout
_by_lang = {}
for k in sorted(BRANDS): _by_lang.setdefault(BRANDS[k]["lang"], []).append(k)
for lang, keys in _by_lang.items():
    for i, k in enumerate(keys):
        BRANDS[k]["vi"] = i
        BRANDS[k]["flip"] = (i % 2 == 1)

# ---------------------------------------------------------------- KLEURSETS
# Productvisuals (duplet, cluster, slinger, kit, zweefvoorbeelden) tonen per distri EN per blog een andere set
# ballonkleuren. 12 harmonieuze sets uit de 18 uitgeknipte R12-foto's; de keuze draait op vi (index in de
# taalgroep), de taal en een vaste seed per blogonderwerp, zodat dezelfde distri bij een volgende blog andere
# kleuren krijgt en twee distri's met dezelfde taal zelden dezelfde set hebben (EN: 18 distri's, 12 sets,
# de herhalingen krijgen een ander kleurenduo vooraan). Blogs die zelf paletten voorschrijven (kleurencombinaties)
# gebruiken hun eigen paletten en niet deze sets.
PAL_SETS = [
    ["rosewood", "duskrose", "mattepink", "whitesand"],      # blush
    ["eucalyptus", "greentea", "golddust", "whitesand"],     # sage
    ["royalblue", "caribbean", "matteblue", "whitesand"],    # ocean
    ["fuchsia", "violet", "rosewood", "mattepink"],          # berry
    ["orange", "matteyellow", "reflexgold", "whitesand"],    # sunset
    ["red", "yellow", "royalblue", "whitesand"],             # primary
    ["limegreen", "caribbean", "matteyellow", "whitesand"],  # fresh
    ["violet", "matteblue", "mattepink", "whitesand"],       # lilac
    ["golddust", "reflexgold", "eucalyptus", "rosewood"],    # autumn
    ["caribbean", "fuchsia", "yellow", "whitesand"],         # pop
    ["duskrose", "golddust", "greentea", "matteblue"],       # dusty
    ["red", "whitesand", "matteblue", "royalblue"],          # nautical
]
_LANG_OFF = {"nl": 0, "en": 1, "de": 2, "fr": 3, "it": 4, "pl": 5, "el": 6, "hu": 7, "lt": 8}
def topic_seed(topic):
    return sum(ord(ch) for ch in topic) % len(PAL_SETS)
def assign_palettes(topic):
    """Zet b['pal'] (4 keys) per distri voor dit blogonderwerp."""
    seed = topic_seed(topic)
    for k, b in BRANDS.items():
        idx = (b["vi"] * 5 + _LANG_OFF.get(b["lang"], 0) + seed) % len(PAL_SETS)
        p = list(PAL_SETS[idx])
        if b["vi"] >= len(PAL_SETS): p = p[2:] + p[:2]          # herhaling binnen een grote taalgroep: ander duo vooraan
        if b.get("flip"): p = [p[1], p[0], p[3], p[2]]
        b["pal"] = p; b["pal_idx"] = idx
def pal_label(key, short=True):
    """'Rosewood 010' (short) of 'Fashion Rosewood 010' voor onder een productfoto."""
    s = SX[key]; nm = s["name"]
    if short: nm = nm.replace("Fashion ", "").replace("Pastel Dusk ", "P. Dusk ").replace("Pastel Matte ", "Matte ")
    return f"{nm} {s['code']}"

# fonts: alle fontsource-pakketten scannen (latin, latin-ext, greek)
_PKG = {"Montserrat": "montserrat", "Lato": "lato", "Albert Sans": "albert-sans", "Quicksand": "quicksand", "Inter": "inter",
        "Open Sans": "open-sans", "Comfortaa": "comfortaa", "Poppins": "poppins", "Kaushan Script": "kaushan-script",
        "Roboto Serif": "roboto-serif", "Karla": "karla", "Abril Fatface": "abril-fatface", "Figtree": "figtree", "Fredoka": "fredoka",
        "Kanit": "kanit", "Nunito Sans": "nunito-sans", "Playfair Display": "playfair-display", "Catamaran": "catamaran", "Rethink Sans": "rethink-sans"}
_RANGES = {"latin": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
           "latin-ext": "U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF",
           "greek": "U+0370-03FF", "greek-ext": "U+1F00-1FFF"}
def font_weights(fam):
    pkg = _PKG[fam]; ws = set()
    for f in glob.glob(f"{FONTS}/{pkg}/files/{pkg}-latin-*-normal.woff2"):
        part = os.path.basename(f).split("-latin-")[1].split("-")[0]
        if part.isdigit(): ws.add(int(part))
    return sorted(ws)
def font_faces(*families):
    css = ""
    for fam in families:
        pkg = _PKG[fam]
        for w in font_weights(fam):
            for sub, rng in _RANGES.items():
                f = f"{FONTS}/{pkg}/files/{pkg}-{sub}-{w}-normal.woff2"
                if os.path.exists(f):
                    css += f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};src:url('file://{f}') format('woff2');unicode-range:{rng};}}\n"
    return css
def heavy(fam, cap=900):
    ws = [w for w in font_weights(fam) if w <= cap]; return max(ws) if ws else 700
def body_bold(fam):
    ws = font_weights(fam); return 700 if 700 in ws else (max(ws) if ws else 700)

PALETTES["communion"] = {"name": "Kickoff Communion", "keys": ["whitesand", "matteblue", "eucalyptus"]}
BASE_COPY = dict(COPY); BASE_COPY.update(EXTRA)

def make_copy(bkey):
    """Copy voor een distri: basistaal + varianten op basis van de index binnen de taalgroep."""
    b = BRANDS[bkey]; lang = b["lang"]; c = dict(BASE_COPY[lang]); v = VARIANTS[lang]; i = b["vi"]
    c["cover_title"] = v["cover_title"][i % 3]
    c["cover_sub"] = v["cover_sub"][i % 2]
    c["client_question"] = v["client_question"][(i * 2) % 3]
    c["s3_old_quote"] = v["s3_old_quote"][(i + 1) % 3]
    c["s3_client_old"] = v["s3_client_old"][i % 2]
    c["palette2"] = ["sage", "daisies", "communion"][(i + 1) % 3]
    c["cta_title"] = v["cta_title_tpl"].format(name=b["name"])
    c["cta_sub"] = b.get("cta_sub") or v["cta_sub_generic"]
    c["cta_url"] = b["domain"]
    c["caption"] = CAPTIONS_TPL[lang].format(domain=b["domain"], tag=re.sub(r"[^a-z0-9]", "", b["name"].lower()))
    return c
import re
def rot(b, deg):
    """Rotatie-teken wisselt per distri (flip) voor een net iets andere lay-out."""
    return -deg if b.get("flip") else deg

# ---------------------------------------------------------------- BALLOON
# Echte productfoto's (R12 packshots van sempertexeurope.com, uitgeknipt) in /balloons/<key>.png
BALLOONS = f"{ROOT}/balloons"
HEX2KEY = {v["hex"].upper(): k for k, v in SX.items()}
HEX2KEY.update({"#D7262B": "red", "#F2D22E": "yellow", "#2D4FB5": "royalblue", "#A9D83C": "limegreen",
                "#D63384": "fuchsia", "#F07E22": "orange", "#6B3FB9": "violet", "#3CB7D9": "caribbean",
                "#F3C6D3": "mattepink", "#B9D6EC": "matteblue", "#E8DFD0": "whitesand",
                "#E0B45C": "reflexgold", "#D4B27C": "golddust", "#C4838C": "rosewood"})
PHOTO_RATIO = 634 / 451  # hoogte/breedte van de packshots

_RATIO_CACHE = {}
def photo_ratio(key):
    """hoogte/breedte van een uitgeknipte productfoto (R12 ≈ 1.405, een 260 ≈ 8.7)."""
    if key not in _RATIO_CACHE:
        try:
            from PIL import Image
            w, h = Image.open(f"{BALLOONS}/{key}.png").size; _RATIO_CACHE[key] = h / w
        except Exception:
            _RATIO_CACHE[key] = PHOTO_RATIO
    return _RATIO_CACHE[key]

def balloon(hexc, tex="fashion", size=120, extra_style="", cls=""):
    """size = breedte in px. Gebruikt de echte productfoto als die bestaat, anders CSS-ballon."""
    key = hexc if os.path.exists(f"{BALLOONS}/{hexc}.png") else HEX2KEY.get(str(hexc).upper())
    if key and os.path.exists(f"{BALLOONS}/{key}.png"):
        return (f'<img class="bl {cls}" src="file://{BALLOONS}/{key}.png" '
                f'style="width:{size}px;height:{int(size*photo_ratio(key))}px;{extra_style}">')
    return css_balloon(hexc, tex, size, extra_style, cls)

def css_balloon(hexc, tex="fashion", size=120, extra_style="", cls=""):
    hl = {
      "fashion": f"radial-gradient(circle at 34% 28%, rgba(255,255,255,.62) 0, rgba(255,255,255,.22) 16%, rgba(255,255,255,0) 42%), radial-gradient(circle at 68% 88%, rgba(0,0,0,.20) 0, rgba(0,0,0,0) 52%), {hexc}",
      "matte":   f"radial-gradient(circle at 34% 28%, rgba(255,255,255,.34) 0, rgba(255,255,255,0) 48%), radial-gradient(circle at 68% 88%, rgba(0,0,0,.10) 0, rgba(0,0,0,0) 52%), {hexc}",
      "silk":    f"linear-gradient(135deg, rgba(255,255,255,.62) 0%, rgba(255,255,255,0) 34%, rgba(255,255,255,0) 62%, rgba(255,255,255,.38) 100%), radial-gradient(circle at 30% 24%, rgba(255,255,255,.7) 0, rgba(255,255,255,0) 38%), radial-gradient(circle at 70% 90%, rgba(0,0,0,.22) 0, rgba(0,0,0,0) 50%), {hexc}",
      "reflex":  f"radial-gradient(circle at 30% 24%, #fff 0, rgba(255,255,255,.9) 9%, rgba(255,255,255,0) 30%), linear-gradient(160deg, rgba(255,255,255,.55) 0%, rgba(255,255,255,0) 38%, rgba(0,0,0,.30) 72%, rgba(255,255,255,.35) 100%), {hexc}",
    }[tex]
    return (f'<div class="bl {cls}" style="width:{size}px;height:{int(size*1.08)}px;background:{hl};{extra_style}">'
            f'<i style="border-top-color:{hexc}"></i></div>')

def palette_row(keys, size=86, gap=18, labels=True, lang="nl", codes=True, name_size=18):
    out = f'<div class="prow" style="gap:{gap}px">'
    for k in keys:
        c = SX[k]
        out += '<div class="pitem">' + balloon(c["hex"], c["tex"], size)
        if labels:
            nm = c["name"].replace("Fashion ", "").replace("Pastel Dusk ", "P. Dusk ").replace("Pastel Matte ", "P. Matte ")
            out += f'<div class="pname" style="font-size:{name_size}px">{esc(nm)}'
            if codes: out += f'<span class="pcode"> {c["code"]}</span>'
            out += '</div>'
        out += '</div>'
    return out + '</div>'

def mini_palette(pkey, size=54):
    p = PALETTES[pkey]
    return (f'<div class="mini"><div class="mini-name">{esc(p["name"])}</div><div class="prow" style="gap:10px">'
            + "".join(f'<div class="pitem">{balloon(SX[k]["hex"], SX[k]["tex"], size)}<div class="pcode-only">{SX[k]["code"]}</div></div>' for k in p["keys"])
            + '</div></div>')

def cursor_svg(color):
    return (f'<svg class="cur" viewBox="0 0 24 24" width="30" height="30"><path d="M3 2 L21 11 L12 13 L9 22 Z" fill="{color}" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg>')

def arrow_svg(color="#111", w=160, h=140, flip=False, cls=""):
    # gebogen handgetekende pijl
    path = "M10 10 C 20 80, 60 120, 150 120" if not flip else "M150 10 C 140 80, 100 120, 10 120"
    head = "M126 100 L150 120 L122 138" if not flip else "M34 100 L10 120 L38 138"
    return (f'<svg class="arrow {cls}" viewBox="0 0 160 150" width="{w}" height="{h}">'
            f'<path d="{path}" fill="none" stroke="{color}" stroke-width="4.5" stroke-linecap="round"/>'
            f'<path d="{head}" fill="none" stroke="{color}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def logo_img(b, on_dark=False, height=60, card=False):
    """Distri logo. Op donker: witte versie als die bestaat, anders in witte kaart."""
    if on_dark and b["logo_white"]:
        return f'<img class="dlogo" src="file://{b["logo_white"]}" style="height:{height}px">'
    if on_dark or card:
        return f'<div class="logocard"><img class="dlogo" src="file://{b["logo"]}" style="height:{height}px"></div>'
    return f'<img class="dlogo" src="file://{b["logo"]}" style="height:{height}px">'

def flor_img(height=64):
    return f'<img class="flor" src="file://{FLOR}" style="height:{height}px">'

# ================================================================ STIJL 1: STUDIO (cream)
def css_s1(b):
    return f"""
.s1{{background:{b['paper']};color:{b['ink']};font-family:'{b['body']}',sans-serif}}
.s1 h1,.s1 h2,.s1 .big{{font-family:'{b['head']}',sans-serif;font-weight:{b['head_w']};letter-spacing:-0.025em;line-height:1.02;margin:0}}
.s1 .body{{font-size:30px;line-height:1.38}}
.s1 .box{{position:absolute;background:#fff;border:4px solid {b['ink']};border-radius:34px;padding:48px 52px;box-sizing:border-box}}
.s1 .pill{{position:absolute;display:inline-block;padding:12px 24px;border-radius:999px;color:#fff;font-family:'{b['body']}';font-weight:{b['body_b']};font-size:28px;white-space:nowrap;box-shadow:0 6px 18px rgba(0,0,0,.12)}}
.s1 .pill .cur{{position:absolute;left:-26px;top:-26px}}
.s1 .tag{{position:absolute;display:inline-flex;align-items:center;gap:12px;padding:12px 26px;border:3px solid {b['ink']};border-radius:999px;background:#fff;font-size:28px;font-weight:{b['body_b']}}}
.s1 .tag .ast{{color:{b['c1']};font-size:34px;line-height:1}}
.s1 .footer{{position:absolute;left:70px;right:70px;bottom:52px;display:flex;align-items:center;justify-content:space-between}}
.s1 .footer .stx{{display:flex;align-items:center;gap:14px;font-size:22px;font-weight:{b['body_b']};color:{b['ink']}}}
.s1 .step{{display:flex;gap:18px;align-items:flex-start;font-size:30px;line-height:1.32;margin-top:16px}}
.s1 .step b{{font-family:'{b['ui']}';font-weight:{b['head_w']};min-width:44px}}
.s1 .stack{{position:absolute;left:90px;right:90px}}
.s1 .card{{position:absolute;left:0;right:0;background:#fff;border:3px solid {b['ink']};border-radius:26px;padding:34px 40px;box-sizing:border-box;box-shadow:0 10px 30px rgba(0,0,0,.10)}}
.s1 .chat{{position:absolute;left:80px;right:80px;background:#fff;border:3px solid {b['ink']};border-radius:28px;padding:34px 40px;box-sizing:border-box;font-size:32px;line-height:1.3}}
.s1 .chat .send{{position:absolute;right:28px;bottom:26px;width:64px;height:64px;border-radius:16px;background:{b['c1']};color:#fff;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:700}}
.s1 .url{{display:inline-block;background:{b['c1']};color:#fff;border-radius:999px;padding:26px 54px;font-size:44px;font-weight:{b['body_b']};font-family:'{b['ui']}'}}
.s1 .bigballoon{{position:absolute}}
.s1 .sx{{background:#6b3fb9;color:#fff;border-radius:.22em;padding:0 .16em .04em;line-height:1;display:inline-block}}
"""

def s1_footer(b, stx_h=66):
    return (f'<div class="footer">{logo_img(b, height=b["footer_h"])}'
            f'<img src="file://{STX_FULL}" style="height:{stx_h}px"></div>')

def s1_slides(b, c):
    S = []
    # 1 COVER
    pills = c["cover_pills"]
    S.append(f"""
<section class="slide s1">
  <h1 data-fit style="position:absolute;left:70px;right:70px;top:250px;max-height:560px;font-size:104px;text-align:center;line-height:1.06">{hl(c['cover_title'])}</h1>
  <div class="pill" style="background:{b['c1']};color:{b['c1t']};right:60px;top:130px;transform:rotate({rot(b,-4)}deg)">{cursor_svg(b['c1'])}{esc(pills[0])}</div>
  <div class="pill" style="background:{b['c2']};color:{b['c2t']};right:90px;top:835px;transform:rotate({rot(b,3)}deg)">{cursor_svg(b['c2'])}{esc(pills[1])}</div>
  <div class="pill" style="background:{b['c3']};color:{b['c3t']};left:90px;top:880px;transform:rotate({rot(b,-2)}deg)">{cursor_svg(b['c3'])}{esc(pills[2])}</div>
  <div style="position:absolute;left:150px;top:960px">{arrow_svg(b['ink'], 130, 120)}</div>
  <div style="position:absolute;left:310px;right:90px;top:1020px;font-size:30px;line-height:1.35">{esc(c['cover_sub'])}</div>
  {s1_footer(b, stx_h=84)}
</section>""")
    # 2 STEPS
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s1">
  <div class="box" style="left:70px;top:120px;width:800px;height:560px">
    <h2 data-fit style="font-size:84px;max-height:460px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:830px;top:90px;transform:rotate(14deg)">{balloon(b['hero'], 'fashion', 180)}</div>
  <div style="position:absolute;left:120px;top:690px">{arrow_svg(b['ink'], 150, 140)}</div>
  <div class="box" style="left:300px;top:720px;width:710px;height:440px;padding:40px 46px">
    <div style="font-size:30px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    # 3 RULE 1 (4-5 kleuren)
    tags = c["rule1_tags"]
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:420px;padding:44px 50px">
    <h2 data-fit style="font-size:62px;max-height:150px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:22px">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:660px;height:440px">
    <div class="card" style="top:0;height:360px;transform:translate(60px,-70px) scale(.92);opacity:.5"></div>
    <div class="card" style="top:0;height:360px;transform:translate(30px,-36px) scale(.96);opacity:.75"></div>
    <div class="card" style="top:0;height:400px;display:flex;align-items:center;justify-content:space-around;padding:30px 40px">
      <div style="text-align:center">{balloon(SX['rosewood']['hex'],'fashion',190)}<div class="pname" style="font-size:24px;margin-top:14px;font-weight:{b['body_b']}">1 {esc(tags[0])}</div></div>
      <div style="text-align:center;display:flex;flex-direction:column;align-items:center"><div style="display:flex;gap:12px">{balloon(SX['eucalyptus']['hex'],'fashion',104)}{balloon(SX['greentea']['hex'],'matte',104)}{balloon(SX['duskrose']['hex'],'matte',104)}</div><div class="pname" style="font-size:24px;margin-top:14px;font-weight:{b['body_b']}">2 à 3 {esc(tags[1])}</div></div>
      <div style="text-align:center">{balloon(SX['golddust']['hex'],'silk',120)}<div class="pname" style="font-size:24px;margin-top:14px;font-weight:{b['body_b']}">1 {esc(tags[2])}</div></div>
    </div>
  </div>
  {s1_footer(b)}
</section>""")
    # 4 RULE 2 (textuur)
    tex = "".join(f'<div style="text-align:center">{balloon(hx, t, 150)}<div class="pname" style="font-size:24px;margin-top:14px;font-weight:{b["body_b"]}">{esc(n)}</div></div>' for n, hx, t in TEXTURE_DEMO)
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule2_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:440px;padding:44px 50px">
    <h2 data-fit style="font-size:58px;max-height:200px">{esc(c['rule2_title'])}</h2>
    <div class="body" style="margin-top:22px">{esc(c['rule2_body'])}</div>
  </div>
  <div class="stack" style="top:680px;height:420px">
    <div class="card" style="top:0;height:340px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:380px;display:flex;align-items:center;justify-content:space-around;padding:30px 30px">{tex}</div>
  </div>
  {s1_footer(b)}
</section>""")
    # 5 EXAMPLE palette with cursor pills
    roles = c["roles"]
    keys = PALETTES["meadow"]["keys"]
    cols = [b['c1'], b['c2'], b['c2'], b['c3']]; colt = [b['c1t'], b['c2t'], b['c2t'], b['c3t']]
    items = ""
    for i, k in enumerate(keys):
        sx = SX[k]
        nm = sx["name"].replace("Fashion ", "").replace("Pastel Dusk ", "P. Dusk ")
        items += (f'<div style="text-align:center;position:relative;width:200px">{balloon(sx["hex"], sx["tex"], 150)}'
                  f'<div class="pname" style="font-size:22px;margin-top:12px;font-weight:{b["body_b"]}">{esc(nm)}<br><span style="opacity:.65">{sx["code"]}</span></div>'
                  f'<div class="pill" style="background:{cols[i]};color:{colt[i]};left:{[70,110,60,110][i]}px;top:{[-46,-52,-46,-52][i]}px;font-size:22px;padding:8px 18px;transform:rotate({[-5,4,-3,5][i]}deg)">{cursor_svg(cols[i])}{esc(roles[i])}</div></div>')
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:500px;padding:50px 40px 40px">
    <h2 style="font-size:54px;margin-bottom:90px;text-align:center">{esc(c['example_title'])}</h2>
    <div style="display:flex;justify-content:space-between;padding:0 10px">{items}</div>
  </div>
  <div class="box" style="left:70px;top:720px;width:940px;padding:44px 50px"><div class="body" style="font-size:33px">{esc(c['example_body'])}</div></div>
  {s1_footer(b)}
</section>""")
    # 6 CLIENT chat + stacked palettes
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:56px;max-height:140px">{esc(c['client_title'])}</h2>
  <div class="chat" style="top:300px;height:170px">{esc(c['client_question'])}<div class="send">↑</div></div>
  <div class="stack" style="top:500px;height:380px">
    <div class="card" style="top:0;left:0;right:auto;width:470px">{mini_palette(c['palette2'], 72)}</div>
    <div class="card" style="top:150px;left:430px;right:auto;width:470px">{mini_palette('meadow', 72)}</div>
  </div>
  <div style="position:absolute;left:80px;right:80px;top:930px" class="body">{esc(c['client_body'])}</div>
  {s1_footer(b)}
</section>""")
    # 7 CTA
    S.append(f"""
<section class="slide s1">
  <h1 data-fit style="position:absolute;left:80px;right:80px;top:200px;max-height:420px;font-size:88px;text-align:center">{esc(c['cta_title'])}</h1>
  <div style="position:absolute;left:120px;right:120px;top:650px;font-size:30px;line-height:1.4;text-align:center">{esc(c['cta_sub'])}</div>
  <div style="position:absolute;left:0;right:0;top:800px;text-align:center"><span class="url">{esc(c['cta_url'])}</span></div>
  <div style="position:absolute;left:200px;top:745px">{arrow_svg(b['ink'], 130, 120)}</div>
  <div style="position:absolute;left:0;right:0;top:980px;display:flex;justify-content:center;align-items:center;gap:40px">{logo_img(b, height=b['cta_logo_h'])}<span style="font-size:40px;opacity:.5">×</span><img src="file://{STX_FULL}" style="height:96px"></div>
</section>""")
    return S

# ================================================================ STIJL 2: STUDIO DARK (dotted)
def css_s2(b):
    return f"""
.s2{{background-color:{b['dark']};background-image:radial-gradient(rgba(255,255,255,.13) 2.2px, transparent 2.6px);background-size:30px 30px;color:#fff;font-family:'{b['body']}',sans-serif}}
.s2 h1,.s2 h2{{font-family:'{b['head']}',sans-serif;font-weight:{b['head_w']};letter-spacing:-0.02em;line-height:1.06;margin:0;color:#fff}}
.s2 .label{{position:absolute;left:70px;right:70px;font-size:26px;letter-spacing:.14em;text-transform:uppercase;font-weight:{b['body_b']};padding-bottom:14px;border-bottom:6px solid #fff}}
.s2 .body{{font-size:31px;line-height:1.4;color:#fff}}
.s2 .body b{{font-weight:{b['body_b']}}}
.s2 .frame{{position:absolute;background:#fff;padding:16px;box-shadow:0 18px 50px rgba(0,0,0,.45);border-radius:6px}}
.s2 .frame .ph{{background:{b['tint']};border-radius:4px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:14px}}
.s2 .sq{{position:absolute;background:#fff;border-radius:10px;display:flex;align-items:center;justify-content:center;padding:18px}}
.s2 .tagw{{position:absolute;background:#fff;color:{b['ink']};border-radius:14px;padding:14px 26px;font-size:30px;font-weight:{b['body_b']};display:flex;align-items:center;gap:12px;box-shadow:0 10px 30px rgba(0,0,0,.35)}}
.s2 .tagw .ast{{color:{b['c2']};font-size:34px;line-height:1}}
.s2 .footer{{position:absolute;left:70px;right:70px;bottom:50px;display:flex;align-items:center;justify-content:space-between}}
.s2 .footer .stx{{display:flex;align-items:center;gap:14px;font-size:22px;font-weight:{b['body_b']};color:#fff}}
.s2 .logocard{{background:#fff;border-radius:12px;padding:12px 18px;display:inline-flex;align-items:center}}
.s2 .conn{{position:absolute;border-left:3px solid #fff;border-bottom:3px solid #fff}}
.s2 .step{{display:flex;gap:18px;align-items:flex-start;font-size:31px;line-height:1.32;margin-top:18px}}
.s2 .step b{{font-family:'{b['ui']}';font-weight:{b['head_w']};min-width:44px;color:{b['pill_dark_text']}}}
.s2 .pname{{color:{b['ink']};font-weight:{b['body_b']}}}
.s2 .pcode{{opacity:.6;font-weight:400}}
.s2 .pcode-only{{color:{b['ink']};font-size:18px;font-weight:{b['body_b']};text-align:center;margin-top:6px}}
.s2 .mini-name{{color:{b['ink']};font-weight:{b['body_b']};font-size:24px;margin-bottom:12px}}
.s2 .url{{display:inline-block;background:#fff;color:{b['ink']};border-radius:999px;padding:24px 50px;font-size:42px;font-weight:{b['body_b']};font-family:'{b['ui']}'}}
.s2 .sx{{background:#6b3fb9;color:#fff;border-radius:.22em;padding:0 .16em .04em;line-height:1;display:inline-block}}
"""

def s2_footer(b):
    return (f'<div class="footer">{logo_img(b, on_dark=True, height=b["footer_h"]-6)}'
            f'<img src="file://{STX_WT}" style="height:62px"></div>')

def s2_slides(b, c):
    S = []
    keys = PALETTES["meadow"]["keys"]
    # 1 COVER: klein logo-vierkant linksboven, connector naar frame, headline rechts, "met Sempertex Europe" onderaan
    S.append(f"""
<section class="slide s2">
  <div class="sq" style="left:70px;top:70px;width:200px;height:120px">{f'<img src="file://{b["logo"]}" style="max-width:170px;max-height:90px">'}</div>
  <div class="conn" style="left:170px;top:190px;width:140px;height:380px"></div>
  <div style="position:absolute;left:300px;top:552px;width:0;height:0;border-left:22px solid #fff;border-top:14px solid transparent;border-bottom:14px solid transparent"></div>
  <h1 data-fit style="position:absolute;left:320px;right:70px;top:70px;max-height:430px;font-size:74px">{hl(c['cover_title'])}</h1>
  <div class="frame" style="left:320px;top:520px;width:690px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:460px">{palette_row(keys, 122, 24, labels=False)}</div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    # 2 METHOD: label, paragraph, two overlapping frames
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px"><b style="font-size:40px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:600px;width:600px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:400px"><div class="prow" style="gap:22px">{balloon(SX['rosewood']['hex'],'fashion',150)}{balloon(SX['eucalyptus']['hex'],'fashion',110)}{balloon(SX['golddust']['hex'],'silk',90)}</div></div>
  </div>
  <div class="frame" style="left:560px;top:760px;width:430px;transform:rotate({rot(b,3)}deg)">
    <div class="ph" style="height:300px">{balloon(SX['golddust']['hex'],'silk',200)}</div>
  </div>
  {s2_footer(b)}
</section>""")
    # 3 RULE 1
    tags = c["rule1_tags"]
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:64px;max-height:160px">{esc(c['rule1_title'])}</h2>
  <div class="frame" style="left:70px;top:350px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:420px;flex-direction:row;justify-content:space-around;padding:0 20px;box-sizing:border-box">
      <div style="text-align:center">{balloon(SX['rosewood']['hex'],'fashion',160)}<div class="pname" style="font-size:22px;margin-top:12px">1 {esc(tags[0])}</div></div>
      <div style="text-align:center;display:flex;flex-direction:column;align-items:center"><div style="display:flex;gap:12px">{balloon(SX['eucalyptus']['hex'],'fashion',90)}{balloon(SX['greentea']['hex'],'matte',90)}{balloon(SX['duskrose']['hex'],'matte',90)}</div><div class="pname" style="font-size:22px;margin-top:12px">2 à 3 {esc(tags[1])}</div></div>
      <div style="text-align:center">{balloon(SX['golddust']['hex'],'silk',110)}<div class="pname" style="font-size:22px;margin-top:12px">1 {esc(tags[2])}</div></div>
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:880px">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    # 4 RULE 2 textures
    tex = "".join(f'<div style="text-align:center">{balloon(hx, t, 150)}<div class="pname" style="font-size:22px;margin-top:12px">{esc(n)}</div></div>' for n, hx, t in TEXTURE_DEMO)
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:60px;max-height:170px">{esc(c['rule2_title'])}</h2>
  <div class="frame" style="left:70px;top:370px;width:940px;transform:rotate({rot(b,1.5)}deg)">
    <div class="ph" style="height:380px;flex-direction:row;justify-content:space-around;padding:0 20px;box-sizing:border-box">{tex}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:880px">{esc(c['rule2_body'])}</div>
  {s2_footer(b)}
</section>""")
    # 5 EXAMPLE
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 style="position:absolute;left:70px;right:70px;top:160px;font-size:64px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:290px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box">{palette_row(keys, 140, 26, labels=True, name_size=21)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:860px">{esc(c['example_body'])}</div>
  {s2_footer(b)}
</section>""")
    # 6 CLIENT: two overlapping frames with mini palettes
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:58px;max-height:150px">{esc(c['client_title'])}</h2>
  <div class="frame" style="left:70px;top:340px;width:620px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:260px;padding:20px;box-sizing:border-box">{mini_palette('meadow', 70)}</div>
  </div>
  <div class="frame" style="left:490px;top:590px;width:520px;transform:rotate({rot(b,2.5)}deg)">
    <div class="ph" style="height:260px;padding:20px;box-sizing:border-box">{mini_palette(c['palette2'], 70)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:880px">{esc(c['client_body'])}</div>
  {s2_footer(b)}
</section>""")
    # 7 CTA
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['cta_label'])}</div>
  <h1 data-fit style="position:absolute;left:70px;right:70px;top:170px;max-height:380px;font-size:80px">{esc(c['cta_title'])}</h1>
  <div class="frame" style="left:160px;top:600px;width:760px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:260px;background:#fff"><img src="file://{b['logo']}" style="max-width:600px;max-height:200px"></div>
  </div>
  <div style="position:absolute;left:0;right:0;top:930px;text-align:center"><span class="url">{esc(c['cta_url'])}</span></div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1060px;text-align:center;font-size:28px">{esc(c['cta_sub'])}</div>
  <div style="position:absolute;left:0;right:0;bottom:50px;text-align:center"><img src="file://{STX_WT}" style="height:80px;display:inline-block"></div>
</section>""")
    return S

# ================================================================ STIJL 3: BOLD (neon)
def css_s3(b):
    return f"""
.s3{{background:{b['bright']};color:{b['bright_text']};font-family:'{b['body']}',sans-serif}}
.s3 h1,.s3 h2{{font-family:'{b['head']}',sans-serif;font-weight:{heavy(b['head'])};letter-spacing:-0.025em;line-height:1.0;margin:0}}
.s3 .hl{{display:inline-block;background:{b['pill_dark']};color:{b['pill_dark_text']};border-radius:22px;padding:4px 26px 10px;line-height:1.05}}
.s3 .lblw{{position:absolute;background:#fff;color:{b['bright_text']};border-radius:14px;padding:10px 22px;font-size:30px;font-weight:900;font-family:'{b['ui']}';letter-spacing:.02em;box-shadow:0 8px 0 rgba(0,0,0,.18)}}
.s3 .lbld{{position:absolute;background:{b['pill_dark']};color:{b['pill_dark_text']};border-radius:14px;padding:10px 22px;font-size:30px;font-weight:900;font-family:'{b['ui']}';letter-spacing:.02em;box-shadow:0 8px 0 rgba(0,0,0,.18)}}
.s3 .meta{{display:inline-flex;align-items:center;gap:8px;background:{b['pill_dark']};color:#fff;border-radius:8px;padding:6px 14px;font-size:22px;font-weight:700;margin-top:10px}}
.s3 .vsmark{{position:absolute;left:0;right:0;top:420px;text-align:center;font-family:'{b['ui']}';font-weight:900;font-size:620px;line-height:1;color:rgba(0,0,0,.07);letter-spacing:-.05em}}
.s3 .vsbadge{{position:absolute;width:110px;height:110px;border-radius:50%;background:{b['pill_dark']};color:{b['pill_dark_text']};display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:900;font-family:'{b['ui']}';border:6px solid #fff;box-shadow:0 8px 20px rgba(0,0,0,.2)}}
.s3 .cardw{{position:absolute;background:#fff;border-radius:40px;padding:40px 44px;box-sizing:border-box;color:{b['bright_text']};box-shadow:0 10px 0 rgba(0,0,0,.12)}}
.s3 .cardd{{position:absolute;background:{b['pill_dark']};border-radius:40px;padding:40px 44px;box-sizing:border-box;color:#fff;box-shadow:0 10px 0 rgba(0,0,0,.2)}}
.s3 .chip{{display:inline-block;border-radius:14px;padding:12px 26px;font-size:30px;font-weight:800;font-family:'{b['ui']}';margin:0 8px}}
.s3 .chipd{{background:{b['pill_dark']};color:#fff}}
.s3 .chipb{{background:transparent;color:{b['pill_dark_text']};border:4px solid {b['pill_dark_text']}}}
.s3 .plus{{font-size:36px;font-weight:900;margin:0 6px;vertical-align:middle}}
.s3 .strike{{color:#E03131;text-decoration:line-through;text-decoration-thickness:4px;font-size:30px;line-height:1.3;margin-top:22px}}
.s3 .quote{{font-size:30px;line-height:1.3;margin-top:22px;color:#fff;font-weight:600}}
.s3 .badge{{display:inline-flex;align-items:center;gap:10px;background:rgba(0,0,0,.35);color:#fff;border-radius:8px;padding:6px 16px;font-size:22px;font-weight:700;margin-top:18px}}
.s3 .pilltitle{{position:absolute;z-index:5;left:50%;transform:translateX(-50%);background:{b['pill_dark']};color:{b['pill_dark_text']};border-radius:14px;padding:8px 26px;font-size:28px;font-weight:900;font-family:'{b['ui']}';letter-spacing:.04em;white-space:nowrap;box-shadow:0 6px 0 rgba(0,0,0,.15)}}
.s3 .onwhite .mini-name,.s3 .onwhite .pcode-only{{color:{b['bright_text']}}}
.s3 .downarrow{{position:absolute;left:50%;transform:translateX(-50%);width:70px;height:70px;border-radius:50%;background:{b['pill_dark']};color:#fff;display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:900}}
.s3 .bottom{{position:absolute;left:70px;right:70px;text-align:center;font-size:34px;font-weight:800;font-family:'{b['ui']}';line-height:1.25;white-space:pre-line}}
.s3 .topic{{position:absolute;left:50%;transform:translateX(-50%);max-width:960px;box-sizing:border-box;background:#fff;border-radius:20px;padding:8px 10px 8px 8px;display:flex;align-items:center;gap:18px;box-shadow:0 8px 0 rgba(0,0,0,.12)}}
.s3 .topic .k{{background:{b['pill_dark']};color:{b['pill_dark_text']};border-radius:14px;padding:12px 22px;font-size:24px;font-weight:900;letter-spacing:.1em;font-family:'{b['ui']}';white-space:nowrap}}
.s3 .topic .v{{font-size:44px;font-weight:900;font-family:'{b['ui']}';padding-right:20px;white-space:nowrap;overflow:hidden;text-overflow:clip;min-width:0}}
.s3 .oldlbl{{display:inline-block;background:#fff;color:{b['bright_text']};border-radius:999px;padding:8px 20px;font-size:22px;font-weight:900;font-family:'{b['ui']}';letter-spacing:.06em}}
.s3 .newlbl{{display:inline-block;background:{b['pill_dark']};color:{b['pill_dark_text']};border-radius:999px;padding:8px 20px;font-size:22px;font-weight:900;font-family:'{b['ui']}';letter-spacing:.06em}}
.s3 img.bl{{filter:drop-shadow(3px 0 0 #fff) drop-shadow(-3px 0 0 #fff) drop-shadow(0 3px 0 #fff) drop-shadow(0 -3px 0 #fff) drop-shadow(0 10px 12px rgba(0,0,0,.18))}}
.s3 div.bl{{box-shadow:0 0 0 8px #fff}}
.s3 div.bl i{{display:none}}
.s3 .footer{{position:absolute;left:70px;right:70px;bottom:44px;display:flex;align-items:center;justify-content:space-between}}
.s3 .logocard{{background:#fff;border-radius:16px;padding:12px 20px;display:inline-flex;align-items:center;box-shadow:0 6px 0 rgba(0,0,0,.12)}}
.s3 .pname{{font-weight:800;color:{b['bright_text']}}}
.s3 .pcode{{opacity:.6;font-weight:600}}
.s3 .pcode-only{{color:#fff;font-size:18px;font-weight:800;text-align:center;margin-top:8px}}
.s3 .mini-name{{color:#fff;font-weight:800;font-size:22px;margin-bottom:10px}}
.s3 .url{{display:inline-block;background:{b['pill_dark']};color:#fff;border-radius:999px;padding:24px 50px;font-size:42px;font-weight:900;font-family:'{b['ui']}'}}
.s3 .sx{{background:#6b3fb9;color:#fff;border-radius:22px;padding:4px 26px 10px;line-height:1.05;display:inline-block}}
"""

def s3_footer(b, stx_h=52):
    return (f'<div class="footer">{logo_img(b, card=True, height=b["footer_h"]-12)}'
            f'<div class="logocard"><img src="file://{STX_FULL}" style="height:{stx_h}px"></div></div>')

def messy_cluster():
    # 8 ballonnen rommelig
    pos = [(0,40,96),(80,0,110),(170,50,90),(30,140,100),(130,120,120),(230,140,86),(70,240,104),(180,230,96)]
    out = '<div style="position:relative;width:330px;height:360px">'
    for (x,y,s), col in zip(pos, MESSY):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px">{balloon(col,"fashion",s)}</div>'
    return out + '</div>'

def clean_cluster():
    keys = PALETTES["meadow"]["keys"]
    pos = [(70,20,170),(0,170,110),(190,180,110),(100,260,96)]
    out = '<div style="position:relative;width:330px;height:360px">'
    for (x,y,s), k in zip(pos, keys):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px">{balloon(SX[k]["hex"],SX[k]["tex"],s)}</div>'
    return out + '</div>'

def s3_slides(b, c):
    S = []
    keys = PALETTES["meadow"]["keys"]
    # 1 COVER: old vs new
    S.append(f"""
<section class="slide s3">
  <h1 data-fit style="position:absolute;left:50px;right:50px;top:60px;max-height:400px;font-size:88px;text-align:center;line-height:1.08">{hl(c['s3_cover_a'])} {esc(c['s3_cover_b'])} {esc(c['s3_cover_c'])}<br><span class="hl">{esc(c['s3_cover_d'])}</span></h1>
  <div class="vsmark" style="top:520px">VS</div>
  <div class="lblw" style="left:110px;top:500px;transform:rotate({rot(b,-4)}deg)">{esc(c['s3_left'])}<br><span class="meta">● {esc(c['s3_left_meta'])}</span></div>
  <div class="lbld" style="right:110px;top:500px;transform:rotate({rot(b,4)}deg)">{esc(c['s3_right'])}<br><span class="meta" style="background:rgba(255,255,255,.18)">● {esc(c['s3_right_meta'])}</span></div>
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{messy_cluster()}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{clean_cluster()}</div>
  <div class="vsbadge" style="left:485px;top:850px">vs</div>
  {s3_footer(b, stx_h=60)}
</section>""")
    # 2 WHAT CHANGED
    old_tags = "".join(f'<span class="chip chipd">{esc(t)}</span>' + ('<span class="plus">+</span>' if i < len(c["s3_old_tags"])-1 else '') for i, t in enumerate(c["s3_old_tags"]))
    new_tags = "".join(f'<span class="chip chipb">{esc(t)}</span>' + ('<span class="plus" style="color:#fff">+</span>' if i < len(c["s3_new_tags"])-1 else '') for i, t in enumerate(c["s3_new_tags"]))
    S.append(f"""
<section class="slide s3">
  <h1 data-fit style="position:absolute;left:60px;right:60px;top:80px;max-height:130px;font-size:92px;text-align:center">{esc(c['s3_changed_title'])}</h1>
  <div class="pilltitle" style="top:232px">{esc(c['s3_old_lbl'])}</div>
  <div class="cardw" style="left:70px;right:70px;top:260px;height:300px;text-align:center;display:flex;flex-direction:column;justify-content:center;align-items:center">
    <div>{old_tags}</div>
    <div class="strike" style="font-size:34px">{esc(c['s3_old_quote'])}</div>
  </div>
  <div class="downarrow" style="top:590px">↓</div>
  <div class="pilltitle" style="top:692px;background:#fff;color:{b['bright_text']}">{esc(c['s3_new_lbl'])}</div>
  <div class="cardd" style="left:70px;right:70px;top:720px;height:370px;text-align:center;display:flex;flex-direction:column;justify-content:center;align-items:center">
    <div>{new_tags}</div>
    <div class="quote" style="font-size:32px">{esc(c['s3_new_quote'])}</div>
    <div class="badge">◉ {esc(c['s3_new_badge'])}</div>
  </div>
  <div class="bottom" style="top:1125px">{esc(c['s3_changed_bottom'])}</div>
  {s3_footer(b)}
</section>""")
    # helper: topic slide with OLD (dark, strikethrough) vs NEW (white, visual)
    def topic_slide(topic, old_text, new_visual, quote, label=None):
        label = label or c['s3_topic_lbl']
        old_meta = " + ".join(c['s3_old_tags'])
        return f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(label)}</span><span class="v">{esc(topic)}</span></div>
  <div class="cardd" style="left:70px;top:230px;width:440px;height:600px;padding:34px 36px">
    <span class="oldlbl">{esc(c['s3_old_lbl'])}</span>
    <div class="strike" style="font-size:42px;line-height:1.2;color:#fff;text-decoration-color:#E03131;margin-top:34px;font-weight:700;font-family:'{b['ui']}'">{esc(old_text)}</div>
    <div style="position:absolute;left:36px;right:36px;bottom:34px;font-size:22px;opacity:.55;font-weight:600">{esc(old_meta)}</div>
  </div>
  <div class="cardw onwhite" style="left:570px;top:230px;width:440px;height:600px;padding:34px 36px">
    <span class="newlbl">{esc(c['s3_new_lbl'])}</span>
    <div style="margin-top:30px;display:flex;justify-content:center">{new_visual}</div>
  </div>
  <div class="bottom" style="top:890px;font-size:34px;font-weight:700">{esc(quote)}</div>
  {s3_footer(b)}
</section>"""
    # 3 RULE 1
    vis1 = (f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px">{balloon(SX["rosewood"]["hex"],"fashion",118)}'
            f'<div style="display:flex;gap:18px">{balloon(SX["eucalyptus"]["hex"],"fashion",72)}{balloon(SX["greentea"]["hex"],"matte",72)}{balloon(SX["duskrose"]["hex"],"matte",72)}</div>'
            f'{balloon(SX["golddust"]["hex"],"silk",82)}</div>')
    S.append(topic_slide(c["s3_rule1_topic"], c["s3_rule1_old"], vis1, c["s3_rule1_quote"]))
    # 4 RULE 2
    vis2 = (f'<div style="display:flex;flex-direction:column;align-items:center;gap:18px"><div style="display:flex;gap:22px">{balloon("#F3C6D3","matte",100)}{balloon("#B9D6EC","matte",100)}</div>'
            f'<div style="display:flex;gap:22px">{balloon("#E8DFD0","matte",100)}{balloon(SX["reflexgold"]["hex"],"reflex",100)}</div>'
            f'<div class="pname" style="font-size:22px;text-align:center">Pastel Matte + 1 Reflex</div></div>')
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    # 5 EXAMPLE: full white card
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v">{esc(c['example_title'])}</span></div>
  <div class="cardw" style="left:70px;right:70px;top:230px;height:620px;padding:50px 30px;display:flex;align-items:center;justify-content:center">
    {palette_row(keys, 160, 20, labels=True, name_size=22)}
  </div>
  <div class="bottom" style="top:910px;font-size:34px;font-weight:700">{esc(c['s3_example_quote'])}</div>
  {s3_footer(b)}
</section>""")
    # 6 CLIENT
    vis6 = f'<div style="display:flex;flex-direction:column;gap:34px;align-items:center">{mini_palette("meadow", 64)}{mini_palette(c["palette2"], 64)}</div>'
    S.append(topic_slide(c["s3_client_topic"], c["s3_client_old"], vis6, c["s3_client_quote"], label=c["s3_client_lbl"]))
    # 7 CTA
    S.append(f"""
<section class="slide s3">
  <div class="pilltitle" style="top:90px">{esc(c['s3_cta_kicker'])}</div>
  <h1 data-fit style="position:absolute;left:60px;right:60px;top:180px;max-height:420px;font-size:88px;text-align:center">{esc(c['cta_title'])}</h1>
  <div class="cardw" style="left:160px;right:160px;top:640px;height:240px;display:flex;align-items:center;justify-content:center"><img src="file://{b['logo']}" style="max-width:560px;max-height:170px"></div>
  <div style="position:absolute;left:0;right:0;top:930px;text-align:center"><span class="url">{esc(c['cta_url'])}</span></div>
  <div class="bottom" style="top:1060px;font-size:26px;font-weight:600">{esc(c['cta_sub'])}</div>
  <div style="position:absolute;left:0;right:0;bottom:44px;text-align:center"><span class="logocard"><img src="file://{STX_FULL}" style="height:64px"></span></div>
</section>""")
    return S

# ================================================================ PAGE
BASE_CSS = f"""
*{{box-sizing:border-box}}
body{{margin:0;background:#888}}
.slide{{position:relative;width:{W}px;height:{H}px;overflow:hidden;margin:0 0 40px 0}}
div.bl{{position:relative;border-radius:50% 50% 50% 50% / 46% 46% 54% 54%;flex-shrink:0;box-shadow:inset -6px -10px 18px rgba(0,0,0,.08)}}
div.bl i{{position:absolute;left:50%;bottom:-9px;transform:translateX(-50%);width:0;height:0;border-left:9px solid transparent;border-right:9px solid transparent;border-top:12px solid}}
img.bl{{display:block;flex-shrink:0;object-fit:contain;filter:drop-shadow(0 10px 14px rgba(0,0,0,.14))}}
.prow{{display:flex;align-items:flex-end;justify-content:center;flex-wrap:nowrap}}
.pitem{{display:flex;flex-direction:column;align-items:center}}
.pname{{margin-top:12px;text-align:center;line-height:1.15}}
.pcode{{opacity:.6}}
.mini{{display:flex;flex-direction:column;align-items:flex-start}}
.mini-name{{font-size:26px;font-weight:700;margin-bottom:12px}}
.pcode-only{{font-size:19px;font-weight:700;text-align:center;margin-top:6px;opacity:.75}}
h1,h2{{overflow-wrap:normal;word-break:normal;hyphens:manual}}
img{{display:block}}
"""

FIT_JS = """
document.querySelectorAll('[data-fit]').forEach(el=>{
  let fs = parseFloat(getComputedStyle(el).fontSize);
  const maxH = parseFloat(getComputedStyle(el).maxHeight) || Infinity;
  let guard = 0;
  while ((el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > maxH + 1) && fs > 24 && guard < 80) {
    fs -= 2; el.style.fontSize = fs + 'px'; guard++;
  }
});
"""

def build_html(bkey, style):
    b = BRANDS[bkey]; c = make_copy(bkey); b["body_b"] = body_bold(b["body"])
    css = {1: css_s1, 2: css_s2, 3: css_s3}[style](b)
    slides = {1: s1_slides, 2: s2_slides, 3: s3_slides}[style](b, c)
    fams = [b["head"], b["body"]] if b["head"] != b["body"] else [b["head"]]
    return f"""<!doctype html><html lang="{b['lang']}"><head><meta charset="utf-8"><title>{b['name']} stijl {style}</title>
<style>{font_faces(*fams)}{BASE_CSS}{css}</style></head><body>
{''.join(slides)}
<script>{FIT_JS}</script></body></html>"""

# ---------------------------------------------------------------- TOPIC (andere blog = andere copy + slide-templates)
assign_palettes(TOPIC)
if TOPIC != "colours":
    import importlib
    _t = importlib.import_module(f"topic_{TOPIC}")
    _t.setup(globals())
    BASE_COPY = _t.BASE; VARIANTS = _t.VARIANTS; CAPTIONS_TPL = _t.CAPTIONS_TPL
    s1_slides, s2_slides, s3_slides = _t.s1_slides, _t.s2_slides, _t.s3_slides
    BASE_CSS = BASE_CSS + getattr(_t, "EXTRA_CSS", "")

def main():
    os.makedirs(OUT, exist_ok=True)
    jobs = []
    only = [a.split("=",1)[1] for a in sys.argv if a.startswith("--brands=")]
    keys = only[0].split(",") if only else sorted(BRANDS)
    st = [a.split("=",1)[1] for a in sys.argv if a.startswith("--styles=")]
    styles = tuple(int(x) for x in st[0].split(",")) if st else (1, 2, 3)
    for bkey in keys:
        for style in styles:
            path = f"{OUT}/{bkey}_stijl{style}.html"
            with open(path, "w", encoding="utf-8") as f:
                f.write(build_html(bkey, style))
            jobs.append((bkey, style, path))
    print("HTML klaar:", len(jobs))
    return jobs

if __name__ == "__main__":
    jobs = main()
    if "--render" in sys.argv:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            br = p.chromium.launch()
            pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
            for bkey, style, path in jobs:
                only = [a for a in sys.argv if a.startswith("--only=")]
                if only and f"{bkey}_stijl{style}" not in only[0]: continue
                pg.goto("file://" + path)
                pg.wait_for_timeout(400)
                pg.evaluate("document.fonts.ready.then(()=>1)")
                pg.wait_for_timeout(200)
                pg.evaluate(FIT_JS)
                d = f"{OUT}/{bkey}_stijl{style}"
                os.makedirs(d, exist_ok=True)
                slides = pg.query_selector_all(".slide")
                for i, s in enumerate(slides, 1):
                    s.screenshot(path=f"{d}/slide-{i:02d}.png")
                print("render:", bkey, style, len(slides))
            br.close()
