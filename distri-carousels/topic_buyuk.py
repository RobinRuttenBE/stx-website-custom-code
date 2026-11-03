# -*- coding: utf-8 -*-
"""Topic: 'Where do you buy Sempertex balloons in the UK? The official sales points'
(sempertexeurope.com/en_GB/blog/where-to-buy-sempertex-balloons-uk). Alleen voor de 14 UK-distri's (Engels).
Uit de blog: Sempertex Europe verkoopt in de UK uitsluitend via officiële wholesale partners, de webshop verzendt niet
naar de UK; stockists per regio (Schotland, Noord-, Centraal/Zuidoost-, Zuid-Engeland, Tiger Feet met 7 vestigingen);
B2B + B2C waar aangegeven; 3 redenen (je weet wat je krijgt, stock rechtstreeks uit de officiële keten, vers en goed
bewaard, ze kennen het gamma); STX Family Tree om te checken wie officieel is; stockist worden via de distributor page.
Elke carousel is distri-specifiek: eigen naam, stad, regio en B2B/B2C in de copy; de regiokaart markeert de distri zelf."""

G = {}
def setup(g): G.update(g)

# ---------------------------------------------------------------- UK-DISTRI'S (uit de blog)
UK = {
    "balloons4u":             {"blog": "Balloons4U", "city": "Glasgow", "region": "Scotland", "b2c": True},
    "bodieswholesaleballoons":{"blog": "Bodie's Wholesale Balloons", "city": "Glasgow", "region": "Scotland", "b2c": True},
    "hiflyers":               {"blog": "Hi Flyers", "city": "Glasgow", "region": "Scotland", "b2c": True},
    "mgcwholesale":           {"blog": "MGC Wholesale", "city": "Liverpool", "region": "North England", "b2c": True},
    "northwestgreetings":     {"blog": "Northwest Greetings", "city": "Haydock", "region": "North England", "b2c": False},
    "gointernational":        {"blog": "Go International", "city": "Stevenage", "region": "Central and Southeast England", "b2c": True},
    "proballoonshop":         {"blog": "Pro Balloon Shop", "city": "Buckinghamshire", "region": "Central and Southeast England", "b2c": True},
    "crossweartradingltd":    {"blog": "Crosswear Trading", "city": "Enfield", "region": "Central and Southeast England", "b2c": False},
    "dattaswholesale":        {"blog": "Datta's Wholesale", "city": "Bromley", "region": "Central and Southeast England", "b2c": False},
    "cutpricewholesaler":     {"blog": "Cut Price Wholesaler", "city": "Edenbridge", "region": "Central and Southeast England", "b2c": True},
    "upupandaway":            {"blog": "Up Up & Away", "city": "Basildon", "region": "Central and Southeast England", "b2c": True},
    "bubblegumdirect":        {"blog": "Bubblegum Direct", "city": "Farnborough", "region": "Central and Southeast England", "b2c": False},
    "balloonmarket":          {"blog": "Balloon Market", "city": "Southampton", "region": "South England", "b2c": False},
    "tigerfeet":              {"blog": "Tiger Feet", "city": "7 branches", "region": "Multiple locations", "b2c": True,
                               "branches": "Belfast, Birmingham, Bradford, Bristol, Gateshead, Manchester and Nottingham"},
}
REGIONS = ["Scotland", "North England", "Central and Southeast England", "South England", "Multiple locations"]
UK_KEYS = list(UK)

