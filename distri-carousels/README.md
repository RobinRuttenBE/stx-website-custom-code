# STX distri carousels (generator)

Maakt van een STX EU blog per distributeur 3 Instagram-carousels (7 slides, 1080x1350) in de huisstijl en taal van die distri.

## Inhoud
- `build.py` : templates voor de 3 stijlen + renderer (Playwright) -> `out/<distri>_stijl<n>/slide-01..07.png` en `.html`
- `carousel_copy.py` : basiscopy NL/EN/DE voor het kleurenonderwerp + Sempertex kleuren/paletten
- `copy_extra.py` : copy FR/IT/PL/EL/HU/LT + varianten per taal (hooks, klantvragen, quotes, CTA) + captions (kleurenonderwerp)
- `topic_<slug>.py` : een extra blogonderwerp (copy in 9 talen, varianten, captions en slide-templates), zie "Nieuw blogonderwerp"
- `brands.json` : per distri fonts, kleuren, logo, taal, domein (gegenereerd door `brands_build.py` uit `Distri huisstijlen/`)
- `assets/logos/` : uitgeknipte distri-logo's; `assets/stx_*` : Sempertex logo's en flor
- `balloons/` : uitgeknipte productfoto's van sempertexeurope.com (18 R12 kleuren + `red260` 260 modelleerballon + `red5` 5 inch); namen en codes in `carousel_copy.SX`
- `cut_balloons.py` : knipt nieuwe productfoto's uit Chrome-screenshots
- `deliver_all.py` : zips per land + preview_all.html ; `sheet.py` : contactsheet voor QA
- `fonts/package.json` : `cd fonts && npm install` (fontsource)
- `SKILL.md` : de werkwijze (zelfde tekst als de skill in Claude)

Alle paden zijn relatief aan deze map; de map mag overal staan.

## Snel starten
```
cd fonts && npm install && cd ..
python3 build.py --render --brands=mooideco,gointernational,segelken
python3 sheet.py mooideco_stijl1
python3 deliver_all.py
```

## Blogonderwerpen
| topic | blog | module | output |
|---|---|---|---|
| `colours` (standaard) | Kleurencombinaties kiezen | carousel_copy.py + copy_extra.py | `out/` |
| `artist` | Hoe word je ballonartiest | topic_artist.py | `out/artist/` |
| `helium` | Helium voor ballonnen | topic_helium.py | `out/helium/` |
| `pricing` | Prijs voor ballondecoratie (bedragen per markt via `money()`) | topic_pricing.py | `out/pricing/` |
| `doublestuff` | Double stuffing (gesimuleerde ballon-in-ballon via `dstuff()`) | topic_doublestuff.py | `out/doublestuff/` |
| `storage` | Ballonnen bewaren | topic_storage.py | `out/storage/` |
| `releases` | Geen ballonoplatingen (standpunt + 4 alternatieven) | topic_releases.py | `out/releases/` |
| `buyuk` | Waar koop je Sempertex in de UK (alleen EN, alleen de 14 UK-distri's; regiokaart markeert de distri zelf, B2B/B2C per distri) | topic_buyuk.py | `out/buyuk/` |
| `startbiz` | Een ballonbusiness starten (4 dingen eerst, bestelvolgorde, 5 fouten, 3 portfoliostukken uit 1 startersvoorraad, SYBB als voetnoot) | topic_startbiz.py | `out/startbiz/` |

```
python3 build.py --topic=artist --render
SHEET_OUT=out/artist python3 sheet.py mooideco_stijl1
python3 deliver_all.py --topic=artist          # Carousels_artist_<land>.zip + preview_all_artist.html
```

## Ballonkleuren per distri (variatie)
`build.assign_palettes(topic)` geeft elke distri `b["pal"]`: 4 ballonkeys uit 12 harmonieuze sets (`PAL_SETS`). De keuze draait op de index in de taalgroep, de taal en een vaste seed per blogonderwerp, dus dezelfde distri krijgt bij elke blog andere kleuren en twee distri's met dezelfde taal tonen nooit dezelfde set. Topic-modules gebruiken `b["pal"]` voor alle productvisuals en vullen `{p0}`..`{p3}` in de copy met naam + code (`fill_pal`). Alleen blogs die zelf paletten voorschrijven (kleurencombinaties) gebruiken hun eigen paletten.

## Nieuw blogonderwerp
1. Maak `topic_<slug>.py` naar het voorbeeld van `topic_helium.py` (of `topic_artist.py`) met: `BASE` (copy per taal: nl, en, de, fr, it, pl, el, hu, lt), `VARIANTS` (per taal 3 covertitels, 2 subtitels, 3 klantvragen, 3 oude quotes, 2 klant-quotes, CTA-template), `CAPTIONS_TPL`, `setup(G)`, `s1_slides`, `s2_slides`, `s3_slides` en optioneel `EXTRA_CSS`.
2. Voeg de titel toe aan `TOPIC_TITLES` in `build.py`.
3. Render, check contactsheets, lever op met `--topic=<slug>`.
4. Blog voor één markt (bv. alleen UK): `BASE`/`VARIANTS`/`CAPTIONS_TPL` alleen in die taal, renderen met `--brands=<keys>`; `deliver_all.py` pakt automatisch alleen de gerenderde distri's.
De drie stijlen zelf (css_s1/s2/s3, footers, Sempertex-logo) blijven in `build.py` en veranderen niet per onderwerp.

## Skill
De Claude-skill `stx-distri-carousels` clonet deze repo en gebruikt deze map. Nieuwe distri: map toevoegen onder `Distri huisstijlen/` (huisstijl.md + logo), dan `python3 brands_build.py`.
