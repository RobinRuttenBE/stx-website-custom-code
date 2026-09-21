# Test harness: mbp-page

Draait `sections/mbp-v1.html` tegen een nagebouwde Odoo-pagina op `/mbp` en de taalversies,
zonder verbinding met de live site.

```
node test.js
```

Playwright komt uit `stx-tools/node_modules` (of zet `STX_PLAYWRIGHT` naar een ander pad).

## Wat het controleert

De sectie verschijnt in `#wrap`, is vertaald in nl, en_GB, fr en de, en links houden de
taalprefix zoals Odoo hem schrijft (`/en_GB/events`, niet `/en_gb/events`). De acht
examencriteria tellen samen op tot 100 punten. De lijst toont alle 266 MBPs: 63 Europese
bovenaan met zoekveld en landenfilter, de 203 andere eronder en ingeklapt op 16. Filteren op
land en zoeken op naam werken. Buiten `/mbp` haalt de sectie zichzelf weg. Op 390px is er geen
horizontale scroll.

## Screenshots

`mbp-nl.png` en `mbp-mobile.png` worden bij elke run overschreven (gitignored).