# ---------------------------------------------------------------- COPY (alleen EN)
BASE = {
"en": {
    "cover_pills": ["Official stockist…", "{city}…", "Fresh stock…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "UK stockists…",
    "steps_title": "Sempertex Europe doesn't sell direct in the UK. The official stockists do.", "steps_lead": "How it works in the UK:",
    "steps": ["UK sales go only through official UK wholesale partners", "The webshop doesn't ship to the UK: partners stock the range locally", "Professionals buy wholesale; B2B + B2C stockists also sell to individuals", "Who's official? Check the STX Family Tree on sempertexeurope.com"],
    "steps_label": "The basics",
    "rule1_label": "Why official", "rule1_title": "3 reasons to buy from an official stockist",
    "rule1_body": "You know exactly what you're getting. The stock comes straight from the official Sempertex chain, so it arrives fresh and properly stored. And an official stockist knows the range through and through: every colour, texture and size, and what works for your build.",
    "rule1_facts": [["official", "stock straight from the Sempertex chain"], ["fresh", "properly stored, as it should be"], ["the full range", "every colour, texture and size"], ["local", "faster delivery, no import hassle"]],
    "rule2_label": "Where", "rule2_title": "Official Sempertex stockists in the UK, Glasgow to Kent",
    "rule2_body": "Grouped by region. Stockists marked B2B + B2C also sell to individuals.",
    "you_lbl": "that's us", "b2c_lbl": "B2B + B2C", "b2b_lbl": "B2B",
    "example_label": "In stock", "example_title": "The Sempertex range, on the shelf at {name}",
    "example_body": "Fashion, Pastel Matte, Pastel Dusk, Silk, Reflex, Metallic, Neon and Crystal. Four from the shelf: {p0}, {p1}, {p2} and {p3}. Same codes as the Sempertex catalogue, so what you plan is what you order.",
    "lines": [["Fashion", "solid, the workhorse"], ["Pastel Matte", "soft, no shine"], ["Pastel Dusk", "muted, dusty tones"], ["Silk", "satin sheen"], ["Reflex", "mirror finish"], ["Metallic", "classic metallic"], ["Neon", "bright, high-energy"], ["Crystal", "transparent, for double stuffing"]],
    "client_label": "Client chat", "client_title": "What you answer when a customer asks",
    "client_answers": [
        "No. Sempertex Europe sells in the UK through official wholesale partners only, and the webshop doesn't ship here. We stock the range locally, so you get it faster and without import hassle.",
        "Only an official stockist gets stock straight from the Sempertex chain, fresh and properly stored. Check the STX Family Tree on sempertexeurope.com: if a seller isn't on it, they're not official.",
        "{b2c_answer}",
    ],
    "b2c_yes": "Yes. We're marked B2B + B2C on the official list, so we sell to individuals as well as trade. Same range, same codes.",
    "b2c_no": "We're a trade stockist. For individuals, the official UK list marks the stockists that also sell B2C: check the STX Family Tree on sempertexeurope.com.",
    "avoid_lead": "How to check a stockist is official:",
    "steps5": ["Look them up in the STX Family Tree on sempertexeurope.com", "Their stock comes from the official Sempertex chain", "They know the full range, by name and code", "They hold stock locally: fast delivery, no import", "Want to become a stockist? Apply via the distributor page"],
    "client_body": "Sempertex Europe opens wholesale partnerships country by country in Europe and the UK. Apply via the distributor page, have a conversation, and see whether it fits.",
    "cta_label": "Order",
    "s3_cover_a": "Buying Sempertex in the UK", "s3_cover_b": "any seller", "s3_cover_c": "vs.", "s3_cover_d": "official stockist",
    "s3_left": "ANY SELLER", "s3_right": "OFFICIAL STOCKIST", "s3_left_meta": "no idea where it's been", "s3_right_meta": "straight from the chain",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["Cheapest listing", "Order from Belgium"], "s3_new_tags": ["Family Tree", "Straight from the chain", "Local stock", "Knows the range"],
    "s3_new_quote": "“I buy from an official UK stockist. Fresh stock, every code in the catalogue, and someone who knows the range.”", "s3_new_badge": "{name}, {city}",
    "s3_changed_bottom": "Same balloons, same codes.\nNow you know where they've been.",
    "s3_topic_lbl": "WHY", "s3_rule1_topic": "Official", "s3_rule1_old": "Sempertex is Sempertex, wherever you buy it",
    "s3_rule1_quote": "“Official stock comes straight from the Sempertex chain: fresh, properly stored, and the stockist knows the range.”",
    "s3_rule2_topic": "Where", "s3_rule2_old": "I'll just order from Belgium",
    "s3_rule2_quote": "“The webshop doesn't ship to the UK. Official stockists from Glasgow to Kent hold the range locally.”",
    "s3_example_lbl": "IN STOCK", "s3_example_quote": "“Fashion, Pastel Matte, Pastel Dusk, Silk, Reflex, Metallic, Neon and Crystal. {p0}, {p1}, {p2} and {p3} on the shelf at {name}.”",
    "s3_client_lbl": "CUSTOMER", "s3_client_topic": "Client chat",
    "s3_client_quote": "“Not on the Family Tree? Not official. That's the whole check.”",
    "s3_cta_kicker": "Your official Sempertex stockist in {city}",
    "shelf_lbl": "on the shelf",
},
}

VARIANTS = {
"en": {
  "cover_title": ["Where do you buy Sempertex balloons in the UK? Right here, at {name}", "Sempertex Europe doesn't ship to the UK. {name} in {city} does", "Official Sempertex stockist in {city}: {name}, with the full range in stock"],
  "cover_sub": ["Sempertex Europe sells in the UK through official stockists only, Glasgow to Kent. Why that matters, and where to find us.", "Fresh stock straight from the Sempertex chain, every colour by code, and someone who knows the range. That's what official means."],
  "client_question": ["Can I order directly from Sempertex Europe instead?", "I found Sempertex cheaper on a marketplace. Is it the same?", "I'm not a business. Can I still buy from you?"],
  "s3_old_quote": ["“Sempertex is Sempertex, wherever you buy it”", "“The cheapest listing wins”", "“I'll just order from Belgium”"],
  "s3_client_old": ["“Order from Belgium? Sure, try”", "“A marketplace seller is fine”"],
  "cta_title_tpl": "Order your Sempertex balloons at {name}", "cta_sub_generic": "Official Sempertex stockist in {city}. {trade_line}",
},
}

CAPTIONS_TPL = {
 "en": "Sempertex Europe doesn't sell direct in the UK and the webshop doesn't ship here. UK sales go through official stockists only, and we're one of them. In this carousel: why that matters (fresh stock straight from the Sempertex chain, the full range by code, local delivery), the official UK stockists from Glasgow to Kent, and how to check who's official with the STX Family Tree.\n\nOrder your Sempertex balloons at {domain}.\n\n#sempertex #officialstockist #{tag} #balloons #balloondecor #ukballoons",
}

# ---------------------------------------------------------------- VISUALS
CUR = {"pal": ["rosewood", "eucalyptus", "greentea", "golddust"]}

def fill_pal(b, c):
    key = b.get("key") or next((k for k in UK if G["BRANDS"].get(k) is b), None)
    info = UK.get(key, {"blog": b["name"], "city": "", "region": "", "b2c": True})
    lab = {f"p{i}": G["pal_label"](k, short=False).replace("Fashion ", "").replace("Pastel ", "") for i, k in enumerate(b["pal"][:4])}
    lab.update(name=b["name"], city=info["city"], region=info["region"],
               trade_line="Trade and individuals welcome." if info["b2c"] else "Trade customers only.",
               b2c_answer=c["b2c_yes"] if info["b2c"] else c["b2c_no"])
    def f(v): return v.format(**lab) if isinstance(v, str) and "{" in v else v
    out = {}
    for k, v in c.items():
        if isinstance(v, str): out[k] = f(v)
        elif isinstance(v, list): out[k] = [[f(x) for x in item] if isinstance(item, list) else f(item) for item in v]
        else: out[k] = v
    qs = VARIANTS[b["lang"]]["client_question"]
    qi = qs.index(c["client_question"]) if c["client_question"] in qs else 0
    out["client_answer"] = out["client_answers"][qi]
    out["info"] = info; out["key"] = key
    return out

def _bl(key, size, cls="", extra=""):
    return G["balloon"](key, "fashion", size, extra_style=extra, cls=cls)

def facts_grid(items, cls="facts", num_size=44, lab_size=20):
    esc = G["esc"]
    def fs(n):
        L = len(n); return num_size if L <= 9 else (int(num_size * .72) if L <= 15 else int(num_size * .58))
    cells = "".join(f'<div class="fact"><b style="font-size:{fs(n)}px">{esc(n)}</b><span style="font-size:{lab_size}px">{esc(l)}</span></div>' for n, l in items)
    return f'<div class="{cls}">{cells}</div>'

def region_map(c, cls="regions", font=None, name_size=19, head_size=16, ink="#111", layout="cols"):
    """Alle UK-stockists per regio; de eigen distri gemarkeerd.
    layout='cols': 2 kolommen (links Schotland/Noord/Zuid/Meerdere, rechts Centraal en Zuidoost), naam + tag op 1 lijn, stad eronder.
    layout='list': 1 kolom, alles op 1 lijn (voor de smalle stijl-3 kaart)."""
    esc = G["esc"]; me = c["key"]
    def row(k, i):
        mine = (k == me); city = i["city"] if k != "tigerfeet" else "7 branches"
        tag = c["b2c_lbl"] if i["b2c"] else c["b2b_lbl"]
        you = f'<span class="you">{esc(c["you_lbl"])}</span>' if mine else ""
        if layout == "list":
            return (f'<div class="rrow{" me" if mine else ""}" style="font-size:{name_size}px"><span class="rn">{esc(i["blog"])}</span>'
                    f'<span class="rc">{esc(city)}</span><span class="rt">{esc(tag)}</span>{you}</div>')
        return (f'<div class="rrow{" me" if mine else ""}" style="font-size:{name_size}px"><div class="rl1"><span class="rn">{esc(i["blog"])}</span>{you}<span class="rt">{esc(tag)}</span></div>'
                f'<div class="rc">{esc(city)}</div></div>')
    def region(r):
        rows = "".join(row(k, i) for k, i in UK.items() if i["region"] == r)
        return f'<div class="region"><div class="rh" style="font-size:{head_size}px">{esc(r)}</div>{rows}</div>'
    out = f'<div class="{cls}"' + (f' style="font-family:\'{font}\'"' if font else '') + '>'
    if layout == "list":
        out += "".join(region(r) for r in REGIONS)
    else:
        out += '<div class="rcol">' + "".join(region(r) for r in ["Scotland", "North England", "South England", "Multiple locations"]) + '</div>'
        out += '<div class="rcol">' + region("Central and Southeast England") + '</div>'
    return out + '</div>'

def shelf_row(c, P, size=120, lab=19, ink="#111", gap=26):
    esc = G["esc"]; out = '<div style="display:flex;flex-direction:column;align-items:center;width:100%">'
    out += f'<div style="display:flex;align-items:flex-end;justify-content:center;gap:{gap}px">'
    for k in P[:4]:
        out += (f'<div style="text-align:center"><div class="bag">{_bl(k, size)}</div>'
                f'<div class="pname" style="font-size:{lab}px;margin-top:10px;color:{ink};white-space:nowrap">{esc(G["pal_label"](k))}</div></div>')
    out += '</div>'
    out += f'<div style="width:96%;height:10px;background:{ink};border-radius:4px;margin-top:-4px;opacity:.9"></div>'
    return out + '</div>'

def lines_chips(c, cls="hours"):
    esc = G["esc"]
    return f'<div class="{cls}">' + "".join(f'<span class="hchip"><b>{esc(n)}</b> {esc(d)}</span>' for n, d in c["lines"]) + '</div>'

def avoid_list(c, cls=""):
    esc = G["esc"]
    return ('<div class="' + cls + '">' + "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps5"])) + '</div>')

