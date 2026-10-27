"""Turn a standalone STX page (one .html with its own <head>, <style> and
base64 fonts/images) into a section file for the section loader.

The page is drawn inside a shadow root, so its CSS (body, h2, section,
footer, *) never touches Odoo, and Odoo's CSS never touches the page.

  python -I code/build-shadow-section.py team  <source.html>
  python -I code/build-shadow-section.py mbp   <source.html>

What it does:
- drops the base64 @font-face rules (Rethink Sans comes from Google Fonts,
  @font-face does not work inside a shadow root anyway)
- moves base64 images to assets/<name>/ and points the page at them
  through the loader's commit (window.STX_SECTIONS_BASE + ../assets/)
- rewrites :root / html / body selectors to :host / .stx-doc
- writes sections/<name>-vN.html from the template below
The page script of the source is NOT copied: each page gets its own
shadow-aware script (PAGE_JS below).
"""
import base64
import hashlib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

PAGES = {
    'team': {
        'out': 'sections/team-v1.html',
        'assets': 'assets/team',
        'title': 'STX EU / TEAM PAGINA v1',
        'paths': '/team (alle talen)',
    },
    'mbp': {
        'out': 'sections/mbp-v2.html',
        'assets': 'assets/mbp',
        'title': 'STX EU / MBP PAGINA v2',
        'paths': '/mbp (alle talen)',
    },
}


def extract(src):
    head = src.split('</head>', 1)[0]
    styles = re.findall(r'<style[^>]*>(.*?)</style>', head, re.S)
    body = re.search(r'<body[^>]*>(.*)</body>', src, re.S).group(1)
    body = re.sub(r'<script\b.*?</script>', '', body, flags=re.S)
    return '\n'.join(styles), body.strip()


def fix_css(css):
    css = re.sub(r"@font-face\s*\{[^}]*base64[^}]*\}\s*", '', css)
    css = css.replace(':root', ':host')
    css = re.sub(r'(^|[\s,}])html(?=[\s,{])', r'\1:host', css)
    css = re.sub(r'(^|[\s,}])body(?=[\s,{>.:])', r'\1.stx-doc', css)
    return css.strip()


def move_images(html, name, asset_dir):
    out_dir = REPO / asset_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    n = [0]

    def repl(m):
        mime, data = m.group(1), m.group(2)
        ext = {'image/jpeg': 'jpg', 'image/png': 'png', 'image/webp': 'webp', 'image/svg+xml': 'svg'}[mime]
        raw = base64.b64decode(data)
        n[0] += 1
        fname = '%s-%02d-%s.%s' % (name, n[0], hashlib.sha1(raw).hexdigest()[:8], ext)
        (out_dir / fname).write_bytes(raw)
        return '__ASSETS__/' + fname

    html = re.sub(r'data:(image/[\w+.-]+);base64,([A-Za-z0-9+/=]+)', repl, html)
    return html, n[0]


HEADER = """<!-- ============================================================
     {title}
     Bestand hoort in de repo onder /sections/ en wordt door de
     stx-loader geladen op {paths}. NIET los in Odoo plakken.

     GEBOUWD met code/build-shadow-section.py uit Robins losse pagina
     ({source}). Niet met de hand aanpassen: pas de losse pagina aan
     en bouw opnieuw, anders ben je de wijziging bij de volgende
     build kwijt.

     Werking: de pagina staat in een shadow root, in #wrap. Daardoor
     raakt de CSS van de pagina (body, h2, section, footer, *) de rest
     van de site niet, en de CSS van Odoo deze pagina niet. Wat Odoo
     zelf in #wrap heeft staan, wordt verborgen (niet gewist): in de
     editor zie je het nog en doet dit bestand niets.
     Links naar www.sempertexeurope.com krijgen de taalprefix van de
     pagina (/en_GB, /fr, /de). Beelden staan in {assets}/,
     op dezelfde commit als de loader.
     ============================================================ -->
"""

