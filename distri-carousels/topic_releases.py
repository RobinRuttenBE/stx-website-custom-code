# -*- coding: utf-8 -*-
"""Topic: 'Sempertex Europe: why we do not support balloon releases.'
(sempertexeurope.com/en_GB/blog/our-position-on-balloon-releases).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=releases.
Uit de blog: geen oplatingen van welke soort ook, klanten gevraagd hetzelfde te doen, European Code of Best Practice,
elke opgelaten ballon landt ergens als afval (natuur, water, dieren), latex is natuurlijk en afbreekbaar maar dat
duurt maanden; alternatieven: ballondrop, luchtgevuld fotomoment, verankerde heliumdesigns, herdenkingsmoment met
1 verankerd design; na afloop knippen en bij het restafval; PartySafe-materiaal op partysafe.eu/balloons."""

G = {}
def setup(g): G.update(g)

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["Nooit oplaten…", "4 alternatieven…", "Knippen en weg…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Ons standpunt…",
    "steps_title": "Wij doen niet mee aan ballonoplatingen. Van geen enkele soort.", "steps_lead": "Ons standpunt, in 4 zinnen:",
    "steps": ["Wij organiseren, promoten of steunen geen oplatingen", "Wij vragen onze klanten om hetzelfde te doen", "Dat volgt de European Code of Best Practice van de sector", "Vraagt een klant een oplating? Dan is het antwoord nee, met een beter alternatief erbij"],
    "steps_label": "Het standpunt",
    "rule1_label": "Waarom", "rule1_title": "Elke opgelaten ballon landt ergens als afval",
    "rule1_body": "Eens losgelaten wordt een ballon afval dat ergens neerkomt, vaak in een natuurgebied of in het water, waar hij dieren in gevaar brengt. Latex is natuurlijk en biologisch afbreekbaar, maar dat verandert niets: afbreken duurt maanden, en al die tijd ligt de ballon waar hij niet hoort. In steeds meer landen en gemeenten is oplaten ook gewoon verboden.",
    "rule1_facts": [["elke", "opgelaten ballon landt ergens als afval"], ["maanden", "duurt het afbreken van latex"], ["natuur en water", "waar hij meestal neerkomt"], ["nee", "ons antwoord op elke aanvraag"]],
    "rule2_label": "Alternatieven", "rule2_title": "4 alternatieven die mooier zijn dan een oplating",
    "rule2_body": "Voor een symbolisch of spectaculair moment heb je geen oplating nodig.",
    "alts": [["Ballondrop", "honderden ballonnen vallen op het juiste moment uit een net. Binnen, en nadien opgeruimd."], ["Luchtgevuld fotomoment", "backdrop, boog of installatie waar gasten foto's nemen. Blijft de hele dag staan."], ["Verankerde heliumdesigns", "clusters en zwevend decor, elk stuk apart aan een gewicht. 0 risico op wegdrijven."], ["Herdenkingsmoment", "1 verankerd design op een betekenisvolle plek, nadien bewust weggehaald. Persoonlijker en respectvoller."]],
    "example_label": "Voorbeeld", "example_title": "Zo bouw je het alternatief",
    "ex_drop_title": "Ballondrop", "ex_drop_body": "100 × R12 in {p0}, {p1}, {p2} en {p3}, in een net boven de dansvloer. Valt op het juiste moment, binnen, en gaat nadien in de vuilniszak.",
    "ex_mem_title": "Herdenkingsmoment", "ex_mem_body": "3 × R12 in {p0} op een gewicht, op de plek die telt. Na het moment haal je het bewust weg.",
    "example_body": "Na elk event geldt dezelfde regel: gebruikte ballonnen knippen en bij het restafval, samen met accessoires en verpakking. Zo wordt niets zwerfvuil.",
    "client_label": "Klantgesprek", "client_title": "Wat je antwoordt als de klant vraagt",
    "client_answers": [
        "Dat doen we niet, en ik leg je graag uit waarom: elke opgelaten ballon landt ergens als afval. Voor opa stel ik 1 verankerd design voor op de plek die voor hem telt, en daarna halen we het samen weg.",
        "Het ziet er 10 seconden mooi uit en daarna ligt alles ergens in een weide of in het water. Ik bouw je een ballondrop: honderden ballonnen die op het juiste moment uit een net vallen, binnen, met dezelfde wow.",
        "Latex is natuurlijk en breekt af, maar dat duurt maanden. Al die tijd ligt die ballon waar hij niet hoort. Daarom bouwen we liever iets dat blijft staan en nadien opgeruimd wordt.",
    ],
    "avoid_lead": "De Code of Best Practice, in 5 regels:",
    "steps5": ["Nooit ballonnen oplaten", "Veilig opblazen, met een pomp", "Nooit helium inademen", "Kinderen onder 8 jaar onder toezicht", "Na afloop knippen en bij het restafval"],
    "client_body": "Officieel PartySafe-materiaal voor je studio of winkel: een poster, een zorgkaart en brochure voor klanten, en stickers voor op de verpakking. Op partysafe.eu/balloons.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Sempertex ballonnen", "s3_cover_b": "oplaten", "s3_cover_c": "vs.", "s3_cover_d": "opbouwen",
    "s3_left": "OPLATEN", "s3_right": "OPBOUWEN", "s3_left_meta": "landt ergens als afval", "s3_right_meta": "blijft, en wordt opgeruimd",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["Oplaten", "Omdat de klant het vraagt"], "s3_new_tags": ["Ballondrop", "Fotomoment", "Verankerd", "Knippen en weg"],
    "s3_new_quote": "“Wij laten niets op. We bouwen iets dat blijft staan, en ruimen het nadien zelf op.”", "s3_new_badge": "Code of Best Practice",
    "s3_changed_bottom": "Zelfde wow, zelfde klant.\nGeen ballon die ergens landt.",
    "s3_topic_lbl": "WAAROM", "s3_rule1_topic": "Afval", "s3_rule1_old": "Latex breekt toch af",
    "s3_rule1_quote": "“Afbreken duurt maanden. Al die tijd ligt de ballon in een weide of in het water.”",
    "s3_rule2_topic": "Alternatief", "s3_rule2_old": "Zonder oplating geen wow-moment",
    "s3_rule2_quote": "“Ballondrop, fotomoment, verankerd design of herdenkingsmoment: dezelfde wow, binnen en opgeruimd.”",
    "s3_example_lbl": "VOORBEELD", "s3_example_quote": "“100 R12 in {p0}, {p1}, {p2} en {p3} in een net boven de dansvloer. Valt op het juiste moment, en gaat nadien in de vuilniszak.”",
    "s3_client_lbl": "KLANT", "s3_client_topic": "Klantgesprek",
    "s3_client_quote": "“Nee zeggen is makkelijk als je meteen iets mooiers kunt voorstellen.”",
    "s3_cta_kicker": "Bouw het alternatief voor je volgende event",
    "net_lbl": "net", "weight_lbl": "gewicht", "litter_lbl": "afval", "drop_lbl": "ballondrop", "mem_lbl": "verankerd",
},
"en": {
    "cover_pills": ["Never release…", "4 alternatives…", "Snip and bin…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Our position…",
    "steps_title": "We don't take part in balloon releases. Of any kind.", "steps_lead": "Our position, in 4 lines:",
    "steps": ["We don't organise, promote or support releases", "We ask our customers to do the same", "That follows the industry's European Code of Best Practice", "A client asks for a release? The answer is no, with a better alternative attached"],
    "steps_label": "The position",
    "rule1_label": "Why", "rule1_title": "Every released balloon lands somewhere as litter",
    "rule1_body": "Once released, a balloon becomes waste that comes down somewhere, often in a nature reserve or in the water, where it endangers animals. Latex is natural and biodegradable, but that changes nothing: breaking down takes months, and all that time the balloon sits where it shouldn't. In more and more countries and councils, releases are simply banned.",
    "rule1_facts": [["every", "released balloon lands somewhere as litter"], ["months", "for latex to break down"], ["nature and water", "where it usually comes down"], ["no", "our answer to every request"]],
    "rule2_label": "Alternatives", "rule2_title": "4 alternatives that beat a release",
    "rule2_body": "You don't need a release for a symbolic or spectacular moment.",
    "alts": [["Balloon drop", "hundreds of balloons fall from a net at the right moment. Indoors, and cleaned up afterwards."], ["Air-filled photo moment", "a backdrop, arch or installation where guests take photos. Stays up all day."], ["Anchored helium designs", "clusters and floating decor, each piece tied to its own weight. 0 risk of drifting off."], ["Memorial moment", "1 anchored design in a meaningful place, removed deliberately afterwards. More personal and respectful."]],
    "example_label": "Example", "example_title": "How to build the alternative",
    "ex_drop_title": "Balloon drop", "ex_drop_body": "100 × R12 in {p0}, {p1}, {p2} and {p3}, in a net above the dance floor. Falls at the right moment, indoors, and goes in the bin afterwards.",
    "ex_mem_title": "Memorial moment", "ex_mem_body": "3 × R12 in {p0} on a weight, in the place that matters. After the moment you remove it deliberately.",
    "example_body": "After every event the same rule applies: snip used balloons and put them in the general waste, together with accessories and packaging. That way nothing becomes litter.",
    "client_label": "Client chat", "client_title": "What you answer when the client asks",
    "client_answers": [
        "We don't do that, and I'm happy to tell you why: every released balloon lands somewhere as litter. For grandad I'd suggest 1 anchored design in the place that mattered to him, and afterwards we take it down together.",
        "It looks lovely for 10 seconds and then it all ends up in a field or in the water. I'll build you a balloon drop: hundreds of balloons falling from a net at the right moment, indoors, with the same wow.",
        "Latex is natural and does break down, but that takes months. All that time the balloon sits where it shouldn't. So we'd rather build something that stays up and gets cleaned up afterwards.",
    ],
    "avoid_lead": "The Code of Best Practice, in 5 rules:",
    "steps5": ["Never release balloons", "Inflate safely, with a pump", "Never inhale helium", "Supervise children under 8", "Snip afterwards and put in the general waste"],
    "client_body": "Official PartySafe materials for your studio or shop: a poster, a care card and brochure for customers, and stickers for packaging. At partysafe.eu/balloons.",
    "cta_label": "Order",
    "s3_cover_a": "Sempertex balloons", "s3_cover_b": "released", "s3_cover_c": "vs.", "s3_cover_d": "built",
    "s3_left": "RELEASED", "s3_right": "BUILT", "s3_left_meta": "lands somewhere as litter", "s3_right_meta": "stays up, gets cleaned up",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["Release", "Because the client asks"], "s3_new_tags": ["Balloon drop", "Photo moment", "Anchored", "Snip and bin"],
    "s3_new_quote": "“We don't release anything. We build something that stays up, and clean it up ourselves afterwards.”", "s3_new_badge": "Code of Best Practice",
    "s3_changed_bottom": "Same wow, same client.\nNo balloon landing anywhere.",
    "s3_topic_lbl": "WHY", "s3_rule1_topic": "Litter", "s3_rule1_old": "Latex breaks down anyway",
    "s3_rule1_quote": "“Breaking down takes months. All that time the balloon sits in a field or in the water.”",
    "s3_rule2_topic": "Alternative", "s3_rule2_old": "No release, no wow moment",
    "s3_rule2_quote": "“Balloon drop, photo moment, anchored design or memorial moment: the same wow, indoors and cleaned up.”",
    "s3_example_lbl": "EXAMPLE", "s3_example_quote": "“100 R12 in {p0}, {p1}, {p2} and {p3} in a net above the dance floor. Falls at the right moment, and goes in the bin afterwards.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Client chat",
    "s3_client_quote": "“Saying no is easy when you can offer something better straight away.”",
    "s3_cta_kicker": "Build the alternative for your next event",
    "net_lbl": "net", "weight_lbl": "weight", "litter_lbl": "litter", "drop_lbl": "balloon drop", "mem_lbl": "anchored",
},
"de": {
    "cover_pills": ["Nie steigen lassen…", "4 Alternativen…", "Zerschneiden und weg…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Unsere Haltung…",
    "steps_title": "Wir machen bei Ballonmassenstarts nicht mit. Bei keinem einzigen.", "steps_lead": "Unsere Haltung, in 4 Sätzen:",
    "steps": ["Wir organisieren, bewerben oder unterstützen keine Massenstarts", "Wir bitten unsere Kunden, es genauso zu halten", "Das folgt dem European Code of Best Practice der Branche", "Ein Kunde fragt nach einem Massenstart? Die Antwort ist nein, mit einer besseren Alternative dazu"],
    "steps_label": "Die Haltung",
    "rule1_label": "Warum", "rule1_title": "Jeder losgelassene Ballon landet irgendwo als Müll",
    "rule1_body": "Einmal losgelassen wird ein Ballon zu Abfall, der irgendwo runterkommt, oft in einem Naturschutzgebiet oder im Wasser, wo er Tiere gefährdet. Latex ist natürlich und biologisch abbaubar, aber das ändert nichts: Der Abbau dauert Monate, und die ganze Zeit liegt der Ballon dort, wo er nicht hingehört. In immer mehr Ländern und Gemeinden sind Massenstarts schlicht verboten.",
    "rule1_facts": [["jeder", "losgelassene Ballon landet irgendwo als Müll"], ["Monate", "dauert der Abbau von Latex"], ["Natur und Wasser", "wo er meistens runterkommt"], ["nein", "unsere Antwort auf jede Anfrage"]],
    "rule2_label": "Alternativen", "rule2_title": "4 Alternativen, die schöner sind als ein Massenstart",
    "rule2_body": "Für einen symbolischen oder spektakulären Moment brauchst du keinen Massenstart.",
    "alts": [["Ballon-Drop", "Hunderte Ballons fallen im richtigen Moment aus einem Netz. Drinnen, und danach aufgeräumt."], ["Luftgefüllter Fotomoment", "Backdrop, Bogen oder Installation, wo Gäste Fotos machen. Bleibt den ganzen Tag stehen."], ["Verankerte Helium-Designs", "Cluster und schwebende Deko, jedes Teil einzeln an einem Gewicht. 0 Risiko, dass etwas davonfliegt."], ["Gedenkmoment", "1 verankertes Design an einem bedeutungsvollen Ort, danach bewusst entfernt. Persönlicher und respektvoller."]],
    "example_label": "Beispiel", "example_title": "So baust du die Alternative",
    "ex_drop_title": "Ballon-Drop", "ex_drop_body": "100 × R12 in {p0}, {p1}, {p2} und {p3}, in einem Netz über der Tanzfläche. Fällt im richtigen Moment, drinnen, und kommt danach in den Müllsack.",
    "ex_mem_title": "Gedenkmoment", "ex_mem_body": "3 × R12 in {p0} auf einem Gewicht, an dem Ort, der zählt. Nach dem Moment nimmst du es bewusst weg.",
    "example_body": "Nach jedem Event gilt dieselbe Regel: gebrauchte Ballons zerschneiden und in den Restmüll, zusammen mit Zubehör und Verpackung. So wird nichts zu Müll in der Natur.",
    "client_label": "Kundengespräch", "client_title": "Was du antwortest, wenn der Kunde fragt",
    "client_answers": [
        "Das machen wir nicht, und ich erkläre dir gern, warum: Jeder losgelassene Ballon landet irgendwo als Müll. Für Opa schlage ich 1 verankertes Design an dem Ort vor, der für ihn zählte, und danach nehmen wir es gemeinsam weg.",
        "Es sieht 10 Sekunden schön aus, und danach liegt alles irgendwo auf einer Wiese oder im Wasser. Ich baue dir einen Ballon-Drop: Hunderte Ballons, die im richtigen Moment aus einem Netz fallen, drinnen, mit demselben Wow.",
        "Latex ist natürlich und baut sich ab, aber das dauert Monate. Die ganze Zeit liegt der Ballon dort, wo er nicht hingehört. Deshalb bauen wir lieber etwas, das stehen bleibt und danach aufgeräumt wird.",
    ],
    "avoid_lead": "Der Code of Best Practice, in 5 Regeln:",
    "steps5": ["Nie Ballons steigen lassen", "Sicher aufblasen, mit einer Pumpe", "Nie Helium einatmen", "Kinder unter 8 Jahren beaufsichtigen", "Danach zerschneiden und in den Restmüll"],
    "client_body": "Offizielles PartySafe-Material für dein Studio oder deinen Laden: ein Poster, eine Pflegekarte und Broschüre für Kunden, und Sticker für die Verpackung. Auf partysafe.eu/balloons.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Sempertex Ballons", "s3_cover_b": "steigen lassen", "s3_cover_c": "vs.", "s3_cover_d": "aufbauen",
    "s3_left": "STEIGEN LASSEN", "s3_right": "AUFBAUEN", "s3_left_meta": "landet irgendwo als Müll", "s3_right_meta": "bleibt, und wird aufgeräumt",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["Massenstart", "Weil der Kunde fragt"], "s3_new_tags": ["Ballon-Drop", "Fotomoment", "Verankert", "Zerschneiden und weg"],
    "s3_new_quote": "“Wir lassen nichts steigen. Wir bauen etwas, das stehen bleibt, und räumen es danach selbst auf.”", "s3_new_badge": "Code of Best Practice",
    "s3_changed_bottom": "Gleiches Wow, gleicher Kunde.\nKein Ballon, der irgendwo landet.",
    "s3_topic_lbl": "WARUM", "s3_rule1_topic": "Müll", "s3_rule1_old": "Latex baut sich doch ab",
    "s3_rule1_quote": "“Der Abbau dauert Monate. Die ganze Zeit liegt der Ballon auf einer Wiese oder im Wasser.”",
    "s3_rule2_topic": "Alternative", "s3_rule2_old": "Ohne Massenstart kein Wow-Moment",
    "s3_rule2_quote": "“Ballon-Drop, Fotomoment, verankertes Design oder Gedenkmoment: dasselbe Wow, drinnen und aufgeräumt.”",
    "s3_example_lbl": "BEISPIEL", "s3_example_quote": "“100 R12 in {p0}, {p1}, {p2} und {p3} in einem Netz über der Tanzfläche. Fällt im richtigen Moment, und kommt danach in den Müllsack.”",
    "s3_client_lbl": "KUNDE", "s3_client_topic": "Kundengespräch",
    "s3_client_quote": "“Nein sagen ist leicht, wenn du sofort etwas Schöneres vorschlagen kannst.”",
    "s3_cta_kicker": "Bau die Alternative für dein nächstes Event",
    "net_lbl": "Netz", "weight_lbl": "Gewicht", "litter_lbl": "Müll", "drop_lbl": "Ballon-Drop", "mem_lbl": "verankert",
},
"fr": {
    "cover_pills": ["Jamais de lâcher…", "4 alternatives…", "Couper et jeter…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Notre position…",
    "steps_title": "Nous ne participons à aucun lâcher de ballons. D'aucune sorte.", "steps_lead": "Notre position, en 4 phrases :",
    "steps": ["Nous n'organisons, ne promouvons ni ne soutenons aucun lâcher", "Nous demandons à nos clients de faire pareil", "Cela suit le European Code of Best Practice du secteur", "Un client demande un lâcher ? La réponse est non, avec une meilleure alternative à la clé"],
    "steps_label": "La position",
    "rule1_label": "Pourquoi", "rule1_title": "Chaque ballon lâché atterrit quelque part comme déchet",
    "rule1_body": "Une fois lâché, un ballon devient un déchet qui retombe quelque part, souvent dans une réserve naturelle ou dans l'eau, où il met des animaux en danger. Le latex est naturel et biodégradable, mais ça ne change rien : la dégradation prend des mois, et pendant tout ce temps le ballon est là où il ne devrait pas être. Dans de plus en plus de pays et de communes, les lâchers sont tout simplement interdits.",
    "rule1_facts": [["chaque", "ballon lâché atterrit quelque part comme déchet"], ["des mois", "pour que le latex se dégrade"], ["nature et eau", "là où il retombe le plus souvent"], ["non", "notre réponse à chaque demande"]],
    "rule2_label": "Alternatives", "rule2_title": "4 alternatives plus belles qu'un lâcher",
    "rule2_body": "Pour un moment symbolique ou spectaculaire, tu n'as pas besoin d'un lâcher.",
    "alts": [["Balloon drop", "des centaines de ballons tombent d'un filet au bon moment. En intérieur, et nettoyé ensuite."], ["Moment photo à l'air", "backdrop, arche ou installation où les invités se prennent en photo. Reste en place toute la journée."], ["Créations hélium lestées", "clusters et décor flottant, chaque pièce attachée à son poids. 0 risque de s'envoler."], ["Moment de recueillement", "1 création lestée dans un lieu qui compte, retirée ensuite volontairement. Plus personnel et plus respectueux."]],
    "example_label": "Exemple", "example_title": "Comment monter l'alternative",
    "ex_drop_title": "Balloon drop", "ex_drop_body": "100 × R12 en {p0}, {p1}, {p2} et {p3}, dans un filet au-dessus de la piste. Tombe au bon moment, en intérieur, et part ensuite dans le sac poubelle.",
    "ex_mem_title": "Moment de recueillement", "ex_mem_body": "3 × R12 en {p0} sur un poids, à l'endroit qui compte. Après le moment, tu le retires volontairement.",
    "example_body": "Après chaque événement, la même règle : couper les ballons utilisés et les mettre aux déchets ménagers, avec les accessoires et l'emballage. Ainsi rien ne devient un déchet sauvage.",
    "client_label": "Discussion client", "client_title": "Ce que tu réponds quand le client demande",
    "client_answers": [
        "On ne le fait pas, et je t'explique volontiers pourquoi : chaque ballon lâché atterrit quelque part comme déchet. Pour papy, je te propose 1 création lestée à l'endroit qui comptait pour lui, et après, on la retire ensemble.",
        "C'est joli 10 secondes, puis tout finit dans un champ ou dans l'eau. Je te monte un balloon drop : des centaines de ballons qui tombent d'un filet au bon moment, en intérieur, avec le même effet wow.",
        "Le latex est naturel et se dégrade, mais ça prend des mois. Pendant tout ce temps, le ballon est là où il ne devrait pas être. On préfère donc monter quelque chose qui reste en place et qu'on nettoie ensuite.",
    ],
    "avoid_lead": "Le Code of Best Practice, en 5 règles :",
    "steps5": ["Ne jamais lâcher de ballons", "Gonfler en sécurité, avec une pompe", "Ne jamais inhaler d'hélium", "Surveiller les enfants de moins de 8 ans", "Couper après usage et mettre aux déchets ménagers"],
    "client_body": "Du matériel PartySafe officiel pour ton studio ou ta boutique : une affiche, une carte d'entretien et une brochure pour les clients, et des stickers pour l'emballage. Sur partysafe.eu/balloons.",
    "cta_label": "Commander",
    "s3_cover_a": "Ballons Sempertex", "s3_cover_b": "lâchés", "s3_cover_c": "vs.", "s3_cover_d": "montés",
    "s3_left": "LÂCHÉS", "s3_right": "MONTÉS", "s3_left_meta": "atterrit quelque part comme déchet", "s3_right_meta": "reste en place, puis nettoyé",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["Lâcher", "Parce que le client le demande"], "s3_new_tags": ["Balloon drop", "Moment photo", "Lesté", "Couper et jeter"],
    "s3_new_quote": "“On ne lâche rien. On monte quelque chose qui reste en place, et on le nettoie nous-mêmes ensuite.”", "s3_new_badge": "Code of Best Practice",
    "s3_changed_bottom": "Même effet wow, même client.\nAucun ballon qui atterrit quelque part.",
    "s3_topic_lbl": "POURQUOI", "s3_rule1_topic": "Déchet", "s3_rule1_old": "Le latex se dégrade de toute façon",
    "s3_rule1_quote": "“La dégradation prend des mois. Pendant tout ce temps, le ballon est dans un champ ou dans l'eau.”",
    "s3_rule2_topic": "Alternative", "s3_rule2_old": "Sans lâcher, pas d'effet wow",
    "s3_rule2_quote": "“Balloon drop, moment photo, création lestée ou recueillement : le même wow, en intérieur et nettoyé.”",
    "s3_example_lbl": "EXEMPLE", "s3_example_quote": "“100 R12 en {p0}, {p1}, {p2} et {p3} dans un filet au-dessus de la piste. Tombe au bon moment, et part ensuite dans le sac poubelle.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Discussion client",
    "s3_client_quote": "“Dire non est facile quand tu peux proposer tout de suite quelque chose de plus beau.”",
    "s3_cta_kicker": "Monte l'alternative pour ton prochain événement",
    "net_lbl": "filet", "weight_lbl": "poids", "litter_lbl": "déchet", "drop_lbl": "balloon drop", "mem_lbl": "lesté",
},
"it": {
    "cover_pills": ["Mai liberarli…", "4 alternative…", "Taglia e butta…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "La nostra posizione…",
    "steps_title": "Non partecipiamo a lanci di palloncini. Di nessun tipo.", "steps_lead": "La nostra posizione, in 4 frasi:",
    "steps": ["Non organizziamo, promuoviamo né sosteniamo lanci", "Chiediamo ai nostri clienti di fare lo stesso", "Segue lo European Code of Best Practice del settore", "Un cliente chiede un lancio? La risposta è no, con un'alternativa migliore allegata"],
    "steps_label": "La posizione",
    "rule1_label": "Perché", "rule1_title": "Ogni palloncino liberato atterra da qualche parte come rifiuto",
    "rule1_body": "Una volta liberato, un palloncino diventa un rifiuto che cade da qualche parte, spesso in una riserva naturale o in acqua, dove mette in pericolo gli animali. Il lattice è naturale e biodegradabile, ma non cambia nulla: la degradazione richiede mesi, e per tutto quel tempo il palloncino sta dove non dovrebbe. In sempre più paesi e comuni i lanci sono semplicemente vietati.",
    "rule1_facts": [["ogni", "palloncino liberato atterra da qualche parte come rifiuto"], ["mesi", "perché il lattice si degradi"], ["natura e acqua", "dove di solito cade"], ["no", "la nostra risposta a ogni richiesta"]],
    "rule2_label": "Alternative", "rule2_title": "4 alternative più belle di un lancio",
    "rule2_body": "Per un momento simbolico o spettacolare non serve un lancio.",
    "alts": [["Balloon drop", "centinaia di palloncini cadono da una rete al momento giusto. Al chiuso, e ripuliti dopo."], ["Momento foto ad aria", "backdrop, arco o installazione dove gli ospiti si fotografano. Resta su tutto il giorno."], ["Composizioni a elio zavorrate", "cluster e decori volanti, ogni pezzo legato al suo peso. 0 rischio che voli via."], ["Momento di ricordo", "1 composizione zavorrata in un luogo significativo, rimossa dopo di proposito. Più personale e rispettoso."]],
    "example_label": "Esempio", "example_title": "Come costruire l'alternativa",
    "ex_drop_title": "Balloon drop", "ex_drop_body": "100 × R12 in {p0}, {p1}, {p2} e {p3}, in una rete sopra la pista. Cade al momento giusto, al chiuso, e poi finisce nel sacco dei rifiuti.",
    "ex_mem_title": "Momento di ricordo", "ex_mem_body": "3 × R12 in {p0} su un peso, nel posto che conta. Dopo il momento lo rimuovi di proposito.",
    "example_body": "Dopo ogni evento vale la stessa regola: tagliare i palloncini usati e metterli nell'indifferenziata, insieme ad accessori e confezioni. Così niente diventa un rifiuto abbandonato.",
    "client_label": "Dialogo con il cliente", "client_title": "Cosa rispondi quando il cliente chiede",
    "client_answers": [
        "Non lo facciamo, e ti spiego volentieri perché: ogni palloncino liberato atterra da qualche parte come rifiuto. Per il nonno propongo 1 composizione zavorrata nel posto che contava per lui, e dopo la togliamo insieme.",
        "È bello per 10 secondi e poi finisce tutto in un prato o in acqua. Ti costruisco un balloon drop: centinaia di palloncini che cadono da una rete al momento giusto, al chiuso, con lo stesso wow.",
        "Il lattice è naturale e si degrada, ma ci vogliono mesi. Per tutto quel tempo il palloncino sta dove non dovrebbe. Per questo preferiamo costruire qualcosa che resta su e poi viene ripulito.",
    ],
    "avoid_lead": "Il Code of Best Practice, in 5 regole:",
    "steps5": ["Mai liberare palloncini", "Gonfiare in sicurezza, con una pompa", "Mai inalare elio", "Sorvegliare i bambini sotto gli 8 anni", "Dopo l'evento tagliare e mettere nell'indifferenziata"],
    "client_body": "Materiale PartySafe ufficiale per il tuo studio o negozio: un poster, una scheda di cura e una brochure per i clienti, e adesivi per le confezioni. Su partysafe.eu/balloons.",
    "cta_label": "Ordina",
    "s3_cover_a": "Palloncini Sempertex", "s3_cover_b": "liberati", "s3_cover_c": "vs.", "s3_cover_d": "costruiti",
    "s3_left": "LIBERATI", "s3_right": "COSTRUITI", "s3_left_meta": "atterra da qualche parte come rifiuto", "s3_right_meta": "resta su, e viene ripulito",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["Lancio", "Perché il cliente lo chiede"], "s3_new_tags": ["Balloon drop", "Momento foto", "Zavorrato", "Taglia e butta"],
    "s3_new_quote": "“Non liberiamo nulla. Costruiamo qualcosa che resta su, e lo ripuliamo noi stessi dopo.”", "s3_new_badge": "Code of Best Practice",
    "s3_changed_bottom": "Stesso wow, stesso cliente.\nNessun palloncino che atterra da qualche parte.",
    "s3_topic_lbl": "PERCHÉ", "s3_rule1_topic": "Rifiuto", "s3_rule1_old": "Il lattice si degrada comunque",
    "s3_rule1_quote": "“La degradazione richiede mesi. Per tutto quel tempo il palloncino sta in un prato o in acqua.”",
    "s3_rule2_topic": "Alternativa", "s3_rule2_old": "Senza lancio niente momento wow",
    "s3_rule2_quote": "“Balloon drop, momento foto, composizione zavorrata o momento di ricordo: lo stesso wow, al chiuso e ripulito.”",
    "s3_example_lbl": "ESEMPIO", "s3_example_quote": "“100 R12 in {p0}, {p1}, {p2} e {p3} in una rete sopra la pista. Cade al momento giusto, e poi finisce nel sacco dei rifiuti.”",
    "s3_client_lbl": "CLIENTE", "s3_client_topic": "Dialogo con il cliente",
    "s3_client_quote": "“Dire di no è facile quando puoi proporre subito qualcosa di più bello.”",
    "s3_cta_kicker": "Costruisci l'alternativa per il tuo prossimo evento",
    "net_lbl": "rete", "weight_lbl": "peso", "litter_lbl": "rifiuto", "drop_lbl": "balloon drop", "mem_lbl": "zavorrato",
},
"pl": {
    "cover_pills": ["Nigdy nie wypuszczaj…", "4 alternatywy…", "Przetnij i wyrzuć…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Nasze stanowisko…",
    "steps_title": "Nie bierzemy udziału w wypuszczaniu balonów. Żadnego rodzaju.", "steps_lead": "Nasze stanowisko, w 4 zdaniach:",
    "steps": ["Nie organizujemy, nie promujemy i nie wspieramy wypuszczania balonów", "Prosimy naszych klientów o to samo", "To wynika z branżowego European Code of Best Practice", "Klient prosi o wypuszczenie balonów? Odpowiedź brzmi nie, z lepszą alternatywą w zamian"],
    "steps_label": "Stanowisko",
    "rule1_label": "Dlaczego", "rule1_title": "Każdy wypuszczony balon ląduje gdzieś jako śmieć",
    "rule1_body": "Raz wypuszczony balon staje się odpadem, który gdzieś spada, często w rezerwacie przyrody albo w wodzie, gdzie zagraża zwierzętom. Lateks jest naturalny i biodegradowalny, ale to nic nie zmienia: rozkład trwa miesiące, a przez cały ten czas balon leży tam, gdzie nie powinien. W coraz większej liczbie krajów i gmin wypuszczanie balonów jest po prostu zakazane.",
    "rule1_facts": [["każdy", "wypuszczony balon ląduje gdzieś jako śmieć"], ["miesiące", "trwa rozkład lateksu"], ["przyroda i woda", "tam zwykle spada"], ["nie", "nasza odpowiedź na każdą prośbę"]],
    "rule2_label": "Alternatywy", "rule2_title": "4 alternatywy piękniejsze niż wypuszczanie",
    "rule2_body": "Na symboliczny albo spektakularny moment nie potrzebujesz wypuszczania balonów.",
    "alts": [["Balloon drop", "setki balonów spadają z siatki w odpowiednim momencie. W środku, a potem sprzątnięte."], ["Fotościanka na powietrze", "ścianka, łuk albo instalacja, przy której goście robią zdjęcia. Stoi cały dzień."], ["Obciążone dekoracje helowe", "klastry i unoszący się dekor, każdy element przy własnym obciążniku. 0 ryzyka, że odleci."], ["Moment pamięci", "1 obciążona dekoracja w ważnym miejscu, potem celowo zabrana. Bardziej osobiście i z szacunkiem."]],
    "example_label": "Przykład", "example_title": "Jak zbudować alternatywę",
    "ex_drop_title": "Balloon drop", "ex_drop_body": "100 × R12 w kolorach {p0}, {p1}, {p2} i {p3}, w siatce nad parkietem. Spada w odpowiednim momencie, w środku, a potem trafia do worka na śmieci.",
    "ex_mem_title": "Moment pamięci", "ex_mem_body": "3 × R12 w kolorze {p0} na obciążniku, w miejscu, które się liczy. Po tym momencie celowo go zabierasz.",
    "example_body": "Po każdym evencie obowiązuje ta sama zasada: zużyte balony przeciąć i wyrzucić do odpadów zmieszanych, razem z akcesoriami i opakowaniem. Dzięki temu nic nie staje się śmieciem w naturze.",
    "client_label": "Rozmowa z klientem", "client_title": "Co odpowiadasz, gdy klient pyta",
    "client_answers": [
        "Tego nie robimy i chętnie wyjaśnię dlaczego: każdy wypuszczony balon ląduje gdzieś jako śmieć. Dla dziadka proponuję 1 obciążoną dekorację w miejscu, które było dla niego ważne, a potem zabieramy ją razem.",
        "Przez 10 sekund wygląda pięknie, a potem wszystko leży gdzieś na łące albo w wodzie. Zbuduję ci balloon drop: setki balonów spadających z siatki w odpowiednim momencie, w środku, z tym samym efektem wow.",
        "Lateks jest naturalny i się rozkłada, ale to trwa miesiące. Przez cały ten czas balon leży tam, gdzie nie powinien. Dlatego wolimy zbudować coś, co stoi, a potem zostaje sprzątnięte.",
    ],
    "avoid_lead": "Code of Best Practice, w 5 zasadach:",
    "steps5": ["Nigdy nie wypuszczaj balonów", "Pompuj bezpiecznie, pompką", "Nigdy nie wdychaj helu", "Dzieci poniżej 8 lat pod opieką", "Po evencie przetnij i wyrzuć do odpadów zmieszanych"],
    "client_body": "Oficjalne materiały PartySafe dla twojego studia albo sklepu: plakat, karta i broszura dla klientów oraz naklejki na opakowania. Na partysafe.eu/balloons.",
    "cta_label": "Zamów",
    "s3_cover_a": "Balony Sempertex", "s3_cover_b": "wypuszczone", "s3_cover_c": "vs.", "s3_cover_d": "zbudowane",
    "s3_left": "WYPUSZCZONE", "s3_right": "ZBUDOWANE", "s3_left_meta": "ląduje gdzieś jako śmieć", "s3_right_meta": "stoi, potem sprzątnięte",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "STARE", "s3_new_lbl": "NOWE",
    "s3_old_tags": ["Wypuszczanie", "Bo klient prosi"], "s3_new_tags": ["Balloon drop", "Fotościanka", "Obciążone", "Przetnij i wyrzuć"],
    "s3_new_quote": "“Niczego nie wypuszczamy. Budujemy coś, co stoi, i sami to potem sprzątamy.”", "s3_new_badge": "Code of Best Practice",
    "s3_changed_bottom": "Ten sam efekt wow, ten sam klient.\nŻaden balon nigdzie nie ląduje.",
    "s3_topic_lbl": "DLACZEGO", "s3_rule1_topic": "Śmieci", "s3_rule1_old": "Lateks i tak się rozkłada",
    "s3_rule1_quote": "“Rozkład trwa miesiące. Przez cały ten czas balon leży na łące albo w wodzie.”",
    "s3_rule2_topic": "Alternatywa", "s3_rule2_old": "Bez wypuszczania nie ma efektu wow",
    "s3_rule2_quote": "“Balloon drop, fotościanka, obciążona dekoracja albo moment pamięci: ten sam efekt wow, w środku i sprzątnięte.”",
    "s3_example_lbl": "PRZYKŁAD", "s3_example_quote": "“100 R12 w kolorach {p0}, {p1}, {p2} i {p3} w siatce nad parkietem. Spada w odpowiednim momencie, a potem trafia do worka na śmieci.”",
    "s3_client_lbl": "KLIENT", "s3_client_topic": "Rozmowa z klientem",
    "s3_client_quote": "“Łatwo powiedzieć nie, gdy od razu możesz zaproponować coś piękniejszego.”",
    "s3_cta_kicker": "Zbuduj alternatywę na swój następny event",
    "net_lbl": "siatka", "weight_lbl": "obciążnik", "litter_lbl": "śmieć", "drop_lbl": "balloon drop", "mem_lbl": "obciążone",
},
"el": {
    "cover_pills": ["Ποτέ απελευθέρωση…", "4 εναλλακτικές…", "Κόψε και πέτα…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Η θέση μας…",
    "steps_title": "Δεν συμμετέχουμε σε απελευθερώσεις μπαλονιών. Κανενός είδους.", "steps_lead": "Η θέση μας, σε 4 προτάσεις:",
    "steps": ["Δεν οργανώνουμε, δεν προωθούμε και δεν στηρίζουμε απελευθερώσεις", "Ζητάμε από τους πελάτες μας να κάνουν το ίδιο", "Αυτό ακολουθεί τον European Code of Best Practice του κλάδου", "Ένας πελάτης ζητά απελευθέρωση; Η απάντηση είναι όχι, μαζί με μια καλύτερη εναλλακτική"],
    "steps_label": "Η θέση",
    "rule1_label": "Γιατί", "rule1_title": "Κάθε μπαλόνι που απελευθερώνεται πέφτει κάπου ως σκουπίδι",
    "rule1_body": "Μόλις απελευθερωθεί, ένα μπαλόνι γίνεται απόβλητο που πέφτει κάπου, συχνά σε προστατευόμενη περιοχή ή στο νερό, όπου βάζει ζώα σε κίνδυνο. Το latex είναι φυσικό και βιοδιασπώμενο, αλλά αυτό δεν αλλάζει τίποτα: η διάσπαση παίρνει μήνες, και όλο αυτό το διάστημα το μπαλόνι βρίσκεται εκεί που δεν πρέπει. Σε όλο και περισσότερες χώρες και δήμους οι απελευθερώσεις είναι απλώς απαγορευμένες.",
    "rule1_facts": [["κάθε", "μπαλόνι που απελευθερώνεται πέφτει κάπου ως σκουπίδι"], ["μήνες", "παίρνει η διάσπαση του latex"], ["φύση και νερό", "εκεί πέφτει συνήθως"], ["όχι", "η απάντησή μας σε κάθε αίτημα"]],
    "rule2_label": "Εναλλακτικές", "rule2_title": "4 εναλλακτικές πιο όμορφες από μια απελευθέρωση",
    "rule2_body": "Για μια συμβολική ή θεαματική στιγμή δεν χρειάζεσαι απελευθέρωση.",
    "alts": [["Balloon drop", "εκατοντάδες μπαλόνια πέφτουν από δίχτυ την κατάλληλη στιγμή. Σε εσωτερικό χώρο, και μετά μαζεύονται."], ["Φωτογραφική στιγμή με αέρα", "backdrop, αψίδα ή κατασκευή όπου οι καλεσμένοι φωτογραφίζονται. Μένει όλη μέρα."], ["Αγκυρωμένες κατασκευές ηλίου", "clusters και αιωρούμενη διακόσμηση, κάθε κομμάτι δεμένο σε δικό του βαρίδι. 0 κίνδυνος να φύγει."], ["Στιγμή μνήμης", "1 αγκυρωμένη κατασκευή σε σημαντικό μέρος, που αφαιρείται μετά συνειδητά. Πιο προσωπικό και με σεβασμό."]],
    "example_label": "Παράδειγμα", "example_title": "Έτσι στήνεις την εναλλακτική",
    "ex_drop_title": "Balloon drop", "ex_drop_body": "100 × R12 σε {p0}, {p1}, {p2} και {p3}, σε δίχτυ πάνω από την πίστα. Πέφτει την κατάλληλη στιγμή, σε εσωτερικό χώρο, και μετά πάει στη σακούλα σκουπιδιών.",
    "ex_mem_title": "Στιγμή μνήμης", "ex_mem_body": "3 × R12 σε {p0} πάνω σε βαρίδι, στο μέρος που μετράει. Μετά τη στιγμή το αφαιρείς συνειδητά.",
    "example_body": "Μετά από κάθε εκδήλωση ισχύει ο ίδιος κανόνας: κόβεις τα χρησιμοποιημένα μπαλόνια και τα βάζεις στα κοινά απορρίμματα, μαζί με αξεσουάρ και συσκευασία. Έτσι τίποτα δεν γίνεται σκουπίδι στη φύση.",
    "client_label": "Συζήτηση με πελάτη", "client_title": "Τι απαντάς όταν ο πελάτης ρωτά",
    "client_answers": [
        "Αυτό δεν το κάνουμε, και σου εξηγώ ευχαρίστως γιατί: κάθε μπαλόνι που απελευθερώνεται πέφτει κάπου ως σκουπίδι. Για τον παππού προτείνω 1 αγκυρωμένη κατασκευή στο μέρος που μετρούσε για εκείνον, και μετά την αφαιρούμε μαζί.",
        "Είναι όμορφο για 10 δευτερόλεπτα και μετά όλα καταλήγουν σε ένα χωράφι ή στο νερό. Σου στήνω ένα balloon drop: εκατοντάδες μπαλόνια που πέφτουν από δίχτυ την κατάλληλη στιγμή, σε εσωτερικό χώρο, με το ίδιο wow.",
        "Το latex είναι φυσικό και διασπάται, αλλά αυτό παίρνει μήνες. Όλο αυτό το διάστημα το μπαλόνι βρίσκεται εκεί που δεν πρέπει. Γι' αυτό προτιμάμε να στήσουμε κάτι που μένει και μετά μαζεύεται.",
    ],
    "avoid_lead": "Ο Code of Best Practice, σε 5 κανόνες:",
    "steps5": ["Ποτέ απελευθέρωση μπαλονιών", "Ασφαλές φούσκωμα, με τρόμπα", "Ποτέ εισπνοή ηλίου", "Παιδιά κάτω των 8 υπό επίβλεψη", "Μετά, κόψιμο και στα κοινά απορρίμματα"],
    "client_body": "Επίσημο υλικό PartySafe για το στούντιο ή το κατάστημά σου: αφίσα, κάρτα φροντίδας και φυλλάδιο για πελάτες, και αυτοκόλλητα για τη συσκευασία. Στο partysafe.eu/balloons.",
    "cta_label": "Παραγγελία",
    "s3_cover_a": "Μπαλόνια Sempertex", "s3_cover_b": "απελευθέρωση", "s3_cover_c": "vs.", "s3_cover_d": "κατασκευή",
    "s3_left": "ΑΠΕΛΕΥΘΕΡΩΣΗ", "s3_right": "ΚΑΤΑΣΚΕΥΗ", "s3_left_meta": "πέφτει κάπου ως σκουπίδι", "s3_right_meta": "μένει, και μαζεύεται",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["Απελευθέρωση", "Επειδή το ζητά ο πελάτης"], "s3_new_tags": ["Balloon drop", "Φωτογραφική στιγμή", "Αγκυρωμένο", "Κόψε και πέτα"],
    "s3_new_quote": "“Δεν απελευθερώνουμε τίποτα. Στήνουμε κάτι που μένει, και το μαζεύουμε μετά μόνοι μας.”", "s3_new_badge": "Code of Best Practice",
    "s3_changed_bottom": "Ίδιο wow, ίδιος πελάτης.\nΚανένα μπαλόνι δεν πέφτει κάπου.",
    "s3_topic_lbl": "ΓΙΑΤΙ", "s3_rule1_topic": "Σκουπίδι", "s3_rule1_old": "Το latex διασπάται έτσι κι αλλιώς",
    "s3_rule1_quote": "“Η διάσπαση παίρνει μήνες. Όλο αυτό το διάστημα το μπαλόνι είναι σε ένα χωράφι ή στο νερό.”",
    "s3_rule2_topic": "Εναλλακτική", "s3_rule2_old": "Χωρίς απελευθέρωση δεν υπάρχει wow",
    "s3_rule2_quote": "“Balloon drop, φωτογραφική στιγμή, αγκυρωμένη κατασκευή ή στιγμή μνήμης: το ίδιο wow, σε εσωτερικό χώρο και μαζεμένο.”",
    "s3_example_lbl": "ΠΑΡΑΔΕΙΓΜΑ", "s3_example_quote": "“100 R12 σε {p0}, {p1}, {p2} και {p3} σε δίχτυ πάνω από την πίστα. Πέφτει την κατάλληλη στιγμή, και μετά πάει στη σακούλα σκουπιδιών.”",
    "s3_client_lbl": "ΠΕΛΑΤΗΣ", "s3_client_topic": "Συζήτηση με πελάτη",
    "s3_client_quote": "“Το όχι είναι εύκολο όταν μπορείς αμέσως να προτείνεις κάτι πιο όμορφο.”",
    "s3_cta_kicker": "Στήσε την εναλλακτική για την επόμενη εκδήλωσή σου",
    "net_lbl": "δίχτυ", "weight_lbl": "βαρίδι", "litter_lbl": "σκουπίδι", "drop_lbl": "balloon drop", "mem_lbl": "αγκυρωμένο",
},
"hu": {
    "cover_pills": ["Soha ne engedd el…", "4 alternatíva…", "Vágd el és dobd ki…"], "cover_with": "partner:", "cover_brand": "Sempertex Europe", "cover_tag": "Az álláspontunk…",
    "steps_title": "Nem veszünk részt lufieregetésben. Semmilyenben.", "steps_lead": "Az álláspontunk, 4 mondatban:",
    "steps": ["Nem szervezünk, nem népszerűsítünk és nem támogatunk eregetést", "Az ügyfeleinktől ugyanezt kérjük", "Ez a szakma European Code of Best Practice-ét követi", "Egy ügyfél eregetést kér? A válasz nem, egy jobb alternatívával együtt"],
    "steps_label": "Az álláspont",
    "rule1_label": "Miért", "rule1_title": "Minden elengedett lufi valahol szemétként landol",
    "rule1_body": "Ha egyszer elengeded, a lufi hulladékká válik, ami valahol leesik, gyakran természetvédelmi területen vagy vízben, ahol állatokat veszélyeztet. A latex természetes és biológiailag lebomló, de ez semmin nem változtat: a lebomlás hónapokig tart, és egész idő alatt ott fekszik a lufi, ahol nem kellene. Egyre több országban és településen az eregetés egyszerűen tilos.",
    "rule1_facts": [["minden", "elengedett lufi valahol szemétként landol"], ["hónapok", "amíg a latex lebomlik"], ["természet és víz", "ahol általában leesik"], ["nem", "a válaszunk minden kérésre"]],
    "rule2_label": "Alternatívák", "rule2_title": "4 alternatíva, ami szebb az eregetésnél",
    "rule2_body": "Egy szimbolikus vagy látványos pillanathoz nincs szükséged eregetésre.",
    "alts": [["Lufiesés", "több száz lufi hullik egy hálóból a megfelelő pillanatban. Beltéren, és utána összeszedve."], ["Levegős fotópont", "háttér, ív vagy installáció, ahol a vendégek fotóznak. Egész nap áll."], ["Rögzített héliumos dekorációk", "klaszterek és lebegő dekor, minden darab saját nehezékhez kötve. 0 esély az elszállásra."], ["Emlékező pillanat", "1 rögzített dekoráció egy fontos helyen, utána tudatosan eltávolítva. Személyesebb és tiszteletteljesebb."]],
    "example_label": "Példa", "example_title": "Így építed meg az alternatívát",
    "ex_drop_title": "Lufiesés", "ex_drop_body": "100 × R12 {p0}, {p1}, {p2} és {p3} színben, hálóban a táncparkett fölött. A megfelelő pillanatban hullik, beltéren, utána pedig a szemeteszsákba kerül.",
    "ex_mem_title": "Emlékező pillanat", "ex_mem_body": "3 × R12 {p0} színben nehezéken, azon a helyen, ami számít. A pillanat után tudatosan elviszed.",
    "example_body": "Minden rendezvény után ugyanaz a szabály: a használt lufikat elvágod és a vegyes hulladékba teszed, a kellékekkel és a csomagolással együtt. Így semmi nem lesz szemét a természetben.",
    "client_label": "Ügyfélbeszélgetés", "client_title": "Mit válaszolsz, ha az ügyfél megkérdezi",
    "client_answers": [
        "Ezt nem csináljuk, és szívesen elmondom, miért: minden elengedett lufi valahol szemétként landol. A nagypapának 1 rögzített dekorációt javaslok azon a helyen, ami neki fontos volt, utána pedig együtt szedjük le.",
        "10 másodpercig szép, aztán minden egy mezőn vagy a vízben köt ki. Építek neked egy lufiesést: több száz lufi hullik egy hálóból a megfelelő pillanatban, beltéren, ugyanazzal a wow-val.",
        "A latex természetes és lebomlik, de az hónapokig tart. Egész idő alatt ott fekszik a lufi, ahol nem kellene. Ezért inkább olyat építünk, ami áll, és utána összeszedjük.",
    ],
    "avoid_lead": "A Code of Best Practice, 5 szabályban:",
    "steps5": ["Soha ne engedj el lufit", "Fújd fel biztonságosan, pumpával", "Soha ne lélegezz be héliumot", "8 év alatti gyerekek felügyelettel", "Utána vágd el és tedd a vegyes hulladékba"],
    "client_body": "Hivatalos PartySafe anyagok a stúdiódba vagy üzletedbe: poszter, gondozási kártya és brosúra az ügyfeleknek, matricák a csomagolásra. A partysafe.eu/balloons oldalon.",
    "cta_label": "Rendelés",
    "s3_cover_a": "Sempertex lufik", "s3_cover_b": "elengedve", "s3_cover_c": "vs.", "s3_cover_d": "megépítve",
    "s3_left": "ELENGEDVE", "s3_right": "MEGÉPÍTVE", "s3_left_meta": "valahol szemétként landol", "s3_right_meta": "áll, és összeszedik",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "RÉGI", "s3_new_lbl": "ÚJ",
    "s3_old_tags": ["Eregetés", "Mert az ügyfél kéri"], "s3_new_tags": ["Lufiesés", "Fotópont", "Rögzített", "Vágd el és dobd ki"],
    "s3_new_quote": "“Semmit nem engedünk el. Olyat építünk, ami áll, és utána magunk szedjük össze.”", "s3_new_badge": "Code of Best Practice",
    "s3_changed_bottom": "Ugyanaz a wow, ugyanaz az ügyfél.\nEgyetlen lufi sem landol sehol.",
    "s3_topic_lbl": "MIÉRT", "s3_rule1_topic": "Szemét", "s3_rule1_old": "A latex úgyis lebomlik",
    "s3_rule1_quote": "“A lebomlás hónapokig tart. Egész idő alatt a lufi egy mezőn vagy a vízben fekszik.”",
    "s3_rule2_topic": "Alternatíva", "s3_rule2_old": "Eregetés nélkül nincs wow pillanat",
    "s3_rule2_quote": "“Lufiesés, fotópont, rögzített dekoráció vagy emlékező pillanat: ugyanaz a wow, beltéren és összeszedve.”",
    "s3_example_lbl": "PÉLDA", "s3_example_quote": "“100 R12 {p0}, {p1}, {p2} és {p3} színben hálóban a táncparkett fölött. A megfelelő pillanatban hullik, utána a szemeteszsákba kerül.”",
    "s3_client_lbl": "ÜGYFÉL", "s3_client_topic": "Ügyfélbeszélgetés",
    "s3_client_quote": "“Könnyű nemet mondani, ha rögtön valami szebbet tudsz ajánlani.”",
    "s3_cta_kicker": "Építsd meg az alternatívát a következő rendezvényedre",
    "net_lbl": "háló", "weight_lbl": "nehezék", "litter_lbl": "szemét", "drop_lbl": "lufiesés", "mem_lbl": "rögzített",
},
"lt": {
    "cover_pills": ["Niekada nepaleisk…", "4 alternatyvos…", "Perkirpk ir išmesk…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Mūsų pozicija…",
    "steps_title": "Mes nedalyvaujame balionų paleidimuose. Jokiuose.", "steps_lead": "Mūsų pozicija, 4 sakiniais:",
    "steps": ["Neorganizuojame, nereklamuojame ir neremiame paleidimų", "Prašome savo klientų daryti tą patį", "Tai atitinka sektoriaus European Code of Best Practice", "Klientas prašo paleidimo? Atsakymas yra ne, kartu su geresne alternatyva"],
    "steps_label": "Pozicija",
    "rule1_label": "Kodėl", "rule1_title": "Kiekvienas paleistas balionas kažkur nusileidžia kaip šiukšlė",
    "rule1_body": "Kartą paleistas balionas tampa atlieka, kuri kažkur nukrenta, dažnai saugomoje teritorijoje ar vandenyje, kur kelia pavojų gyvūnams. Lateksas yra natūralus ir biologiškai skaidus, bet tai nieko nekeičia: skaidymasis trunka mėnesius, ir visą tą laiką balionas guli ten, kur neturėtų. Vis daugiau šalių ir savivaldybių paleidimai yra tiesiog uždrausti.",
    "rule1_facts": [["kiekvienas", "paleistas balionas kažkur nusileidžia kaip šiukšlė"], ["mėnesiai", "trunka latekso skaidymasis"], ["gamta ir vanduo", "kur jis dažniausiai nukrenta"], ["ne", "mūsų atsakymas į kiekvieną prašymą"]],
    "rule2_label": "Alternatyvos", "rule2_title": "4 alternatyvos, gražesnės už paleidimą",
    "rule2_body": "Simbolinei ar įspūdingai akimirkai paleidimo nereikia.",
    "alts": [["Balloon drop", "šimtai balionų tinkamu momentu krenta iš tinklo. Patalpoje, o po to sutvarkoma."], ["Oru pripūsta foto zona", "fonas, arka ar instaliacija, kur svečiai fotografuojasi. Stovi visą dieną."], ["Pritvirtintos helio dekoracijos", "klasteriai ir skrendantis dekoras, kiekviena dalis pririšta prie savo svarelio. 0 rizikos nuskristi."], ["Atminimo akimirka", "1 pritvirtinta dekoracija reikšmingoje vietoje, po to sąmoningai pašalinta. Asmeniškiau ir pagarbiau."]],
    "example_label": "Pavyzdys", "example_title": "Taip sukuri alternatyvą",
    "ex_drop_title": "Balloon drop", "ex_drop_body": "100 × R12 {p0}, {p1}, {p2} ir {p3} spalvomis, tinkle virš šokių aikštelės. Krenta tinkamu momentu, patalpoje, o po to keliauja į šiukšlių maišą.",
    "ex_mem_title": "Atminimo akimirka", "ex_mem_body": "3 × R12 {p0} spalvos ant svarelio, toje vietoje, kuri svarbi. Po akimirkos sąmoningai jį pašalini.",
    "example_body": "Po kiekvieno renginio galioja ta pati taisyklė: panaudotus balionus perkirpk ir išmesk į mišrias atliekas kartu su priedais ir pakuote. Taip niekas netampa šiukšle gamtoje.",
    "client_label": "Pokalbis su klientu", "client_title": "Ką atsakai, kai klientas klausia",
    "client_answers": [
        "To mes nedarome, ir mielai paaiškinsiu kodėl: kiekvienas paleistas balionas kažkur nusileidžia kaip šiukšlė. Seneliui siūlau 1 pritvirtintą dekoraciją toje vietoje, kuri jam buvo svarbi, o po to ją nuimame kartu.",
        "10 sekundžių gražu, o paskui viskas guli kažkur pievoje ar vandenyje. Sukursiu tau balloon drop: šimtai balionų, tinkamu momentu krentančių iš tinklo, patalpoje, su tuo pačiu wow.",
        "Lateksas natūralus ir suyra, bet tai trunka mėnesius. Visą tą laiką balionas guli ten, kur neturėtų. Todėl mieliau statome kažką, kas stovi ir po to sutvarkoma.",
    ],
    "avoid_lead": "Code of Best Practice, 5 taisyklėmis:",
    "steps5": ["Niekada nepaleisk balionų", "Pūsk saugiai, su pompa", "Niekada neįkvėpk helio", "Vaikai iki 8 metų prižiūrimi", "Po renginio perkirpk ir išmesk į mišrias atliekas"],
    "client_body": "Oficiali PartySafe medžiaga tavo studijai ar parduotuvei: plakatas, priežiūros kortelė ir brošiūra klientams, lipdukai pakuotėms. Adresu partysafe.eu/balloons.",
    "cta_label": "Užsakyti",
    "s3_cover_a": "Sempertex balionai", "s3_cover_b": "paleisti", "s3_cover_c": "vs.", "s3_cover_d": "sukurti",
    "s3_left": "PALEISTI", "s3_right": "SUKURTI", "s3_left_meta": "kažkur nusileidžia kaip šiukšlė", "s3_right_meta": "stovi, ir sutvarkoma",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "SENA", "s3_new_lbl": "NAUJA",
    "s3_old_tags": ["Paleidimas", "Nes klientas prašo"], "s3_new_tags": ["Balloon drop", "Foto zona", "Pritvirtinta", "Perkirpk ir išmesk"],
    "s3_new_quote": "“Nieko nepaleidžiame. Sukuriame tai, kas stovi, ir po to patys sutvarkome.”", "s3_new_badge": "Code of Best Practice",
    "s3_changed_bottom": "Tas pats wow, tas pats klientas.\nNė vienas balionas niekur nenusileidžia.",
    "s3_topic_lbl": "KODĖL", "s3_rule1_topic": "Šiukšlės", "s3_rule1_old": "Lateksas vis tiek suyra",
    "s3_rule1_quote": "“Skaidymasis trunka mėnesius. Visą tą laiką balionas guli pievoje ar vandenyje.”",
    "s3_rule2_topic": "Alternatyva", "s3_rule2_old": "Be paleidimo nėra wow akimirkos",
    "s3_rule2_quote": "“Balloon drop, foto zona, pritvirtinta dekoracija ar atminimo akimirka: tas pats wow, patalpoje ir sutvarkyta.”",
    "s3_example_lbl": "PAVYZDYS", "s3_example_quote": "“100 R12 {p0}, {p1}, {p2} ir {p3} spalvomis tinkle virš šokių aikštelės. Krenta tinkamu momentu, o po to keliauja į šiukšlių maišą.”",
    "s3_client_lbl": "KLIENTAS", "s3_client_topic": "Pokalbis su klientu",
    "s3_client_quote": "“Pasakyti ne lengva, kai iškart gali pasiūlyti kažką gražesnio.”",
    "s3_cta_kicker": "Sukurk alternatyvą kitam savo renginiui",
    "net_lbl": "tinklas", "weight_lbl": "svarelis", "litter_lbl": "šiukšlė", "drop_lbl": "balloon drop", "mem_lbl": "pritvirtinta",
},
}

# ---------------------------------------------------------------- VARIANTEN
VARIANTS = {
"nl": {
  "cover_title": ["Waarom wij geen ballonnen oplaten, en wat je met Sempertex in de plaats doet", "Elke opgelaten ballon landt ergens als afval. Het standpunt van Sempertex, en 4 alternatieven", "Geen oplatingen: zo zegt een ballonprofessional nee, en wat je met Sempertex wel bouwt"],
  "cover_sub": ["Het standpunt van Sempertex Europe, de reden erachter en 4 alternatieven die hetzelfde wow-moment geven, binnen en opgeruimd.", "Ballondrop, fotomoment, verankerd design of herdenkingsmoment. En het antwoord als een klant toch om een oplating vraagt."],
  "client_question": ["Kunnen we op het einde 50 ballonnen oplaten voor opa?", "Alle gasten tegelijk een ballon laten loslaten, dat is toch prachtig?", "Jullie ballonnen zijn toch biologisch afbreekbaar? Dan mag het toch?"],
  "s3_old_quote": ["“Latex breekt toch af”", "“Het is maar één keer”", "“De klant wil het, dus doen we het”"],
  "s3_client_old": ["“50 ballonnen voor opa? Tuurlijk”", "“Als iedereen er één loslaat is het niet erg”"],
  "cta_title_tpl": "Bestel je Sempertex ballonnen bij {name}", "cta_sub_generic": "Bouw het alternatief: ballondrop, fotomoment of verankerd design.",
},
"en": {
  "cover_title": ["Why we don't release balloons, and what you build with Sempertex instead", "Every released balloon lands somewhere as litter. Sempertex's position, and 4 alternatives", "No releases: how a balloon professional says no, and what you build with Sempertex instead"],
  "cover_sub": ["Sempertex Europe's position, the reason behind it and 4 alternatives that give the same wow moment, indoors and cleaned up.", "Balloon drop, photo moment, anchored design or memorial moment. And the answer when a client asks for a release anyway."],
  "client_question": ["Can we release 50 balloons for grandad at the end?", "All the guests letting go of a balloon at once, that's beautiful though?", "Your balloons are biodegradable, aren't they? So it's fine?"],
  "s3_old_quote": ["“Latex breaks down anyway”", "“It's only the once”", "“The client wants it, so we do it”"],
  "s3_client_old": ["“50 balloons for grandad? Sure”", "“If everyone lets one go it's no big deal”"],
  "cta_title_tpl": "Order your Sempertex balloons at {name}", "cta_sub_generic": "Build the alternative: balloon drop, photo moment or anchored design.",
},
"de": {
  "cover_title": ["Warum wir keine Ballons steigen lassen, und was du mit Sempertex stattdessen baust", "Jeder losgelassene Ballon landet irgendwo als Müll. Die Haltung von Sempertex, und 4 Alternativen", "Keine Massenstarts: So sagt ein Ballonprofi nein, und was du mit Sempertex stattdessen baust"],
  "cover_sub": ["Die Haltung von Sempertex Europe, der Grund dahinter und 4 Alternativen, die denselben Wow-Moment geben, drinnen und aufgeräumt.", "Ballon-Drop, Fotomoment, verankertes Design oder Gedenkmoment. Und die Antwort, wenn ein Kunde trotzdem nach einem Massenstart fragt."],
  "client_question": ["Können wir am Ende 50 Ballons für Opa steigen lassen?", "Alle Gäste lassen gleichzeitig einen Ballon los, das ist doch wunderschön?", "Eure Ballons sind doch biologisch abbaubar? Dann geht das doch?"],
  "s3_old_quote": ["“Latex baut sich doch ab”", "“Ist ja nur einmal”", "“Der Kunde will es, also machen wir es”"],
  "s3_client_old": ["“50 Ballons für Opa? Klar”", "“Wenn jeder einen loslässt, ist das nicht schlimm”"],
  "cta_title_tpl": "Bestell deine Sempertex Ballons bei {name}", "cta_sub_generic": "Bau die Alternative: Ballon-Drop, Fotomoment oder verankertes Design.",
},
"fr": {
  "cover_title": ["Pourquoi nous ne lâchons pas de ballons, et ce que tu montes avec Sempertex à la place", "Chaque ballon lâché atterrit quelque part comme déchet. La position de Sempertex, et 4 alternatives", "Pas de lâchers : comment un pro du ballon dit non, et ce que tu montes avec Sempertex à la place"],
  "cover_sub": ["La position de Sempertex Europe, la raison derrière, et 4 alternatives qui donnent le même effet wow, en intérieur et nettoyé.", "Balloon drop, moment photo, création lestée ou moment de recueillement. Et la réponse quand un client demande quand même un lâcher."],
  "client_question": ["On peut lâcher 50 ballons pour papy à la fin ?", "Tous les invités qui lâchent un ballon en même temps, c'est magnifique, non ?", "Vos ballons sont biodégradables, non ? Alors c'est permis ?"],
  "s3_old_quote": ["“Le latex se dégrade de toute façon”", "“C'est juste une fois”", "“Le client le veut, donc on le fait”"],
  "s3_client_old": ["“50 ballons pour papy ? Bien sûr”", "“Si chacun en lâche un, ce n'est pas grave”"],
  "cta_title_tpl": "Commande tes ballons Sempertex chez {name}", "cta_sub_generic": "Monte l'alternative : balloon drop, moment photo ou création lestée.",
},
"it": {
  "cover_title": ["Perché non liberiamo palloncini, e cosa costruisci con Sempertex al posto loro", "Ogni palloncino liberato atterra da qualche parte come rifiuto. La posizione di Sempertex, e 4 alternative", "Niente lanci: come un professionista dice di no, e cosa costruisci con Sempertex al posto loro"],
  "cover_sub": ["La posizione di Sempertex Europe, il motivo dietro e 4 alternative che danno lo stesso momento wow, al chiuso e ripulito.", "Balloon drop, momento foto, composizione zavorrata o momento di ricordo. E la risposta quando un cliente chiede comunque un lancio."],
  "client_question": ["Possiamo liberare 50 palloncini per il nonno alla fine?", "Tutti gli ospiti che liberano un palloncino insieme, è bellissimo, no?", "I vostri palloncini sono biodegradabili, no? Allora si può?"],
  "s3_old_quote": ["“Il lattice si degrada comunque”", "“È solo una volta”", "“Il cliente lo vuole, quindi lo facciamo”"],
  "s3_client_old": ["“50 palloncini per il nonno? Certo”", "“Se ognuno ne libera uno non è grave”"],
  "cta_title_tpl": "Ordina i tuoi palloncini Sempertex da {name}", "cta_sub_generic": "Costruisci l'alternativa: balloon drop, momento foto o composizione zavorrata.",
},
"pl": {
  "cover_title": ["Dlaczego nie wypuszczamy balonów i co w zamian budujesz z Sempertex", "Każdy wypuszczony balon ląduje gdzieś jako śmieć. Stanowisko Sempertex i 4 alternatywy", "Bez wypuszczania: jak profesjonalista mówi nie i co w zamian budujesz z Sempertex"],
  "cover_sub": ["Stanowisko Sempertex Europe, powód za nim i 4 alternatywy, które dają ten sam efekt wow, w środku i sprzątnięte.", "Balloon drop, fotościanka, obciążona dekoracja albo moment pamięci. I odpowiedź, gdy klient mimo to prosi o wypuszczenie."],
  "client_question": ["Możemy na koniec wypuścić 50 balonów dla dziadka?", "Wszyscy goście wypuszczają balon jednocześnie, to przecież piękne?", "Wasze balony są przecież biodegradowalne? To chyba można?"],
  "s3_old_quote": ["“Lateks i tak się rozkłada”", "“To tylko ten jeden raz”", "“Klient chce, więc robimy”"],
  "s3_client_old": ["“50 balonów dla dziadka? Jasne”", "“Jak każdy wypuści jeden, to nic takiego”"],
  "cta_title_tpl": "Zamów balony Sempertex w {name}", "cta_sub_generic": "Zbuduj alternatywę: balloon drop, fotościankę albo obciążoną dekorację.",
},
"el": {
  "cover_title": ["Γιατί δεν απελευθερώνουμε μπαλόνια, και τι στήνεις με Sempertex αντί γι' αυτό", "Κάθε μπαλόνι που απελευθερώνεται πέφτει κάπου ως σκουπίδι. Η θέση της Sempertex, και 4 εναλλακτικές", "Καμία απελευθέρωση: έτσι λέει όχι ένας επαγγελματίας, και τι στήνεις με Sempertex αντί γι' αυτό"],
  "cover_sub": ["Η θέση της Sempertex Europe, ο λόγος πίσω της και 4 εναλλακτικές που δίνουν την ίδια wow στιγμή, σε εσωτερικό χώρο και μαζεμένες.", "Balloon drop, φωτογραφική στιγμή, αγκυρωμένη κατασκευή ή στιγμή μνήμης. Και η απάντηση όταν ένας πελάτης ζητά παρ' όλα αυτά απελευθέρωση."],
  "client_question": ["Μπορούμε στο τέλος να απελευθερώσουμε 50 μπαλόνια για τον παππού;", "Όλοι οι καλεσμένοι να αφήσουν ένα μπαλόνι μαζί, δεν είναι υπέροχο;", "Τα μπαλόνια σας είναι βιοδιασπώμενα, έτσι; Άρα επιτρέπεται;"],
  "s3_old_quote": ["“Το latex διασπάται έτσι κι αλλιώς”", "“Μία φορά είναι”", "“Ο πελάτης το θέλει, άρα το κάνουμε”"],
  "s3_client_old": ["“50 μπαλόνια για τον παππού; Φυσικά”", "“Αν ο καθένας αφήσει ένα, δεν πειράζει”"],
  "cta_title_tpl": "Παράγγειλε τα μπαλόνια Sempertex σου από {name}", "cta_sub_generic": "Στήσε την εναλλακτική: balloon drop, φωτογραφική στιγμή ή αγκυρωμένη κατασκευή.",
},
"hu": {
  "cover_title": ["Miért nem eregetünk lufit, és mit építesz helyette Sempertex-szel", "Minden elengedett lufi valahol szemétként landol. A Sempertex álláspontja, és 4 alternatíva", "Nincs eregetés: így mond nemet egy profi, és mit építesz helyette Sempertex-szel"],
  "cover_sub": ["A Sempertex Europe álláspontja, az ok mögötte, és 4 alternatíva, ami ugyanazt a wow pillanatot adja, beltéren és összeszedve.", "Lufiesés, fotópont, rögzített dekoráció vagy emlékező pillanat. És a válasz, ha egy ügyfél mégis eregetést kér."],
  "client_question": ["Elengedhetünk a végén 50 lufit a nagypapáért?", "Ha minden vendég egyszerre elenged egy lufit, az gyönyörű, nem?", "A lufijaitok biológiailag lebomlók, ugye? Akkor szabad?"],
  "s3_old_quote": ["“A latex úgyis lebomlik”", "“Csak egyszer”", "“Az ügyfél akarja, hát megcsináljuk”"],
  "s3_client_old": ["“50 lufi a nagypapáért? Persze”", "“Ha mindenki egyet enged el, nem nagy ügy”"],
  "cta_title_tpl": "Rendeld a Sempertex lufijaidat innen: {name}", "cta_sub_generic": "Építsd meg az alternatívát: lufiesés, fotópont vagy rögzített dekoráció.",
},
"lt": {
  "cover_title": ["Kodėl nepaleidžiame balionų ir ką vietoj to kuri su Sempertex", "Kiekvienas paleistas balionas kažkur nusileidžia kaip šiukšlė. Sempertex pozicija ir 4 alternatyvos", "Jokių paleidimų: kaip profesionalas sako ne ir ką vietoj to kuri su Sempertex"],
  "cover_sub": ["Sempertex Europe pozicija, priežastis už jos ir 4 alternatyvos, kurios suteikia tą pačią wow akimirką, patalpoje ir sutvarkytos.", "Balloon drop, foto zona, pritvirtinta dekoracija ar atminimo akimirka. Ir atsakymas, kai klientas vis tiek prašo paleidimo."],
  "client_question": ["Ar galime pabaigoje paleisti 50 balionų seneliui?", "Visi svečiai vienu metu paleidžia po balioną, juk gražu?", "Jūsų balionai juk biologiškai skaidūs? Tai galima?"],
  "s3_old_quote": ["“Lateksas vis tiek suyra”", "“Tik vieną kartą”", "“Klientas nori, tai darome”"],
  "s3_client_old": ["“50 balionų seneliui? Žinoma”", "“Jei kiekvienas paleis po vieną, nieko tokio”"],
  "cta_title_tpl": "Užsisakyk Sempertex balionus iš {name}", "cta_sub_generic": "Sukurk alternatyvą: balloon drop, foto zoną ar pritvirtintą dekoraciją.",
},
}

CAPTIONS_TPL = {
 "nl": "Sempertex Europe doet niet mee aan ballonoplatingen, van geen enkele soort, en vraagt klanten hetzelfde. Elke opgelaten ballon landt ergens als afval, en afbreken duurt maanden. In deze carousel: het standpunt, de reden en 4 alternatieven met dezelfde wow: ballondrop, luchtgevuld fotomoment, verankerde heliumdesigns en een herdenkingsmoment. Plus wat je antwoordt als een klant toch om een oplating vraagt.\n\nBestel je Sempertex ballonnen bij {domain}.\n\n#geenoplating #partysafe #sempertex #{tag} #ballondecoratie #ballonartiest",
 "en": "Sempertex Europe doesn't take part in balloon releases, of any kind, and asks customers to do the same. Every released balloon lands somewhere as litter, and breaking down takes months. In this carousel: the position, the reason and 4 alternatives with the same wow: balloon drop, air-filled photo moment, anchored helium designs and a memorial moment. Plus what to answer when a client asks for a release anyway.\n\nOrder your Sempertex balloons at {domain}.\n\n#noballoonrelease #partysafe #sempertex #{tag} #balloondecor #balloonartist",
 "de": "Sempertex Europe macht bei Ballonmassenstarts nicht mit, bei keinem einzigen, und bittet Kunden um dasselbe. Jeder losgelassene Ballon landet irgendwo als Müll, und der Abbau dauert Monate. Im Carousel: die Haltung, der Grund und 4 Alternativen mit demselben Wow: Ballon-Drop, luftgefüllter Fotomoment, verankerte Helium-Designs und ein Gedenkmoment. Plus, was du antwortest, wenn ein Kunde trotzdem nach einem Massenstart fragt.\n\nBestell deine Sempertex Ballons bei {domain}.\n\n#keinmassenstart #partysafe #sempertex #{tag} #ballondeko #ballonkünstler",
 "fr": "Sempertex Europe ne participe à aucun lâcher de ballons, d'aucune sorte, et demande à ses clients de faire pareil. Chaque ballon lâché atterrit quelque part comme déchet, et la dégradation prend des mois. Dans ce carrousel : la position, la raison et 4 alternatives avec le même wow : balloon drop, moment photo à l'air, créations hélium lestées et moment de recueillement. Plus ce que tu réponds quand un client demande quand même un lâcher.\n\nCommande tes ballons Sempertex chez {domain}.\n\n#pasdelacher #partysafe #sempertex #{tag} #decorationballons #artisteballon",
 "it": "Sempertex Europe non partecipa a lanci di palloncini, di nessun tipo, e chiede ai clienti di fare lo stesso. Ogni palloncino liberato atterra da qualche parte come rifiuto, e la degradazione richiede mesi. Nel carosello: la posizione, il motivo e 4 alternative con lo stesso wow: balloon drop, momento foto ad aria, composizioni a elio zavorrate e momento di ricordo. Più cosa rispondi quando un cliente chiede comunque un lancio.\n\nOrdina i tuoi palloncini Sempertex da {domain}.\n\n#nolanci #partysafe #sempertex #{tag} #palloncini #balloonartist",
 "pl": "Sempertex Europe nie bierze udziału w wypuszczaniu balonów, żadnego rodzaju, i prosi klientów o to samo. Każdy wypuszczony balon ląduje gdzieś jako śmieć, a rozkład trwa miesiące. W karuzeli: stanowisko, powód i 4 alternatywy z tym samym efektem wow: balloon drop, fotościanka na powietrze, obciążone dekoracje helowe i moment pamięci. Plus co odpowiedzieć, gdy klient mimo to prosi o wypuszczenie.\n\nZamów balony Sempertex w {domain}.\n\n#niewypuszczamy #partysafe #sempertex #{tag} #dekoracjebalonowe #artystabalonowy",
 "el": "Η Sempertex Europe δεν συμμετέχει σε απελευθερώσεις μπαλονιών, κανενός είδους, και ζητά το ίδιο από τους πελάτες. Κάθε μπαλόνι που απελευθερώνεται πέφτει κάπου ως σκουπίδι, και η διάσπαση παίρνει μήνες. Στο carousel: η θέση, ο λόγος και 4 εναλλακτικές με το ίδιο wow: balloon drop, φωτογραφική στιγμή με αέρα, αγκυρωμένες κατασκευές ηλίου και στιγμή μνήμης. Και τι απαντάς όταν ένας πελάτης ζητά παρ' όλα αυτά απελευθέρωση.\n\nΠαράγγειλε τα μπαλόνια Sempertex σου από {domain}.\n\n#χωριςαπελευθερωση #partysafe #sempertex #{tag} #μπαλονια #balloonartist",
 "hu": "A Sempertex Europe nem vesz részt lufieregetésben, semmilyenben, és az ügyfeleitől ugyanezt kéri. Minden elengedett lufi valahol szemétként landol, a lebomlás pedig hónapokig tart. A carouselben: az álláspont, az ok és 4 alternatíva ugyanazzal a wow-val: lufiesés, levegős fotópont, rögzített héliumos dekorációk és emlékező pillanat. Plusz mit válaszolj, ha egy ügyfél mégis eregetést kér.\n\nRendeld a Sempertex lufijaidat innen: {domain}.\n\n#nincseregetes #partysafe #sempertex #{tag} #lufidekoracio #lufiművész",
 "lt": "Sempertex Europe nedalyvauja balionų paleidimuose, jokiuose, ir prašo klientų daryti tą patį. Kiekvienas paleistas balionas kažkur nusileidžia kaip šiukšlė, o skaidymasis trunka mėnesius. Karuselėje: pozicija, priežastis ir 4 alternatyvos su tuo pačiu wow: balloon drop, oru pripūsta foto zona, pritvirtintos helio dekoracijos ir atminimo akimirka. Ir ką atsakyti, kai klientas vis tiek prašo paleidimo.\n\nUžsisakyk Sempertex balionus iš {domain}.\n\n#jokiupaleidimu #partysafe #sempertex #{tag} #balionai #balionumenininkas",
}

# ---------------------------------------------------------------- VISUALS
CUR = {"pal": ["rosewood", "eucalyptus", "greentea", "golddust"]}

def fill_pal(b, c):
    lab = {f"p{i}": G["pal_label"](k, short=False).replace("Fashion ", "").replace("Pastel ", "") for i, k in enumerate(b["pal"][:4])}
    def f(v): return v.format(**lab) if isinstance(v, str) and "{p" in v else v
    out = {}
    for k, v in c.items():
        if isinstance(v, str): out[k] = f(v)
        elif isinstance(v, list): out[k] = [[f(x) for x in item] if isinstance(item, list) else f(item) for item in v]
        else: out[k] = v
    qs = VARIANTS[b["lang"]]["client_question"]
    qi = qs.index(c["client_question"]) if c["client_question"] in qs else 0
    out["client_answer"] = c["client_answers"][qi]
    return out

def _bl(key, size, cls="", extra=""):
    return G["balloon"](key, "fashion", size, extra_style=extra, cls=cls)

def facts_grid(items, cls="facts", num_size=44, lab_size=20):
    esc = G["esc"]
    def fs(n):
        L = len(n); return num_size if L <= 9 else (int(num_size * .72) if L <= 15 else int(num_size * .58))
    cells = "".join(f'<div class="fact"><b style="font-size:{fs(n)}px">{esc(n)}</b><span style="font-size:{lab_size}px">{esc(l)}</span></div>' for n, l in items)
    return f'<div class="{cls}">{cells}</div>'

def drop_visual(keys, w=300, h=220, lbl="", ink="#111", n=9):
    """Ballondrop: een net (gestippelde lijn + mazen) met ballonnen die eruit vallen."""
    esc = G["esc"]
    net = f'<div style="position:absolute;left:0;top:0;width:{w}px;height:34px;border:3px dashed {ink};border-radius:0 0 40px 40px;opacity:.55"></div>'
    out = f'<div style="position:relative;width:{w}px;height:{h}px">{net}'
    pos = [(10, 40, 56), (60, 70, 50), (110, 40, 60), (165, 80, 52), (215, 45, 58), (255, 90, 50), (40, 130, 54), (130, 140, 58), (220, 150, 54)]
    for i, (x, y, s) in enumerate(pos[:n]):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({(i*37)%40-20}deg)">{_bl(keys[i % len(keys)], s)}</div>'
    if lbl:
        out += f'<div style="position:absolute;left:0;right:0;bottom:-28px;text-align:center;font-size:17px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:{ink};opacity:.6">{esc(lbl)}</div>'
    return out + '</div>'

def anchored(keys, size=96, w=250, h=300, weight_lbl="", ink="#111", n=3):
    """Verankerd design: ballonnen op lint naar één gewicht."""
    esc = G["esc"]; ratio = G["PHOTO_RATIO"]
    pos = [(int(w*0.05), 10), (int(w*0.5 - size/2), 40), (int(w*0.95 - size), 18)][:n]
    bh = int(size * ratio); wx, wy = w // 2, h - 40
    svg = f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="position:absolute;left:0;top:0">'
    for (x, y) in pos:
        bx, by = x + size // 2, y + bh - 4
        svg += f'<path d="M{bx} {by} C {bx} {by+50}, {wx} {wy-60}, {wx} {wy}" fill="none" stroke="{ink}" stroke-width="2.5" stroke-linecap="round" opacity=".8"/>'
    svg += '</svg>'
    out = f'<div style="position:relative;width:{w}px;height:{h}px">{svg}'
    for (x, y), k in zip(pos, keys):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px">{_bl(k, size)}</div>'
    out += (f'<div style="position:absolute;left:{wx-40}px;top:{wy-4}px;width:80px;height:40px;border-radius:9px;background:{ink};color:#fff;'
            f'font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;letter-spacing:.06em">{esc(weight_lbl.upper())}</div>')
    return out + '</div>'

def garland(keys, big=84, small=56, n=6):
    out = '<div style="display:flex;align-items:flex-end;justify-content:center;gap:0">'
    for i in range(n):
        k = keys[i % len(keys)]; s = big if i % 2 == 0 else small
        rotv = (-10, 12, -6, 10, -12, 8, -9)[i % 7]
        out += f'<div style="margin:0 -8px"><div style="transform:rotate({rotv}deg)">{_bl(k, s)}</div></div>'
    return out + '</div>'

def alt_cards(c, P, cls="alts", title_size=24, body_size=18, ink="#111", font=None):
    """4 alternatieven als kaarten met nummer, titel en één regel. font = bodyfont van de distri (stijl 1 erft anders het kopfont)."""
    esc = G["esc"]
    out = f'<div class="{cls}"' + (f' style="font-family:\'{font}\'"' if font else '') + '>'
    for i, (t, body) in enumerate(c["alts"]):
        out += f'<div class="alt"><b style="font-size:{title_size}px"><span class="num">{i+1}</span>{esc(t)}</b><span style="font-size:{body_size}px">{esc(body)}</span></div>'
    return out + '</div>'

def avoid_list(c, cls=""):
    esc = G["esc"]
    return ('<div class="' + cls + '">' + "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps5"])) + '</div>')

def release_visual(keys, c, ink="#111"):
    """'Oplaten': ballonnen die wegdrijven met lint, stippellijn, en een afval-kaartje onderaan."""
    esc = G["esc"]; w, h = 330, 360
    pos = [(20, 0, 72), (110, 30, 64), (200, 10, 70), (60, 110, 60), (160, 120, 66), (250, 100, 58)]
    svg = f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="position:absolute;left:0;top:0">'
    for (x, y, s) in pos:
        bx, by = x + s // 2, y + int(s * 1.4)
        svg += f'<path d="M{bx} {by} q 10 40 -6 80" fill="none" stroke="{ink}" stroke-width="2" opacity=".6" stroke-linecap="round" stroke-dasharray="6 6"/>'
    svg += '</svg>'
    out = f'<div style="position:relative;width:{w}px;height:{h}px">{svg}'
    for i, (x, y, s) in enumerate(pos):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({(i*41)%30-15}deg)">{_bl(keys[i % len(keys)], s)}</div>'
    out += (f'<div style="position:absolute;left:30px;top:250px;transform:rotate(-6deg);background:#fff;color:#E03131;border:3px solid {ink};'
            f'border-radius:10px;padding:8px 16px;font-size:22px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 4px 0 rgba(0,0,0,.18)">{esc(c["litter_lbl"])} ↓</div>')
    out += f'<div style="position:absolute;left:0;top:320px;width:{w}px;height:6px;background:{ink};opacity:.5;border-radius:3px"></div>'
    return out + '</div>'

def build_visual(keys, c, ink="#111"):
    """'Opbouwen': luchtslinger bovenaan + verankerd boeket."""
    return (f'<div style="position:relative;width:330px;height:380px">'
            f'<div style="position:absolute;left:-10px;top:0;width:350px;transform:scale(.9);transform-origin:top left">{garland(keys, 84, 56, 6)}</div>'
            f'<div style="position:absolute;left:40px;top:110px;transform:scale(.85);transform-origin:top left">{anchored(keys[:3], 96, 250, 290, c["weight_lbl"], ink)}</div></div>')

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
  <div class="box" style="left:70px;top:120px;width:790px;height:500px">
    <h2 data-fit style="font-size:76px;max-height:400px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:790px;top:60px;transform:scale(.7);transform-origin:top left">{anchored([b['hero'], P[0], P[1]], 96, 250, 300, c['weight_lbl'], b['ink'])}</div>
  <div style="position:absolute;left:120px;top:630px">{arrow_svg(b['ink'], 150, 140)}</div>
  <div class="box" style="left:300px;top:660px;width:710px;height:500px;padding:36px 46px">
    <div style="font-size:30px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:470px;padding:44px 50px">
    <h2 data-fit style="font-size:58px;max-height:150px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:27px">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:700px;height:410px">
    <div class="card" style="top:0;height:330px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:380px;padding:30px 34px">{facts_grid(c['rule1_facts'])}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:56px;max-height:150px">{esc(c['rule2_title'])}</h2>
  <div style="position:absolute;left:80px;right:80px;top:330px;font-size:27px;line-height:1.35" class="body">{esc(c['rule2_body'])}</div>
  <div style="position:absolute;left:70px;right:70px;top:410px">{alt_cards(c, P, "alts big", 29, 23, b["ink"], b["ui"])}</div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:660px;padding:36px 36px 30px">
    <h2 data-fit style="font-size:50px;margin-bottom:24px;text-align:center;max-height:120px">{esc(c['example_title'])}</h2>
    <div style="display:flex;gap:30px;align-items:flex-start">
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:40px"><div style="transform:scale(1.25);transform-origin:top center;height:275px">{drop_visual(P, 300, 220, c['drop_lbl'], b['ink'])}</div><div style="font-size:22px;line-height:1.3"><b>{esc(c['ex_drop_title'])}</b><br>{esc(c['ex_drop_body'])}</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:14px"><div style="transform:scale(1.02);transform-origin:top center;height:300px">{anchored(P[:3], 96, 250, 290, c['weight_lbl'], b['ink'])}</div><div style="font-size:22px;line-height:1.3"><b>{esc(c['ex_mem_title'])}</b><br>{esc(c['ex_mem_body'])}</div></div>
    </div>
  </div>
  <div class="box" style="left:70px;top:860px;width:940px;padding:24px 50px"><div class="body" style="font-size:24px">{esc(c['example_body'])}</div></div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:54px;max-height:140px">{esc(c['client_title'])}</h2>
  <div class="chat" style="top:320px;min-height:130px;padding-right:120px">{esc(c['client_question'])}<div class="send">↑</div></div>
  <div style="position:absolute;left:80px;right:80px;top:490px;display:flex;flex-direction:column;gap:18px">
    <div class="card" style="position:relative;left:auto;right:auto;padding:24px 36px"><div style="font-size:26px;line-height:1.35">{esc(c['client_answer'])}</div></div>
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
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box"><div style="transform:scale(1.1)">{build_visual(P, c, '#111')}</div></div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px;font-size:27px"><b style="font-size:36px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:700px;width:560px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:340px;padding:10px;box-sizing:border-box"><div style="transform:scale(.8)">{release_visual(P, c, '#111')}</div></div>
  </div>
  <div class="frame" style="left:600px;top:820px;width:410px;transform:rotate({rot(b,3)}deg)">
    <div class="ph" style="height:260px;padding:10px;box-sizing:border-box"><div style="transform:scale(.7)">{anchored([b['hero'], P[0], P[1]], 96, 250, 290, c['weight_lbl'], '#111')}</div></div>
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
  <div class="body" style="position:absolute;left:70px;right:70px;top:860px;font-size:25px">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:56px;max-height:150px">{esc(c['rule2_title'])}</h2>
  <div class="body" style="position:absolute;left:70px;right:70px;top:330px;font-size:26px">{esc(c['rule2_body'])}</div>
  <div class="frame" style="left:70px;top:410px;width:940px;transform:rotate({rot(b,1)}deg)">
    <div class="ph" style="height:auto;padding:26px 30px;box-sizing:border-box;align-items:stretch;background:#fff;color:#111">{alt_cards(c, P, 'alts onwhite', 23, 17)}</div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:58px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:auto;padding:24px 30px;box-sizing:border-box;flex-direction:row;gap:30px;align-items:flex-start;background:#fff;color:#111">
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:40px"><div style="transform:scale(1.15);transform-origin:top center;height:250px">{drop_visual(P, 300, 210, c['drop_lbl'], '#111')}</div><div style="font-size:21px;line-height:1.3"><b>{esc(c['ex_drop_title'])}</b><br>{esc(c['ex_drop_body'])}</div></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:12px"><div style="transform:scale(.98);transform-origin:top center;height:286px">{anchored(P[:3], 96, 250, 290, c['weight_lbl'], '#111')}</div><div style="font-size:21px;line-height:1.3"><b>{esc(c['ex_mem_title'])}</b><br>{esc(c['ex_mem_body'])}</div></div>
    </div>
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
      <div style="font-size:28px;line-height:1.3;color:{b['ink']};font-style:italic">{esc(c['client_question'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:12px 0"></div>
      <div style="font-size:23px;line-height:1.35;color:{b['ink']}">{esc(c['client_answer'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:12px 0"></div>
      <div style="font-size:21px;font-weight:{b['body_b']};color:{b['ink']}">{esc(c['avoid_lead'])}</div>
      {avoid_list(c, 'onwhite')}
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1080px;font-size:21px">{esc(c['client_body'])}</div>
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
  <h1 data-fit style="position:absolute;left:50px;right:50px;top:60px;max-height:400px;font-size:84px;text-align:center;line-height:1.08">{hl(c['s3_cover_a'])} {esc(c['s3_cover_b'])} {esc(c['s3_cover_c'])}<br><span class="hl">{esc(c['s3_cover_d'])}</span></h1>
  <div class="vsmark" style="top:520px">VS</div>
  <div class="lblw" style="left:110px;top:500px;transform:rotate({rot(b,-4)}deg)">{esc(c['s3_left'])}<br><span class="meta">● {esc(c['s3_left_meta'])}</span></div>
  <div class="lbld" style="right:110px;top:500px;transform:rotate({rot(b,4)}deg)">{esc(c['s3_right'])}<br><span class="meta" style="background:rgba(255,255,255,.18)">● {esc(c['s3_right_meta'])}</span></div>
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{release_visual(loud, c, b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{build_visual(P, c, b['ink'])}</div>
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
    <div class="strike" style="font-size:40px;line-height:1.2;color:#fff;text-decoration-color:#E03131;margin-top:34px;font-weight:700;font-family:'{b['ui']}'">{esc(old_text)}</div>
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
    vis2 = f'<div style="width:100%">{alt_cards(c, P, "alts s3alts", 19, 15)}</div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    t = c['example_title']
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v" style="font-size:{44 if len(t) <= 24 else (36 if len(t) <= 30 else 30)}px">{esc(t)}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:620px;padding:36px 30px;display:flex;gap:26px;align-items:flex-start;justify-content:center">
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:40px"><div style="transform:scale(1.2);transform-origin:top center;height:262px">{drop_visual(P, 300, 210, c['drop_lbl'], '#111')}</div><div style="font-size:21px;line-height:1.3"><b>{esc(c['ex_drop_title'])}</b><br>{esc(c['ex_drop_body'])}</div></div>
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:12px"><div style="transform:scale(1);transform-origin:top center;height:292px">{anchored(P[:3], 96, 250, 290, c['weight_lbl'], '#111')}</div><div style="font-size:21px;line-height:1.3"><b>{esc(c['ex_mem_title'])}</b><br>{esc(c['ex_mem_body'])}</div></div>
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
.s1 .step{font-size:25px;margin-top:10px}
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
.alts{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.alts .alt{display:flex;flex-direction:column;gap:8px;border:3px solid #111;border-radius:18px;padding:20px 22px;background:#fff;line-height:1.3}
.alts .alt b{display:flex;align-items:center;gap:12px;line-height:1.15}
.alts .alt .num{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:#111;color:#fff;font-size:20px;flex:0 0 36px}
.alts.onwhite .alt{color:#111;border-color:#111}
.alts.big{gap:22px}
.alts.big .alt{padding:30px 30px;gap:14px;min-height:330px;justify-content:center}
.alts.big .alt .num{width:44px;height:44px;font-size:24px;flex-basis:44px}
.alts.s3alts{grid-template-columns:1fr;gap:10px}
.alts.s3alts .alt{border-width:2px;padding:10px 14px;border-radius:14px;gap:4px}
.alts.s3alts .alt .num{width:26px;height:26px;font-size:14px;flex-basis:26px}
"""