def any_seller(keys, ink="#111"):
    """'Any seller': ballonnen kriskras met vraagtekens (waar komen ze vandaan?)."""
    w, h = 330, 360
    pos = [(0, 30, 92), (100, 0, 84), (200, 40, 96), (40, 150, 88), (150, 140, 104), (250, 170, 80), (90, 250, 92), (200, 250, 84)]
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    for i, (x, y, s) in enumerate(pos):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px;filter:saturate(.6) brightness(.95)">{_bl(keys[i % len(keys)], s)}</div>'
    for (x, y, r) in ((30, 110, -12), (210, 15, 8), (130, 300, -6)):
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg);background:#fff;color:{ink};border:3px solid {ink};'
                f'border-radius:50%;width:46px;height:46px;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:900;box-shadow:0 4px 0 rgba(0,0,0,.18)">?</div>')
    return out + '</div>'

def official_shelf(keys, c, ink="#111"):
    """'Official stockist': 2 planken met ballonnen + stempel met de distri-naam."""
    esc = G["esc"]
    row = "".join(f'<div class="bag" style="margin:0 2px">{_bl(k, 72)}</div>' for k in keys[:4])
    label = f'{c["info"]["blog"]}, {c["info"]["city"]}'
    fs = 18 if len(label) <= 22 else (15 if len(label) <= 28 else 13)
    return (f'<div style="position:relative;width:330px;height:370px">'
            f'<div style="position:absolute;left:0;top:70px;width:330px;display:flex;align-items:flex-end;justify-content:center">{row}</div>'
            f'<div style="position:absolute;left:10px;top:182px;width:310px;height:10px;background:{ink};border-radius:4px"></div>'
            f'<div style="position:absolute;left:0;top:220px;width:330px;display:flex;align-items:flex-end;justify-content:center">{row}</div>'
            f'<div style="position:absolute;left:10px;top:332px;width:310px;height:10px;background:{ink};border-radius:4px"></div>'
            f'<div style="position:absolute;left:-10px;right:-10px;top:0;transform:rotate(-3deg);background:#fff;color:{ink};border:3px solid {ink};border-radius:10px;padding:8px 10px;font-size:{fs}px;font-weight:900;letter-spacing:.02em;text-align:center;box-shadow:0 4px 0 rgba(0,0,0,.18);white-space:nowrap;overflow:hidden">✓ {esc(label)}</div></div>')