TEMPLATE = """{header}
<template id="stx-{name}-tpl">
<style>
:host {{ all: initial; display: block; overflow-x: clip; }}
.stx-doc {{ display: block; }}
{css}
</style>
<div class="stx-doc">
{body}
</div>
</template>

<script>
(function () {{
  'use strict';
  if (window.__stx_{name}) {{ return; }}
  window.__stx_{name} = true;
  if (document.body.classList.contains('editor_enable') || document.querySelector('.odoo-editor-editable') || document.querySelector('#wrap.o_editable')) {{ return; }}
  var tpl = document.getElementById('stx-{name}-tpl');
  var target = document.getElementById('wrap') || document.querySelector('main');
  if (!tpl || !target) {{ return; }}

  /* Rethink Sans in het document zelf: @font-face werkt niet binnen een shadow root. */
  if (!document.querySelector('link[data-stx-rethink]')) {{
    var fl = document.createElement('link');
    fl.rel = 'stylesheet';
    fl.href = 'https://fonts.googleapis.com/css2?family=Rethink+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,700&display=swap';
    fl.setAttribute('data-stx-rethink', '1');
    document.head.appendChild(fl);
  }}

  var base = (window.STX_SECTIONS_BASE || '').replace(/sections\\/?$/, '');
  var seg = (window.location.pathname.split('/')[1] || '');
  var prefix = /^(en_gb|fr|de)$/i.test(seg) ? '/' + seg : '';

  var host = document.createElement('div');
  host.id = 'stx-{name}-host';
  var root = host.attachShadow({{ mode: 'open' }});
  root.appendChild(tpl.content.cloneNode(true));
  Array.prototype.forEach.call(root.querySelectorAll('img[src^="__ASSETS__/"]'), function (img) {{
    img.src = base + '{assets}/' + img.getAttribute('src').slice(11);
  }});
  Array.prototype.forEach.call(root.querySelectorAll('a[href^="https://www.sempertexeurope.com/"]'), function (a) {{
    a.href = prefix + a.getAttribute('href').slice(31);
  }});

  Array.prototype.forEach.call(target.children, function (el) {{ el.style.display = 'none'; }});
  target.appendChild(host);

  /* Hoogte van een vaste Odoo-header, zodat sticky balken en ankers eronder blijven. */
  function headerOffset() {{
    var h = document.querySelector('header#top');
    if (!h) {{ return 0; }}
    var pos = window.getComputedStyle(h).position;
    if (pos !== 'fixed' && pos !== 'sticky') {{ return 0; }}
    return Math.max(0, Math.round(h.getBoundingClientRect().bottom));
  }}
  var ticking = false;
  function syncTop() {{
    ticking = false;
    host.style.setProperty('--stx-top', headerOffset() + 'px');
  }}
  window.addEventListener('scroll', function () {{ if (!ticking) {{ ticking = true; requestAnimationFrame(syncTop); }} }}, {{ passive: true }});
  window.addEventListener('resize', syncTop);
  syncTop();

  /* Ankerlinks (#ceo, #exam): de browser vindt ids in een shadow root niet zelf. */
  root.addEventListener('click', function (e) {{
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) {{ return; }}
    var el = root.getElementById(a.getAttribute('href').slice(1));
    if (!el) {{ return; }}
    e.preventDefault();
    var nav = root.querySelector('.dept-nav');
    var extra = nav ? nav.offsetHeight : 16;
    var y = el.getBoundingClientRect().top + window.pageYOffset - headerOffset() - extra - 8;
    window.scrollTo({{ top: y, behavior: 'smooth' }});
  }});
{page_js}
}})();
</script>
"""

PAGE_JS = {
    'team': """
  /* Ontbrekende portretfoto: dan blijven de initialen staan. */
  Array.prototype.forEach.call(root.querySelectorAll('.portrait img'), function (img) {
    img.addEventListener('error', function () { img.classList.add('is-missing'); });
    if (img.complete && img.naturalWidth === 0) { img.classList.add('is-missing'); }
  });
""",
    'mbp': """
  /* Tabs van het examen (deel 1 / deel 2). */
  var tabs = root.querySelectorAll('.tab');
  Array.prototype.forEach.call(tabs, function (t) {
    t.addEventListener('click', function () {
      Array.prototype.forEach.call(tabs, function (o) {
        var open = o === t;
        o.setAttribute('aria-selected', open ? 'true' : 'false');
        root.getElementById(o.getAttribute('aria-controls')).hidden = !open;
      });
    });
  });
""",
}

EXTRA_CSS = {
    # sticky afdelingsbalk onder een vaste Odoo-header
    # en geen overflow-x: hidden op .stx-doc (uit body), dat breekt sticky; :host knipt al af
    'team': ".dept-nav { top: var(--stx-top, 0px); }\n.stx-doc { overflow-x: visible; }",
    'mbp': "",
}


def main():
    name, source = sys.argv[1], Path(sys.argv[2])
    cfg = PAGES[name]
    src = source.read_text(encoding='utf-8')
    css, body = extract(src)
    css = fix_css(css) + '\n' + EXTRA_CSS[name]
    body, nimg = move_images(body, name, cfg['assets'])
    css, ncss = move_images(css, name + '-css', cfg['assets'])
    if 'base64,' in body or 'base64,' in css:
        raise SystemExit('base64 left over')
    header = HEADER.format(title=cfg['title'], paths=cfg['paths'], source=source.name, assets=cfg['assets'])
    out = TEMPLATE.format(header=header, name=name, css=css, body=body,
                          assets=cfg['assets'], page_js=PAGE_JS[name])
    (REPO / cfg['out']).write_text(out, encoding='utf-8', newline='\n')
    print(cfg['out'], len(out), 'bytes,', nimg + ncss, 'images')


if __name__ == '__main__':
    main()
