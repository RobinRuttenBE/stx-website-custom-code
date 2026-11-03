# -*- coding: utf-8 -*-
"""Topic: 'Helium for balloons: what it is, how to use it and what to avoid'
(sempertexeurope.com/en_GB/blog/helium-for-balloons).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=helium.
Cijfers uit de blog: R12 15 L, R18 56 L, R36 226 L; 1 m3 = 1.000 L = 66 R12 of 4 R36; Hi-Float tot 20x;
zweeftijd onbehandeld latex R9 10-14 u, R12 18-24 u, R18 36 u, R36 3-5 dagen."""

G = {}
def setup(g): G.update(g)

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["15 L per R12…", "Hi-Float ×20…", "Nooit oplaten…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Heliumgids…",
    "steps_title": "Helium gebruik je enkel voor wat echt moet zweven.", "steps_lead": "De 3 gouden regels:",
    "steps": ["Nooit inademen: het verdringt zuurstof", "Nooit ballonnen oplaten", "Elk zwevend design verzwaren, ook binnen"],
    "steps_label": "De basis",
    "rule1_label": "Regel 1", "rule1_title": "Reken vooraf: liters per maat",
    "rule1_body": "Een R12 vraagt 15 L helium, een R18 56 L, een R36 226 L. Een fles van 1 m³ bevat 1.000 L: goed voor 66 R12 of 4 R36. Een R36 kost 15 keer meer helium dan een R12, dus zet dat in je offerte.",
    "rule1_tags": ["R12 · 15 L", "R18 · 56 L", "R36 · 226 L"],
    "rule2_label": "Regel 2", "rule2_title": "Zo zweven ze langer",
    "rule2_body": "Hi-Float aan de binnenkant van latex geeft tot 20 keer langere zweeftijd. Folie houdt helium dagen vast zonder behandeling. Onbehandeld latex blaas je de dag zelf op, met Hi-Float de dag ervoor, folie dagen vooraf. Warmte zet helium uit, kou laat ballonnen tijdelijk zakken.",
    "rule2_facts": [["×20", "zweeftijd met Hi-Float"], ["dagen", "folie, zonder behandeling"], ["dag zelf", "onbehandeld latex opblazen"], ["0 min", "in een warme auto"]],
    "example_label": "Zweeftijden", "example_title": "Onbehandeld latex, gemiddeld",
    "example_sizes": [["R9", "10 tot 14 u"], ["R12", "18 tot 24 u"], ["R18", "36 u"], ["R36", "3 tot 5 dagen"]],
    "example_body": "Vier maten, vier zweeftijden, hier in {p0}, {p1}, {p2} en {p3}. Hi-Float maakt er tot 20 keer meer van. De volledige tabel met liters, lift en zweeftijd per maat staat in de Sempertex Gas Capacity Chart.",
    "client_label": "Klantgesprek", "client_title": "Wat je antwoordt als de klant vraagt",
    "client_answers": [
        "Een slinger hangen we op en vullen we met lucht. Helium zou hier alleen kost toevoegen. Wil je iets dat zweeft, dan zet ik 3 R12 op een gewicht naast de tafel.",
        "Onbehandeld latex zweeft 18 tot 24 uur. Met Hi-Float tot 20 keer langer, folie houdt het dagen vol. Voor een week kies ik folie of een installatie met lucht.",
        "Folie en latex met Hi-Float: ja. Onbehandeld latex blaas ik de dag zelf op, zo dicht mogelijk bij het event. En de auto blijft koel.",
    ],
    "avoid_lead": "Wat je altijd vermijdt:",
    "steps5": ["Inademen: pomp of kraan, nooit je mond", "Ballonnen oplaten", "Helium in een R5 of 260: die zweven niet", "Zwevend werk zonder gewicht", "Fles los in de auto of in de zon"],
    "client_body": "Helium is eindig en je grootste variabele kost. Lucht waar het kan maakt je offerte scherper en je klant hoort dat graag.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Helium voor Sempertex ballonnen", "s3_cover_b": "overal", "s3_cover_c": "vs.", "s3_cover_d": "enkel waar het moet zweven",
    "s3_left": "OVERAL HELIUM", "s3_right": "ENKEL WAAR NODIG", "s3_left_meta": "duurste gewoonte", "s3_right_meta": "scherpere offerte",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["Helium in alles", "Op gevoel"], "s3_new_tags": ["Lucht waar het kan", "Rekenen", "Hi-Float"],
    "s3_new_quote": "“Enkel wat vrij moet zweven krijgt helium. De rest vul ik met lucht en reken ik vooraf uit.”", "s3_new_badge": "15 L per R12",
    "s3_changed_bottom": "Zelfde ballonnen, zelfde klant.\nMinder helium, betere marge.",
    "s3_topic_lbl": "REGEL", "s3_rule1_topic": "Rekenen", "s3_rule1_old": "Ik zie wel hoeveel de fles geeft",
    "s3_rule1_quote": "“R12 15 L, R18 56 L, R36 226 L. Eén fles van 1 m³ is 66 R12 of 4 R36.”",
    "s3_rule2_topic": "Zweeftijd", "s3_rule2_old": "Alles de dag ervoor opblazen",
    "s3_rule2_quote": "“Onbehandeld latex de dag zelf, met Hi-Float de dag ervoor, folie dagen vooraf.”",
    "s3_example_lbl": "ZWEEFTIJD", "s3_example_quote": "“R9 10 tot 14 uur, R12 18 tot 24 uur, R18 36 uur, R36 3 tot 5 dagen. Hi-Float maakt daar tot 20 keer meer van.”",
    "s3_client_lbl": "KLANT", "s3_client_topic": "Klantgesprek",
    "s3_client_quote": "“Lucht waar het kan: minder kost, scherpere offerte, en de klant hoort dat graag.”",
    "s3_cta_kicker": "Je heliumchecklist voor de volgende job",
    "weight_lbl": "gewicht", "air_lbl": "lucht", "helium_lbl": "helium",
},
"en": {
    "cover_pills": ["15 L per R12…", "Hi-Float ×20…", "Never release…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Helium guide…",
    "steps_title": "Helium is only for designs that have to float.", "steps_lead": "The 3 golden rules:",
    "steps": ["Never inhale it: it displaces oxygen", "Never release balloons", "Anchor every floating design with a weight, indoors too"],
    "steps_label": "The basics",
    "rule1_label": "Rule 1", "rule1_title": "Work it out first: litres per size",
    "rule1_body": "An R12 needs 15 L of helium, an R18 56 L, an R36 226 L. A 1 m³ cylinder holds 1,000 L: enough for 66 R12 or 4 R36. An R36 uses 15 times the helium of an R12, so price it that way.",
    "rule1_tags": ["R12 · 15 L", "R18 · 56 L", "R36 · 226 L"],
    "rule2_label": "Rule 2", "rule2_title": "How to make them float longer",
    "rule2_body": "Hi-Float inside latex extends float time up to 20 times. Foil holds helium for days without treatment. Inflate untreated latex on the day, Hi-Float latex the day before, foil days ahead. Heat expands helium, cold makes balloons sink for a while.",
    "rule2_facts": [["×20", "float time with Hi-Float"], ["days", "foil, no treatment"], ["same day", "inflate untreated latex"], ["0 min", "in a hot car"]],
    "example_label": "Float times", "example_title": "Untreated latex, on average",
    "example_sizes": [["R9", "10 to 14 hrs"], ["R12", "18 to 24 hrs"], ["R18", "36 hrs"], ["R36", "3 to 5 days"]],
    "example_body": "Four sizes, four float times, shown here in {p0}, {p1}, {p2} and {p3}. Hi-Float turns that into up to 20 times more. The full table with litres, lift and float time per size is in the Sempertex Gas Capacity Chart.",
    "client_label": "Client chat", "client_title": "What you answer when the client asks",
    "client_answers": [
        "A garland is hung up and filled with air. Helium would only add cost here. If you want something floating, I'll put 3 R12 on a weight next to the table.",
        "Untreated latex floats 18 to 24 hours. With Hi-Float up to 20 times longer, foil lasts for days. For a full week I'd go with foil or an air-filled installation.",
        "Foil and Hi-Float latex: yes. Untreated latex I inflate on the day, as close to the event as I can. And the car stays cool.",
    ],
    "avoid_lead": "What you always avoid:",
    "steps5": ["Inhaling: pump or cylinder tap, never your mouth", "Releasing balloons", "Helium in an R5 or a 260: they won't float", "Floating work without a weight", "Cylinder loose in the car or in the sun"],
    "client_body": "Helium is finite and your biggest variable cost. Air wherever it works makes your quote sharper, and clients like hearing it.",
    "cta_label": "Order",
    "s3_cover_a": "Helium for Sempertex balloons", "s3_cover_b": "everywhere", "s3_cover_c": "vs.", "s3_cover_d": "only where it has to float",
    "s3_left": "HELIUM EVERYWHERE", "s3_right": "ONLY WHERE NEEDED", "s3_left_meta": "most expensive habit", "s3_right_meta": "sharper quote",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["Helium in everything", "By feel"], "s3_new_tags": ["Air where it works", "Calculate", "Hi-Float"],
    "s3_new_quote": "“Only what has to float freely gets helium. The rest I fill with air and work out in advance.”", "s3_new_badge": "15 L per R12",
    "s3_changed_bottom": "Same balloons, same client.\nLess helium, better margin.",
    "s3_topic_lbl": "RULE", "s3_rule1_topic": "Calculate", "s3_rule1_old": "I'll see how far the cylinder goes",
    "s3_rule1_quote": "“R12 15 L, R18 56 L, R36 226 L. One 1 m³ cylinder is 66 R12 or 4 R36.”",
    "s3_rule2_topic": "Float time", "s3_rule2_old": "Inflate everything the day before",
    "s3_rule2_quote": "“Untreated latex on the day, Hi-Float the day before, foil days ahead.”",
    "s3_example_lbl": "FLOAT TIME", "s3_example_quote": "“R9 10 to 14 hours, R12 18 to 24 hours, R18 36 hours, R36 3 to 5 days. Hi-Float makes that up to 20 times more.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Client chat",
    "s3_client_quote": "“Air where it works: lower cost, sharper quote, and the client likes hearing it.”",
    "s3_cta_kicker": "Your helium checklist for the next job",
    "weight_lbl": "weight", "air_lbl": "air", "helium_lbl": "helium",
},
"de": {
    "cover_pills": ["15 L pro R12…", "Hi-Float ×20…", "Nie steigen lassen…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Helium-Guide…",
    "steps_title": "Helium nimmst du nur für Designs, die wirklich schweben müssen.", "steps_lead": "Die 3 goldenen Regeln:",
    "steps": ["Nie einatmen: es verdrängt Sauerstoff", "Nie Ballons steigen lassen", "Jedes schwebende Design beschweren, auch drinnen"],
    "steps_label": "Die Basis",
    "rule1_label": "Regel 1", "rule1_title": "Vorher rechnen: Liter pro Größe",
    "rule1_body": "Ein R12 braucht 15 L Helium, ein R18 56 L, ein R36 226 L. Eine 1-m³-Flasche enthält 1.000 L: das reicht für 66 R12 oder 4 R36. Ein R36 verbraucht 15-mal so viel Helium wie ein R12, also kalkulier das ins Angebot ein.",
    "rule1_tags": ["R12 · 15 L", "R18 · 56 L", "R36 · 226 L"],
    "rule2_label": "Regel 2", "rule2_title": "So schweben sie länger",
    "rule2_body": "Hi-Float innen im Latex verlängert die Schwebezeit bis zu 20-fach. Folie hält Helium tagelang ohne Behandlung. Unbehandeltes Latex füllst du am Tag selbst, mit Hi-Float am Vortag, Folie Tage vorher. Wärme dehnt Helium aus, Kälte lässt Ballons vorübergehend sinken.",
    "rule2_facts": [["×20", "Schwebezeit mit Hi-Float"], ["Tage", "Folie, ohne Behandlung"], ["am Tag", "unbehandeltes Latex füllen"], ["0 Min", "im heißen Auto"]],
    "example_label": "Schwebezeiten", "example_title": "Unbehandeltes Latex, im Schnitt",
    "example_sizes": [["R9", "10 bis 14 Std"], ["R12", "18 bis 24 Std"], ["R18", "36 Std"], ["R36", "3 bis 5 Tage"]],
    "example_body": "Vier Größen, vier Schwebezeiten, hier in {p0}, {p1}, {p2} und {p3}. Hi-Float macht daraus bis zu 20-mal mehr. Die komplette Tabelle mit Litern, Auftrieb und Schwebezeit pro Größe steht im Sempertex Gas Capacity Chart.",
    "client_label": "Kundengespräch", "client_title": "Was du antwortest, wenn der Kunde fragt",
    "client_answers": [
        "Eine Girlande hängen wir auf und füllen sie mit Luft. Helium würde hier nur Kosten bringen. Wenn etwas schweben soll, stelle ich 3 R12 auf ein Gewicht neben den Tisch.",
        "Unbehandeltes Latex schwebt 18 bis 24 Stunden. Mit Hi-Float bis zu 20-mal länger, Folie hält Tage durch. Für eine Woche nehme ich Folie oder eine Installation mit Luft.",
        "Folie und Latex mit Hi-Float: ja. Unbehandeltes Latex fülle ich am Tag selbst, so nah am Event wie möglich. Und das Auto bleibt kühl.",
    ],
    "avoid_lead": "Was du immer vermeidest:",
    "steps5": ["Einatmen: Pumpe oder Flaschenventil, nie der Mund", "Ballons steigen lassen", "Helium in R5 oder 260: die schweben nicht", "Schwebende Arbeit ohne Gewicht", "Flasche lose im Auto oder in der Sonne"],
    "client_body": "Helium ist endlich und dein größter variabler Kostenpunkt. Luft, wo es geht, macht dein Angebot schärfer, und der Kunde hört das gern.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Helium für Sempertex Ballons", "s3_cover_b": "überall", "s3_cover_c": "vs.", "s3_cover_d": "nur wo es schweben muss",
    "s3_left": "ÜBERALL HELIUM", "s3_right": "NUR WO NÖTIG", "s3_left_meta": "teuerste Gewohnheit", "s3_right_meta": "schärferes Angebot",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["Helium in allem", "Nach Gefühl"], "s3_new_tags": ["Luft, wo es geht", "Rechnen", "Hi-Float"],
    "s3_new_quote": "“Nur was frei schweben muss, bekommt Helium. Den Rest fülle ich mit Luft und rechne vorher durch.”", "s3_new_badge": "15 L pro R12",
    "s3_changed_bottom": "Gleiche Ballons, gleicher Kunde.\nWeniger Helium, bessere Marge.",
    "s3_topic_lbl": "REGEL", "s3_rule1_topic": "Rechnen", "s3_rule1_old": "Mal sehen, wie weit die Flasche reicht",
    "s3_rule1_quote": "“R12 15 L, R18 56 L, R36 226 L. Eine 1-m³-Flasche sind 66 R12 oder 4 R36.”",
    "s3_rule2_topic": "Schwebezeit", "s3_rule2_old": "Alles am Vortag aufblasen",
    "s3_rule2_quote": "“Unbehandeltes Latex am Tag selbst, mit Hi-Float am Vortag, Folie Tage vorher.”",
    "s3_example_lbl": "SCHWEBEZEIT", "s3_example_quote": "“R9 10 bis 14 Stunden, R12 18 bis 24 Stunden, R18 36 Stunden, R36 3 bis 5 Tage. Hi-Float macht daraus bis zu 20-mal mehr.”",
    "s3_client_lbl": "KUNDE", "s3_client_topic": "Kundengespräch",
    "s3_client_quote": "“Luft, wo es geht: weniger Kosten, schärferes Angebot, und der Kunde hört das gern.”",
    "s3_cta_kicker": "Deine Helium-Checkliste für den nächsten Job",
    "weight_lbl": "Gewicht", "air_lbl": "Luft", "helium_lbl": "Helium",
},
"fr": {
    "cover_pills": ["15 L par R12…", "Hi-Float ×20…", "Jamais de lâcher…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Guide hélium…",
    "steps_title": "L'hélium, c'est uniquement pour ce qui doit vraiment flotter.", "steps_lead": "Les 3 règles d'or :",
    "steps": ["Ne jamais l'inhaler : il remplace l'oxygène", "Ne jamais lâcher de ballons", "Lester chaque création flottante, même en intérieur"],
    "steps_label": "La base",
    "rule1_label": "Règle 1", "rule1_title": "Calcule avant : les litres par taille",
    "rule1_body": "Un R12 demande 15 L d'hélium, un R18 56 L, un R36 226 L. Une bouteille de 1 m³ contient 1 000 L : de quoi gonfler 66 R12 ou 4 R36. Un R36 consomme 15 fois plus d'hélium qu'un R12, alors mets-le dans ton devis.",
    "rule1_tags": ["R12 · 15 L", "R18 · 56 L", "R36 · 226 L"],
    "rule2_label": "Règle 2", "rule2_title": "Pour qu'ils flottent plus longtemps",
    "rule2_body": "Le Hi-Float à l'intérieur du latex multiplie le temps de flottaison jusqu'à 20 fois. Le foil garde l'hélium des jours sans traitement. Latex non traité : gonfle le jour même. Avec Hi-Float : la veille. Foil : plusieurs jours avant. La chaleur dilate l'hélium, le froid fait redescendre les ballons un moment.",
    "rule2_facts": [["×20", "flottaison avec Hi-Float"], ["jours", "foil, sans traitement"], ["le jour J", "gonfler le latex non traité"], ["0 min", "dans une voiture chaude"]],
    "example_label": "Temps de flottaison", "example_title": "Latex non traité, en moyenne",
    "example_sizes": [["R9", "10 à 14 h"], ["R12", "18 à 24 h"], ["R18", "36 h"], ["R36", "3 à 5 jours"]],
    "example_body": "Quatre tailles, quatre temps de flottaison, ici en {p0}, {p1}, {p2} et {p3}. Le Hi-Float multiplie ça jusqu'à 20 fois. Le tableau complet avec litres, portance et flottaison par taille est dans le Sempertex Gas Capacity Chart.",
    "client_label": "Discussion client", "client_title": "Ce que tu réponds quand le client demande",
    "client_answers": [
        "Une guirlande, on la suspend et on la gonfle à l'air. L'hélium n'ajouterait que du coût. Si tu veux quelque chose qui flotte, je mets 3 R12 sur un poids à côté de la table.",
        "Le latex non traité flotte 18 à 24 heures. Avec Hi-Float jusqu'à 20 fois plus, le foil tient des jours. Pour une semaine, je choisis le foil ou une installation à l'air.",
        "Foil et latex avec Hi-Float : oui. Le latex non traité, je le gonfle le jour même, au plus près de l'événement. Et la voiture reste au frais.",
    ],
    "avoid_lead": "Ce que tu évites toujours :",
    "steps5": ["Inhaler : pompe ou robinet, jamais la bouche", "Lâcher des ballons", "De l'hélium dans un R5 ou un 260 : ils ne flottent pas", "Une création flottante sans poids", "La bouteille non fixée dans la voiture ou au soleil"],
    "client_body": "L'hélium est une ressource limitée et ton plus gros coût variable. De l'air partout où c'est possible rend ton devis plus compétitif, et le client aime l'entendre.",
    "cta_label": "Commander",
    "s3_cover_a": "L'hélium pour les ballons Sempertex", "s3_cover_b": "partout", "s3_cover_c": "vs.", "s3_cover_d": "seulement là où ça doit flotter",
    "s3_left": "HÉLIUM PARTOUT", "s3_right": "SEULEMENT SI NÉCESSAIRE", "s3_left_meta": "l'habitude la plus chère", "s3_right_meta": "devis plus juste",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["Hélium dans tout", "Au feeling"], "s3_new_tags": ["Air quand c'est possible", "Calculer", "Hi-Float"],
    "s3_new_quote": "“Seul ce qui doit flotter librement reçoit de l'hélium. Le reste, je le gonfle à l'air et je le calcule à l'avance.”", "s3_new_badge": "15 L par R12",
    "s3_changed_bottom": "Mêmes ballons, même client.\nMoins d'hélium, meilleure marge.",
    "s3_topic_lbl": "RÈGLE", "s3_rule1_topic": "Calculer", "s3_rule1_old": "On verra ce que donne la bouteille",
    "s3_rule1_quote": "“R12 15 L, R18 56 L, R36 226 L. Une bouteille de 1 m³, c'est 66 R12 ou 4 R36.”",
    "s3_rule2_topic": "Flottaison", "s3_rule2_old": "Tout gonfler la veille",
    "s3_rule2_quote": "“Latex non traité le jour même, Hi-Float la veille, foil plusieurs jours avant.”",
    "s3_example_lbl": "FLOTTAISON", "s3_example_quote": "“R9 10 à 14 heures, R12 18 à 24 heures, R18 36 heures, R36 3 à 5 jours. Le Hi-Float multiplie ça jusqu'à 20 fois.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Discussion client",
    "s3_client_quote": "“De l'air quand c'est possible : moins de coût, devis plus juste, et le client aime l'entendre.”",
    "s3_cta_kicker": "Ta checklist hélium pour la prochaine commande",
    "weight_lbl": "poids", "air_lbl": "air", "helium_lbl": "hélium",
},
"it": {
    "cover_pills": ["15 L per R12…", "Hi-Float ×20…", "Mai liberarli…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "Guida all'elio…",
    "steps_title": "L'elio lo usi solo per ciò che deve davvero volare.", "steps_lead": "Le 3 regole d'oro:",
    "steps": ["Mai inalarlo: sostituisce l'ossigeno", "Mai liberare palloncini in cielo", "Zavorra ogni composizione volante, anche al chiuso"],
    "steps_label": "La base",
    "rule1_label": "Regola 1", "rule1_title": "Calcola prima: litri per misura",
    "rule1_body": "Un R12 richiede 15 L di elio, un R18 56 L, un R36 226 L. Una bombola da 1 m³ contiene 1.000 L: bastano per 66 R12 o 4 R36. Un R36 consuma 15 volte l'elio di un R12, quindi mettilo nel preventivo.",
    "rule1_tags": ["R12 · 15 L", "R18 · 56 L", "R36 · 226 L"],
    "rule2_label": "Regola 2", "rule2_title": "Così volano più a lungo",
    "rule2_body": "L'Hi-Float all'interno del lattice allunga il tempo di volo fino a 20 volte. Il foil trattiene l'elio per giorni senza trattamento. Lattice non trattato: gonfia il giorno stesso. Con Hi-Float: il giorno prima. Foil: giorni prima. Il caldo dilata l'elio, il freddo fa scendere i palloncini per un po'.",
    "rule2_facts": [["×20", "tempo di volo con Hi-Float"], ["giorni", "foil, senza trattamento"], ["stesso giorno", "gonfiare il lattice non trattato"], ["0 min", "in un'auto calda"]],
    "example_label": "Tempi di volo", "example_title": "Lattice non trattato, in media",
    "example_sizes": [["R9", "10 - 14 ore"], ["R12", "18 - 24 ore"], ["R18", "36 ore"], ["R36", "3 - 5 giorni"]],
    "example_body": "Quattro misure, quattro tempi di volo, qui in {p0}, {p1}, {p2} e {p3}. L'Hi-Float li moltiplica fino a 20 volte. La tabella completa con litri, portanza e tempo di volo per misura è nel Sempertex Gas Capacity Chart.",
    "client_label": "Dialogo con il cliente", "client_title": "Cosa rispondi quando il cliente chiede",
    "client_answers": [
        "Una ghirlanda la appendiamo e la gonfiamo ad aria. Qui l'elio aggiungerebbe solo costo. Se vuoi qualcosa che vola, metto 3 R12 su un peso accanto al tavolo.",
        "Il lattice non trattato vola 18-24 ore. Con Hi-Float fino a 20 volte di più, il foil regge per giorni. Per una settimana scelgo il foil o un'installazione ad aria.",
        "Foil e lattice con Hi-Float: sì. Il lattice non trattato lo gonfio il giorno stesso, il più vicino possibile all'evento. E l'auto resta fresca.",
    ],
    "avoid_lead": "Cosa eviti sempre:",
    "steps5": ["Inalare: pompa o rubinetto, mai la bocca", "Liberare palloncini in cielo", "Elio in un R5 o in un 260: non volano", "Composizioni volanti senza peso", "Bombola libera in auto o al sole"],
    "client_body": "L'elio è una risorsa limitata e il tuo costo variabile più grande. Aria ovunque sia possibile rende il preventivo più competitivo, e il cliente lo apprezza.",
    "cta_label": "Ordina",
    "s3_cover_a": "Elio per i palloncini Sempertex", "s3_cover_b": "ovunque", "s3_cover_c": "vs.", "s3_cover_d": "solo dove deve volare",
    "s3_left": "ELIO OVUNQUE", "s3_right": "SOLO DOVE SERVE", "s3_left_meta": "l'abitudine più cara", "s3_right_meta": "preventivo più giusto",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["Elio in tutto", "A sensazione"], "s3_new_tags": ["Aria dove si può", "Calcolare", "Hi-Float"],
    "s3_new_quote": "“Solo ciò che deve volare libero riceve elio. Il resto lo gonfio ad aria e lo calcolo in anticipo.”", "s3_new_badge": "15 L per R12",
    "s3_changed_bottom": "Stessi palloncini, stesso cliente.\nMeno elio, margine migliore.",
    "s3_topic_lbl": "REGOLA", "s3_rule1_topic": "Calcolare", "s3_rule1_old": "Vedo quanto dura la bombola",
    "s3_rule1_quote": "“R12 15 L, R18 56 L, R36 226 L. Una bombola da 1 m³ sono 66 R12 o 4 R36.”",
    "s3_rule2_topic": "Tempo di volo", "s3_rule2_old": "Gonfiare tutto il giorno prima",
    "s3_rule2_quote": "“Lattice non trattato il giorno stesso, Hi-Float il giorno prima, foil giorni prima.”",
    "s3_example_lbl": "TEMPO DI VOLO", "s3_example_quote": "“R9 10-14 ore, R12 18-24 ore, R18 36 ore, R36 3-5 giorni. L'Hi-Float li moltiplica fino a 20 volte.”",
    "s3_client_lbl": "CLIENTE", "s3_client_topic": "Dialogo con il cliente",
    "s3_client_quote": "“Aria dove si può: meno costo, preventivo più giusto, e il cliente lo apprezza.”",
    "s3_cta_kicker": "La tua checklist elio per il prossimo lavoro",
    "weight_lbl": "peso", "air_lbl": "aria", "helium_lbl": "elio",
},
"pl": {
    "cover_pills": ["15 L na R12…", "Hi-Float ×20…", "Nigdy nie wypuszczaj…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Przewodnik po helu…",
    "steps_title": "Helu używasz tylko tam, gdzie coś naprawdę ma unosić się w powietrzu.", "steps_lead": "3 złote zasady:",
    "steps": ["Nigdy nie wdychaj: wypiera tlen", "Nigdy nie wypuszczaj balonów do nieba", "Każdą unoszącą się dekorację obciążaj, także w pomieszczeniu"],
    "steps_label": "Podstawy",
    "rule1_label": "Zasada 1", "rule1_title": "Policz wcześniej: litry na rozmiar",
    "rule1_body": "R12 potrzebuje 15 L helu, R18 56 L, R36 226 L. Butla 1 m³ mieści 1000 L: wystarczy na 66 R12 albo 4 R36. R36 zużywa 15 razy więcej helu niż R12, więc uwzględnij to w wycenie.",
    "rule1_tags": ["R12 · 15 L", "R18 · 56 L", "R36 · 226 L"],
    "rule2_label": "Zasada 2", "rule2_title": "Tak unoszą się dłużej",
    "rule2_body": "Hi-Float wewnątrz lateksu wydłuża czas unoszenia nawet 20 razy. Folia trzyma hel przez wiele dni bez obróbki. Lateks bez Hi-Float pompujesz w dniu eventu, z Hi-Float dzień wcześniej, folię kilka dni wcześniej. Ciepło rozszerza hel, zimno sprawia, że balony na chwilę opadają.",
    "rule2_facts": [["×20", "czas unoszenia z Hi-Float"], ["dni", "folia, bez obróbki"], ["w dniu eventu", "pompowanie lateksu bez Hi-Float"], ["0 min", "w nagrzanym aucie"]],
    "example_label": "Czas unoszenia", "example_title": "Lateks bez Hi-Float, średnio",
    "example_sizes": [["R9", "10 do 14 godz."], ["R12", "18 do 24 godz."], ["R18", "36 godz."], ["R36", "3 do 5 dni"]],
    "example_body": "Cztery rozmiary, cztery czasy unoszenia, tutaj w kolorach {p0}, {p1}, {p2} i {p3}. Hi-Float wydłuża je nawet 20 razy. Pełna tabela z litrami, siłą nośną i czasem unoszenia dla każdego rozmiaru jest w Sempertex Gas Capacity Chart.",
    "client_label": "Rozmowa z klientem", "client_title": "Co odpowiadasz, gdy klient pyta",
    "client_answers": [
        "Girlandę wieszamy i pompujemy powietrzem. Hel tylko podniósłby koszt. Jeśli chcesz coś unoszącego się, postawię 3 R12 na obciążniku obok stołu.",
        "Lateks bez Hi-Float unosi się 18 do 24 godzin. Z Hi-Float nawet 20 razy dłużej, folia wytrzymuje wiele dni. Na tydzień wybieram folię albo instalację na powietrze.",
        "Folia i lateks z Hi-Float: tak. Lateks bez Hi-Float pompuję w dniu eventu, jak najbliżej jego startu. A auto zostaje chłodne.",
    ],
    "avoid_lead": "Czego zawsze unikasz:",
    "steps5": ["Wdychania: pompka albo zawór butli, nigdy usta", "Wypuszczania balonów do nieba", "Helu w R5 albo 260: nie uniosą się", "Unoszących się dekoracji bez obciążnika", "Luźnej butli w aucie albo na słońcu"],
    "client_body": "Hel jest zasobem ograniczonym i twoim największym kosztem zmiennym. Powietrze wszędzie tam, gdzie się da, daje ostrzejszą wycenę, a klient chętnie to słyszy.",
    "cta_label": "Zamów",
    "s3_cover_a": "Hel do balonów Sempertex", "s3_cover_b": "wszędzie", "s3_cover_c": "vs.", "s3_cover_d": "tylko tam, gdzie ma się unosić",
    "s3_left": "HEL WSZĘDZIE", "s3_right": "TYLKO GDZIE TRZEBA", "s3_left_meta": "najdroższy nawyk", "s3_right_meta": "ostrzejsza wycena",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "STARE", "s3_new_lbl": "NOWE",
    "s3_old_tags": ["Hel we wszystkim", "Na wyczucie"], "s3_new_tags": ["Powietrze gdzie się da", "Liczenie", "Hi-Float"],
    "s3_new_quote": "“Hel dostaje tylko to, co ma swobodnie się unosić. Resztę pompuję powietrzem i liczę z góry.”", "s3_new_badge": "15 L na R12",
    "s3_changed_bottom": "Te same balony, ten sam klient.\nMniej helu, lepsza marża.",
    "s3_topic_lbl": "ZASADA", "s3_rule1_topic": "Liczenie", "s3_rule1_old": "Zobaczę, na ile starczy butla",
    "s3_rule1_quote": "“R12 15 L, R18 56 L, R36 226 L. Butla 1 m³ to 66 R12 albo 4 R36.”",
    "s3_rule2_topic": "Czas unoszenia", "s3_rule2_old": "Wszystko pompuję dzień wcześniej",
    "s3_rule2_quote": "“Lateks bez Hi-Float w dniu eventu, z Hi-Float dzień wcześniej, folia kilka dni wcześniej.”",
    "s3_example_lbl": "CZAS UNOSZENIA", "s3_example_quote": "“R9 10 do 14 godzin, R12 18 do 24 godzin, R18 36 godzin, R36 3 do 5 dni. Hi-Float wydłuża to nawet 20 razy.”",
    "s3_client_lbl": "KLIENT", "s3_client_topic": "Rozmowa z klientem",
    "s3_client_quote": "“Powietrze gdzie się da: niższy koszt, ostrzejsza wycena, a klient chętnie to słyszy.”",
    "s3_cta_kicker": "Twoja helowa checklista na następne zlecenie",
    "weight_lbl": "obciążnik", "air_lbl": "powietrze", "helium_lbl": "hel",
},
"el": {
    "cover_pills": ["15 L ανά R12…", "Hi-Float ×20…", "Ποτέ απελευθέρωση…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Οδηγός ηλίου…",
    "steps_title": "Το ήλιο το χρησιμοποιείς μόνο για ό,τι πρέπει πραγματικά να αιωρείται.", "steps_lead": "Οι 3 χρυσοί κανόνες:",
    "steps": ["Ποτέ εισπνοή: εκτοπίζει το οξυγόνο", "Ποτέ απελευθέρωση μπαλονιών στον ουρανό", "Κάθε αιωρούμενη κατασκευή θέλει βαρίδι, και σε εσωτερικό χώρο"],
    "steps_label": "Τα βασικά",
    "rule1_label": "Κανόνας 1", "rule1_title": "Υπολόγισε πρώτα: λίτρα ανά μέγεθος",
    "rule1_body": "Ένα R12 θέλει 15 L ήλιο, ένα R18 56 L, ένα R36 226 L. Μια φιάλη 1 m³ έχει 1.000 L: αρκούν για 66 R12 ή 4 R36. Ένα R36 καταναλώνει 15 φορές περισσότερο ήλιο από ένα R12, οπότε βάλ' το στην προσφορά σου.",
    "rule1_tags": ["R12 · 15 L", "R18 · 56 L", "R36 · 226 L"],
    "rule2_label": "Κανόνας 2", "rule2_title": "Έτσι αιωρούνται περισσότερο",
    "rule2_body": "Το Hi-Float στο εσωτερικό του latex αυξάνει τον χρόνο αιώρησης έως 20 φορές. Το foil κρατά το ήλιο για μέρες χωρίς επεξεργασία. Latex χωρίς Hi-Float: φούσκωμα την ίδια μέρα. Με Hi-Float: την προηγούμενη. Foil: μέρες πριν. Η ζέστη διαστέλλει το ήλιο, το κρύο κάνει τα μπαλόνια να κατεβαίνουν προσωρινά.",
    "rule2_facts": [["×20", "αιώρηση με Hi-Float"], ["μέρες", "foil, χωρίς επεξεργασία"], ["ίδια μέρα", "φούσκωμα latex χωρίς Hi-Float"], ["0 λεπτά", "σε ζεστό αυτοκίνητο"]],
    "example_label": "Χρόνοι αιώρησης", "example_title": "Latex χωρίς Hi-Float, κατά μέσο όρο",
    "example_sizes": [["R9", "10 έως 14 ώρες"], ["R12", "18 έως 24 ώρες"], ["R18", "36 ώρες"], ["R36", "3 έως 5 μέρες"]],
    "example_body": "Τέσσερα μεγέθη, τέσσερις χρόνοι αιώρησης, εδώ σε {p0}, {p1}, {p2} και {p3}. Το Hi-Float τους πολλαπλασιάζει έως 20 φορές. Ο πλήρης πίνακας με λίτρα, άνωση και χρόνο αιώρησης ανά μέγεθος είναι στο Sempertex Gas Capacity Chart.",
    "client_label": "Συζήτηση με πελάτη", "client_title": "Τι απαντάς όταν ο πελάτης ρωτά",
    "client_answers": [
        "Μια γιρλάντα την κρεμάμε και τη φουσκώνουμε με αέρα. Το ήλιο εδώ θα πρόσθετε μόνο κόστος. Αν θέλεις κάτι που αιωρείται, βάζω 3 R12 σε βαρίδι δίπλα στο τραπέζι.",
        "Το latex χωρίς Hi-Float αιωρείται 18 έως 24 ώρες. Με Hi-Float έως 20 φορές περισσότερο, το foil αντέχει μέρες. Για μία εβδομάδα διαλέγω foil ή κατασκευή με αέρα.",
        "Foil και latex με Hi-Float: ναι. Το latex χωρίς Hi-Float το φουσκώνω την ίδια μέρα, όσο πιο κοντά στην εκδήλωση γίνεται. Και το αυτοκίνητο μένει δροσερό.",
    ],
    "avoid_lead": "Τι αποφεύγεις πάντα:",
    "steps5": ["Εισπνοή: τρόμπα ή βάνα φιάλης, ποτέ το στόμα", "Απελευθέρωση μπαλονιών", "Ήλιο σε R5 ή 260: δεν αιωρούνται", "Αιωρούμενη κατασκευή χωρίς βαρίδι", "Φιάλη ελεύθερη στο αυτοκίνητο ή στον ήλιο"],
    "client_body": "Το ήλιο είναι πεπερασμένο και το μεγαλύτερο μεταβλητό σου κόστος. Αέρας όπου γίνεται κάνει την προσφορά σου πιο ανταγωνιστική, και ο πελάτης χαίρεται να το ακούει.",
    "cta_label": "Παραγγελία",
    "s3_cover_a": "Ήλιο για μπαλόνια Sempertex", "s3_cover_b": "παντού", "s3_cover_c": "vs.", "s3_cover_d": "μόνο όπου πρέπει να αιωρείται",
    "s3_left": "ΗΛΙΟ ΠΑΝΤΟΥ", "s3_right": "ΜΟΝΟ ΟΠΟΥ ΧΡΕΙΑΖΕΤΑΙ", "s3_left_meta": "η πιο ακριβή συνήθεια", "s3_right_meta": "πιο σωστή προσφορά",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["Ήλιο σε όλα", "Με το μάτι"], "s3_new_tags": ["Αέρας όπου γίνεται", "Υπολογισμός", "Hi-Float"],
    "s3_new_quote": "“Ήλιο παίρνει μόνο ό,τι πρέπει να αιωρείται ελεύθερα. Τα υπόλοιπα τα φουσκώνω με αέρα και τα υπολογίζω από πριν.”", "s3_new_badge": "15 L ανά R12",
    "s3_changed_bottom": "Ίδια μπαλόνια, ίδιος πελάτης.\nΛιγότερο ήλιο, καλύτερο περιθώριο.",
    "s3_topic_lbl": "ΚΑΝΟΝΑΣ", "s3_rule1_topic": "Υπολογισμός", "s3_rule1_old": "Θα δω πόσο βγάζει η φιάλη",
    "s3_rule1_quote": "“R12 15 L, R18 56 L, R36 226 L. Μία φιάλη 1 m³ είναι 66 R12 ή 4 R36.”",
    "s3_rule2_topic": "Αιώρηση", "s3_rule2_old": "Όλα φουσκωμένα από την προηγούμενη",
    "s3_rule2_quote": "“Latex χωρίς Hi-Float την ίδια μέρα, με Hi-Float την προηγούμενη, foil μέρες πριν.”",
    "s3_example_lbl": "ΑΙΩΡΗΣΗ", "s3_example_quote": "“R9 10 έως 14 ώρες, R12 18 έως 24 ώρες, R18 36 ώρες, R36 3 έως 5 μέρες. Το Hi-Float τα κάνει έως 20 φορές περισσότερο.”",
    "s3_client_lbl": "ΠΕΛΑΤΗΣ", "s3_client_topic": "Συζήτηση με πελάτη",
    "s3_client_quote": "“Αέρας όπου γίνεται: λιγότερο κόστος, πιο σωστή προσφορά, και ο πελάτης χαίρεται να το ακούει.”",
    "s3_cta_kicker": "Η checklist ηλίου σου για την επόμενη δουλειά",
    "weight_lbl": "βαρίδι", "air_lbl": "αέρας", "helium_lbl": "ήλιο",
},
"hu": {
    "cover_pills": ["15 L egy R12-höz…", "Hi-Float ×20…", "Soha ne engedd el…"], "cover_with": "partner:", "cover_brand": "Sempertex Europe", "cover_tag": "Hélium kisokos…",
    "steps_title": "Héliumot csak oda tegyél, ahol tényleg lebegnie kell.", "steps_lead": "A 3 aranyszabály:",
    "steps": ["Soha ne lélegezd be: kiszorítja az oxigént", "Soha ne engedd el a lufikat", "Minden lebegő dekorációt nehezékkel rögzíts, beltéren is"],
    "steps_label": "Az alapok",
    "rule1_label": "1. szabály", "rule1_title": "Számolj előre: liter méretenként",
    "rule1_body": "Egy R12-höz 15 L hélium kell, egy R18-hoz 56 L, egy R36-hoz 226 L. Egy 1 m³-es palackban 1000 L van: ez 66 R12-re vagy 4 R36-ra elég. Egy R36 15-ször annyi héliumot fogyaszt, mint egy R12, ezért tedd bele az árajánlatba.",
    "rule1_tags": ["R12 · 15 L", "R18 · 56 L", "R36 · 226 L"],
    "rule2_label": "2. szabály", "rule2_title": "Így lebegnek tovább",
    "rule2_body": "A latex belsejébe tett Hi-Float akár 20-szorosára növeli a lebegési időt. A fólia kezelés nélkül is napokig tartja a héliumot. Kezeletlen latexet aznap fújj fel, Hi-Floattal előző nap, fóliát napokkal korábban. A meleg tágítja a héliumot, a hideg egy időre leülteti a lufikat.",
    "rule2_facts": [["×20", "lebegési idő Hi-Floattal"], ["napok", "fólia, kezelés nélkül"], ["aznap", "kezeletlen latex felfújása"], ["0 perc", "forró autóban"]],
    "example_label": "Lebegési idők", "example_title": "Kezeletlen latex, átlagosan",
    "example_sizes": [["R9", "10-14 óra"], ["R12", "18-24 óra"], ["R18", "36 óra"], ["R36", "3-5 nap"]],
    "example_body": "Négy méret, négy lebegési idő, itt {p0}, {p1}, {p2} és {p3} színekben. A Hi-Float ezt akár 20-szorosára növeli. A teljes táblázat literrel, emelőerővel és lebegési idővel méretenként a Sempertex Gas Capacity Chartban van.",
    "client_label": "Ügyfélbeszélgetés", "client_title": "Mit válaszolsz, ha az ügyfél megkérdezi",
    "client_answers": [
        "A girlandot felakasztjuk és levegővel fújjuk. A hélium itt csak a költséget növelné. Ha szeretnél valamit, ami lebeg, teszek 3 R12-t nehezékre az asztal mellé.",
        "A kezeletlen latex 18-24 órát lebeg. Hi-Floattal akár 20-szor tovább, a fólia napokig bírja. Egy hétre fóliát vagy levegős installációt választok.",
        "Fólia és Hi-Floatos latex: igen. A kezeletlen latexet aznap fújom fel, a rendezvényhez a lehető legközelebb. És az autó hűvös marad.",
    ],
    "avoid_lead": "Amit mindig elkerülsz:",
    "steps5": ["Belélegzés: pumpa vagy palackcsap, soha a száj", "Lufik elengedése", "Hélium R5-ben vagy 260-ban: nem lebegnek", "Lebegő munka nehezék nélkül", "Palack szabadon az autóban vagy a napon"],
    "client_body": "A hélium véges, és a legnagyobb változó költséged. Levegő mindenhol, ahol lehet: élesebb árajánlat, és az ügyfél ezt szívesen hallja.",
    "cta_label": "Rendelés",
    "s3_cover_a": "Hélium a Sempertex lufikhoz", "s3_cover_b": "mindenhova", "s3_cover_c": "vs.", "s3_cover_d": "csak oda, ahol lebegnie kell",
    "s3_left": "HÉLIUM MINDENHOVA", "s3_right": "CSAK AHOL KELL", "s3_left_meta": "a legdrágább szokás", "s3_right_meta": "élesebb árajánlat",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "RÉGI", "s3_new_lbl": "ÚJ",
    "s3_old_tags": ["Hélium mindenbe", "Érzésre"], "s3_new_tags": ["Levegő, ahol lehet", "Számolás", "Hi-Float"],
    "s3_new_quote": "“Csak az kap héliumot, aminek szabadon lebegnie kell. A többit levegővel fújom, és előre kiszámolom.”", "s3_new_badge": "15 L egy R12-höz",
    "s3_changed_bottom": "Ugyanazok a lufik, ugyanaz az ügyfél.\nKevesebb hélium, jobb árrés.",
    "s3_topic_lbl": "SZABÁLY", "s3_rule1_topic": "Számolás", "s3_rule1_old": "Majd meglátom, mire elég a palack",
    "s3_rule1_quote": "“R12 15 L, R18 56 L, R36 226 L. Egy 1 m³-es palack 66 R12 vagy 4 R36.”",
    "s3_rule2_topic": "Lebegési idő", "s3_rule2_old": "Mindent előző nap felfújok",
    "s3_rule2_quote": "“Kezeletlen latex aznap, Hi-Floattal előző nap, fólia napokkal korábban.”",
    "s3_example_lbl": "LEBEGÉSI IDŐ", "s3_example_quote": "“R9 10-14 óra, R12 18-24 óra, R18 36 óra, R36 3-5 nap. A Hi-Float ezt akár 20-szorosára növeli.”",
    "s3_client_lbl": "ÜGYFÉL", "s3_client_topic": "Ügyfélbeszélgetés",
    "s3_client_quote": "“Levegő, ahol lehet: kisebb költség, élesebb árajánlat, és az ügyfél ezt szívesen hallja.”",
    "s3_cta_kicker": "A hélium-checklisted a következő munkához",
    "weight_lbl": "nehezék", "air_lbl": "levegő", "helium_lbl": "hélium",
},
"lt": {
    "cover_pills": ["15 L vienam R12…", "Hi-Float ×20…", "Niekada nepaleisk…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Helio gidas…",
    "steps_title": "Helį naudok tik ten, kur dekoracija tikrai turi skristi.", "steps_lead": "3 auksinės taisyklės:",
    "steps": ["Niekada neįkvėpk: jis išstumia deguonį", "Niekada nepaleisk balionų į dangų", "Kiekvieną skrendančią dekoraciją pritvirtink svareliu, ir patalpoje"],
    "steps_label": "Pagrindai",
    "rule1_label": "1 taisyklė", "rule1_title": "Suskaičiuok iš anksto: litrai pagal dydį",
    "rule1_body": "R12 reikia 15 L helio, R18 56 L, R36 226 L. 1 m³ balione yra 1000 L: užtenka 66 R12 arba 4 R36. R36 suvartoja 15 kartų daugiau helio nei R12, todėl įtrauk tai į pasiūlymą.",
    "rule1_tags": ["R12 · 15 L", "R18 · 56 L", "R36 · 226 L"],
    "rule2_label": "2 taisyklė", "rule2_title": "Taip jie skrenda ilgiau",
    "rule2_body": "Hi-Float latekso viduje pailgina skrydžio laiką iki 20 kartų. Folija išlaiko helį kelias dienas be apdorojimo. Neapdorotą lateksą pripūsk tą pačią dieną, su Hi-Float dieną prieš, foliją kelias dienas prieš. Šiluma plečia helį, šaltis laikinai nuleidžia balionus.",
    "rule2_facts": [["×20", "skrydžio laikas su Hi-Float"], ["dienos", "folija, be apdorojimo"], ["tą pačią dieną", "neapdoroto latekso pūtimas"], ["0 min", "karštame automobilyje"]],
    "example_label": "Skrydžio laikas", "example_title": "Neapdorotas lateksas, vidutiniškai",
    "example_sizes": [["R9", "10-14 val."], ["R12", "18-24 val."], ["R18", "36 val."], ["R36", "3-5 dienos"]],
    "example_body": "Keturi dydžiai, keturi skrydžio laikai, čia {p0}, {p1}, {p2} ir {p3} spalvomis. Hi-Float juos pailgina iki 20 kartų. Visa lentelė su litrais, keliamąja galia ir skrydžio laiku pagal dydį yra Sempertex Gas Capacity Chart.",
    "client_label": "Pokalbis su klientu", "client_title": "Ką atsakai, kai klientas klausia",
    "client_answers": [
        "Girliandą pakabiname ir pripučiame oru. Helis čia tik pabrangintų. Jei nori, kad kažkas skristų, pastatysiu 3 R12 ant svarelio šalia stalo.",
        "Neapdorotas lateksas skrenda 18-24 valandas. Su Hi-Float iki 20 kartų ilgiau, folija laikosi kelias dienas. Savaitei renkuosi foliją arba oru pripūstą instaliaciją.",
        "Folija ir lateksas su Hi-Float: taip. Neapdorotą lateksą pripučiu tą pačią dieną, kuo arčiau renginio. O automobilis lieka vėsus.",
    ],
    "avoid_lead": "Ko visada vengi:",
    "steps5": ["Įkvėpimo: pompa arba baliono čiaupas, niekada burna", "Balionų paleidimo į dangų", "Helio R5 ar 260 balione: jie neskrenda", "Skrendančios dekoracijos be svarelio", "Palaido dujų baliono automobilyje ar saulėje"],
    "client_body": "Helis yra ribotas ir didžiausia tavo kintama sąnauda. Oras visur, kur įmanoma, daro pasiūlymą konkurencingesnį, ir klientas tai mielai girdi.",
    "cta_label": "Užsakyti",
    "s3_cover_a": "Helis Sempertex balionams", "s3_cover_b": "visur", "s3_cover_c": "vs.", "s3_cover_d": "tik ten, kur turi skristi",
    "s3_left": "HELIS VISUR", "s3_right": "TIK KUR REIKIA", "s3_left_meta": "brangiausias įprotis", "s3_right_meta": "tikslesnis pasiūlymas",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "SENA", "s3_new_lbl": "NAUJA",
    "s3_old_tags": ["Helis į viską", "Iš akies"], "s3_new_tags": ["Oras, kur įmanoma", "Skaičiavimas", "Hi-Float"],
    "s3_new_quote": "“Helį gauna tik tai, kas turi laisvai skristi. Visa kita pripučiu oru ir suskaičiuoju iš anksto.”", "s3_new_badge": "15 L vienam R12",
    "s3_changed_bottom": "Tie patys balionai, tas pats klientas.\nMažiau helio, geresnė marža.",
    "s3_topic_lbl": "TAISYKLĖ", "s3_rule1_topic": "Skaičiavimas", "s3_rule1_old": "Pažiūrėsiu, kiek balionas duos",
    "s3_rule1_quote": "“R12 15 L, R18 56 L, R36 226 L. Vienas 1 m³ balionas yra 66 R12 arba 4 R36.”",
    "s3_rule2_topic": "Skrydžio laikas", "s3_rule2_old": "Viską pripučiu dieną prieš",
    "s3_rule2_quote": "“Neapdorotas lateksas tą pačią dieną, su Hi-Float dieną prieš, folija kelias dienas prieš.”",
    "s3_example_lbl": "SKRYDŽIO LAIKAS", "s3_example_quote": "“R9 10-14 valandų, R12 18-24 valandos, R18 36 valandos, R36 3-5 dienos. Hi-Float tai pailgina iki 20 kartų.”",
    "s3_client_lbl": "KLIENTAS", "s3_client_topic": "Pokalbis su klientu",
    "s3_client_quote": "“Oras, kur įmanoma: mažesnės sąnaudos, tikslesnis pasiūlymas, ir klientas tai mielai girdi.”",
    "s3_cta_kicker": "Tavo helio kontrolinis sąrašas kitam užsakymui",
    "weight_lbl": "svarelis", "air_lbl": "oras", "helium_lbl": "helis",
},
}

# ---------------------------------------------------------------- VARIANTEN (per distri anders, op basis van vi)
VARIANTS = {
"nl": {
  "cover_title": ["Helium voor je Sempertex ballonnen: hoeveel, hoelang en wat je vermijdt", "1 fles helium = 66 Sempertex R12 of 4 reuzen van 36 inch", "Helium of lucht? De regel die je offerte voor Sempertex ballonnen scherper maakt"],
  "cover_sub": ["Liters per maat, zweeftijden en de 3 gouden regels, uit de Sempertex blog. Om te printen naast je offerte.", "Helium is je grootste variabele kost. Deze cijfers vertellen je waar het moet en waar lucht volstaat."],
  "client_question": ["Kan die slinger ook zweven, zodat hij boven de tafel hangt?", "Blijven de ballonnen een hele week hangen?", "Kun je alles de dag ervoor al klaarzetten?"],
  "s3_old_quote": ["“Helium hangt toch mooier”", "“Ik vul alles, dan ben ik zeker”", "“De fles is op als hij op is”"],
  "s3_client_old": ["“Ik doe wat de klant vraagt”", "“Helium is nu eenmaal duur”"],
  "cta_title_tpl": "Bestel je Sempertex ballonnen bij {name}", "cta_sub_generic": "Bestel per maat uit deze post en reken je helium vooraf uit.",
},
"en": {
  "cover_title": ["Helium for your Sempertex balloons: how much, how long and what to avoid", "1 cylinder of helium = 66 Sempertex R12 or 4 giants of 36 inch", "Helium or air? The rule that sharpens your quote for Sempertex balloons"],
  "cover_sub": ["Litres per size, float times and the 3 golden rules, from the Sempertex blog. Print it next to your quote sheet.", "Helium is your biggest variable cost. These figures tell you where it's needed and where air will do."],
  "client_question": ["Can that garland float too, so it hangs above the table?", "Will the balloons stay up for a whole week?", "Can you have everything ready the day before?"],
  "s3_old_quote": ["“Helium just looks nicer”", "“I fill everything, then I'm safe”", "“The cylinder's empty when it's empty”"],
  "s3_client_old": ["“I do what the client asks”", "“Helium is just expensive”"],
  "cta_title_tpl": "Order your Sempertex balloons at {name}", "cta_sub_generic": "Order by size from this post and work out your helium before the job.",
},
"de": {
  "cover_title": ["Helium für deine Sempertex Ballons: wie viel, wie lange und was du vermeidest", "1 Flasche Helium = 66 Sempertex R12 oder 4 Riesen mit 36 Zoll", "Helium oder Luft? Die Regel, die dein Angebot für Sempertex Ballons schärfer macht"],
  "cover_sub": ["Liter pro Größe, Schwebezeiten und die 3 goldenen Regeln, aus dem Sempertex Blog. Zum Ausdrucken neben dein Angebot.", "Helium ist dein größter variabler Kostenpunkt. Diese Zahlen zeigen dir, wo es nötig ist und wo Luft reicht."],
  "client_question": ["Kann die Girlande auch schweben, damit sie über dem Tisch hängt?", "Bleiben die Ballons eine ganze Woche oben?", "Kannst du alles schon am Vortag fertig machen?"],
  "s3_old_quote": ["“Helium sieht einfach schöner aus”", "“Ich fülle alles, dann bin ich sicher”", "“Die Flasche ist leer, wenn sie leer ist”"],
  "s3_client_old": ["“Ich mache, was der Kunde will”", "“Helium ist nun mal teuer”"],
  "cta_title_tpl": "Bestell deine Sempertex Ballons bei {name}", "cta_sub_generic": "Bestell nach Größe aus diesem Post und rechne dein Helium vor dem Job durch.",
},
"fr": {
  "cover_title": ["L'hélium pour tes ballons Sempertex : combien, combien de temps et quoi éviter", "1 bouteille d'hélium = 66 Sempertex R12 ou 4 géants de 36 pouces", "Hélium ou air ? La règle qui rend ton devis pour ballons Sempertex plus juste"],
  "cover_sub": ["Litres par taille, temps de flottaison et les 3 règles d'or, tirés du blog Sempertex. À imprimer à côté de ton devis.", "L'hélium est ton plus gros coût variable. Ces chiffres te disent où il est nécessaire et où l'air suffit."],
  "client_question": ["La guirlande peut-elle flotter aussi, au-dessus de la table ?", "Les ballons restent-ils en l'air toute une semaine ?", "Tu peux tout préparer la veille ?"],
  "s3_old_quote": ["“L'hélium, c'est quand même plus joli”", "“Je gonfle tout à l'hélium, comme ça je suis sûr”", "“La bouteille est vide quand elle est vide”"],
  "s3_client_old": ["“Je fais ce que le client demande”", "“L'hélium, c'est cher, c'est comme ça”"],
  "cta_title_tpl": "Commande tes ballons Sempertex chez {name}", "cta_sub_generic": "Commande par taille à partir de ce post et calcule ton hélium avant la prestation.",
},
"it": {
  "cover_title": ["Elio per i tuoi palloncini Sempertex: quanto, per quanto tempo e cosa evitare", "1 bombola di elio = 66 Sempertex R12 o 4 giganti da 36 pollici", "Elio o aria? La regola che rende più giusto il preventivo per i palloncini Sempertex"],
  "cover_sub": ["Litri per misura, tempi di volo e le 3 regole d'oro, dal blog Sempertex. Da stampare accanto al preventivo.", "L'elio è il tuo costo variabile più grande. Questi numeri ti dicono dove serve e dove basta l'aria."],
  "client_question": ["La ghirlanda può volare anche lei, sopra il tavolo?", "I palloncini restano su per una settimana intera?", "Puoi preparare tutto il giorno prima?"],
  "s3_old_quote": ["“L'elio è comunque più bello”", "“Gonfio tutto a elio, così sono tranquillo”", "“La bombola finisce quando finisce”"],
  "s3_client_old": ["“Faccio quello che chiede il cliente”", "“L'elio costa, punto”"],
  "cta_title_tpl": "Ordina i tuoi palloncini Sempertex da {name}", "cta_sub_generic": "Ordina per misura da questo post e calcola l'elio prima del lavoro.",
},
"pl": {
  "cover_title": ["Hel do balonów Sempertex: ile, na jak długo i czego unikać", "1 butla helu = 66 balonów Sempertex R12 albo 4 olbrzymy 36 cali", "Hel czy powietrze? Zasada, która wyostrza twoją wycenę balonów Sempertex"],
  "cover_sub": ["Litry na rozmiar, czasy unoszenia i 3 złote zasady, z bloga Sempertex. Do wydrukowania obok wyceny.", "Hel to twój największy koszt zmienny. Te liczby mówią, gdzie jest potrzebny, a gdzie wystarczy powietrze."],
  "client_question": ["Czy girlanda też może się unosić, nad stołem?", "Czy balony wytrzymają cały tydzień?", "Możesz przygotować wszystko dzień wcześniej?"],
  "s3_old_quote": ["“Hel po prostu ładniej wygląda”", "“Pompuję wszystko helem, to mam spokój”", "“Butla się kończy, kiedy się kończy”"],
  "s3_client_old": ["“Robię to, o co prosi klient”", "“Hel jest drogi i tyle”"],
  "cta_title_tpl": "Zamów balony Sempertex w {name}", "cta_sub_generic": "Zamów według rozmiarów z tego posta i policz hel przed zleceniem.",
},
"el": {
  "cover_title": ["Ήλιο για τα μπαλόνια Sempertex: πόσο, για πόσο και τι αποφεύγεις", "1 φιάλη ήλιο = 66 Sempertex R12 ή 4 γίγαντες 36 ιντσών", "Ήλιο ή αέρας; Ο κανόνας που κάνει πιο σωστή την προσφορά σου για μπαλόνια Sempertex"],
  "cover_sub": ["Λίτρα ανά μέγεθος, χρόνοι αιώρησης και οι 3 χρυσοί κανόνες, από το blog της Sempertex. Για εκτύπωση δίπλα στην προσφορά σου.", "Το ήλιο είναι το μεγαλύτερο μεταβλητό σου κόστος. Αυτοί οι αριθμοί σου λένε πού χρειάζεται και πού αρκεί ο αέρας."],
  "client_question": ["Μπορεί και η γιρλάντα να αιωρείται, πάνω από το τραπέζι;", "Θα μείνουν τα μπαλόνια ψηλά μια ολόκληρη εβδομάδα;", "Μπορείς να τα ετοιμάσεις όλα από την προηγούμενη;"],
  "s3_old_quote": ["“Το ήλιο φαίνεται πιο όμορφο”", "“Βάζω ήλιο παντού, για σιγουριά”", "“Η φιάλη τελειώνει όταν τελειώνει”"],
  "s3_client_old": ["“Κάνω ό,τι ζητά ο πελάτης”", "“Το ήλιο είναι ακριβό, τέλος”"],
  "cta_title_tpl": "Παράγγειλε τα μπαλόνια Sempertex σου από {name}", "cta_sub_generic": "Παράγγειλε ανά μέγεθος από αυτό το post και υπολόγισε το ήλιο πριν τη δουλειά.",
},
"hu": {
  "cover_title": ["Hélium a Sempertex lufikhoz: mennyi, meddig és mit kerülj", "1 palack hélium = 66 Sempertex R12 vagy 4 óriás 36 inches lufi", "Hélium vagy levegő? A szabály, amitől élesebb lesz a Sempertex lufis árajánlatod"],
  "cover_sub": ["Liter méretenként, lebegési idők és a 3 aranyszabály, a Sempertex blogból. Nyomtasd ki az árajánlatod mellé.", "A hélium a legnagyobb változó költséged. Ezek a számok megmondják, hol kell, és hol elég a levegő."],
  "client_question": ["A girland is lebeghet, az asztal fölött?", "Fent maradnak a lufik egy egész hétig?", "Elő tudod készíteni az egészet előző nap?"],
  "s3_old_quote": ["“A hélium egyszerűen szebb”", "“Mindent héliummal fújok, úgy biztos”", "“A palack akkor fogy ki, amikor kifogy”"],
  "s3_client_old": ["“Azt csinálom, amit az ügyfél kér”", "“A hélium drága, és kész”"],
  "cta_title_tpl": "Rendeld a Sempertex lufijaidat innen: {name}", "cta_sub_generic": "Rendelj méret szerint a poszt alapján, és számold ki a héliumot a munka előtt.",
},
"lt": {
  "cover_title": ["Helis tavo Sempertex balionams: kiek, kiek laiko ir ko vengti", "1 helio balionas = 66 Sempertex R12 arba 4 milžinai po 36 colius", "Helis ar oras? Taisyklė, kuri patikslina tavo Sempertex balionų pasiūlymą"],
  "cover_sub": ["Litrai pagal dydį, skrydžio laikai ir 3 auksinės taisyklės iš Sempertex tinklaraščio. Atsispausdink šalia pasiūlymo.", "Helis yra didžiausia tavo kintama sąnauda. Šie skaičiai parodo, kur jo reikia ir kur užtenka oro."],
  "client_question": ["Ar girlianda irgi gali skristi, virš stalo?", "Ar balionai išsilaikys visą savaitę?", "Ar gali viską paruošti dieną prieš?"],
  "s3_old_quote": ["“Su heliu tiesiog gražiau”", "“Pripučiu viską heliu, tada ramu”", "“Balionas baigiasi, kai baigiasi”"],
  "s3_client_old": ["“Darau tai, ko prašo klientas”", "“Helis brangus, ir tiek”"],
  "cta_title_tpl": "Užsisakyk Sempertex balionus iš {name}", "cta_sub_generic": "Užsisakyk pagal dydžius iš šio įrašo ir suskaičiuok helį prieš darbą.",
},
}

CAPTIONS_TPL = {
 "nl": "Helium gebruik je enkel voor wat echt moet zweven. In deze carousel: liters per maat (R12 15 L, R18 56 L, R36 226 L), wat 1 fles van 1 m³ oplevert, zweeftijden per maat en de 3 gouden regels. Plus wat je antwoordt als de klant vraagt of de slinger ook kan zweven.\n\nBestel je Sempertex ballonnen bij {domain}.\n\n#helium #sempertex #{tag} #ballondecoratie #ballonnen #ballonartiest",
 "en": "Helium is only for designs that have to float. In this carousel: litres per size (R12 15 L, R18 56 L, R36 226 L), what one 1 m³ cylinder gives you, float times per size and the 3 golden rules. Plus what to answer when the client asks if the garland can float too.\n\nOrder your Sempertex balloons at {domain}.\n\n#helium #sempertex #{tag} #balloondecor #balloons #balloonartist",
 "de": "Helium nimmst du nur für Designs, die wirklich schweben müssen. Im Carousel: Liter pro Größe (R12 15 L, R18 56 L, R36 226 L), was eine 1-m³-Flasche bringt, Schwebezeiten pro Größe und die 3 goldenen Regeln. Plus, was du antwortest, wenn der Kunde fragt, ob die Girlande auch schweben kann.\n\nBestell deine Sempertex Ballons bei {domain}.\n\n#helium #sempertex #{tag} #ballondeko #ballons #ballonkünstler",
 "fr": "L'hélium, c'est uniquement pour ce qui doit flotter. Dans ce carrousel : litres par taille (R12 15 L, R18 56 L, R36 226 L), ce que donne une bouteille de 1 m³, temps de flottaison par taille et les 3 règles d'or. Plus ce que tu réponds quand le client demande si la guirlande peut flotter aussi.\n\nCommande tes ballons Sempertex chez {domain}.\n\n#helium #sempertex #{tag} #decorationballons #ballons #artisteballon",
 "it": "L'elio lo usi solo per ciò che deve volare. Nel carosello: litri per misura (R12 15 L, R18 56 L, R36 226 L), cosa dà una bombola da 1 m³, tempi di volo per misura e le 3 regole d'oro. Più cosa rispondi quando il cliente chiede se anche la ghirlanda può volare.\n\nOrdina i tuoi palloncini Sempertex da {domain}.\n\n#elio #sempertex #{tag} #palloncini #decorazioni #balloonartist",
 "pl": "Helu używasz tylko tam, gdzie coś ma się unosić. W karuzeli: litry na rozmiar (R12 15 L, R18 56 L, R36 226 L), ile daje butla 1 m³, czasy unoszenia dla każdego rozmiaru i 3 złote zasady. Plus co odpowiedzieć, gdy klient pyta, czy girlanda też może się unosić.\n\nZamów balony Sempertex w {domain}.\n\n#hel #sempertex #{tag} #dekoracjebalonowe #balony #artystabalonowy",
 "el": "Το ήλιο το χρησιμοποιείς μόνο για ό,τι πρέπει να αιωρείται. Στο carousel: λίτρα ανά μέγεθος (R12 15 L, R18 56 L, R36 226 L), τι δίνει μια φιάλη 1 m³, χρόνοι αιώρησης ανά μέγεθος και οι 3 χρυσοί κανόνες. Και τι απαντάς όταν ο πελάτης ρωτά αν μπορεί να αιωρείται και η γιρλάντα.\n\nΠαράγγειλε τα μπαλόνια Sempertex σου από {domain}.\n\n#ήλιο #sempertex #{tag} #μπαλονια #balloonartist",
 "hu": "Héliumot csak oda tegyél, ahol tényleg lebegnie kell. A carouselben: liter méretenként (R12 15 L, R18 56 L, R36 226 L), mire elég egy 1 m³-es palack, lebegési idők méretenként és a 3 aranyszabály. Plusz mit válaszolj, ha az ügyfél megkérdezi, lebeghet-e a girland is.\n\nRendeld a Sempertex lufijaidat innen: {domain}.\n\n#hélium #sempertex #{tag} #lufidekoracio #lufi #lufiművész",
 "lt": "Helį naudok tik ten, kur dekoracija tikrai turi skristi. Karuselėje: litrai pagal dydį (R12 15 L, R18 56 L, R36 226 L), kiek duoda 1 m³ balionas, skrydžio laikas pagal dydį ir 3 auksinės taisyklės. Ir ką atsakyti, kai klientas klausia, ar girlianda irgi gali skristi.\n\nUžsisakyk Sempertex balionus iš {domain}.\n\n#helis #sempertex #{tag} #balionai #balionumenininkas",
}

# ---------------------------------------------------------------- VISUALS
CUR = {"pal": ["rosewood", "eucalyptus", "greentea", "golddust"]}  # per distri gezet uit b["pal"]

def fill_pal(b, c):
    """Vult {p0}..{p3} in de copy met kleurnaam + code van het palet van deze distri; kiest het klantantwoord bij de vraag."""
    lab = {f"p{i}": G["pal_label"](k, short=False).replace("Fashion ", "").replace("Pastel ", "") for i, k in enumerate(b["pal"][:4])}
    out = {}
    for k, v in c.items():
        if isinstance(v, str): out[k] = v.format(**lab) if "{p" in v else v
        else: out[k] = v
    qs = VARIANTS[b["lang"]]["client_question"]
    qi = qs.index(c["client_question"]) if c["client_question"] in qs else 0
    out["client_answer"] = c["client_answers"][qi]
    return out

def _bl(key, size, cls=""):
    return G["balloon"](key, "fashion", size, cls=cls)

def size_row(sizes, keys, big=210, labels=None, sub=None, ink="#111", gap=26, lab_size=24, sub_size=19):
    """Ballonnen van klein naar groot, onderkant uitgelijnd, met label (maat) en sublabel (zweeftijd of liters)."""
    n = len(sizes); esc = G["esc"]
    scale = {3: (0.52, 0.74, 1.0), 4: (0.42, 0.56, 0.76, 1.0)}[n]
    out = f'<div style="display:flex;align-items:flex-end;justify-content:center;gap:{gap}px">'
    for i in range(n):
        w = int(big * scale[i]); k = keys[i % len(keys)]
        lab = f'<div class="pname" style="font-size:{lab_size}px;margin-top:10px;color:{ink};white-space:nowrap">{esc(labels[i])}</div>' if labels else ""
        sb = f'<div class="pcode-only" style="font-size:{sub_size}px;color:{ink};opacity:.75;white-space:nowrap">{esc(sub[i])}</div>' if sub else ""
        out += f'<div style="text-align:center">{_bl(k, w)}{lab}{sb}</div>'
    return out + '</div>'

def bouquet(keys, size=110, w=360, h=430, weight_lbl="", ink="#111", string="#333", n=3):
    """3 ballonnen op lint naar één gewicht (zwevend design, verzwaard)."""
    esc = G["esc"]; ratio = G["PHOTO_RATIO"]
    pos = [(int(w*0.08), 10), (int(w*0.5 - size/2), 46), (int(w*0.92 - size), 22)][:n]
    bh = int(size * ratio); wx, wy = w // 2, h - 46
    svg = f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="position:absolute;left:0;top:0">'
    for (x, y), k in zip(pos, keys):
        bx, by = x + size // 2, y + bh - 4
        svg += f'<path d="M{bx} {by} C {bx} {by+60}, {wx} {wy-80}, {wx} {wy}" fill="none" stroke="{string}" stroke-width="2.5" stroke-linecap="round"/>'
    svg += '</svg>'
    out = f'<div style="position:relative;width:{w}px;height:{h}px">{svg}'
    for (x, y), k in zip(pos, keys):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px">{_bl(k, size)}</div>'
    out += (f'<div style="position:absolute;left:{wx-44}px;top:{wy-6}px;width:88px;height:44px;border-radius:10px;background:{ink};color:#fff;'
            f'font-size:16px;font-weight:700;display:flex;align-items:center;justify-content:center;letter-spacing:.06em">{esc(weight_lbl.upper())}</div>')
    return out + '</div>'

def garland(keys, big=96, small=62, n=7):
    """Luchtgevulde slinger: groot, klein, groot… licht gedraaid, onderkant uitgelijnd."""
    out = '<div style="display:flex;align-items:flex-end;justify-content:center;gap:0">'
    for i in range(n):
        k = keys[i % len(keys)]; s = big if i % 2 == 0 else small
        rotv = (-10, 12, -6, 10, -12, 8, -9)[i % 7]
        out += f'<div style="margin:0 -9px"><div style="transform:rotate({rotv}deg)">{_bl(k, s)}</div></div>'
    return out + '</div>'

def facts_grid(c, cls="facts", num_size=58, lab_size=22):
    esc = G["esc"]
    cells = "".join(f'<div class="fact"><b style="font-size:{num_size}px">{esc(n)}</b><span style="font-size:{lab_size}px">{esc(l)}</span></div>' for n, l in c["rule2_facts"])
    return f'<div class="{cls}">{cells}</div>'

def avoid_list(c, cls=""):
    esc = G["esc"]
    return ('<div class="' + cls + '">' + "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps5"])) + '</div>')

def helium_everywhere(keys, ink="#111"):
    """'Overal helium': 8 ballonnen op lint, elk apart, kriskras (dure gewoonte)."""
    ratio = G["PHOTO_RATIO"]; w, h = 330, 360
    pos = [(0, 20, 84), (90, 0, 96), (190, 30, 80), (250, 110, 72), (20, 130, 90), (120, 120, 104), (210, 190, 84), (60, 230, 92)]
    svg = f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="position:absolute;left:0;top:0">'
    for i, (x, y, s) in enumerate(pos):
        bx, by = x + s // 2, y + int(s * ratio) - 4
        svg += f'<path d="M{bx} {by} q {(-18, 22)[i%2]} 40 {(6,-8)[i%2]} 90" fill="none" stroke="{ink}" stroke-width="2" opacity=".7" stroke-linecap="round"/>'
    svg += '</svg>'
    out = f'<div style="position:relative;width:{w}px;height:{h}px">{svg}'
    for i, (x, y, s) in enumerate(pos):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px">{_bl(keys[i % len(keys)], s)}</div>'
    return out + '</div>'

def helium_smart(keys, weight_lbl, ink="#111"):
    """'Enkel waar nodig': luchtslinger bovenaan + één verzwaard boeket."""
    return (f'<div style="position:relative;width:330px;height:380px">'
            f'<div style="position:absolute;left:-10px;top:0;width:350px;transform:scale(.9);transform-origin:top left">{garland(keys, 84, 56, 6)}</div>'
            f'<div style="position:absolute;left:30px;top:100px;transform:scale(.78);transform-origin:top left">{bouquet(keys[:3], 110, 340, 370, weight_lbl, ink)}</div></div>')

# ---------------------------------------------------------------- STIJL 1
def s1_slides(b, c):
    CUR["pal"] = b["pal"]; c = fill_pal(b, c); P = b["pal"]
    esc, hl, cursor_svg, arrow_svg, balloon = G["esc"], G["hl"], G["cursor_svg"], G["arrow_svg"], G["balloon"]
    s1_footer, logo_img, rot, STX_FULL = G["s1_footer"], G["logo_img"], G["rot"], G["STX_FULL"]
    S = []
    pills = c["cover_pills"]
    S.append(f"""
<section class="slide s1">
  <h1 data-fit style="position:absolute;left:70px;right:70px;top:250px;max-height:560px;font-size:100px;text-align:center;line-height:1.06">{hl(c['cover_title'])}</h1>
  <div class="pill" style="background:{b['c1']};color:{b['c1t']};right:60px;top:130px;transform:rotate({rot(b,-4)}deg)">{cursor_svg(b['c1'])}{esc(pills[0])}</div>
  <div class="pill" style="background:{b['c2']};color:{b['c2t']};right:90px;top:835px;transform:rotate({rot(b,3)}deg)">{cursor_svg(b['c2'])}{esc(pills[1])}</div>
  <div class="pill" style="background:{b['c3']};color:{b['c3t']};left:90px;top:880px;transform:rotate({rot(b,-2)}deg)">{cursor_svg(b['c3'])}{esc(pills[2])}</div>
  <div style="position:absolute;left:150px;top:960px">{arrow_svg(b['ink'], 130, 120)}</div>
  <div style="position:absolute;left:310px;right:90px;top:1020px;font-size:30px;line-height:1.35">{esc(c['cover_sub'])}</div>
  {s1_footer(b, stx_h=84)}
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s1">
  <div class="box" style="left:70px;top:120px;width:800px;height:560px">
    <h2 data-fit style="font-size:80px;max-height:460px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:760px;top:70px;transform:scale(.74);transform-origin:top left">{bouquet([b['hero'], P[0], P[1]], 110, 360, 430, c['weight_lbl'], b['ink'])}</div>
  <div style="position:absolute;left:120px;top:690px">{arrow_svg(b['ink'], 150, 140)}</div>
  <div class="box" style="left:300px;top:720px;width:710px;height:440px;padding:40px 46px">
    <div style="font-size:30px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:430px;padding:44px 50px">
    <h2 data-fit style="font-size:62px;max-height:150px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:29px">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:650px;height:460px">
    <div class="card" style="top:0;height:380px;transform:translate(60px,-70px) scale(.92);opacity:.5"></div>
    <div class="card" style="top:0;height:380px;transform:translate(30px,-36px) scale(.96);opacity:.75"></div>
    <div class="card" style="top:0;height:430px;display:flex;align-items:flex-end;justify-content:center;padding:30px 40px 36px">
      {size_row([12, 18, 36], [P[0], P[1], P[2]], 230, labels=c['rule1_tags'], ink=b['ink'], gap=50)}
    </div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule2_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:470px;padding:44px 50px">
    <h2 data-fit style="font-size:58px;max-height:200px">{esc(c['rule2_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:28px">{esc(c['rule2_body'])}</div>
  </div>
  <div class="stack" style="top:700px;height:400px">
    <div class="card" style="top:0;height:340px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:380px;padding:30px 34px">{facts_grid(c)}</div>
  </div>
  {s1_footer(b)}
</section>""")
    sizes = c["example_sizes"]
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:560px;padding:40px 30px 36px">
    <h2 data-fit style="font-size:54px;margin-bottom:34px;text-align:center;max-height:130px">{esc(c['example_title'])}</h2>
    {size_row(sizes, P, 240, labels=[f"{s} · {t}" for s, t in sizes], sub=[G['pal_label'](k) for k in P[:4]], ink=b['ink'], gap=22, lab_size=22, sub_size=18)}
  </div>
  <div class="box" style="left:70px;top:770px;width:940px;padding:36px 50px"><div class="body" style="font-size:29px">{esc(c['example_body'])}</div></div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:54px;max-height:140px">{esc(c['client_title'])}</h2>
  <div class="chat" style="top:320px;min-height:130px;padding-right:120px">{esc(c['client_question'])}<div class="send">↑</div></div>
  <div style="position:absolute;left:80px;right:80px;top:490px;display:flex;flex-direction:column;gap:20px">
    <div class="card" style="position:relative;left:auto;right:auto;padding:26px 36px"><div style="font-size:28px;line-height:1.35">{esc(c['client_answer'])}</div></div>
    <div class="card" style="position:relative;left:auto;right:auto;padding:22px 36px"><div style="font-size:25px;font-weight:{b['body_b']};margin-bottom:2px">{esc(c['avoid_lead'])}</div>{avoid_list(c, 'avoid')}</div>
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
  <h1 data-fit style="position:absolute;left:320px;right:70px;top:70px;max-height:430px;font-size:72px">{hl(c['cover_title'])}</h1>
  <div class="frame" style="left:320px;top:520px;width:690px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:460px;flex-direction:row;gap:30px;align-items:flex-end;padding-bottom:20px;box-sizing:border-box">{size_row([12, 18, 36], P, 200, ink="#111", gap=30)}</div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px"><b style="font-size:38px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:640px;width:560px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:400px;padding:10px;box-sizing:border-box"><div style="transform:scale(.8)">{bouquet([b['hero'], P[0], P[1]], 110, 360, 430, c['weight_lbl'], '#111')}</div></div>
  </div>
  <div class="frame" style="left:600px;top:800px;width:410px;transform:rotate({rot(b,3)}deg)">
    <div class="ph" style="height:280px;padding:10px;box-sizing:border-box"><div style="transform:scale(.72)">{garland(P, 84, 56, 5)}</div><div class="pname" style="font-size:20px;margin-top:-30px">{esc(c['air_lbl'])}</div></div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:64px;max-height:160px">{esc(c['rule1_title'])}</h2>
  <div class="frame" style="left:70px;top:350px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:440px;flex-direction:row;justify-content:center;align-items:flex-end;padding:0 20px 30px;box-sizing:border-box">{size_row([12, 18, 36], [P[0], P[1], P[2]], 220, labels=c['rule1_tags'], ink="#111", gap=50)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:900px;font-size:28px">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:60px;max-height:170px">{esc(c['rule2_title'])}</h2>
  <div class="frame" style="left:70px;top:370px;width:940px;transform:rotate({rot(b,1.5)}deg)">
    <div class="ph" style="height:380px;padding:26px 30px;box-sizing:border-box;align-items:stretch;background:#fff">{facts_grid(c, 'facts onwhite')}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:870px;font-size:27px">{esc(c['rule2_body'])}</div>
  {s2_footer(b)}
</section>""")
    sizes = c["example_sizes"]
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:60px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:470px;padding:20px;box-sizing:border-box;align-items:flex-end">{size_row(sizes, P, 230, labels=[f"{s} · {t}" for s, t in sizes], sub=[G['pal_label'](k) for k in P[:4]], ink="#111", gap=20, lab_size=21, sub_size=17)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:880px;font-size:28px">{esc(c['example_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:56px;max-height:150px">{esc(c['client_title'])}</h2>
  <div class="frame" style="left:70px;top:340px;width:940px">
    <div class="ph" style="height:auto;padding:28px 34px;box-sizing:border-box;align-items:flex-start;background:#fff">
      <div style="font-size:30px;line-height:1.3;color:{b['ink']};font-style:italic">{esc(c['client_question'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:14px 0"></div>
      <div style="font-size:25px;line-height:1.35;color:{b['ink']}">{esc(c['client_answer'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:14px 0"></div>
      <div style="font-size:22px;font-weight:{b['body_b']};color:{b['ink']}">{esc(c['avoid_lead'])}</div>
      {avoid_list(c, 'onwhite')}
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1050px;font-size:24px">{esc(c['client_body'])}</div>
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
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{helium_everywhere(loud, b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{helium_smart(P, c['weight_lbl'], b['ink'])}</div>
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
    <div>{new_tags}</div>
    <div class="quote" style="font-size:31px">{esc(c['s3_new_quote'])}</div>
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
    vis1 = f'<div style="display:flex;flex-direction:column;align-items:center;gap:20px">{size_row([12, 18, 36], P, 156, labels=c["rule1_tags"], ink="#111", gap=12, lab_size=18)}</div>'
    S.append(topic_slide(c["s3_rule1_topic"], c["s3_rule1_old"], vis1, c["s3_rule1_quote"]))
    vis2 = f'<div style="width:100%">{facts_grid(c, "facts s3facts", 36, 18)}</div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    sizes = c["example_sizes"]
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v" style="font-size:{44 if len(c['example_title']) <= 24 else (36 if len(c['example_title']) <= 30 else 30)}px">{esc(c['example_title'])}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:620px;padding:50px 24px;display:flex;align-items:flex-end;justify-content:center">
    {size_row(sizes, P, 230, labels=[f"{s} · {t}" for s, t in sizes], sub=[G['pal_label'](k) for k in P[:4]], ink="#111", gap=20, lab_size=21, sub_size=17)}
  </div>
  <div class="bottom" style="top:910px;font-size:31px;font-weight:700">{esc(c['s3_example_quote'])}</div>
  {s3_footer(b)}
</section>""")
    vis6 = (f'<div style="width:100%"><div style="font-size:23px;line-height:1.3;font-style:italic;margin-bottom:12px">{esc(c["client_question"])}</div>'
            f'<div style="font-size:19px;line-height:1.3;margin-bottom:14px">{esc(c["client_answer"])}</div>'
            f'<div style="font-size:18px;font-weight:800;margin-bottom:2px">{esc(c["avoid_lead"])}</div>{avoid_list(c, "s3steps")}</div>')
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
.s1 .step{font-size:27px;margin-top:12px}
.s1 .avoid .step{font-size:25px;margin-top:10px;line-height:1.25}
.s2 .onwhite .step{color:#111;font-size:21px;margin-top:7px;line-height:1.25}
.s2 .onwhite .step b{color:#6b3fb9}
.s3 .s3steps .step{display:flex;gap:10px;font-size:17px;line-height:1.25;margin-top:6px}
.s3 .s3steps .step b{min-width:24px;font-weight:800}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.facts .fact{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:3px solid #111;border-radius:18px;padding:18px 14px;gap:6px;line-height:1.15}
.facts .fact b{letter-spacing:-.01em;line-height:1}
.facts.onwhite .fact{color:#111}
.facts.s3facts{grid-template-columns:1fr;gap:12px}
.facts.s3facts .fact{border-width:2px;padding:10px 10px;border-radius:14px;flex-direction:row;justify-content:flex-start;gap:16px;text-align:left}
.facts.s3facts .fact b{min-width:120px;text-align:center}
"""