# ---------------------------------------------------------------- STIJL 1
def s1_slides(b, c):
    CUR["pal"] = b["pal"]; c = fill_pal(b, c); P = b["pal"]
    esc, hl, cursor_svg, arrow_svg, balloon = G["esc"], G["hl"], G["cursor_svg"], G["arrow_svg"], G["balloon"]
    s1_footer, logo_img, rot, STX_FULL = G["s1_footer"], G["logo_img"], G["rot"], G["STX_FULL"]
    S = []
    pills = c["cover_pills"]
    S.append(f"""
<section class="slide s1">
  <h1 data-fit style="position:absolute;left:70px;right:70px;top:250px;max-height:560px;font-size:90px;text-align:center;line-height:1.06">{hl(c['cover_title'])}</h1>
  <div class="pill" style="background:{b['c1']};color:{b['c1t']};right:60px;top:130px;transform:rotate({rot(b,-4)}deg)">{cursor_svg(b['c1'])}{esc(pills[0])}</div>
  <div class="pill" style="background:{b['c2']};color:{b['c2t']};right:90px;top:835px;transform:rotate({rot(b,3)}deg)">{cursor_svg(b['c2'])}{esc(pills[1])}</div>
  <div class="pill" style="background:{b['c3']};color:{b['c3t']};left:90px;top:880px;transform:rotate({rot(b,-2)}deg)">{cursor_svg(b['c3'])}{esc(pills[2])}</div>
  <div style="position:absolute;left:150px;top:960px">{arrow_svg(b['ink'], 130, 120)}</div>
  <div style="position:absolute;left:310px;right:90px;top:1020px;font-size:29px;line-height:1.35">{esc(c['cover_sub'])}</div>
  {s1_footer(b, stx_h=84)}
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s1">
  <div class="box" style="left:70px;top:120px;width:800px;height:470px">
    <h2 data-fit style="font-size:72px;max-height:380px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:830px;top:90px;transform:rotate(14deg)">{balloon(b['hero'], 'fashion', 180)}</div>
  <div style="position:absolute;left:120px;top:600px">{arrow_svg(b['ink'], 150, 140)}</div>
  <div class="box" style="left:300px;top:625px;width:710px;height:540px;padding:34px 46px">
    <div style="font-size:30px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:440px;padding:44px 50px">
    <h2 data-fit style="font-size:58px;max-height:150px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:28px">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:670px;height:430px">
    <div class="card" style="top:0;height:340px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:400px;padding:30px 34px">{facts_grid(c['rule1_facts'])}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:52px;max-height:140px">{esc(c['rule2_title'])}</h2>
  <div style="position:absolute;left:80px;right:80px;top:316px;font-size:24px;line-height:1.35" class="body">{esc(c['rule2_body'])}</div>
  <div style="position:absolute;left:70px;right:70px;top:380px">{region_map(c, "regions big", b['ui'], 24, 17, b['ink'])}</div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:600px;padding:36px 30px 30px">
    <h2 data-fit style="font-size:48px;margin-bottom:26px;text-align:center;max-height:130px">{esc(c['example_title'])}</h2>
    {shelf_row(c, P, 140, 19, b['ink'], 30)}
    <div style="margin-top:26px">{lines_chips(c, 'hours small')}</div>
  </div>
  <div class="box" style="left:70px;top:800px;width:940px;padding:28px 50px"><div class="body" style="font-size:25px">{esc(c['example_body'])}</div></div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:54px;max-height:140px">{esc(c['client_title'])}</h2>
  <div class="chat" style="top:320px;min-height:130px;padding-right:120px">{esc(c['client_question'])}<div class="send">↑</div></div>
  <div style="position:absolute;left:80px;right:80px;top:490px;display:flex;flex-direction:column;gap:18px">
    <div class="card" style="position:relative;left:auto;right:auto;padding:24px 36px"><div style="font-size:27px;line-height:1.35">{esc(c['client_answer'])}</div></div>
    <div class="card" style="position:relative;left:auto;right:auto;padding:20px 36px"><div style="font-size:24px;font-weight:{b['body_b']};margin-bottom:2px">{esc(c['avoid_lead'])}</div>{avoid_list(c, 'avoid')}</div>
    <div class="body" style="font-size:22px;line-height:1.35">{esc(c['client_body'])}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <h1 data-fit style="position:absolute;left:80px;right:80px;top:200px;max-height:420px;font-size:88px;text-align:center">{esc(c['cta_title'])}</h1>
  <div style="position:absolute;left:120px;right:120px;top:650px;font-size:30px;line-height:1.4;text-align:center">{esc(c['cta_sub'])}</div>
  <div style="position:absolute;left:0;right:0;top:800px;text-align:center"><span class="url">{esc(c['cta_url'])}</span></div>
  <div style="position:absolute;left:200px;top:745px">{arrow_svg(b['ink'], 130, 120)}</div>
  <div style="position:absolute;left:0;right:0;top:980px;display:flex;justify-content:center;align-items:center;gap:40px">{logo_img(b, height=b['cta_logo_h'])}<span style="font-size:40px;opacity:.5">×</span><img src="file://{STX_FULL}" style="height:96px"></div>
</section>""")
    return S

