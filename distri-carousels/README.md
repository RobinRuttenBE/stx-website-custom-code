# STX distri carousels (generator)

Maakt van een STX EU blog per distributeur 3 Instagram-carousels (7 slides, 1080x1350) in de huisstijl en taal van die distri.

## Inhoud
- `build.py` : templates voor de 3 stijlen + renderer (Playwright) -> `out/<distri>_stijl<n>/slide-01..07.png` en `.html`
- `carousel_copy.py` : basiscopy NL/EN/DE + Sempertex kleuren/paletten
- `copy_extra.py` : copy FR/IT/PL/EL/HU/LT + varianten per taal (hooks, klantvragen, quotes, CTA) + captions
- `brands.json` : per distri fonts, kleuren, logo, taal, domein (gegenereerd door `brands_build.py` uit `Distri huisstijlen/`)
- `assets/logos/` : uitgeknipte distri-logo's; `assets/stx_*` : Sempertex logo's en flor
- `balloons/` : uitgeknipte R12 productfoto's (18 kleuren) van sempertexeurope.com
- `cut_balloons.py` : knipt nieuwe productfoto's uit Chrome-screenshots
- `deliver_all.py` : zips per land + preview_all.html ; `sheet.py` : contactsheet voor QA
- `fonts/package.json` : `cd fonts && npm install` (fontsource)
- `SKILL.md` : de werkwijze (zelfde tekst als de skill in Claude)

## Snel starten
```
cd fonts && npm install && cd ..
python3 build.py --render --brands=mooideco,gointernational,segelken
python3 sheet.py mooideco_stijl1
python3 deliver_all.py
```
Paden staan op `/home/claude/carousels`; pas `ROOT` in build.py/deliver_all.py aan als de map ergens anders staat.

## Skill
De Claude-skill `stx-distri-carousels` clonet deze repo en gebruikt deze map. Nieuwe distri: map toevoegen onder `Distri huisstijlen/` (huisstijl.md + logo), dan `python3 brands_build.py`.
