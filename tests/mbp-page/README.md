# Test harness: mbp-page

Draait de twee publieke MBP-secties tegen een nagebouwde Odoo-pagina, zonder verbinding met de
live site:

- `sections/mbp-v1.html` op `/mbp`, de uitleg
- `sections/mbp-listing-v1.html` op `/mbp-listing`, de lijst

```
node test.js
```

Playwright komt uit `stx-tools/node_modules` (of zet `STX_PLAYWRIGHT` naar een ander pad).

## Wat het controleert

**`/mbp`:** de sectie verschijnt in `#wrap`, de acht examencriteria tellen op tot 100 punten, de
lijst staat er niet meer maar de doorverwijzing naar `/mbp-listing` wel, en de aantallen (266
wereldwijd, 63 Europa) kloppen op beide plekken waar ze staan.

**`/mbp-listing`:** alle 63 Europese MBPs staan er, allemaal met een profielfoto die ook echt van
de Sempertex CDN laadt. Filteren op land en zoeken op naam werken. De 203 anderen staan eronder,
ingeklapt op 16. Klikken op iemand opent zijn profiel met de juiste Instagram-link en de
portfolio-carrousel; iemand zonder portfolio krijgt een nette melding in plaats van een lege
carrousel. Escape sluit het paneel.

**Beide:** vertaald in nl, en_GB, fr en de; links houden de taalprefix zoals Odoo hem schrijft
(`/en_GB/events`, niet `/en_gb/events`); buiten het eigen pad haalt elke sectie zichzelf weg; op
390px is er geen horizontale scroll; en elk zichtbaar stuk tekst staat in Rethink Sans.

## Screenshots

`mbp-nl.png`, `mbp-listing-nl.png`, `mbp-profile.png` en de twee mobiele versies worden bij elke
run overschreven (gitignored).