# ---------------------------------------------------------------- STIJL 2
def s2_slides(b, c):
    CUR["pal"] = b["pal"]; c = fill_pal(b, c); P = b["pal"]
    esc, hl, balloon, rot = G["esc"], G["hl"], G["balloon"], G["rot"]
    s2_footer, STX_WT = G["s2_footer"], G["STX_WT"]
    S = []
    S.append(f"""
<section class="slide s2">
  <div class="sq" style="left:70px;top:70px;width:200px;height:120px"><img src="file://{b['logo']}" style="max-width:170px;max-height:90px"></div>
  <div class="conn" style="left:170px;top:190px;width:140px;height:380px"></div>
  <div style="position:absolute;left:300px;top:552px;width:0;height:0;border-left:22px solid #fff;border-top:14px solid transparent;border-bottom:14px solid transparent"></div>
  <h1 data-fit style="position:absolute;left:320px;right:70px;top:70px;max-height:430px;font-size:64px">{hl(c['cover_title'])}</h1>
  <div class="frame" style="left:320px;top:520px;width:690px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box"><div style="transform:scale(1.1)">{official_shelf(P, c, '#111')}</div></div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px;font-size:26px"><b style="font-size:36px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:720px;width:560px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:320px;padding:10px;box-sizing:border-box"><div style="transform:scale(.78)">{any_seller(P, '#111')}</div></div>
  </div>
  <div class="frame" style="left:600px;top:820px;width:410px;transform:rotate({rot(b,3)}deg)">
    <div class="ph" style="height:260px;padding:10px;box-sizing:border-box"><div style="transform:scale(.8)">{balloon(b['hero'], 'fashion', 150)}</div></div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:58px;max-height:160px">{esc(c['rule1_title'])}</h2>
  <div class="frame" style="left:70px;top:350px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:400px;padding:26px 30px;box-sizing:border-box;align-items:stretch;background:#fff">{facts_grid(c['rule1_facts'], 'facts onwhite')}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:860px;font-size:26px">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:52px;max-height:150px">{esc(c['rule2_title'])}</h2>
  <div class="body" style="position:absolute;left:70px;right:70px;top:318px;font-size:24px">{esc(c['rule2_body'])}</div>
  <div class="frame" style="left:70px;top:385px;width:940px;transform:rotate({rot(b,1)}deg)">
    <div class="ph" style="height:auto;padding:22px 26px;box-sizing:border-box;align-items:stretch;background:#fff;color:#111">{region_map(c, "regions onwhite", None, 18, 14, '#111')}</div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:54px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:auto;padding:24px 30px;box-sizing:border-box;flex-direction:column;gap:22px;background:#fff;color:#111">{shelf_row(c, P, 120, 18, '#111', 26)}{lines_chips(c, 'hours onwhite small')}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1000px;font-size:23px">{esc(c['example_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:56px;max-height:150px">{esc(c['client_title'])}</h2>
  <div class="frame" style="left:70px;top:340px;width:940px">
    <div class="ph" style="height:auto;padding:26px 34px;box-sizing:border-box;align-items:flex-start;background:#fff">
      <div style="font-size:29px;line-height:1.3;color:{b['ink']};font-style:italic">{esc(c['client_question'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:12px 0"></div>
      <div style="font-size:24px;line-height:1.35;color:{b['ink']}">{esc(c['client_answer'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:12px 0"></div>
      <div style="font-size:21px;font-weight:{b['body_b']};color:{b['ink']}">{esc(c['avoid_lead'])}</div>
      {avoid_list(c, 'onwhite')}
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1070px;font-size:22px">{esc(c['client_body'])}</div>
  {s2_footer(b)}
</section>""")
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

