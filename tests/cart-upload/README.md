# Test harness: cart-upload-v1

Draait `sections/cart-upload-v1.html` lokaal tegen een nagebouwde Odoo-winkelmandpagina, met de
shoproutes gemockt. Geen verbinding met de live shop, dus veilig te draaien.

```
node test.js
```

Playwright komt uit `stx-tools/node_modules` (of zet `STX_PLAYWRIGHT` naar een ander pad).

## Wat het nabootst

- `/shop/cart` in nl, en_GB en fr, met en zonder ingelogde gebruiker (de guest-variant via `?guest=1`),
  met dezelfde DOM-structuur als de echte pagina (`.oe_website_sale`, `.oe_cart`, `#shop_cart`).
- De sectie wordt geïnjecteerd zoals de section loader dat doet: markup eerst, scripts daarna apart uitgevoerd.
- `/en_GB/website/snippet/autocomplete` antwoordt uit `autocomplete-fixture.json`: echte antwoorden van
  de live shop, opgehaald op 2026-09-17 voor de 108 codes uit `example-order.csv` plus een paar extra.
  Term `MULTI1` is verzonnen en geeft twee prefix-treffers, om de keuzelijst te testen.
- `/website_sale/get_combination_info` geeft een variant-id terug. `/shop/cart/add` gedraagt zich als de
  echte shop: het **telt op** bij wat er al op de regel staat en geeft `quantity`, `cart_quantity` en het
  regel-id in `notification_info.lines` terug. `/shop/cart/update` zet een exact aantal. Template 3773
  (N160080) faalt expres, zodat het foutpad getest wordt.

## Wat het controleert

De kaart tonen voor elk ingelogd account (live sinds 21/09/2026, `BETA = false`) en niets tonen voor uitgelogde bezoekers,
plaatsing boven de winkelmand, de vier talen, het inlezen van CSV, geplakte tekst en xlsx, samenvoegen van
dubbele codes, koprij en rommelregels overslaan, de vier matchstatussen, aantallen die als verpakkingen
doorgaan, de keuzelijst bij meerdere treffers, en de resultaatmelding die een herlaadbeurt overleeft.

En sinds 21/09/2026: het aantal uit het bestand is ook het aantal dat in het mandje staat. Een tweede
upload van een product dat er al in zit telt niet op maar corrigeert de regel via `/shop/cart/update`.

## example-order.csv

De productcodes komen uit een echte klantbestelling (die codes staan publiek op de shop). **De aantallen
zijn vervangen door een vast patroon**, want bestelhoeveelheden van een klant horen niet in een publieke repo.
Wil je met een echt bestand testen, zet dan `STX_ORDER_CSV` naar dat pad. De assertions over aantallen
regels kloppen dan mogelijk niet meer.
