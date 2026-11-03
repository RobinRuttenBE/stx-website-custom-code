# -*- coding: utf-8 -*-
"""Topic: 'How much do you charge for balloon decoration? This calculates your price'
(sempertexeurope.com/en_GB/blog/how-much-to-charge-for-balloon-decor).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=pricing.
Uit de blog: 4 bouwstenen (materiaal, tijd, overhead, winstmarge); alle uren aan je volle uurtarief (bouwen,
opblazen thuis, opbouw en afbraak incl. wachten, rit heen en terug, klantcontact en admin); factor 1,30 tot 1,50
boven de kostprijs; voorbeeld 300 kosten -> 390 tot 450 klantprijs; verdienste = uren + marge; gratis Kostprijscalculator.
Het rekenvoorbeeld (materiaal 110, 5 u x 30 = 150, overhead 40 = 300) is een illustratie bij het blogvoorbeeld van 300."""

G = {}
def setup(g): G.update(g)

# ---------------------------------------------------------------- GELD per markt
def money(b, n):
    """Bedrag in de notatie van de markt. HU x100 (forint), anders de blogcijfers."""
    lang, country = b["lang"], b["country"]; NB = "\u00a0"
    if lang == "hu":
        v = n * 100; return f"{v:,}".replace(",", NB) + NB + "Ft"
    if lang == "pl": return f"{n}{NB}zł"
    if lang == "en": return ("£" if country == "United Kingdom" else "€") + f"{n}"
    if lang == "nl": return f"€{NB}{n}"
    return f"{n}{NB}€"