# ---------------------------------------------------------------- STIJL 3
def s3_slides(b, c):
    CUR["pal"] = b["pal"]; c = fill_pal(b, c); P = b["pal"]
    esc, hl, balloon, rot = G["esc"], G["hl"], G["balloon"], G["rot"]
    s3_footer, STX_FULL, PAL_SETS = G["s3_footer"], G["STX_FULL"], G["PAL_SETS"]
    loud = P + PAL_SETS[(b["pal_idx"] + 5) % len(PAL_SETS)]
    S = []
    S.append(f"""
<section class="slide s3">
  <h1 data-fit style="position:absolute;left:50px;right:50px;top:60px;max-height:400px;font-size:84px;text-align:center;line-height:1.08">{hl(c['s3_cover_a'])}: {esc(c['s3_cover_b'])} {esc(c['s3_cover_c'])}<br><span class="hl">{esc(c['s3_cover_d'])}</span></h1>
  <div class="vsmark" style="top:520px">VS</div>
  <div class="lblw" style="left:110px;top:500px;transform:rotate({rot(b,-4)}deg)">{esc(c['s3_left'])}<br><span class="meta">● {esc(c['s3_left_meta'])}</span></div>
  <div class="lbld" style="right:110px;top:500px;transform:rotate({rot(b,4)}deg)">{esc(c['s3_right'])}<br><span class="meta" style="background:rgba(255,255,255,.18)">● {esc(c['s3_right_meta'])}</span></div>
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{any_seller(loud, b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{official_shelf(P, c, b['ink'])}</div>
  <div class="vsbadge" style="left:485px;top:850px">vs</div>
  {s3_footer(b, stx_h=60)}
</section>""")
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
    <div style="max-width:880px">{new_tags}</div>
    <div class="quote" style="font-size:30px">{esc(c['s3_new_quote'])}</div>
    <div class="badge">◉ {esc(c['s3_new_badge'])}</div>
  </div>
  <div class="bottom" style="top:1125px">{esc(c['s3_changed_bottom'])}</div>
  {s3_footer(b)}
