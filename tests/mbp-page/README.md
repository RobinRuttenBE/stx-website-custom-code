# Test harness: mbp-page

Draait de twee publieke MBP-secties tegen een nagebouwde Odoo-pagina, zonder verbinding met de
live site:

- `sections/mbp-v1.html` op `/mbp`, de uitleg
- `sections/mbp-listing-v1.html` op `/mbp-listing`, de lijst

```
node test.js        # de twee pagina's in de browser
node check-i18n.js  # de vertaalblokken
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

## check-i18n.js

Apart scriptje voor de vertalingen, want daar is het al twee keer misgegaan: een sleutel die in
een taal ontbrak (de pagina viel dan stilletjes terug op de Engelse tekst uit de HTML), en een
blok dat vier keer met dezelfde taal overschreven werd. Het controleert per bestand dat het
script geldige JavaScript is, dat de vier talen precies dezelfde sleutels hebben, dat er geen
dubbele sleutels zijn, dat er geen tekst uit een andere taal in een blok staat, dat elke
`data-i18n` in de markup een vertaling heeft, en dat er geen vertalingen overblijven die nergens
meer gebruikt worden.

`test.js` doet het daarnaast nog eens vanuit de browser: het leest de hele zichtbare tekst van
elke taalversie en slaat alarm als een andere taal er doorheen loopt.

## Screenshots

`mbp-nl.png`, `mbp-listing-nl.png`, `mbp-profile.png` en de twee mobiele versies worden bij elke
run overschreven (gitignored).
