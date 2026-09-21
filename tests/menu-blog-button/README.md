# Test harness: menu-blog-button

Draait `sections/menu-blog-button.html` tegen een nagebouwde Odoo-header (desktop menurij +
mobiel uitklapmenu), zonder verbinding met de live site.

```
node test.js
```

Playwright komt uit `stx-tools/node_modules` (of zet `STX_PLAYWRIGHT` naar een ander pad).

## Wat het controleert

De Blog-knop staat rechts in de desktop menurij en onderaan het mobiele uitklapmenu, de link
houdt de taalprefix (`/fr/blog`), en sinds 21/09/2026: **er is geen popup meer**, niet op desktop
en niet mobiel, er gaan geen achtergrondrequests meer uit (zoekroute, sitemap, artikelpagina's)
en de oude localStorage-sleutels `stx_blog_pin_v1` en `stx_blog_pop_off` worden opgeruimd.