</section>""")
    def topic_slide(topic, old_text, new_visual, quote, label=None):
        label = label or c['s3_topic_lbl']; old_meta = " + ".join(c['s3_old_tags'])
        return f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(label)}</span><span class="v">{esc(topic)}</span></div>
  <div class="cardd" style="left:70px;top:230px;width:440px;height:600px;padding:34px 36px">
    <span class="oldlbl">{esc(c['s3_old_lbl'])}</span>
    <div class="strike" style="font-size:38px;line-height:1.2;color:#fff;text-decoration-color:#E03131;margin-top:34px;font-weight:700;font-family:'{b['ui']}'">{esc(old_text)}</div>
    <div style="position:absolute;left:36px;right:36px;bottom:34px;font-size:22px;opacity:.55;font-weight:600">{esc(old_meta)}</div>
  </div>
  <div class="cardw onwhite" style="left:570px;top:230px;width:440px;height:600px;padding:34px 36px">
    <span class="newlbl">{esc(c['s3_new_lbl'])}</span>
    <div style="margin-top:30px;display:flex;justify-content:center">{new_visual}</div>
  </div>
  <div class="bottom" style="top:890px;font-size:33px;font-weight:700">{esc(quote)}</div>
  {s3_footer(b)}
</section>"""
    vis1 = f'<div style="width:100%">{facts_grid(c["rule1_facts"], "facts s3facts", 32, 17)}</div>'
    S.append(topic_slide(c["s3_rule1_topic"], c["s3_rule1_old"], vis1, c["s3_rule1_quote"]))
    vis2 = f'<div style="width:100%">{region_map(c, "regions s3regions", None, 14, 12, "#111", "list")}</div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    t = c['example_title']
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v" style="font-size:{44 if len(t) <= 24 else (36 if len(t) <= 30 else 28)}px">{esc(t)}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:620px;padding:40px 30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px">
    {shelf_row(c, P, 130, 19, "#111", 26)}
    {lines_chips(c, 'hours s3hours')}
  </div>
  <div class="bottom" style="top:910px;font-size:29px;font-weight:700">{esc(c['s3_example_quote'])}</div>
  {s3_footer(b)}