AMOUNTS = (300, 390, 450, 110, 150, 40, 30, 90, 240)

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["4 bouwstenen…", "×1,30 tot 1,50…", "Elk uur telt…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Prijsformule…",
    "steps_title": "Je prijs is geen buikgevoel. Hij bestaat uit 4 bouwstenen.", "steps_lead": "De 4 bouwstenen:",
    "steps": ["Materiaal: ballonnen, lijm, lint, frames, gewichten, plus een kleine marge voor misrekeningen", "Tijd: elk uur aan je volle uurtarief", "Overhead: je deel van de vaste kosten per opdracht", "Winstmarge: wat je laat groeien"],
    "steps_label": "De basis",
    "rule1_label": "Regel 1", "rule1_title": "Reken elk uur, aan je volle uurtarief",
    "rule1_body": "Tijd is wat beginners het vaakst onderschatten. Bouwen is maar een deel. Opblazen en voorbereiden thuis, opbouw en afbraak ter plaatse met het wachten op de zaal erbij, de rit heen en terug, klantcontact en administratie: elk uur gaat aan je volle uurtarief in de prijs.",
    "hours": ["Bouwen", "Opblazen thuis", "Opbouw en afbraak, ook het wachten", "Rit heen en terug", "Klantcontact en admin"],
    "rule2_label": "Regel 2", "rule2_title": "Marge: factor 1,30 tot 1,50 boven je kostprijs",
    "rule2_body": "Voor decoratiewerk is een factor 1,30 tot 1,50 boven de totale kostprijs gebruikelijk. Afronden naar een mooi getal mag. De marge is niet je verdienste: je verdienste is je uren plus de marge. Enkel materiaal, overhead en kilometers zijn echte uitgaven.",
    "rule2_facts": [["×1,30", "ondergrens voor decoratiewerk"], ["×1,50", "bovengrens voor decoratiewerk"], ["{m300} → {m390}", "kostprijs naar klantprijs bij ×1,30"], ["{m300} → {m450}", "bij ×1,50, afronden mag"]],
    "example_label": "Voorbeeld", "example_title": "Organic slinger van 3 m, uitgerekend",
    "example_rows": [["Materiaal", "{m110}"], ["Tijd: 5 u × {m30}", "{m150}"], ["Overhead", "{m40}"], ["Kostprijs", "{m300}"], ["Klantprijs ×1,30 tot 1,50", "{m390} tot {m450}"]],
    "example_body": "Materiaal: R12 en R5 in {p0}, {p1}, {p2} en {p3}, lijm, lint en haken. Je verdienste op deze job: 5 uur plus de marge, dus {m240} tot {m300}. Enkel materiaal, overhead en kilometers zijn uitgaven.",
    "client_label": "Klantgesprek", "client_title": "Wat je antwoordt als de klant vraagt",
    "client_answers": [
        "Een slinger van 3 meter is bij mij {m390}. Daar zit materiaal in, 5 uur werk, mijn vaste kosten en een marge. Wil je lager, dan maken we hem korter, niet goedkoper.",
        "Ik reken elk uur aan hetzelfde tarief: ook de rit heen en terug en het wachten tot de zaal open is. Die uren kan ik niet voor een andere klant werken.",
        "Dat hangt af van materiaal, uren, verplaatsing en mijn vaste kosten. Ik reken het uit en je krijgt vandaag nog een offerte-PDF.",
    ],
    "avoid_lead": "Welke uren je altijd aanrekent:",
    "steps5": ["Bouwen", "Opblazen en voorbereiden thuis", "Opbouw en afbraak ter plaatse, ook het wachten", "Rit heen en terug", "Klantcontact en administratie"],
    "client_body": "De gratis Kostprijscalculator op sempertexeurope.com/tools rekent dit uit terwijl je typt en maakt met 1 klik een offerte-PDF met je logo, voorschot en btw.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Prijs voor Sempertex ballondecoratie", "s3_cover_b": "op buikgevoel", "s3_cover_c": "vs.", "s3_cover_d": "uitgerekend",
    "s3_left": "OP BUIKGEVOEL", "s3_right": "UITGEREKEND", "s3_left_meta": "elke keer te laag", "s3_right_meta": "4 bouwstenen",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["Buikgevoel", "Prijs van de concurrent"], "s3_new_tags": ["Materiaal + tijd + overhead", "×1,30 tot 1,50"],
    "s3_new_quote": "“Ik tel elk uur aan mijn volle tarief, zet er mijn vaste kosten bij en vermenigvuldig met 1,30 tot 1,50.”", "s3_new_badge": "{m300} → {m390} tot {m450}",
    "s3_changed_bottom": "Zelfde slinger, zelfde klant.\nEindelijk een prijs die klopt.",
    "s3_topic_lbl": "REGEL", "s3_rule1_topic": "Uren", "s3_rule1_old": "Alleen de bouwuren tellen",
    "s3_rule1_quote": "“Opblazen, opbouw, afbraak, wachten, rijden, mailen: elk uur aan je volle tarief.”",
    "s3_rule2_topic": "Marge", "s3_rule2_old": "Kostprijs plus een beetje",
    "s3_rule2_quote": "“Factor 1,30 tot 1,50 boven je kostprijs. {m300} wordt {m390} tot {m450}.”",
    "s3_example_lbl": "VOORBEELD", "s3_example_quote": "“Materiaal {m110}, 5 uur {m150}, overhead {m40}: kostprijs {m300}, klantprijs {m390} tot {m450}.”",
    "s3_client_lbl": "KLANT", "s3_client_topic": "Klantgesprek",
    "s3_client_quote": "“Een prijs die je kunt uitleggen, verdedig je ook. Dat is het verschil met buikgevoel.”",
    "s3_cta_kicker": "Je prijsformule voor de volgende offerte",
    "tag_lbl": "prijs?", "cost_lbl": "kostprijs", "price_lbl": "klantprijs", "quote_lbl": "offerte",
},
"en": {
    "cover_pills": ["4 building blocks…", "×1.30 to 1.50…", "Every hour counts…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Pricing formula…",
    "steps_title": "Your price is not a gut feeling. It has 4 building blocks.", "steps_lead": "The 4 building blocks:",
    "steps": ["Materials: balloons, glue, ribbon, frames, weights, plus a small margin for miscalculations", "Time: every hour at your full hourly rate", "Overhead: your share of fixed costs per job", "Profit margin: what funds your growth"],
    "steps_label": "The basics",
    "rule1_label": "Rule 1", "rule1_title": "Charge every hour, at your full hourly rate",
    "rule1_body": "Time is what beginners underestimate most. Building is only part of it. Inflating and prepping at home, setup and takedown on site including waiting for the venue, the drive there and back, client contact and admin: every hour goes into the price at your full rate.",
    "hours": ["Building", "Inflating at home", "Setup and takedown, waiting included", "Drive there and back", "Client contact and admin"],
    "rule2_label": "Rule 2", "rule2_title": "Margin: a factor of 1.30 to 1.50 above cost",
    "rule2_body": "For decoration work a factor of 1.30 to 1.50 above total cost is common. Rounding to a neat number is fine. The margin is not your earnings: your earnings are your hours plus the margin. Only materials, overhead and mileage are real expenses.",
    "rule2_facts": [["×1.30", "lower end for decoration work"], ["×1.50", "upper end for decoration work"], ["{m300} → {m390}", "cost to client price at ×1.30"], ["{m300} → {m450}", "at ×1.50, rounding allowed"]],
    "example_label": "Example", "example_title": "A 3 m organic garland, priced",
    "example_rows": [["Materials", "{m110}"], ["Time: 5 hrs × {m30}", "{m150}"], ["Overhead", "{m40}"], ["Cost price", "{m300}"], ["Client price ×1.30 to 1.50", "{m390} to {m450}"]],
    "example_body": "Materials: R12 and R5 in {p0}, {p1}, {p2} and {p3}, glue, ribbon and hooks. Your earnings on this job: 5 hours plus the margin, so {m240} to {m300}. Only materials, overhead and mileage are expenses.",
    "client_label": "Client chat", "client_title": "What you answer when the client asks",
    "client_answers": [
        "A 3 metre garland is {m390} with me. That covers materials, 5 hours of work, my fixed costs and a margin. If you want lower, we make it shorter, not cheaper.",
        "I charge every hour at the same rate: the drive there and back and the wait until the venue opens too. I can't work those hours for another client.",
        "That depends on materials, hours, travel and my fixed costs. I'll work it out and you'll have a quote PDF today.",
    ],
    "avoid_lead": "The hours you always charge:",
    "steps5": ["Building", "Inflating and prepping at home", "Setup and takedown on site, waiting included", "Drive there and back", "Client contact and admin"],
    "client_body": "The free Cost Price Calculator at sempertexeurope.com/tools works this out as you type and makes a quote PDF in 1 click, with your logo, deposit and VAT.",
    "cta_label": "Order",
    "s3_cover_a": "Pricing Sempertex balloon decor", "s3_cover_b": "by gut feeling", "s3_cover_c": "vs.", "s3_cover_d": "worked out",
    "s3_left": "BY GUT FEELING", "s3_right": "WORKED OUT", "s3_left_meta": "too low, every time", "s3_right_meta": "4 building blocks",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["Gut feeling", "Competitor's price"], "s3_new_tags": ["Materials + time + overhead", "×1.30 to 1.50"],
    "s3_new_quote": "“I count every hour at my full rate, add my fixed costs and multiply by 1.30 to 1.50.”", "s3_new_badge": "{m300} → {m390} to {m450}",
    "s3_changed_bottom": "Same garland, same client.\nFinally a price that adds up.",
    "s3_topic_lbl": "RULE", "s3_rule1_topic": "Hours", "s3_rule1_old": "Only count the build hours",
    "s3_rule1_quote": "“Inflating, setup, takedown, waiting, driving, emailing: every hour at your full rate.”",
    "s3_rule2_topic": "Margin", "s3_rule2_old": "Cost plus a little",
    "s3_rule2_quote": "“A factor of 1.30 to 1.50 above cost. {m300} becomes {m390} to {m450}.”",
    "s3_example_lbl": "EXAMPLE", "s3_example_quote": "“Materials {m110}, 5 hours {m150}, overhead {m40}: cost {m300}, client price {m390} to {m450}.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Client chat",
    "s3_client_quote": "“A price you can explain is a price you can defend. That's the difference with gut feeling.”",
    "s3_cta_kicker": "Your pricing formula for the next quote",
    "tag_lbl": "price?", "cost_lbl": "cost", "price_lbl": "client price", "quote_lbl": "quote",
},
"de": {
    "cover_pills": ["4 Bausteine…", "×1,30 bis 1,50…", "Jede Stunde zählt…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Preisformel…",
    "steps_title": "Dein Preis ist kein Bauchgefühl. Er besteht aus 4 Bausteinen.", "steps_lead": "Die 4 Bausteine:",
    "steps": ["Material: Ballons, Kleber, Band, Rahmen, Gewichte, plus eine kleine Reserve für Verschätzungen", "Zeit: jede Stunde zu deinem vollen Stundensatz", "Overhead: dein Anteil an den Fixkosten pro Auftrag", "Gewinnmarge: das, was dich wachsen lässt"],
    "steps_label": "Die Basis",
    "rule1_label": "Regel 1", "rule1_title": "Rechne jede Stunde, zum vollen Stundensatz",
    "rule1_body": "Zeit unterschätzen Anfänger am häufigsten. Bauen ist nur ein Teil. Aufblasen und Vorbereiten zu Hause, Auf- und Abbau vor Ort inklusive Warten auf die Location, Fahrt hin und zurück, Kundenkontakt und Verwaltung: jede Stunde geht zum vollen Stundensatz in den Preis.",
    "hours": ["Bauen", "Aufblasen zu Hause", "Auf- und Abbau, auch das Warten", "Fahrt hin und zurück", "Kundenkontakt und Verwaltung"],
    "rule2_label": "Regel 2", "rule2_title": "Marge: Faktor 1,30 bis 1,50 über den Kosten",
    "rule2_body": "Für Dekoarbeit ist ein Faktor von 1,30 bis 1,50 über den Gesamtkosten üblich. Aufrunden auf eine glatte Zahl ist erlaubt. Die Marge ist nicht dein Verdienst: dein Verdienst sind deine Stunden plus die Marge. Nur Material, Overhead und Kilometer sind echte Ausgaben.",
    "rule2_facts": [["×1,30", "Untergrenze für Dekoarbeit"], ["×1,50", "Obergrenze für Dekoarbeit"], ["{m300} → {m390}", "Kosten zu Kundenpreis bei ×1,30"], ["{m300} → {m450}", "bei ×1,50, Runden erlaubt"]],
    "example_label": "Beispiel", "example_title": "Organic Girlande, 3 m, durchgerechnet",
    "example_rows": [["Material", "{m110}"], ["Zeit: 5 Std × {m30}", "{m150}"], ["Overhead", "{m40}"], ["Kosten", "{m300}"], ["Kundenpreis ×1,30 bis 1,50", "{m390} bis {m450}"]],
    "example_body": "Material: R12 und R5 in {p0}, {p1}, {p2} und {p3}, Kleber, Band und Haken. Dein Verdienst bei diesem Job: 5 Stunden plus die Marge, also {m240} bis {m300}. Nur Material, Overhead und Kilometer sind Ausgaben.",
    "client_label": "Kundengespräch", "client_title": "Was du antwortest, wenn der Kunde fragt",
    "client_answers": [
        "Eine Girlande mit 3 Metern kostet bei mir {m390}. Da stecken Material, 5 Stunden Arbeit, meine Fixkosten und eine Marge drin. Soll es weniger sein, machen wir sie kürzer, nicht billiger.",
        "Ich rechne jede Stunde zum gleichen Satz: auch die Fahrt hin und zurück und das Warten, bis die Location öffnet. In diesen Stunden kann ich für keinen anderen Kunden arbeiten.",
        "Das hängt von Material, Stunden, Anfahrt und meinen Fixkosten ab. Ich rechne es durch und du bekommst noch heute ein Angebot als PDF.",
    ],
    "avoid_lead": "Welche Stunden du immer berechnest:",
    "steps5": ["Bauen", "Aufblasen und Vorbereiten zu Hause", "Auf- und Abbau vor Ort, auch das Warten", "Fahrt hin und zurück", "Kundenkontakt und Verwaltung"],
    "client_body": "Der kostenlose Kostenkalkulator auf sempertexeurope.com/tools rechnet das beim Tippen durch und erstellt mit 1 Klick ein Angebot als PDF, mit deinem Logo, Anzahlung und MwSt.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Preis für Sempertex Ballondeko", "s3_cover_b": "nach Bauchgefühl", "s3_cover_c": "vs.", "s3_cover_d": "durchgerechnet",
    "s3_left": "NACH BAUCHGEFÜHL", "s3_right": "DURCHGERECHNET", "s3_left_meta": "jedes Mal zu niedrig", "s3_right_meta": "4 Bausteine",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["Bauchgefühl", "Preis der Konkurrenz"], "s3_new_tags": ["Material + Zeit + Overhead", "×1,30 bis 1,50"],
    "s3_new_quote": "“Ich zähle jede Stunde zum vollen Satz, lege meine Fixkosten drauf und multipliziere mit 1,30 bis 1,50.”", "s3_new_badge": "{m300} → {m390} bis {m450}",
    "s3_changed_bottom": "Gleiche Girlande, gleicher Kunde.\nEndlich ein Preis, der stimmt.",
    "s3_topic_lbl": "REGEL", "s3_rule1_topic": "Stunden", "s3_rule1_old": "Nur die Baustunden zählen",
    "s3_rule1_quote": "“Aufblasen, Aufbau, Abbau, Warten, Fahren, Mailen: jede Stunde zum vollen Satz.”",
    "s3_rule2_topic": "Marge", "s3_rule2_old": "Kosten plus ein bisschen",
    "s3_rule2_quote": "“Faktor 1,30 bis 1,50 über den Kosten. Aus {m300} werden {m390} bis {m450}.”",
    "s3_example_lbl": "BEISPIEL", "s3_example_quote": "“Material {m110}, 5 Stunden {m150}, Overhead {m40}: Kosten {m300}, Kundenpreis {m390} bis {m450}.”",
    "s3_client_lbl": "KUNDE", "s3_client_topic": "Kundengespräch",
    "s3_client_quote": "“Einen Preis, den du erklären kannst, verteidigst du auch. Das ist der Unterschied zum Bauchgefühl.”",
    "s3_cta_kicker": "Deine Preisformel für das nächste Angebot",
    "tag_lbl": "Preis?", "cost_lbl": "Kosten", "price_lbl": "Kundenpreis", "quote_lbl": "Angebot",
},
"fr": {
    "cover_pills": ["4 briques…", "×1,30 à 1,50…", "Chaque heure compte…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Formule de prix…",
    "steps_title": "Ton prix n'est pas une intuition. Il se compose de 4 briques.", "steps_lead": "Les 4 briques :",
    "steps": ["Matériel : ballons, colle, ruban, structures, poids, plus une petite marge pour les erreurs de calcul", "Temps : chaque heure à ton taux horaire complet", "Frais fixes : ta part de charges fixes par prestation", "Marge : ce qui te permet de grandir"],
    "steps_label": "La base",
    "rule1_label": "Règle 1", "rule1_title": "Facture chaque heure, à ton taux horaire complet",
    "rule1_body": "Le temps est ce que les débutants sous-estiment le plus. Le montage n'en est qu'une partie. Gonflage et préparation à la maison, installation et démontage sur place avec l'attente de la salle, le trajet aller-retour, le contact client et l'administratif : chaque heure entre dans le prix à ton taux complet.",
    "hours": ["Montage", "Gonflage à la maison", "Installation et démontage, attente comprise", "Trajet aller-retour", "Contact client et administratif"],
    "rule2_label": "Règle 2", "rule2_title": "Marge : un facteur de 1,30 à 1,50 au-dessus du coût",
    "rule2_body": "Pour la décoration, un facteur de 1,30 à 1,50 au-dessus du coût de revient total est courant. Arrondir à un chiffre rond est permis. La marge n'est pas ton gain : ton gain, ce sont tes heures plus la marge. Seuls le matériel, les frais fixes et les kilomètres sont de vraies dépenses.",
    "rule2_facts": [["×1,30", "bas de fourchette en décoration"], ["×1,50", "haut de fourchette en décoration"], ["{m300} → {m390}", "du coût au prix client à ×1,30"], ["{m300} → {m450}", "à ×1,50, arrondi permis"]],
    "example_label": "Exemple", "example_title": "Guirlande organique de 3 m, chiffrée",
    "example_rows": [["Matériel", "{m110}"], ["Temps : 5 h × {m30}", "{m150}"], ["Frais fixes", "{m40}"], ["Coût de revient", "{m300}"], ["Prix client ×1,30 à 1,50", "{m390} à {m450}"]],
    "example_body": "Matériel : R12 et R5 en {p0}, {p1}, {p2} et {p3}, colle, ruban et crochets. Ton gain sur cette prestation : 5 heures plus la marge, soit {m240} à {m300}. Seuls le matériel, les frais fixes et les kilomètres sont des dépenses.",
    "client_label": "Discussion client", "client_title": "Ce que tu réponds quand le client demande",
    "client_answers": [
        "Une guirlande de 3 mètres, c'est {m390} chez moi. Il y a dedans le matériel, 5 heures de travail, mes frais fixes et une marge. Si tu veux moins, on la fait plus courte, pas moins chère.",
        "Je facture chaque heure au même taux : le trajet aller-retour et l'attente avant l'ouverture de la salle aussi. Ces heures-là, je ne peux pas les travailler pour un autre client.",
        "Ça dépend du matériel, des heures, du déplacement et de mes frais fixes. Je calcule et tu as un devis PDF aujourd'hui.",
    ],
    "avoid_lead": "Les heures que tu factures toujours :",
    "steps5": ["Montage", "Gonflage et préparation à la maison", "Installation et démontage sur place, attente comprise", "Trajet aller-retour", "Contact client et administratif"],
    "client_body": "Le Calculateur de coût gratuit sur sempertexeurope.com/tools fait le calcul pendant que tu tapes et crée un devis PDF en 1 clic, avec ton logo, l'acompte et la TVA.",
    "cta_label": "Commander",
    "s3_cover_a": "Le prix d'une déco ballons Sempertex", "s3_cover_b": "à l'instinct", "s3_cover_c": "vs.", "s3_cover_d": "calculé",
    "s3_left": "À L'INSTINCT", "s3_right": "CALCULÉ", "s3_left_meta": "trop bas, à chaque fois", "s3_right_meta": "4 briques",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["Instinct", "Prix du concurrent"], "s3_new_tags": ["Matériel + temps + frais fixes", "×1,30 à 1,50"],
    "s3_new_quote": "“Je compte chaque heure à mon taux complet, j'ajoute mes frais fixes et je multiplie par 1,30 à 1,50.”", "s3_new_badge": "{m300} → {m390} à {m450}",
    "s3_changed_bottom": "Même guirlande, même client.\nEnfin un prix qui tient la route.",
    "s3_topic_lbl": "RÈGLE", "s3_rule1_topic": "Heures", "s3_rule1_old": "Compter seulement le montage",
    "s3_rule1_quote": "“Gonflage, installation, démontage, attente, route, mails : chaque heure à ton taux complet.”",
    "s3_rule2_topic": "Marge", "s3_rule2_old": "Le coût plus un petit quelque chose",
    "s3_rule2_quote": "“Un facteur de 1,30 à 1,50 au-dessus du coût. {m300} devient {m390} à {m450}.”",
    "s3_example_lbl": "EXEMPLE", "s3_example_quote": "“Matériel {m110}, 5 heures {m150}, frais fixes {m40} : coût {m300}, prix client {m390} à {m450}.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Discussion client",
    "s3_client_quote": "“Un prix que tu peux expliquer, tu peux le défendre. C'est la différence avec l'instinct.”",
    "s3_cta_kicker": "Ta formule de prix pour le prochain devis",
    "tag_lbl": "prix ?", "cost_lbl": "coût", "price_lbl": "prix client", "quote_lbl": "devis",
},
"it": {
    "cover_pills": ["4 mattoni…", "×1,30 a 1,50…", "Ogni ora conta…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "Formula del prezzo…",
    "steps_title": "Il tuo prezzo non è una sensazione. È fatto di 4 mattoni.", "steps_lead": "I 4 mattoni:",
    "steps": ["Materiale: palloncini, colla, nastro, strutture, pesi, più un piccolo margine per gli errori di calcolo", "Tempo: ogni ora alla tua tariffa oraria piena", "Costi fissi: la tua quota di spese fisse per lavoro", "Margine: ciò che ti fa crescere"],
    "steps_label": "La base",
    "rule1_label": "Regola 1", "rule1_title": "Conta ogni ora, alla tariffa oraria piena",
    "rule1_body": "Il tempo è ciò che i principianti sottovalutano di più. Il montaggio è solo una parte. Gonfiare e preparare a casa, allestimento e smontaggio sul posto con l'attesa della sala, il viaggio andata e ritorno, contatto con il cliente e amministrazione: ogni ora entra nel prezzo alla tariffa piena.",
    "hours": ["Montaggio", "Gonfiaggio a casa", "Allestimento e smontaggio, attesa inclusa", "Viaggio andata e ritorno", "Contatto cliente e amministrazione"],
    "rule2_label": "Regola 2", "rule2_title": "Margine: un fattore da 1,30 a 1,50 sopra il costo",
    "rule2_body": "Per le decorazioni un fattore da 1,30 a 1,50 sopra il costo totale è la norma. Arrotondare a una cifra tonda va bene. Il margine non è il tuo guadagno: il tuo guadagno sono le ore più il margine. Solo materiale, costi fissi e chilometri sono spese vere.",
    "rule2_facts": [["×1,30", "fascia bassa per le decorazioni"], ["×1,50", "fascia alta per le decorazioni"], ["{m300} → {m390}", "dal costo al prezzo cliente a ×1,30"], ["{m300} → {m450}", "a ×1,50, arrotondare va bene"]],
    "example_label": "Esempio", "example_title": "Ghirlanda organic da 3 m, con i conti",
    "example_rows": [["Materiale", "{m110}"], ["Tempo: 5 ore × {m30}", "{m150}"], ["Costi fissi", "{m40}"], ["Costo", "{m300}"], ["Prezzo cliente ×1,30 a 1,50", "{m390} a {m450}"]],
    "example_body": "Materiale: R12 e R5 in {p0}, {p1}, {p2} e {p3}, colla, nastro e ganci. Il tuo guadagno su questo lavoro: 5 ore più il margine, quindi da {m240} a {m300}. Solo materiale, costi fissi e chilometri sono spese.",
    "client_label": "Dialogo con il cliente", "client_title": "Cosa rispondi quando il cliente chiede",
    "client_answers": [
        "Una ghirlanda da 3 metri da me costa {m390}. Dentro ci sono materiale, 5 ore di lavoro, i miei costi fissi e un margine. Se vuoi spendere meno, la facciamo più corta, non più economica.",
        "Conto ogni ora alla stessa tariffa: anche il viaggio andata e ritorno e l'attesa finché la sala apre. In quelle ore non posso lavorare per un altro cliente.",
        "Dipende da materiale, ore, trasferta e costi fissi. Faccio i conti e oggi stesso hai un preventivo in PDF.",
    ],
    "avoid_lead": "Le ore che conti sempre:",
    "steps5": ["Montaggio", "Gonfiaggio e preparazione a casa", "Allestimento e smontaggio sul posto, attesa inclusa", "Viaggio andata e ritorno", "Contatto cliente e amministrazione"],
    "client_body": "Il Calcolatore di costo gratuito su sempertexeurope.com/tools fa i conti mentre scrivi e crea un preventivo PDF con 1 clic, con il tuo logo, acconto e IVA.",
    "cta_label": "Ordina",
    "s3_cover_a": "Il prezzo di una decorazione Sempertex", "s3_cover_b": "a sensazione", "s3_cover_c": "vs.", "s3_cover_d": "calcolato",
    "s3_left": "A SENSAZIONE", "s3_right": "CALCOLATO", "s3_left_meta": "troppo basso, ogni volta", "s3_right_meta": "4 mattoni",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["Sensazione", "Prezzo del concorrente"], "s3_new_tags": ["Materiale + tempo + costi fissi", "×1,30 a 1,50"],
    "s3_new_quote": "“Conto ogni ora alla tariffa piena, aggiungo i costi fissi e moltiplico per 1,30 a 1,50.”", "s3_new_badge": "{m300} → {m390} a {m450}",
    "s3_changed_bottom": "Stessa ghirlanda, stesso cliente.\nFinalmente un prezzo che torna.",
    "s3_topic_lbl": "REGOLA", "s3_rule1_topic": "Ore", "s3_rule1_old": "Contare solo le ore di montaggio",
    "s3_rule1_quote": "“Gonfiaggio, allestimento, smontaggio, attesa, viaggio, email: ogni ora alla tariffa piena.”",
    "s3_rule2_topic": "Margine", "s3_rule2_old": "Il costo più qualcosina",
    "s3_rule2_quote": "“Un fattore da 1,30 a 1,50 sopra il costo. {m300} diventa da {m390} a {m450}.”",
    "s3_example_lbl": "ESEMPIO", "s3_example_quote": "“Materiale {m110}, 5 ore {m150}, costi fissi {m40}: costo {m300}, prezzo cliente da {m390} a {m450}.”",
    "s3_client_lbl": "CLIENTE", "s3_client_topic": "Dialogo con il cliente",
    "s3_client_quote": "“Un prezzo che sai spiegare lo sai anche difendere. È la differenza con la sensazione.”",
    "s3_cta_kicker": "La tua formula di prezzo per il prossimo preventivo",
    "tag_lbl": "prezzo?", "cost_lbl": "costo", "price_lbl": "prezzo cliente", "quote_lbl": "preventivo",
},
"pl": {
    "cover_pills": ["4 elementy…", "×1,30 do 1,50…", "Każda godzina się liczy…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Wzór na cenę…",
    "steps_title": "Twoja cena to nie przeczucie. Składa się z 4 elementów.", "steps_lead": "4 elementy:",
    "steps": ["Materiał: balony, klej, wstążka, stelaże, obciążniki, plus mały zapas na pomyłki", "Czas: każda godzina po pełnej stawce godzinowej", "Koszty stałe: twoja część kosztów stałych na zlecenie", "Marża: to, co pozwala ci rosnąć"],
    "steps_label": "Podstawy",
    "rule1_label": "Zasada 1", "rule1_title": "Licz każdą godzinę, po pełnej stawce",
    "rule1_body": "Czas to coś, co początkujący najczęściej zaniżają. Budowanie to tylko część. Pompowanie i przygotowanie w domu, montaż i demontaż na miejscu razem z czekaniem na salę, dojazd w obie strony, kontakt z klientem i administracja: każda godzina wchodzi do ceny po pełnej stawce.",
    "hours": ["Budowanie", "Pompowanie w domu", "Montaż i demontaż, z czekaniem", "Dojazd w obie strony", "Kontakt z klientem i administracja"],
    "rule2_label": "Zasada 2", "rule2_title": "Marża: mnożnik 1,30 do 1,50 powyżej kosztu",
    "rule2_body": "Przy dekoracjach mnożnik 1,30 do 1,50 powyżej całkowitego kosztu to norma. Zaokrąglenie do równej kwoty jest w porządku. Marża to nie twój zarobek: twój zarobek to godziny plus marża. Tylko materiał, koszty stałe i kilometry to prawdziwe wydatki.",
    "rule2_facts": [["×1,30", "dolna granica przy dekoracjach"], ["×1,50", "górna granica przy dekoracjach"], ["{m300} → {m390}", "koszt do ceny dla klienta przy ×1,30"], ["{m300} → {m450}", "przy ×1,50, można zaokrąglić"]],
    "example_label": "Przykład", "example_title": "Girlanda organiczna 3 m, policzona",
    "example_rows": [["Materiał", "{m110}"], ["Czas: 5 godz. × {m30}", "{m150}"], ["Koszty stałe", "{m40}"], ["Koszt", "{m300}"], ["Cena dla klienta ×1,30 do 1,50", "{m390} do {m450}"]],
    "example_body": "Materiał: R12 i R5 w kolorach {p0}, {p1}, {p2} i {p3}, klej, wstążka i haczyki. Twój zarobek na tym zleceniu: 5 godzin plus marża, czyli {m240} do {m300}. Tylko materiał, koszty stałe i kilometry to wydatki.",
    "client_label": "Rozmowa z klientem", "client_title": "Co odpowiadasz, gdy klient pyta",
    "client_answers": [
        "Girlanda 3 m kosztuje u mnie {m390}. W tym jest materiał, 5 godzin pracy, moje koszty stałe i marża. Jeśli chcesz taniej, robimy krótszą, nie tańszą.",
        "Każdą godzinę liczę po tej samej stawce: dojazd w obie strony i czekanie, aż sala się otworzy, też. W tych godzinach nie mogę pracować dla innego klienta.",
        "To zależy od materiału, godzin, dojazdu i moich kosztów stałych. Policzę i dziś dostaniesz wycenę w PDF.",
    ],
    "avoid_lead": "Godziny, które zawsze liczysz:",
    "steps5": ["Budowanie", "Pompowanie i przygotowanie w domu", "Montaż i demontaż na miejscu, z czekaniem", "Dojazd w obie strony", "Kontakt z klientem i administracja"],
    "client_body": "Darmowy Kalkulator kosztów na sempertexeurope.com/tools liczy to, gdy piszesz, i jednym kliknięciem robi wycenę w PDF, z twoim logo, zaliczką i VAT.",
    "cta_label": "Zamów",
    "s3_cover_a": "Cena dekoracji balonowej Sempertex", "s3_cover_b": "na wyczucie", "s3_cover_c": "vs.", "s3_cover_d": "policzona",
    "s3_left": "NA WYCZUCIE", "s3_right": "POLICZONA", "s3_left_meta": "za nisko, za każdym razem", "s3_right_meta": "4 elementy",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "STARE", "s3_new_lbl": "NOWE",
    "s3_old_tags": ["Wyczucie", "Cena konkurencji"], "s3_new_tags": ["Materiał + czas + koszty stałe", "×1,30 do 1,50"],
    "s3_new_quote": "“Liczę każdą godzinę po pełnej stawce, dodaję koszty stałe i mnożę przez 1,30 do 1,50.”", "s3_new_badge": "{m300} → {m390} do {m450}",
    "s3_changed_bottom": "Ta sama girlanda, ten sam klient.\nW końcu cena, która się zgadza.",
    "s3_topic_lbl": "ZASADA", "s3_rule1_topic": "Godziny", "s3_rule1_old": "Liczyć tylko godziny budowania",
    "s3_rule1_quote": "“Pompowanie, montaż, demontaż, czekanie, jazda, maile: każda godzina po pełnej stawce.”",
    "s3_rule2_topic": "Marża", "s3_rule2_old": "Koszt plus coś niewielkiego",
    "s3_rule2_quote": "“Mnożnik 1,30 do 1,50 powyżej kosztu. {m300} zamienia się w {m390} do {m450}.”",
    "s3_example_lbl": "PRZYKŁAD", "s3_example_quote": "“Materiał {m110}, 5 godzin {m150}, koszty stałe {m40}: koszt {m300}, cena dla klienta {m390} do {m450}.”",
    "s3_client_lbl": "KLIENT", "s3_client_topic": "Rozmowa z klientem",
    "s3_client_quote": "“Cenę, którą umiesz wyjaśnić, umiesz też obronić. To różnica między liczeniem a wyczuciem.”",
    "s3_cta_kicker": "Twój wzór na cenę do następnej wyceny",
    "tag_lbl": "cena?", "cost_lbl": "koszt", "price_lbl": "cena dla klienta", "quote_lbl": "wycena",
},
"el": {
    "cover_pills": ["4 συστατικά…", "×1,30 έως 1,50…", "Κάθε ώρα μετράει…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Φόρμουλα τιμής…",
    "steps_title": "Η τιμή σου δεν είναι ένστικτο. Έχει 4 συστατικά.", "steps_lead": "Τα 4 συστατικά:",
    "steps": ["Υλικά: μπαλόνια, κόλλα, κορδέλα, σκελετοί, βαρίδια, συν ένα μικρό περιθώριο για λάθη", "Χρόνος: κάθε ώρα στην πλήρη ωριαία σου χρέωση", "Πάγια: το μερίδιό σου από τα σταθερά έξοδα ανά δουλειά", "Περιθώριο κέρδους: αυτό που σε κάνει να μεγαλώνεις"],
    "steps_label": "Τα βασικά",
    "rule1_label": "Κανόνας 1", "rule1_title": "Χρέωσε κάθε ώρα, στην πλήρη ωριαία χρέωση",
    "rule1_body": "Ο χρόνος είναι αυτό που οι αρχάριοι υποτιμούν περισσότερο. Το στήσιμο είναι μόνο ένα μέρος. Φούσκωμα και προετοιμασία στο σπίτι, εγκατάσταση και αποξήλωση στον χώρο μαζί με την αναμονή, η διαδρομή πήγαινε-έλα, επαφή με τον πελάτη και διαχείριση: κάθε ώρα μπαίνει στην τιμή στην πλήρη χρέωση.",
    "hours": ["Στήσιμο", "Φούσκωμα στο σπίτι", "Εγκατάσταση και αποξήλωση, με την αναμονή", "Διαδρομή πήγαινε-έλα", "Επαφή με πελάτη και διαχείριση"],
    "rule2_label": "Κανόνας 2", "rule2_title": "Περιθώριο: συντελεστής 1,30 έως 1,50 πάνω από το κόστος",
    "rule2_body": "Για διακοσμήσεις, συντελεστής 1,30 έως 1,50 πάνω από το συνολικό κόστος είναι ο κανόνας. Στρογγυλοποίηση σε ωραίο νούμερο επιτρέπεται. Το περιθώριο δεν είναι το κέρδος σου: το κέρδος σου είναι οι ώρες σου συν το περιθώριο. Μόνο υλικά, πάγια και χιλιόμετρα είναι πραγματικά έξοδα.",
    "rule2_facts": [["×1,30", "κάτω όριο για διακοσμήσεις"], ["×1,50", "πάνω όριο για διακοσμήσεις"], ["{m300} → {m390}", "από κόστος σε τιμή πελάτη με ×1,30"], ["{m300} → {m450}", "με ×1,50, στρογγυλοποίηση επιτρέπεται"]],
    "example_label": "Παράδειγμα", "example_title": "Organic γιρλάντα 3 m, κοστολογημένη",
    "example_rows": [["Υλικά", "{m110}"], ["Χρόνος: 5 ώρες × {m30}", "{m150}"], ["Πάγια", "{m40}"], ["Κόστος", "{m300}"], ["Τιμή πελάτη ×1,30 έως 1,50", "{m390} έως {m450}"]],
    "example_body": "Υλικά: R12 και R5 σε {p0}, {p1}, {p2} και {p3}, κόλλα, κορδέλα και γάντζοι. Το κέρδος σου σε αυτή τη δουλειά: 5 ώρες συν το περιθώριο, δηλαδή {m240} έως {m300}. Μόνο υλικά, πάγια και χιλιόμετρα είναι έξοδα.",
    "client_label": "Συζήτηση με πελάτη", "client_title": "Τι απαντάς όταν ο πελάτης ρωτά",
    "client_answers": [
        "Μια γιρλάντα 3 μέτρων κοστίζει {m390} σε μένα. Μέσα είναι τα υλικά, 5 ώρες δουλειάς, τα πάγιά μου και ένα περιθώριο. Αν θέλεις λιγότερο, την κάνουμε πιο κοντή, όχι πιο φτηνή.",
        "Χρεώνω κάθε ώρα με την ίδια χρέωση: και τη διαδρομή πήγαινε-έλα και την αναμονή μέχρι να ανοίξει ο χώρος. Αυτές τις ώρες δεν μπορώ να δουλέψω για άλλον πελάτη.",
        "Εξαρτάται από υλικά, ώρες, μετακίνηση και τα πάγιά μου. Το υπολογίζω και έχεις προσφορά σε PDF σήμερα.",
    ],
    "avoid_lead": "Οι ώρες που χρεώνεις πάντα:",
    "steps5": ["Στήσιμο", "Φούσκωμα και προετοιμασία στο σπίτι", "Εγκατάσταση και αποξήλωση στον χώρο, με την αναμονή", "Διαδρομή πήγαινε-έλα", "Επαφή με πελάτη και διαχείριση"],
    "client_body": "Ο δωρεάν Υπολογιστής κόστους στο sempertexeurope.com/tools το υπολογίζει όσο πληκτρολογείς και φτιάχνει προσφορά σε PDF με 1 κλικ, με το λογότυπό σου, προκαταβολή και ΦΠΑ.",
    "cta_label": "Παραγγελία",
    "s3_cover_a": "Τιμή για διακόσμηση με μπαλόνια Sempertex", "s3_cover_b": "με το ένστικτο", "s3_cover_c": "vs.", "s3_cover_d": "υπολογισμένη",
    "s3_left": "ΜΕ ΤΟ ΕΝΣΤΙΚΤΟ", "s3_right": "ΥΠΟΛΟΓΙΣΜΕΝΗ", "s3_left_meta": "πολύ χαμηλή, κάθε φορά", "s3_right_meta": "4 συστατικά",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["Ένστικτο", "Τιμή ανταγωνιστή"], "s3_new_tags": ["Υλικά + χρόνος + πάγια", "×1,30 έως 1,50"],
    "s3_new_quote": "“Μετράω κάθε ώρα στην πλήρη χρέωση, προσθέτω τα πάγιά μου και πολλαπλασιάζω με 1,30 έως 1,50.”", "s3_new_badge": "{m300} → {m390} έως {m450}",
    "s3_changed_bottom": "Ίδια γιρλάντα, ίδιος πελάτης.\nΕπιτέλους μια τιμή που βγαίνει.",
    "s3_topic_lbl": "ΚΑΝΟΝΑΣ", "s3_rule1_topic": "Ώρες", "s3_rule1_old": "Μετράω μόνο τις ώρες στησίματος",
    "s3_rule1_quote": "“Φούσκωμα, εγκατάσταση, αποξήλωση, αναμονή, οδήγηση, email: κάθε ώρα στην πλήρη χρέωση.”",
    "s3_rule2_topic": "Περιθώριο", "s3_rule2_old": "Κόστος συν κάτι λίγο",
    "s3_rule2_quote": "“Συντελεστής 1,30 έως 1,50 πάνω από το κόστος. Τα {m300} γίνονται {m390} έως {m450}.”",
    "s3_example_lbl": "ΠΑΡΑΔΕΙΓΜΑ", "s3_example_quote": "“Υλικά {m110}, 5 ώρες {m150}, πάγια {m40}: κόστος {m300}, τιμή πελάτη {m390} έως {m450}.”",
    "s3_client_lbl": "ΠΕΛΑΤΗΣ", "s3_client_topic": "Συζήτηση με πελάτη",
    "s3_client_quote": "“Μια τιμή που μπορείς να εξηγήσεις, μπορείς και να την υπερασπιστείς. Αυτή είναι η διαφορά από το ένστικτο.”",
    "s3_cta_kicker": "Η φόρμουλα τιμής σου για την επόμενη προσφορά",
    "tag_lbl": "τιμή;", "cost_lbl": "κόστος", "price_lbl": "τιμή πελάτη", "quote_lbl": "προσφορά",
},
"hu": {
    "cover_pills": ["4 építőelem…", "×1,30 és 1,50 között…", "Minden óra számít…"], "cover_with": "partner:", "cover_brand": "Sempertex Europe", "cover_tag": "Árképlet…",
    "steps_title": "Az árad nem megérzés. 4 építőelemből áll.", "steps_lead": "A 4 építőelem:",
    "steps": ["Anyag: lufik, ragasztó, szalag, keretek, nehezékek, plusz egy kis tartalék a tévedésekre", "Idő: minden óra a teljes óradíjadon", "Rezsi: a fix költségeid rád eső része munkánként", "Haszonkulcs: amiből növekedni tudsz"],
    "steps_label": "Az alapok",
    "rule1_label": "1. szabály", "rule1_title": "Számolj minden órát, a teljes óradíjon",
    "rule1_body": "Az időt becsülik alá leggyakrabban a kezdők. Az építés csak egy része. Felfújás és előkészítés otthon, fel- és leszerelés a helyszínen a teremre várakozással együtt, az út oda-vissza, ügyfélkapcsolat és adminisztráció: minden óra a teljes óradíjon kerül az árba.",
    "hours": ["Építés", "Felfújás otthon", "Fel- és leszerelés, várakozással", "Út oda-vissza", "Ügyfélkapcsolat és admin"],
    "rule2_label": "2. szabály", "rule2_title": "Haszonkulcs: 1,30 és 1,50 közötti szorzó az önköltség fölött",
    "rule2_body": "Dekorációs munkánál az 1,30 és 1,50 közötti szorzó a teljes önköltség fölött a megszokott. Kerek számra kerekíteni szabad. A haszonkulcs nem a kereseted: a kereseted az óráid plusz a haszonkulcs. Csak az anyag, a rezsi és a kilométerek valódi kiadások.",
    "rule2_facts": [["×1,30", "alsó határ dekorációs munkánál"], ["×1,50", "felső határ dekorációs munkánál"], ["{m300} → {m390}", "önköltségből ügyfélár ×1,30-nál"], ["{m300} → {m450}", "×1,50-nél, kerekíteni szabad"]],
    "example_label": "Példa", "example_title": "3 m-es organikus girland, kiszámolva",
    "example_rows": [["Anyag", "{m110}"], ["Idő: 5 óra × {m30}", "{m150}"], ["Rezsi", "{m40}"], ["Önköltség", "{m300}"], ["Ügyfélár ×1,30 és 1,50 között", "{m390} és {m450} között"]],
    "example_body": "Anyag: R12 és R5 {p0}, {p1}, {p2} és {p3} színben, ragasztó, szalag és kampók. A kereseted ezen a munkán: 5 óra plusz a haszonkulcs, vagyis {m240} és {m300} között. Csak az anyag, a rezsi és a kilométerek kiadások.",
    "client_label": "Ügyfélbeszélgetés", "client_title": "Mit válaszolsz, ha az ügyfél megkérdezi",
    "client_answers": [
        "Egy 3 méteres girland nálam {m390}. Ebben benne van az anyag, 5 óra munka, a fix költségeim és a haszonkulcs. Ha kevesebbet szeretnél, rövidebbet csinálunk, nem olcsóbbat.",
        "Minden órát ugyanazon a díjon számolok: az utat oda-vissza és a várakozást is, amíg a terem kinyit. Azokban az órákban nem dolgozhatok más ügyfélnek.",
        "Az anyagtól, az óráktól, az utazástól és a fix költségeimtől függ. Kiszámolom, és még ma kapsz egy PDF árajánlatot.",
    ],
    "avoid_lead": "Amit mindig felszámolsz:",
    "steps5": ["Építés", "Felfújás és előkészítés otthon", "Fel- és leszerelés a helyszínen, várakozással", "Út oda-vissza", "Ügyfélkapcsolat és adminisztráció"],
    "client_body": "Az ingyenes Önköltség-kalkulátor a sempertexeurope.com/tools oldalon gépelés közben számol, és 1 kattintással PDF árajánlatot készít a logóddal, előleggel és áfával.",
    "cta_label": "Rendelés",
    "s3_cover_a": "Sempertex lufidekoráció ára", "s3_cover_b": "megérzésre", "s3_cover_c": "vs.", "s3_cover_d": "kiszámolva",
    "s3_left": "MEGÉRZÉSRE", "s3_right": "KISZÁMOLVA", "s3_left_meta": "mindig túl alacsony", "s3_right_meta": "4 építőelem",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "RÉGI", "s3_new_lbl": "ÚJ",
    "s3_old_tags": ["Megérzés", "A konkurencia ára"], "s3_new_tags": ["Anyag + idő + rezsi", "×1,30 és 1,50 között"],
    "s3_new_quote": "“Minden órát a teljes díjon számolok, hozzáteszem a fix költségeimet, és szorzom 1,30 és 1,50 közötti szorzóval.”", "s3_new_badge": "{m300} → {m390} és {m450} között",
    "s3_changed_bottom": "Ugyanaz a girland, ugyanaz az ügyfél.\nVégre egy ár, ami stimmel.",
    "s3_topic_lbl": "SZABÁLY", "s3_rule1_topic": "Órák", "s3_rule1_old": "Csak az építés óráit számolom",
    "s3_rule1_quote": "“Felfújás, felszerelés, leszerelés, várakozás, vezetés, e-mail: minden óra a teljes díjon.”",
    "s3_rule2_topic": "Haszonkulcs", "s3_rule2_old": "Önköltség plusz egy kicsi",
    "s3_rule2_quote": "“1,30 és 1,50 közötti szorzó az önköltség fölött. {m300}-ból {m390} és {m450} közötti ár lesz.”",
    "s3_example_lbl": "PÉLDA", "s3_example_quote": "“Anyag {m110}, 5 óra {m150}, rezsi {m40}: önköltség {m300}, ügyfélár {m390} és {m450} között.”",
    "s3_client_lbl": "ÜGYFÉL", "s3_client_topic": "Ügyfélbeszélgetés",
    "s3_client_quote": "“Azt az árat, amit el tudsz magyarázni, meg is tudod védeni. Ez a különbség a megérzéshez képest.”",
    "s3_cta_kicker": "Az árképleted a következő ajánlathoz",
    "tag_lbl": "ár?", "cost_lbl": "önköltség", "price_lbl": "ügyfélár", "quote_lbl": "árajánlat",
},
"lt": {
    "cover_pills": ["4 dalys…", "×1,30 iki 1,50…", "Kiekviena valanda svarbi…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Kainos formulė…",
    "steps_title": "Tavo kaina nėra nuojauta. Ją sudaro 4 dalys.", "steps_lead": "4 dalys:",
    "steps": ["Medžiagos: balionai, klijai, juostelė, karkasai, svareliai, plius maža atsarga klaidoms", "Laikas: kiekviena valanda pagal pilną valandinį įkainį", "Pastoviosios išlaidos: tavo dalis fiksuotų išlaidų vienam užsakymui", "Pelno marža: tai, iš ko augi"],
    "steps_label": "Pagrindai",
    "rule1_label": "1 taisyklė", "rule1_title": "Skaičiuok kiekvieną valandą pagal pilną įkainį",
    "rule1_body": "Laiką pradedantieji nuvertina dažniausiai. Montavimas yra tik dalis. Pūtimas ir paruošimas namuose, įrengimas ir išmontavimas vietoje kartu su laukimu, kelionė pirmyn ir atgal, bendravimas su klientu ir administravimas: kiekviena valanda į kainą eina pilnu įkainiu.",
    "hours": ["Montavimas", "Pūtimas namuose", "Įrengimas ir išmontavimas, su laukimu", "Kelionė pirmyn ir atgal", "Bendravimas su klientu ir administravimas"],
    "rule2_label": "2 taisyklė", "rule2_title": "Marža: koeficientas nuo 1,30 iki 1,50 virš savikainos",
    "rule2_body": "Dekoravimo darbams koeficientas nuo 1,30 iki 1,50 virš visos savikainos yra įprastas. Apvalinti iki gražaus skaičiaus galima. Marža nėra tavo uždarbis: tavo uždarbis yra valandos plius marža. Tik medžiagos, pastoviosios išlaidos ir kilometrai yra tikros išlaidos.",
    "rule2_facts": [["×1,30", "apatinė riba dekoravimo darbams"], ["×1,50", "viršutinė riba dekoravimo darbams"], ["{m300} → {m390}", "iš savikainos į kliento kainą su ×1,30"], ["{m300} → {m450}", "su ×1,50, apvalinti galima"]],
    "example_label": "Pavyzdys", "example_title": "3 m organinė girlianda, suskaičiuota",
    "example_rows": [["Medžiagos", "{m110}"], ["Laikas: 5 val. × {m30}", "{m150}"], ["Pastoviosios išlaidos", "{m40}"], ["Savikaina", "{m300}"], ["Kliento kaina ×1,30 iki 1,50", "{m390} iki {m450}"]],
    "example_body": "Medžiagos: R12 ir R5 {p0}, {p1}, {p2} ir {p3} spalvomis, klijai, juostelė ir kabliukai. Tavo uždarbis iš šio darbo: 5 valandos plius marža, tai yra nuo {m240} iki {m300}. Tik medžiagos, pastoviosios išlaidos ir kilometrai yra išlaidos.",
    "client_label": "Pokalbis su klientu", "client_title": "Ką atsakai, kai klientas klausia",
    "client_answers": [
        "3 metrų girlianda pas mane kainuoja {m390}. Į tai įeina medžiagos, 5 valandos darbo, mano pastoviosios išlaidos ir marža. Jei nori mažiau, darome trumpesnę, ne pigesnę.",
        "Kiekvieną valandą skaičiuoju tuo pačiu įkainiu: ir kelionę pirmyn bei atgal, ir laukimą, kol atsidarys salė. Tomis valandomis negaliu dirbti kitam klientui.",
        "Priklauso nuo medžiagų, valandų, kelionės ir mano pastoviųjų išlaidų. Suskaičiuosiu ir šiandien gausi pasiūlymą PDF formatu.",
    ],
    "avoid_lead": "Valandos, kurias visada skaičiuoji:",
    "steps5": ["Montavimas", "Pūtimas ir paruošimas namuose", "Įrengimas ir išmontavimas vietoje, su laukimu", "Kelionė pirmyn ir atgal", "Bendravimas su klientu ir administravimas"],
    "client_body": "Nemokama Savikainos skaičiuoklė sempertexeurope.com/tools skaičiuoja, kol rašai, ir 1 paspaudimu sukuria pasiūlymo PDF su tavo logotipu, avansu ir PVM.",
    "cta_label": "Užsakyti",
    "s3_cover_a": "Sempertex balionų dekoracijos kaina", "s3_cover_b": "iš nuojautos", "s3_cover_c": "vs.", "s3_cover_d": "suskaičiuota",
    "s3_left": "IŠ NUOJAUTOS", "s3_right": "SUSKAIČIUOTA", "s3_left_meta": "per maža, kiekvieną kartą", "s3_right_meta": "4 dalys",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "SENA", "s3_new_lbl": "NAUJA",
    "s3_old_tags": ["Nuojauta", "Konkurento kaina"], "s3_new_tags": ["Medžiagos + laikas + išlaidos", "×1,30 iki 1,50"],
    "s3_new_quote": "“Skaičiuoju kiekvieną valandą pilnu įkainiu, pridedu pastoviąsias išlaidas ir dauginu iš 1,30 iki 1,50.”", "s3_new_badge": "{m300} → {m390} iki {m450}",
    "s3_changed_bottom": "Ta pati girlianda, tas pats klientas.\nPagaliau kaina, kuri sueina.",
    "s3_topic_lbl": "TAISYKLĖ", "s3_rule1_topic": "Valandos", "s3_rule1_old": "Skaičiuoti tik montavimo valandas",
    "s3_rule1_quote": "“Pūtimas, įrengimas, išmontavimas, laukimas, važiavimas, laiškai: kiekviena valanda pilnu įkainiu.”",
    "s3_rule2_topic": "Marža", "s3_rule2_old": "Savikaina plius truputį",
    "s3_rule2_quote": "“Koeficientas nuo 1,30 iki 1,50 virš savikainos. {m300} tampa {m390} iki {m450}.”",
    "s3_example_lbl": "PAVYZDYS", "s3_example_quote": "“Medžiagos {m110}, 5 valandos {m150}, pastoviosios išlaidos {m40}: savikaina {m300}, kliento kaina {m390} iki {m450}.”",
    "s3_client_lbl": "KLIENTAS", "s3_client_topic": "Pokalbis su klientu",
    "s3_client_quote": "“Kainą, kurią gali paaiškinti, gali ir apginti. Tuo ji skiriasi nuo nuojautos.”",
    "s3_cta_kicker": "Tavo kainos formulė kitam pasiūlymui",
    "tag_lbl": "kaina?", "cost_lbl": "savikaina", "price_lbl": "kliento kaina", "quote_lbl": "pasiūlymas",
},
}

# ---------------------------------------------------------------- VARIANTEN (per distri anders, op basis van vi)
VARIANTS = {
"nl": {
  "cover_title": ["Hoeveel vraag je voor Sempertex ballondecoratie? Dit is de formule", "{m300} kosten wordt {m390} tot {m450} prijs: zo reken je je Sempertex decoratie", "Geen buikgevoel: de 4 bouwstenen van je prijs voor Sempertex ballondecoratie"],
  "cover_sub": ["Materiaal, tijd, overhead en marge, uit de Sempertex blog. Met een rekenvoorbeeld dat je morgen in je offerte zet.", "Tijd is wat beginners het vaakst vergeten. Deze formule telt elk uur mee, ook het wachten en de rit."],
  "client_question": ["Kan het wat goedkoper? Ik zag een slinger voor {m150}.", "Waarom reken je de rit en het wachten aan?", "Hoeveel kost een slinger van 3 meter bij jou?"],
  "s3_old_quote": ["“Ik vraag wat de klant redelijk vindt”", "“Mijn uren tel ik niet, dat is mijn hobby”", "“Ik kijk wat de concurrent vraagt en ga eronder”"],
  "s3_client_old": ["“Kan het goedkoper? Ja hoor”", "“Voor jou een vriendenprijs”"],
  "cta_title_tpl": "Bestel je Sempertex ballonnen bij {name}", "cta_sub_generic": "Bestel je materiaal voor de volgende job en reken je prijs vooraf uit.",
},
"en": {
  "cover_title": ["How much do you charge for Sempertex balloon decor? This is the formula", "{m300} of cost becomes {m390} to {m450} of price: how to price your Sempertex decor", "No gut feeling: the 4 building blocks of your price for Sempertex balloon decor"],
  "cover_sub": ["Materials, time, overhead and margin, from the Sempertex blog. With a worked example you can put in tomorrow's quote.", "Time is what beginners forget most. This formula counts every hour, the waiting and the drive included."],
  "client_question": ["Can you do it a bit cheaper? I saw a garland for {m150}.", "Why do you charge for the drive and the waiting?", "How much is a 3 metre garland with you?"],
  "s3_old_quote": ["“I charge what the client thinks is fair”", "“I don't count my hours, it's my hobby”", "“I check the competitor's price and go under it”"],
  "s3_client_old": ["“Can you do it cheaper? Sure”", "“Mates' rates for you”"],
  "cta_title_tpl": "Order your Sempertex balloons at {name}", "cta_sub_generic": "Order your materials for the next job and work out your price before you quote.",
},
"de": {
  "cover_title": ["Wie viel verlangst du für Sempertex Ballondeko? Das ist die Formel", "Aus {m300} Kosten werden {m390} bis {m450} Preis: so rechnest du deine Sempertex Deko", "Kein Bauchgefühl: die 4 Bausteine deines Preises für Sempertex Ballondeko"],
  "cover_sub": ["Material, Zeit, Overhead und Marge, aus dem Sempertex Blog. Mit einem Rechenbeispiel für dein nächstes Angebot.", "Zeit vergessen Anfänger am häufigsten. Diese Formel zählt jede Stunde, auch das Warten und die Fahrt."],
  "client_question": ["Geht das etwas günstiger? Ich habe eine Girlande für {m150} gesehen.", "Warum berechnest du die Fahrt und das Warten?", "Was kostet eine Girlande mit 3 Metern bei dir?"],
  "s3_old_quote": ["“Ich verlange, was der Kunde fair findet”", "“Meine Stunden zähle ich nicht, das ist mein Hobby”", "“Ich schaue, was die Konkurrenz verlangt, und gehe drunter”"],
  "s3_client_old": ["“Geht's günstiger? Klar”", "“Für dich ein Freundschaftspreis”"],
  "cta_title_tpl": "Bestell deine Sempertex Ballons bei {name}", "cta_sub_generic": "Bestell dein Material für den nächsten Job und rechne deinen Preis vor dem Angebot durch.",
},
"fr": {
  "cover_title": ["Combien demander pour une déco ballons Sempertex ? Voici la formule", "{m300} de coût devient {m390} à {m450} de prix : comment chiffrer ta déco Sempertex", "Pas d'instinct : les 4 briques de ton prix pour une déco ballons Sempertex"],
  "cover_sub": ["Matériel, temps, frais fixes et marge, tirés du blog Sempertex. Avec un exemple chiffré pour ton prochain devis.", "Le temps, c'est ce que les débutants oublient le plus. Cette formule compte chaque heure, l'attente et la route comprises."],
  "client_question": ["Tu peux faire un peu moins cher ? J'ai vu une guirlande à {m150}.", "Pourquoi tu factures la route et l'attente ?", "Combien coûte une guirlande de 3 mètres chez toi ?"],
  "s3_old_quote": ["“Je demande ce que le client trouve raisonnable”", "“Mes heures, je ne les compte pas, c'est ma passion”", "“Je regarde le prix du concurrent et je passe en dessous”"],
  "s3_client_old": ["“Moins cher ? Bien sûr”", "“Pour toi, un prix d'ami”"],
  "cta_title_tpl": "Commande tes ballons Sempertex chez {name}", "cta_sub_generic": "Commande ton matériel pour la prochaine prestation et calcule ton prix avant le devis.",
},
"it": {
  "cover_title": ["Quanto chiedi per una decorazione Sempertex? Questa è la formula", "{m300} di costo diventano {m390} a {m450} di prezzo: come calcolare la tua decorazione Sempertex", "Niente sensazioni: i 4 mattoni del tuo prezzo per le decorazioni Sempertex"],
  "cover_sub": ["Materiale, tempo, costi fissi e margine, dal blog Sempertex. Con un esempio di calcolo per il tuo prossimo preventivo.", "Il tempo è ciò che i principianti dimenticano di più. Questa formula conta ogni ora, attesa e viaggio inclusi."],
  "client_question": ["Puoi fare un po' meno? Ho visto una ghirlanda a {m150}.", "Perché conti il viaggio e l'attesa?", "Quanto costa una ghirlanda da 3 metri da te?"],
  "s3_old_quote": ["“Chiedo quello che il cliente trova giusto”", "“Le mie ore non le conto, è la mia passione”", "“Guardo il prezzo del concorrente e sto sotto”"],
  "s3_client_old": ["“Si può fare a meno? Certo”", "“Per te prezzo da amico”"],
  "cta_title_tpl": "Ordina i tuoi palloncini Sempertex da {name}", "cta_sub_generic": "Ordina il materiale per il prossimo lavoro e calcola il prezzo prima del preventivo.",
},
"pl": {
  "cover_title": ["Ile liczyć za dekorację balonową Sempertex? Oto wzór", "{m300} kosztu to {m390} do {m450} ceny: tak wyceniasz dekorację Sempertex", "Bez wyczucia: 4 elementy twojej ceny za dekorację balonową Sempertex"],
  "cover_sub": ["Materiał, czas, koszty stałe i marża, z bloga Sempertex. Z przykładem obliczeń do twojej następnej wyceny.", "Czas to coś, o czym początkujący zapominają najczęściej. Ten wzór liczy każdą godzinę, także czekanie i dojazd."],
  "client_question": ["Da się trochę taniej? Widziałam girlandę za {m150}.", "Dlaczego liczysz dojazd i czekanie?", "Ile kosztuje u ciebie girlanda 3 m?"],
  "s3_old_quote": ["“Biorę tyle, ile klient uzna za rozsądne”", "“Swoich godzin nie liczę, to moje hobby”", "“Patrzę na cenę konkurencji i schodzę niżej”"],
  "s3_client_old": ["“Da się taniej? Jasne”", "“Dla ciebie cena po znajomości”"],
  "cta_title_tpl": "Zamów balony Sempertex w {name}", "cta_sub_generic": "Zamów materiał na następne zlecenie i policz cenę przed wyceną.",
},
"el": {
  "cover_title": ["Πόσο χρεώνεις μια διακόσμηση με μπαλόνια Sempertex; Αυτή είναι η φόρμουλα", "{m300} κόστος γίνονται {m390} έως {m450} τιμή: έτσι κοστολογείς τη διακόσμηση Sempertex", "Όχι ένστικτο: τα 4 συστατικά της τιμής σου για διακόσμηση με μπαλόνια Sempertex"],
  "cover_sub": ["Υλικά, χρόνος, πάγια και περιθώριο, από το blog της Sempertex. Με παράδειγμα υπολογισμού για την επόμενη προσφορά σου.", "Τον χρόνο ξεχνούν πιο συχνά οι αρχάριοι. Αυτή η φόρμουλα μετράει κάθε ώρα, μαζί με την αναμονή και τη διαδρομή."],
  "client_question": ["Γίνεται λίγο πιο φτηνά; Είδα γιρλάντα με {m150}.", "Γιατί χρεώνεις τη διαδρομή και την αναμονή;", "Πόσο κοστίζει μια γιρλάντα 3 μέτρων σε σένα;"],
  "s3_old_quote": ["“Χρεώνω όσο θεωρεί λογικό ο πελάτης”", "“Τις ώρες μου δεν τις μετράω, είναι το χόμπι μου”", "“Κοιτάω την τιμή του ανταγωνιστή και πάω από κάτω”"],
  "s3_client_old": ["“Πιο φτηνά; Εννοείται”", "“Για σένα, φιλική τιμή”"],
  "cta_title_tpl": "Παράγγειλε τα μπαλόνια Sempertex σου από {name}", "cta_sub_generic": "Παράγγειλε τα υλικά για την επόμενη δουλειά και υπολόγισε την τιμή πριν την προσφορά.",
},
"hu": {
  "cover_title": ["Mennyit kérsz egy Sempertex lufidekorációért? Ez a képlet", "{m300} önköltségből {m390} és {m450} közötti ár lesz: így árazod a Sempertex dekorációd", "Nem megérzés: a 4 építőelem a Sempertex lufidekoráció árához"],
  "cover_sub": ["Anyag, idő, rezsi és haszonkulcs, a Sempertex blogból. Számpéldával a következő árajánlatodhoz.", "Az időt felejtik el leggyakrabban a kezdők. Ez a képlet minden órát számol, a várakozást és az utat is."],
  "client_question": ["Lehet egy kicsit olcsóbban? Láttam girlandot {m150}-ért.", "Miért számolod fel az utat és a várakozást?", "Mennyibe kerül nálad egy 3 méteres girland?"],
  "s3_old_quote": ["“Annyit kérek, amennyit az ügyfél méltányosnak tart”", "“Az óráimat nem számolom, ez a hobbim”", "“Megnézem a konkurencia árát, és alámegyek”"],
  "s3_client_old": ["“Olcsóbban? Persze”", "“Neked baráti ár”"],
  "cta_title_tpl": "Rendeld a Sempertex lufijaidat innen: {name}", "cta_sub_generic": "Rendeld meg az anyagot a következő munkához, és számold ki az árat az ajánlat előtt.",
},
"lt": {
  "cover_title": ["Kiek prašyti už Sempertex balionų dekoraciją? Štai formulė", "{m300} savikainos tampa {m390} iki {m450} kainos: taip skaičiuoji Sempertex dekoraciją", "Jokios nuojautos: 4 tavo kainos dalys Sempertex balionų dekoracijai"],
  "cover_sub": ["Medžiagos, laikas, pastoviosios išlaidos ir marža iš Sempertex tinklaraščio. Su skaičiavimo pavyzdžiu kitam pasiūlymui.", "Laiką pradedantieji pamiršta dažniausiai. Ši formulė skaičiuoja kiekvieną valandą, įskaitant laukimą ir kelionę."],
  "client_question": ["Ar galima šiek tiek pigiau? Mačiau girliandą už {m150}.", "Kodėl skaičiuoji kelionę ir laukimą?", "Kiek pas tave kainuoja 3 metrų girlianda?"],
  "s3_old_quote": ["“Prašau tiek, kiek klientui atrodo teisinga”", "“Savo valandų neskaičiuoju, tai mano hobis”", "“Žiūriu konkurento kainą ir einu žemiau”"],
  "s3_client_old": ["“Pigiau? Žinoma”", "“Tau draugiška kaina”"],
  "cta_title_tpl": "Užsisakyk Sempertex balionus iš {name}", "cta_sub_generic": "Užsisakyk medžiagas kitam darbui ir suskaičiuok kainą prieš pasiūlymą.",
},
}

CAPTIONS_TPL = {
 "nl": "Je prijs voor ballondecoratie is geen buikgevoel. Hij bestaat uit materiaal, tijd, overhead en marge. In deze carousel: welke uren je allemaal aanrekent, de gebruikelijke marge voor decoratiewerk (factor 1,30 tot 1,50) en een rekenvoorbeeld van kostprijs naar klantprijs. Plus wat je antwoordt als de klant vraagt of het goedkoper kan.\n\nBestel je Sempertex ballonnen bij {domain}.\n\n#ballondecoratie #prijs #sempertex #{tag} #ballonartiest #offerte",
 "en": "Your price for balloon decor is not a gut feeling. It's materials, time, overhead and margin. In this carousel: which hours you charge, the usual margin for decoration work (a factor of 1.30 to 1.50) and a worked example from cost to client price. Plus what to answer when the client asks for cheaper.\n\nOrder your Sempertex balloons at {domain}.\n\n#balloondecor #pricing #sempertex #{tag} #balloonartist #quote",
 "de": "Dein Preis für Ballondeko ist kein Bauchgefühl. Er besteht aus Material, Zeit, Overhead und Marge. Im Carousel: welche Stunden du alle berechnest, die übliche Marge für Dekoarbeit (Faktor 1,30 bis 1,50) und ein Rechenbeispiel von Kosten zu Kundenpreis. Plus, was du antwortest, wenn der Kunde fragt, ob es günstiger geht.\n\nBestell deine Sempertex Ballons bei {domain}.\n\n#ballondeko #preis #sempertex #{tag} #ballonkünstler #angebot",
 "fr": "Ton prix pour une déco ballons n'est pas une intuition. C'est du matériel, du temps, des frais fixes et une marge. Dans ce carrousel : les heures que tu factures, la marge courante en décoration (facteur 1,30 à 1,50) et un exemple chiffré du coût au prix client. Plus ce que tu réponds quand le client demande moins cher.\n\nCommande tes ballons Sempertex chez {domain}.\n\n#decorationballons #prix #sempertex #{tag} #artisteballon #devis",
 "it": "Il tuo prezzo per una decorazione con palloncini non è una sensazione. È materiale, tempo, costi fissi e margine. Nel carosello: quali ore conti, il margine abituale per le decorazioni (fattore da 1,30 a 1,50) e un esempio di calcolo dal costo al prezzo cliente. Più cosa rispondi quando il cliente chiede uno sconto.\n\nOrdina i tuoi palloncini Sempertex da {domain}.\n\n#decorazioni #prezzo #sempertex #{tag} #balloonartist #preventivo",
 "pl": "Twoja cena za dekorację balonową to nie przeczucie. To materiał, czas, koszty stałe i marża. W karuzeli: które godziny liczysz, zwykła marża przy dekoracjach (mnożnik 1,30 do 1,50) i przykład obliczeń od kosztu do ceny dla klienta. Plus co odpowiedzieć, gdy klient pyta o taniej.\n\nZamów balony Sempertex w {domain}.\n\n#dekoracjebalonowe #cena #sempertex #{tag} #artystabalonowy #wycena",
 "el": "Η τιμή σου για διακόσμηση με μπαλόνια δεν είναι ένστικτο. Είναι υλικά, χρόνος, πάγια και περιθώριο. Στο carousel: ποιες ώρες χρεώνεις, το συνηθισμένο περιθώριο για διακοσμήσεις (συντελεστής 1,30 έως 1,50) και ένα παράδειγμα από κόστος σε τιμή πελάτη. Και τι απαντάς όταν ο πελάτης ζητά πιο φτηνά.\n\nΠαράγγειλε τα μπαλόνια Sempertex σου από {domain}.\n\n#μπαλονια #τιμη #sempertex #{tag} #balloonartist",
 "hu": "A lufidekoráció árad nem megérzés. Anyag, idő, rezsi és haszonkulcs. A carouselben: mely órákat számolod fel, a szokásos haszonkulcs dekorációs munkánál (1,30 és 1,50 közötti szorzó) és egy számpélda önköltségből ügyfélárig. Plusz mit válaszolj, ha az ügyfél olcsóbbat kér.\n\nRendeld a Sempertex lufijaidat innen: {domain}.\n\n#lufidekoracio #ar #sempertex #{tag} #lufiművész #arajanlat",
 "lt": "Tavo kaina už balionų dekoraciją nėra nuojauta. Tai medžiagos, laikas, pastoviosios išlaidos ir marža. Karuselėje: kurias valandas skaičiuoji, įprasta marža dekoravimo darbams (koeficientas nuo 1,30 iki 1,50) ir skaičiavimo pavyzdys nuo savikainos iki kliento kainos. Ir ką atsakyti, kai klientas prašo pigiau.\n\nUžsisakyk Sempertex balionus iš {domain}.\n\n#balionudekoracijos #kaina #sempertex #{tag} #balionumenininkas",
}

# ---------------------------------------------------------------- VISUALS
CUR = {"pal": ["rosewood", "eucalyptus", "greentea", "golddust"]}

def fill_pal(b, c):
    """Vult {p0}..{p3} (kleurnaam + code) en {m300}.. (bedragen in de notatie van de markt); kiest het klantantwoord bij de vraag."""
    lab = {f"p{i}": G["pal_label"](k, short=False).replace("Fashion ", "").replace("Pastel ", "") for i, k in enumerate(b["pal"][:4])}
    for n in AMOUNTS: lab[f"m{n}"] = money(b, n)
    def f(v): return v.format(**lab) if isinstance(v, str) and "{" in v else v
    out = {}
    for k, v in c.items():
        if isinstance(v, str): out[k] = f(v)
        elif isinstance(v, list): out[k] = [[f(x) for x in item] if isinstance(item, list) else f(item) for item in v]
        else: out[k] = v
    qs = [f(q) for q in VARIANTS[b["lang"]]["client_question"]]
    qi = qs.index(out["client_question"]) if out["client_question"] in qs else 0
    out["client_answer"] = out["client_answers"][qi]
    return out

def _bl(key, size, cls=""):
    return G["balloon"](key, "fashion", size, cls=cls)

def garland(keys, big=96, small=62, n=7):
    out = '<div style="display:flex;align-items:flex-end;justify-content:center;gap:0">'
    for i in range(n):
        k = keys[i % len(keys)]; s = big if i % 2 == 0 else small
        rotv = (-10, 12, -6, 10, -12, 8, -9)[i % 7]
        out += f'<div style="margin:0 -9px"><div style="transform:rotate({rotv}deg)">{_bl(k, s)}</div></div>'
    return out + '</div>'

def hours_chips(c, cls="hours"):
    esc = G["esc"]
    return f'<div class="{cls}">' + "".join(f'<span class="hchip"><i>⏱</i>{esc(h)}</span>' for h in c["hours"]) + '</div>'

def facts_grid(c, cls="facts", num_size=50, lab_size=21):
    esc = G["esc"]
    def fs(n):
        L = len(n); return num_size if L <= 9 else (int(num_size * .74) if L <= 14 else int(num_size * .6))
    cells = "".join(f'<div class="fact"><b style="font-size:{fs(n)}px{";white-space:normal" if len(n) > 18 else ""}">{esc(n)}</b><span style="font-size:{lab_size}px">{esc(l)}</span></div>' for n, l in c["rule2_facts"])
    return f'<div class="{cls}">{cells}</div>'

def price_card(c, cls="pcard", size=26):
    """Mini-offerte: rijen label/bedrag, kostprijs en klantprijs vet."""
    esc = G["esc"]; rows = c["example_rows"]; n = len(rows)
    out = f'<div class="{cls}" style="font-size:{size}px">'
    for i, (lab, val) in enumerate(rows):
        strong = i >= n - 2
        out += f'<div class="prow{" strong" if strong else ""}{" total" if i == n-1 else ""}"><span>{esc(lab)}</span><b>{esc(val)}</b></div>'
    return out + '</div>'

def avoid_list(c, cls=""):
    esc = G["esc"]
    return ('<div class="' + cls + '">' + "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps5"])) + '</div>')

def gut_feel(keys, tag, ink="#111"):
    """'Op buikgevoel': ballonnen kriskras met vraagteken-prijskaartjes."""
    esc = G["esc"]; w, h = 330, 360
    pos = [(0, 20, 96), (110, 0, 84), (210, 40, 100), (30, 150, 88), (150, 130, 110), (250, 170, 80), (80, 250, 96), (190, 250, 84)]
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    for i, (x, y, s) in enumerate(pos):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px">{_bl(keys[i % len(keys)], s)}</div>'
    for (x, y, r) in ((40, 100, -12), (200, 10, 8), (120, 300, -6)):
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg);background:#fff;color:{ink};border:3px solid {ink};'
                f'border-radius:10px;padding:6px 12px;font-size:22px;font-weight:900;box-shadow:0 4px 0 rgba(0,0,0,.18)">{esc(tag)}</div>')
    return out + '</div>'

def calculated(keys, c, ink="#111"):
    """'Uitgerekend': slinger + nette prijskaart kostprijs -> klantprijs."""
    esc = G["esc"]; rows = c["example_rows"]
    return (f'<div style="position:relative;width:330px;height:370px">'
            f'<div style="position:absolute;left:-10px;top:0;width:350px;transform:scale(.9);transform-origin:top left">{garland(keys, 84, 56, 6)}</div>'
            f'<div style="position:absolute;left:30px;top:150px;width:270px;background:#fff;color:{ink};border:3px solid {ink};border-radius:16px;padding:14px 18px;box-shadow:0 6px 0 rgba(0,0,0,.18)">'
            f'<div style="display:flex;justify-content:space-between;font-size:19px;font-weight:700;opacity:.7"><span>{esc(rows[-2][0])}</span><span>{esc(rows[-2][1])}</span></div>'
            f'<div style="height:2px;background:{ink};opacity:.2;margin:8px 0"></div>'
            f'<div style="font-size:17px;font-weight:700;opacity:.7">{esc(c["price_lbl"])} {esc(c["rule2_facts"][0][0])} … {esc(c["rule2_facts"][1][0][1:])}</div>'
            f'<div style="font-size:{30 if len(rows[-1][1]) <= 14 else 24}px;font-weight:900;line-height:1.1;margin-top:4px">{esc(rows[-1][1])}</div></div></div>')

# ---------------------------------------------------------------- STIJL 1
def s1_slides(b, c):
    CUR["pal"] = b["pal"]; c = fill_pal(b, c); P = b["pal"]
    esc, hl, cursor_svg, arrow_svg, balloon = G["esc"], G["hl"], G["cursor_svg"], G["arrow_svg"], G["balloon"]
    s1_footer, logo_img, rot, STX_FULL = G["s1_footer"], G["logo_img"], G["rot"], G["STX_FULL"]
    S = []
    pills = c["cover_pills"]
    S.append(f"""
<section class="slide s1">
  <h1 data-fit style="position:absolute;left:70px;right:70px;top:250px;max-height:560px;font-size:96px;text-align:center;line-height:1.06">{hl(c['cover_title'])}</h1>
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
  <div class="box" style="left:70px;top:120px;width:800px;height:520px">
    <h2 data-fit style="font-size:78px;max-height:420px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:830px;top:90px;transform:rotate(14deg)">{balloon(b['hero'], 'fashion', 180)}</div>
  <div style="position:absolute;left:120px;top:650px">{arrow_svg(b['ink'], 150, 140)}</div>
  <div class="box" style="left:300px;top:680px;width:710px;height:480px;padding:36px 46px">
    <div style="font-size:30px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:430px;padding:44px 50px">
    <h2 data-fit style="font-size:60px;max-height:150px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:28px">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:650px;height:460px">
    <div class="card" style="top:0;height:380px;transform:translate(60px,-70px) scale(.92);opacity:.5"></div>
    <div class="card" style="top:0;height:380px;transform:translate(30px,-36px) scale(.96);opacity:.75"></div>
    <div class="card" style="top:0;height:430px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;padding:30px 40px">
      <div style="transform:scale(.9)">{garland(P, 96, 62, 7)}</div>
      {hours_chips(c)}
    </div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule2_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:470px;padding:44px 50px">
    <h2 data-fit style="font-size:56px;max-height:200px">{esc(c['rule2_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:28px">{esc(c['rule2_body'])}</div>
  </div>
  <div class="stack" style="top:700px;height:400px">
    <div class="card" style="top:0;height:340px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:380px;padding:30px 34px">{facts_grid(c)}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:600px;padding:36px 44px 30px">
    <h2 data-fit style="font-size:50px;margin-bottom:18px;text-align:center;max-height:120px">{esc(c['example_title'])}</h2>
    <div style="transform:scale(.8);transform-origin:top center;height:120px">{garland(P, 96, 62, 7)}</div>
    {price_card(c, "pcard", 27)}
  </div>
  <div class="box" style="left:70px;top:800px;width:940px;padding:32px 50px"><div class="body" style="font-size:27px">{esc(c['example_body'])}</div></div>
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
    <div class="body" style="font-size:23px;line-height:1.35">{esc(c['client_body'])}</div>
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
  <h1 data-fit style="position:absolute;left:320px;right:70px;top:70px;max-height:430px;font-size:70px">{hl(c['cover_title'])}</h1>
  <div class="frame" style="left:320px;top:520px;width:690px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box"><div style="transform:scale(1.15)">{calculated(P, c, '#111')}</div></div>
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
    <div class="ph" style="height:340px;padding:10px;box-sizing:border-box"><div style="transform:scale(.9)">{garland(P, 96, 62, 6)}</div></div>
  </div>
  <div class="frame" style="left:600px;top:820px;width:410px;transform:rotate({rot(b,3)}deg)">
    <div class="ph" style="height:260px;padding:10px;box-sizing:border-box"><div style="transform:scale(.8)">{balloon(b['hero'], 'fashion', 150)}</div></div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:60px;max-height:160px">{esc(c['rule1_title'])}</h2>
  <div class="frame" style="left:70px;top:350px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:440px;flex-direction:column;justify-content:center;gap:24px;padding:20px 30px;box-sizing:border-box;background:#fff"><div style="transform:scale(.85)">{garland(P, 96, 62, 7)}</div>{hours_chips(c, 'hours onwhite')}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:900px;font-size:27px">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:56px;max-height:170px">{esc(c['rule2_title'])}</h2>
  <div class="frame" style="left:70px;top:370px;width:940px;transform:rotate({rot(b,1.5)}deg)">
    <div class="ph" style="height:380px;padding:26px 30px;box-sizing:border-box;align-items:stretch;background:#fff">{facts_grid(c, 'facts onwhite')}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:870px;font-size:27px">{esc(c['rule2_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:56px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:auto;padding:24px 30px;box-sizing:border-box;flex-direction:column;background:#fff;color:#111">
      <div style="transform:scale(.75);transform-origin:top center;height:110px">{garland(P, 96, 62, 7)}</div>
      {price_card(c, "pcard onwhite", 25)}
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:930px;font-size:25px">{esc(c['example_body'])}</div>
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
  <div class="body" style="position:absolute;left:70px;right:70px;top:1060px;font-size:23px">{esc(c['client_body'])}</div>
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
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{gut_feel(loud, c['tag_lbl'], b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{calculated(P, c, b['ink'])}</div>
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
    vis1 = f'<div style="width:100%;display:flex;flex-direction:column;align-items:center;gap:18px"><div style="transform:scale(.7);transform-origin:top center;height:90px">{garland(P, 96, 62, 6)}</div>{hours_chips(c, "hours s3hours")}</div>'
    S.append(topic_slide(c["s3_rule1_topic"], c["s3_rule1_old"], vis1, c["s3_rule1_quote"]))
    vis2 = f'<div style="width:100%">{facts_grid(c, "facts s3facts", 34, 17)}</div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    t = c['example_title']
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v" style="font-size:{44 if len(t) <= 24 else (36 if len(t) <= 30 else 30)}px">{esc(t)}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:620px;padding:40px 44px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px">
    <div style="transform:scale(.85);transform-origin:top center;height:120px">{garland(P, 96, 62, 7)}</div>
    {price_card(c, "pcard onwhite", 26)}
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
.s1 .step{font-size:26px;margin-top:10px}
.s1 .avoid .step{font-size:24px;margin-top:9px;line-height:1.25}
.s2 .onwhite .step{color:#111;font-size:21px;margin-top:7px;line-height:1.25}
.s2 .onwhite .step b{color:#6b3fb9}
.s3 .s3steps .step{display:flex;gap:10px;font-size:17px;line-height:1.25;margin-top:6px}
.s3 .s3steps .step b{min-width:24px;font-weight:800}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.facts .fact{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:3px solid #111;border-radius:18px;padding:16px 14px;gap:6px;line-height:1.15}
.facts .fact b{letter-spacing:-.01em;line-height:1;white-space:nowrap}
.facts.onwhite .fact{color:#111}
.facts.s3facts{grid-template-columns:1fr;gap:12px}
.facts.s3facts .fact{border-width:2px;padding:10px 14px;border-radius:14px;align-items:flex-start;text-align:left;gap:3px}
.facts.s3facts .fact b{white-space:normal}
.hours{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;width:100%}
.hchip{display:inline-flex;align-items:center;gap:8px;border:3px solid #111;border-radius:999px;padding:10px 20px;font-size:23px;font-weight:700;color:#111;background:#fff;white-space:nowrap}
.hchip i{font-style:normal;font-size:20px}
.hours.s3hours{gap:8px}
.hours.s3hours .hchip{font-size:16px;padding:7px 13px;border-width:2px;white-space:normal;text-align:left}
.pcard{width:100%;border:3px solid #111;border-radius:18px;padding:12px 26px;box-sizing:border-box;color:#111}
.pcard .prow{display:flex;justify-content:space-between;gap:20px;padding:9px 0;border-bottom:2px dashed rgba(0,0,0,.18)}
.pcard .prow:last-child{border-bottom:0}
.pcard .prow b{white-space:nowrap}
.pcard .prow.strong{font-weight:900}
.pcard .prow.total{border-top:3px solid #111;margin-top:4px;padding-top:12px;font-size:1.08em}
.pcard .prow.total b{color:#6b3fb9}
"""