</section>""")
    vis6 = (f'<div style="width:100%"><div style="font-size:22px;line-height:1.3;font-style:italic;margin-bottom:12px">{esc(c["client_question"])}</div>'
            f'<div style="font-size:18px;line-height:1.3;margin-bottom:12px">{esc(c["client_answer"])}</div>'
            f'<div style="font-size:17px;font-weight:800;margin-bottom:2px">{esc(c["avoid_lead"])}</div>{avoid_list(c, "s3steps")}</div>')
    S.append(topic_slide(c["s3_client_topic"], c["s3_client_old"], vis6, c["s3_client_quote"], label=c["s3_client_lbl"]))
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

EXTRA_CSS = """
.s1 .step{font-size:24px;margin-top:9px;line-height:1.25}
.s1 .avoid .step{font-size:23px;margin-top:8px;line-height:1.25}
.s2 .onwhite .step{color:#111;font-size:20px;margin-top:6px;line-height:1.25}
.s2 .onwhite .step b{color:#6b3fb9}
.s3 .s3steps .step{display:flex;gap:10px;font-size:16px;line-height:1.25;margin-top:5px}
.s3 .s3steps .step b{min-width:24px;font-weight:800}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.facts .fact{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:3px solid #111;border-radius:18px;padding:16px 12px;gap:6px;line-height:1.15}
.facts .fact b{letter-spacing:-.01em;line-height:1;white-space:nowrap}
.facts.onwhite .fact{color:#111}
.facts.s3facts{grid-template-columns:1fr;gap:12px}
.facts.s3facts .fact{border-width:2px;padding:10px 14px;border-radius:14px;align-items:flex-start;text-align:left;gap:3px}
.facts.s3facts .fact b{white-space:normal}
.regions{display:grid;grid-template-columns:1fr 1fr;gap:14px 26px;width:100%;color:#111;align-items:start}
.regions .rh{font-weight:900;letter-spacing:.08em;text-transform:uppercase;opacity:.55;margin:8px 0 4px}
.regions .rrow{display:flex;flex-direction:column;gap:2px;padding:7px 12px;border-radius:12px;line-height:1.2}
.regions .rrow .rl1{display:flex;align-items:center;gap:10px}
.regions .rrow .rn{font-weight:700}
.regions .rrow .rc{opacity:.6;font-size:.8em}
.regions .rrow .rt{margin-left:auto;font-size:.62em;font-weight:800;letter-spacing:.06em;border:2px solid currentColor;border-radius:999px;padding:1px 8px;opacity:.7;white-space:nowrap}
.regions .rrow.me{background:#6b3fb9;color:#fff}
.regions .rrow.me .rc{opacity:.85}
.regions .rrow.me .rt{opacity:1}
.regions .rrow .you{font-size:.62em;font-weight:900;letter-spacing:.08em;text-transform:uppercase;background:#fff;color:#6b3fb9;border-radius:999px;padding:2px 8px;white-space:nowrap}
.regions.s3regions{grid-template-columns:1fr;gap:2px}
.regions.s3regions .rrow{flex-direction:row;align-items:center;gap:8px;padding:3px 8px;border-radius:8px}
.regions.s3regions .rrow .rn{white-space:nowrap}
.regions.s3regions .rrow .rc{font-size:.9em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
.regions.s3regions .rh{margin:5px 0 2px}
.hours{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;width:100%}
.hchip{display:inline-flex;align-items:center;gap:6px;border:3px solid #111;border-radius:999px;padding:8px 16px;font-size:20px;color:#111;background:#fff;white-space:nowrap}
.hchip b{font-weight:800}
.hours.small .hchip{font-size:18px;padding:6px 14px;border-width:2px}
.hours.s3hours{gap:8px}
.hours.s3hours .hchip{font-size:16px;padding:6px 12px;border-width:2px}
.bag{display:inline-block;padding:10px 10px 6px;border:3px dashed rgba(0,0,0,.35);border-radius:14px;background:rgba(255,255,255,.55)}
"""
