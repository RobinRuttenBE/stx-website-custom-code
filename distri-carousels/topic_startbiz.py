# -*- coding: utf-8 -*-
"""Topic: 'How to start a balloon business: from first garland to first paying customer.'
(sempertexeurope.com/en_GB/blog/how-to-start-a-balloon-business).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=startbiz.
Uit de blog: klanten komen voor logo's; 4 dingen eerst (skills, kleine werkvoorraad + inflator/handpomp/sizer,
3 portfoliostukken, eenvoudige betaalwijze); grootste kostenrisico = verkeerde volgorde (logo, kaartjes, website
voor de eerste klant); 3 portfoliostukken thuis (organic slinger, cijferstack, tafelstuk), foto's bij daglicht tegen
een schone muur; eerste klanten uit je eigen netwerk (Denise boekte haar eerste opdracht via het netwerk van haar
vader); vertel het aan fotografen, zalen, bloemisten en planners; 5 fouten (elk platform, branding voor klanten,
concurreren op prijs, geen voorschot, te snel opgeven); de meeste starters boeken een eerste betalende klant binnen
30 dagen gericht werk; SYBB-workshop van 2 dagen met officieel boekje."""

G = {}
def setup(g): G.update(g)

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["Eerste klant in 30 dagen…", "3 portfoliostukken…", "Logo komt later…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Starten…",
    "steps_title": "Klanten komen voor logo's. 4 dingen die je eerst nodig hebt", "steps_lead": "Voor je eerste betalende klant:",
    "steps": ["Vaardigheden: een slinger, de juiste spanning, clusters die het transport overleven", "Een kleine werkvoorraad: de kleuren en maten die je het vaakst gebruikt, plus inflator, handpomp en ballonsizer", "3 portfoliostukken, gefotografeerd bij daglicht tegen een schone muur", "Een eenvoudige manier om betaald te worden, met een voorschot op elke opdracht"],
    "steps_label": "De basis",
    "rule1_label": "Volgorde", "rule1_title": "Geef uit in de juiste volgorde: training en voorraad eerst, logo laatst",
    "rule1_body": "Het grootste kostenrisico bij de start is niet de voorraad. Het is uitgeven in de verkeerde volgorde: een logo, visitekaartjes en een website voor je één betalende klant hebt. Investeer eerst in training en een kleine werkvoorraad. Branding kan wachten tot je weet wat je aanbiedt en wie ervoor betaalt.",
    "rule1_facts": [["1e", "training: slinger, spanning, transport"], ["2e", "een kleine werkvoorraad"], ["3e", "3 portfoliostukken"], ["laatst", "logo, kaartjes, website"]],
    "rule2_label": "Fouten", "rule2_title": "5 fouten die starters hun eerste jaar kosten",
    "rule2_body": "De meeste nieuwe artiesten stranden niet op techniek. Ze stranden op één van deze:",
    "alts": [["Elk platform tegelijk", "een account overal en aanwezig nergens. Beheers eerst 1 platform."], ["Branding voor klanten", "logo, kaartjes en website betaald met budget dat training en voorraad had moeten kopen."], ["Concurreren op prijs", "de goedkoopste decorateur van de streek trekt de klanten aan die niemand wil."], ["Geen voorschot", "een opdracht zonder voorschot is een opdracht die de dag ervoor kan annuleren."], ["Te snel opgeven", "ondernemen kost tijd. De eerste 30 dagen gaan over berichten sturen, niet over perfecte slingers."]],
    "example_label": "Voorbeeld", "example_title": "3 portfoliostukken uit 1 startersvoorraad",
    "ex_items": [["Organic slinger", "R12 en R5 in {p0}, {p1}, {p2} en {p3}. Je eerste foto en het stuk waar de meeste klanten om vragen."], ["Cijferstack", "dezelfde 4 kleuren rond een cijferframe. Verjaardagen en jubilea, het hele jaar door."], ["Tafelstuk", "3 R12 op een gewicht met R5-accenten. Klein, snel, en de makkelijkste eerste verkoop."]],
    "example_body": "Startersvoorraad: {p0}, {p1}, {p2} en {p3} in R12 en R5, plus een inflator, een handpomp en een ballonsizer. Fotografeer elk stuk bij daglicht tegen een schone muur.",
    "client_label": "Starter vraagt", "client_title": "Wat je antwoordt als een starter het vraagt",
    "client_answers": [
        "Ja. Klanten komen voor logo's. Bouw 3 stukken thuis, fotografeer ze bij daglicht tegen een schone muur en laat je netwerk weten dat je boekingen aanneemt. Logo en website komen na de eerste betalende klant.",
        "Van mensen die je al kent. Denise, één van onze workshopdocenten, boekte haar allereerste opdracht via het netwerk van haar vader. Vertel het aan familie en vrienden, en aan de lokale fotografen, zalen, bloemisten en planners wiens klanten decoratie nodig hebben.",
        "Ja, op elke opdracht. Werk aannemen zonder voorschot is één van de 5 fouten die starters geld kosten. Een voorschot bevestigt de datum, dekt je voorraad en filtert de mensen eruit die toch nooit gingen boeken.",
    ],
    "avoid_lead": "Je eerste 30 dagen, in 5 stappen:",
    "steps5": ["Leer 3 vaardigheden: een slinger, de juiste spanning, transportveilige clusters", "Koop een kleine voorraad: de kleuren en maten die je het vaakst gebruikt, plus inflator, handpomp en sizer", "Bouw 3 stukken thuis en fotografeer ze bij daglicht tegen een schone muur", "Kies 1 platform en vertel het aan je netwerk en aan 4 soorten lokale zaken", "Vraag een voorschot op elke opdracht, en hou vol"],
    "client_body": "Het volledige 30-dagenplan? Start Your Balloon Business is de workshop van 2 dagen van Sempertex Europe: techniek, de prijscalculator, klanten benaderen en het officiële boekje. Data op sempertexeurope.com/events.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Starten met Sempertex:", "s3_cover_b": "logo eerst", "s3_cover_c": "vs.", "s3_cover_d": "klant eerst",
    "s3_left": "LOGO EERST", "s3_right": "KLANT EERST", "s3_left_meta": "website, kaartjes, 0 klanten", "s3_right_meta": "3 stukken, 1 bericht, 1 voorschot",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["Logo", "Website", "Elk platform"], "s3_new_tags": ["Training", "Kleine voorraad", "3 stukken", "Voorschot"],
    "s3_new_quote": "“Drie stukken thuis, één bericht naar mijn netwerk, een voorschot op elke opdracht. Eerste betalende klant binnen 30 dagen.”", "s3_new_badge": "Eerste klant in 30 dagen",
    "s3_changed_bottom": "Zelfde ballonnen, zelfde handen.\nNu in de juiste volgorde.",
    "s3_topic_lbl": "WAAROM", "s3_rule1_topic": "Volgorde", "s3_rule1_old": "Eerst het logo, dan klanten",
    "s3_rule1_quote": "“Training en voorraad eerst. Het logo komt na de eerste betalende klant.”",
    "s3_rule2_topic": "Fouten", "s3_rule2_old": "De goedkoopste van de streek wint",
    "s3_rule2_quote": "“5 fouten kosten starters hun eerste jaar. Prijs is er maar één van.”",
    "s3_example_lbl": "VOORBEELD", "s3_example_quote": "“{p0}, {p1}, {p2} en {p3} in R12 en R5: genoeg voor een slinger, een cijferstack en een tafelstuk.”",
    "s3_client_lbl": "STARTER", "s3_client_topic": "Eerste klanten",
    "s3_client_quote": "“Je eerste klanten kennen je al. Vertel het ze.”",
    "s3_cta_kicker": "Start met een kleine voorraad, in de juiste volgorde",
    "garland_lbl": "slinger", "stack_lbl": "cijferstack", "centre_lbl": "tafelstuk", "logo_lbl": "logo?", "clients_lbl": "0 klanten", "builds_lbl": "3 stukken", "stock_lbl": "startersvoorraad", "tools": ["inflator", "handpomp", "ballonsizer"],
},
"en": {
    "cover_pills": ["First client in 30 days…", "3 portfolio builds…", "Logo comes later…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Starting out…",
    "steps_title": "Customers come before logos. 4 things you need first", "steps_lead": "Before your first paying customer:",
    "steps": ["Skills: a garland, the right tension, clusters that survive transport", "A small working stock: the colours and sizes you'll use most, plus inflator, hand pump and balloon sizer", "3 portfolio builds, photographed in daylight against a clean wall", "A simple way to get paid, with a deposit on every job"],
    "steps_label": "The basics",
    "rule1_label": "Order", "rule1_title": "Spend in the right order: training and stock first, logo last",
    "rule1_body": "The biggest cost risk when you start isn't the stock. It's spending in the wrong order: a logo, business cards and a website before you have a single paying client. Invest first in training and a small working stock. Branding can wait until you know what you offer and who pays for it.",
    "rule1_facts": [["1st", "training: garland, tension, transport"], ["2nd", "a small working stock"], ["3rd", "3 portfolio builds"], ["last", "logo, cards, website"]],
    "rule2_label": "Mistakes", "rule2_title": "5 mistakes that cost starters their first year",
    "rule2_body": "Most new artists don't fail on skill. They fail on one of these:",
    "alts": [["Every platform at once", "an account everywhere and a presence nowhere. Master 1 platform first."], ["Branding before clients", "logo, cards and website paid from a budget that should have bought training and stock."], ["Competing on price", "the cheapest decorator in the area attracts the clients nobody wants."], ["No deposit", "a job without a deposit is a job that can cancel the day before."], ["Giving up too early", "running a business takes time. The first 30 days are about sending messages, not perfecting garlands."]],
    "example_label": "Example", "example_title": "3 portfolio builds from 1 starter stock",
    "ex_items": [["Organic garland", "R12 and R5 in {p0}, {p1}, {p2} and {p3}. Your first photo and the piece most clients ask for."], ["Number stack", "the same 4 colours around a number frame. Birthdays and anniversaries, all year round."], ["Table centrepiece", "3 R12 on a weight with R5 accents. Small, quick, and the easiest first sale."]],
    "example_body": "Starter stock: {p0}, {p1}, {p2} and {p3} in R12 and R5, plus an inflator, a hand pump and a balloon sizer. Photograph every build in daylight against a clean wall.",
    "client_label": "Starter asks", "client_title": "What you answer when a starter asks",
    "client_answers": [
        "Yes. Customers come before logos. Build 3 pieces at home, photograph them in daylight against a clean wall and tell your network you're taking bookings. The logo and website come after the first paying client.",
        "From people you already know. Denise, one of our workshop instructors, booked her very first job through her father's network. Tell family and friends, and the local photographers, venues, florists and planners whose clients need decoration.",
        "Yes, on every job. Taking on work without a deposit is one of the 5 mistakes that cost starters money. A deposit confirms the date, covers your stock and filters out the people who were never going to book.",
    ],
    "avoid_lead": "Your first 30 days, in 5 steps:",
    "steps5": ["Learn 3 skills: a garland, the right tension, transport-safe clusters", "Buy a small stock: the colours and sizes you'll use most, plus inflator, hand pump and sizer", "Build 3 pieces at home and photograph them in daylight against a clean wall", "Pick 1 platform and tell your network and 4 types of local business", "Ask a deposit on every job, and keep going"],
    "client_body": "Want the full 30-day plan? Start Your Balloon Business is the 2-day workshop by Sempertex Europe: technique, the pricing calculator, outreach and the official booklet. Dates on sempertexeurope.com/events.",
    "cta_label": "Order",
    "s3_cover_a": "Starting with Sempertex:", "s3_cover_b": "logo first", "s3_cover_c": "vs.", "s3_cover_d": "client first",
    "s3_left": "LOGO FIRST", "s3_right": "CLIENT FIRST", "s3_left_meta": "website, cards, 0 clients", "s3_right_meta": "3 builds, 1 message, 1 deposit",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["Logo", "Website", "Every platform"], "s3_new_tags": ["Training", "Small stock", "3 builds", "Deposit"],
    "s3_new_quote": "“Three builds at home, one message to my network, a deposit on every job. First paying client within 30 days.”", "s3_new_badge": "First client in 30 days",
    "s3_changed_bottom": "Same balloons, same hands.\nNow in the right order.",
    "s3_topic_lbl": "WHY", "s3_rule1_topic": "Order", "s3_rule1_old": "Logo first, then clients",
    "s3_rule1_quote": "“Training and stock first. The logo comes after the first paying client.”",
    "s3_rule2_topic": "Mistakes", "s3_rule2_old": "Cheapest in the area wins",
    "s3_rule2_quote": "“5 mistakes cost starters their first year. Price is only one of them.”",
    "s3_example_lbl": "EXAMPLE", "s3_example_quote": "“{p0}, {p1}, {p2} and {p3} in R12 and R5: enough for a garland, a number stack and a centrepiece.”",
    "s3_client_lbl": "STARTER", "s3_client_topic": "First clients",
    "s3_client_quote": "“Your first clients already know you. Tell them.”",
    "s3_cta_kicker": "Start with a small stock, in the right order",
    "garland_lbl": "garland", "stack_lbl": "number stack", "centre_lbl": "centrepiece", "logo_lbl": "logo?", "clients_lbl": "0 clients", "builds_lbl": "3 builds", "stock_lbl": "starter stock", "tools": ["inflator", "hand pump", "balloon sizer"],
},
"de": {
    "cover_pills": ["Erster Kunde in 30 Tagen…", "3 Portfolio-Stücke…", "Logo kommt später…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Starten…",
    "steps_title": "Kunden kommen vor Logos. 4 Dinge, die du zuerst brauchst", "steps_lead": "Vor deinem ersten zahlenden Kunden:",
    "steps": ["Können: eine Girlande, die richtige Spannung, Cluster, die den Transport überstehen", "Ein kleiner Arbeitsvorrat: die Farben und Größen, die du am häufigsten brauchst, plus Inflator, Handpumpe und Ballonsizer", "3 Portfolio-Stücke, fotografiert bei Tageslicht vor einer sauberen Wand", "Eine einfache Art, bezahlt zu werden, mit Anzahlung bei jedem Auftrag"],
    "steps_label": "Die Basis",
    "rule1_label": "Reihenfolge", "rule1_title": "In der richtigen Reihenfolge ausgeben: Training und Vorrat zuerst, Logo zuletzt",
    "rule1_body": "Das größte Kostenrisiko am Anfang ist nicht der Vorrat. Es ist die falsche Reihenfolge: Logo, Visitenkarten und Website, bevor du einen einzigen zahlenden Kunden hast. Investiere zuerst in Training und einen kleinen Arbeitsvorrat. Branding kann warten, bis du weißt, was du anbietest und wer dafür bezahlt.",
    "rule1_facts": [["1.", "Training: Girlande, Spannung, Transport"], ["2.", "ein kleiner Arbeitsvorrat"], ["3.", "3 Portfolio-Stücke"], ["zuletzt", "Logo, Karten, Website"]],
    "rule2_label": "Fehler", "rule2_title": "5 Fehler, die Starter ihr erstes Jahr kosten",
    "rule2_body": "Die meisten neuen Artisten scheitern nicht an der Technik. Sie scheitern an einem dieser Punkte:",
    "alts": [["Jede Plattform gleichzeitig", "ein Konto überall und Präsenz nirgends. Beherrsche zuerst 1 Plattform."], ["Branding vor Kunden", "Logo, Karten und Website, bezahlt aus einem Budget, das Training und Vorrat hätte kaufen sollen."], ["Über den Preis konkurrieren", "der billigste Dekorateur der Gegend zieht die Kunden an, die niemand will."], ["Keine Anzahlung", "ein Auftrag ohne Anzahlung ist ein Auftrag, der am Tag davor absagen kann."], ["Zu früh aufgeben", "ein Geschäft braucht Zeit. In den ersten 30 Tagen geht es um Nachrichten, nicht um perfekte Girlanden."]],
    "example_label": "Beispiel", "example_title": "3 Portfolio-Stücke aus 1 Startervorrat",
    "ex_items": [["Organic Girlande", "R12 und R5 in {p0}, {p1}, {p2} und {p3}. Dein erstes Foto und das Stück, nach dem die meisten Kunden fragen."], ["Zahlen-Stack", "dieselben 4 Farben um einen Zahlenrahmen. Geburtstage und Jubiläen, das ganze Jahr."], ["Tischdeko", "3 R12 auf einem Gewicht mit R5-Akzenten. Klein, schnell und der einfachste erste Verkauf."]],
    "example_body": "Startervorrat: {p0}, {p1}, {p2} und {p3} in R12 und R5, plus Inflator, Handpumpe und Ballonsizer. Fotografiere jedes Stück bei Tageslicht vor einer sauberen Wand.",
    "client_label": "Starter fragt", "client_title": "Was du antwortest, wenn ein Starter fragt",
    "client_answers": [
        "Ja. Kunden kommen vor Logos. Bau 3 Stücke zu Hause, fotografiere sie bei Tageslicht vor einer sauberen Wand und sag deinem Netzwerk, dass du Buchungen annimmst. Logo und Website kommen nach dem ersten zahlenden Kunden.",
        "Von Leuten, die du schon kennst. Denise, eine unserer Workshop-Trainerinnen, hat ihren allerersten Auftrag über das Netzwerk ihres Vaters gebucht. Sag es Familie und Freunden, und den lokalen Fotografen, Locations, Floristen und Planern, deren Kunden Dekoration brauchen.",
        "Ja, bei jedem Auftrag. Aufträge ohne Anzahlung anzunehmen ist einer der 5 Fehler, die Starter Geld kosten. Eine Anzahlung bestätigt das Datum, deckt deinen Vorrat und filtert die Leute heraus, die sowieso nie gebucht hätten.",
    ],
    "avoid_lead": "Deine ersten 30 Tage, in 5 Schritten:",
    "steps5": ["Lerne 3 Techniken: eine Girlande, die richtige Spannung, transportsichere Cluster", "Kauf einen kleinen Vorrat: die Farben und Größen, die du am häufigsten brauchst, plus Inflator, Handpumpe und Sizer", "Bau 3 Stücke zu Hause und fotografiere sie bei Tageslicht vor einer sauberen Wand", "Wähl 1 Plattform und sag es deinem Netzwerk und 4 Arten lokaler Betriebe", "Verlange bei jedem Auftrag eine Anzahlung, und bleib dran"],
    "client_body": "Der komplette 30-Tage-Plan? Start Your Balloon Business ist der 2-Tage-Workshop von Sempertex Europe: Technik, der Preiskalkulator, Kundenansprache und das offizielle Booklet. Termine auf sempertexeurope.com/events.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Starten mit Sempertex:", "s3_cover_b": "Logo zuerst", "s3_cover_c": "vs.", "s3_cover_d": "Kunde zuerst",
    "s3_left": "LOGO ZUERST", "s3_right": "KUNDE ZUERST", "s3_left_meta": "Website, Karten, 0 Kunden", "s3_right_meta": "3 Stücke, 1 Nachricht, 1 Anzahlung",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["Logo", "Website", "Jede Plattform"], "s3_new_tags": ["Training", "Kleiner Vorrat", "3 Stücke", "Anzahlung"],
    "s3_new_quote": "“Drei Stücke zu Hause, eine Nachricht an mein Netzwerk, eine Anzahlung bei jedem Auftrag. Erster zahlender Kunde in 30 Tagen.”", "s3_new_badge": "Erster Kunde in 30 Tagen",
    "s3_changed_bottom": "Dieselben Ballons, dieselben Hände.\nJetzt in der richtigen Reihenfolge.",
    "s3_topic_lbl": "WARUM", "s3_rule1_topic": "Reihenfolge", "s3_rule1_old": "Erst das Logo, dann Kunden",
    "s3_rule1_quote": "“Training und Vorrat zuerst. Das Logo kommt nach dem ersten zahlenden Kunden.”",
    "s3_rule2_topic": "Fehler", "s3_rule2_old": "Der Billigste der Gegend gewinnt",
    "s3_rule2_quote": "“5 Fehler kosten Starter ihr erstes Jahr. Der Preis ist nur einer davon.”",
    "s3_example_lbl": "BEISPIEL", "s3_example_quote": "“{p0}, {p1}, {p2} und {p3} in R12 und R5: genug für eine Girlande, einen Zahlen-Stack und eine Tischdeko.”",
    "s3_client_lbl": "STARTER", "s3_client_topic": "Erste Kunden",
    "s3_client_quote": "“Deine ersten Kunden kennen dich schon. Sag es ihnen.”",
    "s3_cta_kicker": "Starte mit einem kleinen Vorrat, in der richtigen Reihenfolge",
    "garland_lbl": "Girlande", "stack_lbl": "Zahlen-Stack", "centre_lbl": "Tischdeko", "logo_lbl": "Logo?", "clients_lbl": "0 Kunden", "builds_lbl": "3 Stücke", "stock_lbl": "Startervorrat", "tools": ["Inflator", "Handpumpe", "Ballonsizer"],
},
"fr": {
    "cover_pills": ["1er client en 30 jours…", "3 pièces portfolio…", "Le logo attend…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Se lancer…",
    "steps_title": "Les clients passent avant le logo. 4 choses à avoir d'abord", "steps_lead": "Avant ton premier client payant :",
    "steps": ["Les gestes : une guirlande, la bonne tension, des clusters qui survivent au transport", "Un petit stock de travail : les couleurs et tailles que tu utiliseras le plus, plus gonfleur, pompe à main et calibreur", "3 pièces portfolio, photographiées à la lumière du jour devant un mur propre", "Une façon simple d'être payé, avec un acompte sur chaque commande"],
    "steps_label": "La base",
    "rule1_label": "Ordre", "rule1_title": "Dépense dans le bon ordre : formation et stock d'abord, logo en dernier",
    "rule1_body": "Le plus gros risque financier au départ, ce n'est pas le stock. C'est dépenser dans le mauvais ordre : un logo, des cartes de visite et un site avant d'avoir un seul client payant. Investis d'abord dans la formation et un petit stock de travail. Le branding peut attendre que tu saches ce que tu proposes et qui paie pour ça.",
    "rule1_facts": [["1er", "formation : guirlande, tension, transport"], ["2e", "un petit stock de travail"], ["3e", "3 pièces portfolio"], ["en dernier", "logo, cartes, site"]],
    "rule2_label": "Erreurs", "rule2_title": "5 erreurs qui coûtent leur première année aux débutants",
    "rule2_body": "La plupart des nouveaux artistes ne bloquent pas sur la technique. Ils bloquent sur l'une de ces erreurs :",
    "alts": [["Toutes les plateformes à la fois", "un compte partout et une présence nulle part. Maîtrise d'abord 1 plateforme."], ["Le branding avant les clients", "logo, cartes et site payés avec un budget qui aurait dû financer formation et stock."], ["Se battre sur le prix", "le décorateur le moins cher du coin attire les clients dont personne ne veut."], ["Pas d'acompte", "une commande sans acompte est une commande qui peut annuler la veille."], ["Abandonner trop vite", "entreprendre prend du temps. Les 30 premiers jours servent à envoyer des messages, pas à perfectionner des guirlandes."]],
    "example_label": "Exemple", "example_title": "3 pièces portfolio avec 1 stock de départ",
    "ex_items": [["Guirlande organique", "R12 et R5 en {p0}, {p1}, {p2} et {p3}. Ta première photo et la pièce que la plupart des clients demandent."], ["Chiffre en ballons", "les mêmes 4 couleurs autour d'une structure chiffre. Anniversaires et jubilés, toute l'année."], ["Centre de table", "3 R12 sur un poids avec des touches de R5. Petit, rapide, et la première vente la plus facile."]],
    "example_body": "Stock de départ : {p0}, {p1}, {p2} et {p3} en R12 et R5, plus un gonfleur, une pompe à main et un calibreur. Photographie chaque pièce à la lumière du jour devant un mur propre.",
    "client_label": "Un débutant demande", "client_title": "Ce que tu réponds quand un débutant demande",
    "client_answers": [
        "Oui. Les clients passent avant le logo. Monte 3 pièces chez toi, photographie-les à la lumière du jour devant un mur propre et dis à ton réseau que tu prends des réservations. Le logo et le site viennent après le premier client payant.",
        "De gens que tu connais déjà. Denise, l'une de nos formatrices, a décroché sa toute première commande via le réseau de son père. Dis-le à ta famille et tes amis, et aux photographes, salles, fleuristes et organisateurs du coin dont les clients ont besoin de décoration.",
        "Oui, sur chaque commande. Accepter un travail sans acompte fait partie des 5 erreurs qui coûtent de l'argent aux débutants. Un acompte confirme la date, couvre ton stock et écarte les gens qui n'allaient de toute façon jamais réserver.",
    ],
    "avoid_lead": "Tes 30 premiers jours, en 5 étapes :",
    "steps5": ["Apprends 3 gestes : une guirlande, la bonne tension, des clusters qui tiennent au transport", "Achète un petit stock : les couleurs et tailles que tu utiliseras le plus, plus gonfleur, pompe à main et calibreur", "Monte 3 pièces chez toi et photographie-les à la lumière du jour devant un mur propre", "Choisis 1 plateforme et préviens ton réseau et 4 types de commerces locaux", "Demande un acompte sur chaque commande, et tiens bon"],
    "client_body": "Le plan complet sur 30 jours ? Start Your Balloon Business est l'atelier de 2 jours de Sempertex Europe : technique, le calculateur de prix, la prospection et le livret officiel. Dates sur sempertexeurope.com/events.",
    "cta_label": "Commander",
    "s3_cover_a": "Se lancer avec Sempertex :", "s3_cover_b": "logo d'abord", "s3_cover_c": "vs.", "s3_cover_d": "client d'abord",
    "s3_left": "LOGO D'ABORD", "s3_right": "CLIENT D'ABORD", "s3_left_meta": "site, cartes, 0 client", "s3_right_meta": "3 pièces, 1 message, 1 acompte",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["Logo", "Site", "Toutes les plateformes"], "s3_new_tags": ["Formation", "Petit stock", "3 pièces", "Acompte"],
    "s3_new_quote": "“Trois pièces chez moi, un message à mon réseau, un acompte sur chaque commande. Premier client payant en 30 jours.”", "s3_new_badge": "1er client en 30 jours",
    "s3_changed_bottom": "Mêmes ballons, mêmes mains.\nMaintenant dans le bon ordre.",
    "s3_topic_lbl": "POURQUOI", "s3_rule1_topic": "Ordre", "s3_rule1_old": "D'abord le logo, puis les clients",
    "s3_rule1_quote": "“Formation et stock d'abord. Le logo vient après le premier client payant.”",
    "s3_rule2_topic": "Erreurs", "s3_rule2_old": "Le moins cher du coin gagne",
    "s3_rule2_quote": "“5 erreurs coûtent leur première année aux débutants. Le prix n'en est qu'une.”",
    "s3_example_lbl": "EXEMPLE", "s3_example_quote": "“{p0}, {p1}, {p2} et {p3} en R12 et R5 : assez pour une guirlande, un chiffre et un centre de table.”",
    "s3_client_lbl": "DÉBUTANT", "s3_client_topic": "Premiers clients",
    "s3_client_quote": "“Tes premiers clients te connaissent déjà. Dis-leur.”",
    "s3_cta_kicker": "Commence avec un petit stock, dans le bon ordre",
    "garland_lbl": "guirlande", "stack_lbl": "chiffre", "centre_lbl": "centre de table", "logo_lbl": "logo ?", "clients_lbl": "0 client", "builds_lbl": "3 pièces", "stock_lbl": "stock de départ", "tools": ["gonfleur", "pompe à main", "calibreur"],
},
"it": {
    "cover_pills": ["1° cliente in 30 giorni…", "3 pezzi portfolio…", "Il logo dopo…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "Iniziare…",
    "steps_title": "I clienti vengono prima del logo. 4 cose che ti servono subito", "steps_lead": "Prima del tuo primo cliente pagante:",
    "steps": ["Le tecniche: una ghirlanda, la tensione giusta, cluster che reggono il trasporto", "Una piccola scorta di lavoro: i colori e le misure che userai di più, più gonfiatore, pompa a mano e calibratore", "3 pezzi portfolio, fotografati alla luce del giorno davanti a una parete pulita", "Un modo semplice per farti pagare, con un acconto su ogni lavoro"],
    "steps_label": "Le basi",
    "rule1_label": "Ordine", "rule1_title": "Spendi nell'ordine giusto: formazione e scorta prima, logo per ultimo",
    "rule1_body": "Il rischio più grande all'inizio non è la scorta. È spendere nell'ordine sbagliato: logo, biglietti da visita e sito prima di avere un solo cliente pagante. Investi prima in formazione e in una piccola scorta di lavoro. Il branding può aspettare finché non sai cosa offri e chi lo paga.",
    "rule1_facts": [["1°", "formazione: ghirlanda, tensione, trasporto"], ["2°", "una piccola scorta di lavoro"], ["3°", "3 pezzi portfolio"], ["ultimo", "logo, biglietti, sito"]],
    "rule2_label": "Errori", "rule2_title": "5 errori che costano il primo anno a chi inizia",
    "rule2_body": "La maggior parte dei nuovi artisti non si ferma sulla tecnica. Si ferma su uno di questi:",
    "alts": [["Tutte le piattaforme insieme", "un account ovunque e presenza da nessuna parte. Padroneggia prima 1 piattaforma."], ["Branding prima dei clienti", "logo, biglietti e sito pagati con un budget che doveva comprare formazione e scorta."], ["Competere sul prezzo", "il decoratore più economico della zona attira i clienti che nessuno vuole."], ["Nessun acconto", "un lavoro senza acconto è un lavoro che può disdire il giorno prima."], ["Mollare troppo presto", "fare impresa richiede tempo. I primi 30 giorni servono a mandare messaggi, non a perfezionare ghirlande."]],
    "example_label": "Esempio", "example_title": "3 pezzi portfolio da 1 scorta iniziale",
    "ex_items": [["Ghirlanda organica", "R12 e R5 in {p0}, {p1}, {p2} e {p3}. La tua prima foto e il pezzo che chiedono quasi tutti i clienti."], ["Numero in palloncini", "gli stessi 4 colori intorno a una struttura numero. Compleanni e anniversari, tutto l'anno."], ["Centrotavola", "3 R12 su un peso con accenti R5. Piccolo, veloce, e la prima vendita più facile."]],
    "example_body": "Scorta iniziale: {p0}, {p1}, {p2} e {p3} in R12 e R5, più un gonfiatore, una pompa a mano e un calibratore. Fotografa ogni pezzo alla luce del giorno davanti a una parete pulita.",
    "client_label": "Chi inizia chiede", "client_title": "Cosa rispondi quando chi inizia te lo chiede",
    "client_answers": [
        "Sì. I clienti vengono prima del logo. Costruisci 3 pezzi a casa, fotografali alla luce del giorno davanti a una parete pulita e fai sapere alla tua rete che prendi prenotazioni. Logo e sito arrivano dopo il primo cliente pagante.",
        "Da persone che conosci già. Denise, una delle nostre istruttrici, ha preso il suo primissimo lavoro tramite la rete di suo padre. Dillo a famiglia e amici, e ai fotografi, location, fioristi e planner della zona i cui clienti hanno bisogno di decorazioni.",
        "Sì, su ogni lavoro. Accettare lavori senza acconto è uno dei 5 errori che costano soldi a chi inizia. Un acconto conferma la data, copre la scorta e filtra le persone che tanto non avrebbero mai prenotato.",
    ],
    "avoid_lead": "I tuoi primi 30 giorni, in 5 passi:",
    "steps5": ["Impara 3 tecniche: una ghirlanda, la tensione giusta, cluster sicuri per il trasporto", "Compra una piccola scorta: i colori e le misure che userai di più, più gonfiatore, pompa a mano e calibratore", "Costruisci 3 pezzi a casa e fotografali alla luce del giorno davanti a una parete pulita", "Scegli 1 piattaforma e avvisa la tua rete e 4 tipi di attività locali", "Chiedi un acconto su ogni lavoro, e vai avanti"],
    "client_body": "Vuoi il piano completo di 30 giorni? Start Your Balloon Business è il workshop di 2 giorni di Sempertex Europe: tecnica, il calcolatore dei prezzi, come trovare clienti e il libretto ufficiale. Date su sempertexeurope.com/events.",
    "cta_label": "Ordina",
    "s3_cover_a": "Iniziare con Sempertex:", "s3_cover_b": "prima il logo", "s3_cover_c": "vs.", "s3_cover_d": "prima il cliente",
    "s3_left": "PRIMA IL LOGO", "s3_right": "PRIMA IL CLIENTE", "s3_left_meta": "sito, biglietti, 0 clienti", "s3_right_meta": "3 pezzi, 1 messaggio, 1 acconto",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["Logo", "Sito", "Tutte le piattaforme"], "s3_new_tags": ["Formazione", "Piccola scorta", "3 pezzi", "Acconto"],
    "s3_new_quote": "“Tre pezzi a casa, un messaggio alla mia rete, un acconto su ogni lavoro. Primo cliente pagante in 30 giorni.”", "s3_new_badge": "1° cliente in 30 giorni",
    "s3_changed_bottom": "Stessi palloncini, stesse mani.\nOra nell'ordine giusto.",
    "s3_topic_lbl": "PERCHÉ", "s3_rule1_topic": "Ordine", "s3_rule1_old": "Prima il logo, poi i clienti",
    "s3_rule1_quote": "“Prima formazione e scorta. Il logo arriva dopo il primo cliente pagante.”",
    "s3_rule2_topic": "Errori", "s3_rule2_old": "Vince il più economico della zona",
    "s3_rule2_quote": "“5 errori costano il primo anno a chi inizia. Il prezzo è solo uno.”",
    "s3_example_lbl": "ESEMPIO", "s3_example_quote": "“{p0}, {p1}, {p2} e {p3} in R12 e R5: bastano per una ghirlanda, un numero e un centrotavola.”",
    "s3_client_lbl": "CHI INIZIA", "s3_client_topic": "Primi clienti",
    "s3_client_quote": "“I tuoi primi clienti ti conoscono già. Diglielo.”",
    "s3_cta_kicker": "Inizia con una piccola scorta, nell'ordine giusto",
    "garland_lbl": "ghirlanda", "stack_lbl": "numero", "centre_lbl": "centrotavola", "logo_lbl": "logo?", "clients_lbl": "0 clienti", "builds_lbl": "3 pezzi", "stock_lbl": "scorta iniziale", "tools": ["gonfiatore", "pompa a mano", "calibratore"],
},
"pl": {
    "cover_pills": ["1. klient w 30 dni…", "3 prace do portfolio…", "Logo później…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Start…",
    "steps_title": "Klienci są ważniejsi niż logo. 4 rzeczy, które musisz mieć najpierw", "steps_lead": "Zanim zdobędziesz pierwszego płacącego klienta:",
    "steps": ["Umiejętności: girlanda, właściwe napięcie, klastry, które przetrwają transport", "Mały zapas roboczy: kolory i rozmiary, których użyjesz najczęściej, plus inflator, pompka ręczna i kalibrator", "3 prace do portfolio, sfotografowane w dziennym świetle na tle czystej ściany", "Prosty sposób przyjmowania płatności, z zaliczką przy każdym zleceniu"],
    "steps_label": "Podstawy",
    "rule1_label": "Kolejność", "rule1_title": "Wydawaj we właściwej kolejności: szkolenie i zapas najpierw, logo na końcu",
    "rule1_body": "Największe ryzyko kosztowe na starcie to nie zapas. To wydawanie w złej kolejności: logo, wizytówki i strona, zanim masz choć jednego płacącego klienta. Zainwestuj najpierw w szkolenie i mały zapas roboczy. Branding może poczekać, aż wiesz, co oferujesz i kto za to płaci.",
    "rule1_facts": [["1.", "szkolenie: girlanda, napięcie, transport"], ["2.", "mały zapas roboczy"], ["3.", "3 prace do portfolio"], ["na końcu", "logo, wizytówki, strona"]],
    "rule2_label": "Błędy", "rule2_title": "5 błędów, które kosztują początkujących pierwszy rok",
    "rule2_body": "Większość nowych artystów nie przegrywa na technice. Przegrywa na jednym z tych punktów:",
    "alts": [["Wszystkie platformy naraz", "konto wszędzie i obecność nigdzie. Opanuj najpierw 1 platformę."], ["Branding przed klientami", "logo, wizytówki i strona opłacone z budżetu, który miał kupić szkolenie i zapas."], ["Konkurowanie ceną", "najtańszy dekorator w okolicy przyciąga klientów, których nikt nie chce."], ["Brak zaliczki", "zlecenie bez zaliczki to zlecenie, które może odwołać się dzień wcześniej."], ["Zbyt szybkie poddanie się", "biznes potrzebuje czasu. Pierwsze 30 dni to wysyłanie wiadomości, nie doskonalenie girland."]],
    "example_label": "Przykład", "example_title": "3 prace do portfolio z 1 zapasu startowego",
    "ex_items": [["Girlanda organiczna", "R12 i R5 w kolorach {p0}, {p1}, {p2} i {p3}. Twoje pierwsze zdjęcie i praca, o którą prosi większość klientów."], ["Cyfra z balonów", "te same 4 kolory wokół stelaża cyfry. Urodziny i rocznice, przez cały rok."], ["Dekoracja stołu", "3 R12 na obciążniku z akcentami R5. Mała, szybka i najłatwiejsza pierwsza sprzedaż."]],
    "example_body": "Zapas startowy: {p0}, {p1}, {p2} i {p3} w R12 i R5, plus inflator, pompka ręczna i kalibrator. Każdą pracę fotografuj w dziennym świetle na tle czystej ściany.",
    "client_label": "Początkujący pyta", "client_title": "Co odpowiadasz, gdy pyta początkujący",
    "client_answers": [
        "Tak. Klienci są ważniejsi niż logo. Zbuduj 3 prace w domu, sfotografuj je w dziennym świetle na tle czystej ściany i daj znać swojej sieci, że przyjmujesz rezerwacje. Logo i strona przyjdą po pierwszym płacącym kliencie.",
        "Od ludzi, których już znasz. Denise, jedna z naszych instruktorek, zdobyła swoje pierwsze zlecenie przez sieć kontaktów swojego ojca. Powiedz rodzinie i znajomym, a także lokalnym fotografom, salom, kwiaciarniom i planerom, których klienci potrzebują dekoracji.",
        "Tak, przy każdym zleceniu. Przyjmowanie pracy bez zaliczki to jeden z 5 błędów, które kosztują początkujących pieniądze. Zaliczka potwierdza termin, pokrywa zapas i odsiewa ludzi, którzy i tak nigdy nie zamierzali rezerwować.",
    ],
    "avoid_lead": "Twoje pierwsze 30 dni, w 5 krokach:",
    "steps5": ["Naucz się 3 umiejętności: girlanda, właściwe napięcie, klastry bezpieczne w transporcie", "Kup mały zapas: kolory i rozmiary, których użyjesz najczęściej, plus inflator, pompka ręczna i kalibrator", "Zbuduj 3 prace w domu i sfotografuj je w dziennym świetle na tle czystej ściany", "Wybierz 1 platformę i powiedz o sobie swojej sieci oraz 4 typom lokalnych firm", "Bierz zaliczkę przy każdym zleceniu i nie odpuszczaj"],
    "client_body": "Chcesz pełny plan na 30 dni? Start Your Balloon Business to 2-dniowy warsztat Sempertex Europe: technika, kalkulator cen, pozyskiwanie klientów i oficjalna broszura. Terminy na sempertexeurope.com/events.",
    "cta_label": "Zamów",
    "s3_cover_a": "Start z Sempertex:", "s3_cover_b": "najpierw logo", "s3_cover_c": "vs.", "s3_cover_d": "najpierw klient",
    "s3_left": "NAJPIERW LOGO", "s3_right": "NAJPIERW KLIENT", "s3_left_meta": "strona, wizytówki, 0 klientów", "s3_right_meta": "3 prace, 1 wiadomość, 1 zaliczka",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "STARE", "s3_new_lbl": "NOWE",
    "s3_old_tags": ["Logo", "Strona", "Każda platforma"], "s3_new_tags": ["Szkolenie", "Mały zapas", "3 prace", "Zaliczka"],
    "s3_new_quote": "“Trzy prace w domu, jedna wiadomość do mojej sieci, zaliczka przy każdym zleceniu. Pierwszy płacący klient w 30 dni.”", "s3_new_badge": "1. klient w 30 dni",
    "s3_changed_bottom": "Te same balony, te same ręce.\nTeraz we właściwej kolejności.",
    "s3_topic_lbl": "DLACZEGO", "s3_rule1_topic": "Kolejność", "s3_rule1_old": "Najpierw logo, potem klienci",
    "s3_rule1_quote": "“Najpierw szkolenie i zapas. Logo przychodzi po pierwszym płacącym kliencie.”",
    "s3_rule2_topic": "Błędy", "s3_rule2_old": "Wygrywa najtańszy w okolicy",
    "s3_rule2_quote": "“5 błędów kosztuje początkujących pierwszy rok. Cena to tylko jeden z nich.”",
    "s3_example_lbl": "PRZYKŁAD", "s3_example_quote": "“{p0}, {p1}, {p2} i {p3} w R12 i R5: wystarczy na girlandę, cyfrę i dekorację stołu.”",
    "s3_client_lbl": "START", "s3_client_topic": "Pierwsi klienci",
    "s3_client_quote": "“Twoi pierwsi klienci już cię znają. Powiedz im.”",
    "s3_cta_kicker": "Zacznij od małego zapasu, we właściwej kolejności",
    "garland_lbl": "girlanda", "stack_lbl": "cyfra", "centre_lbl": "dekoracja stołu", "logo_lbl": "logo?", "clients_lbl": "0 klientów", "builds_lbl": "3 prace", "stock_lbl": "zapas startowy", "tools": ["inflator", "pompka ręczna", "kalibrator"],
},
"el": {
    "cover_pills": ["1ος πελάτης σε 30 μέρες…", "3 κομμάτια portfolio…", "Το logo μετά…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Ξεκίνημα…",
    "steps_title": "Οι πελάτες έρχονται πριν από το logo. 4 πράγματα που χρειάζεσαι πρώτα", "steps_lead": "Πριν τον πρώτο πελάτη που πληρώνει:",
    "steps": ["Δεξιότητες: γιρλάντα, σωστή τάση, clusters που αντέχουν τη μεταφορά", "Μικρό απόθεμα εργασίας: τα χρώματα και μεγέθη που χρησιμοποιείς πιο συχνά, συν φουσκωτήρα, τρόμπα και sizer", "3 κομμάτια portfolio, φωτογραφημένα με φως ημέρας σε καθαρό τοίχο", "Απλός τρόπος πληρωμής, με προκαταβολή σε κάθε δουλειά"],
    "steps_label": "Τα βασικά",
    "rule1_label": "Σειρά", "rule1_title": "Ξόδεψε με τη σωστή σειρά: εκπαίδευση και απόθεμα πρώτα, logo τελευταίο",
    "rule1_body": "Ο μεγαλύτερος κίνδυνος κόστους στην αρχή δεν είναι το απόθεμα. Είναι να ξοδεύεις με λάθος σειρά: logo, επαγγελματικές κάρτες και site πριν έχεις έστω έναν πελάτη που πληρώνει. Επένδυσε πρώτα σε εκπαίδευση και σε ένα μικρό απόθεμα εργασίας. Το branding μπορεί να περιμένει μέχρι να ξέρεις τι προσφέρεις και ποιος το πληρώνει.",
    "rule1_facts": [["1ο", "εκπαίδευση: γιρλάντα, τάση, μεταφορά"], ["2ο", "ένα μικρό απόθεμα εργασίας"], ["3ο", "3 κομμάτια portfolio"], ["τελευταίο", "logo, κάρτες, site"]],
    "rule2_label": "Λάθη", "rule2_title": "5 λάθη που κοστίζουν στους αρχάριους τον πρώτο χρόνο",
    "rule2_body": "Οι περισσότεροι νέοι καλλιτέχνες δεν κολλάνε στην τεχνική. Κολλάνε σε ένα από αυτά:",
    "alts": [["Όλες οι πλατφόρμες μαζί", "λογαριασμός παντού και παρουσία πουθενά. Μάθε πρώτα 1 πλατφόρμα."], ["Branding πριν τους πελάτες", "logo, κάρτες και site πληρωμένα από budget που έπρεπε να πάει σε εκπαίδευση και απόθεμα."], ["Ανταγωνισμός στην τιμή", "ο φθηνότερος διακοσμητής της περιοχής τραβάει τους πελάτες που κανείς δεν θέλει."], ["Χωρίς προκαταβολή", "δουλειά χωρίς προκαταβολή είναι δουλειά που μπορεί να ακυρωθεί μια μέρα πριν."], ["Παρατάς πολύ νωρίς", "η επιχείρηση θέλει χρόνο. Οι πρώτες 30 μέρες είναι για μηνύματα, όχι για τέλειες γιρλάντες."]],
    "example_label": "Παράδειγμα", "example_title": "3 κομμάτια portfolio από 1 αρχικό απόθεμα",
    "ex_items": [["Organic γιρλάντα", "R12 και R5 σε {p0}, {p1}, {p2} και {p3}. Η πρώτη σου φωτογραφία και το κομμάτι που ζητούν οι περισσότεροι πελάτες."], ["Αριθμός με μπαλόνια", "τα ίδια 4 χρώματα γύρω από σκελετό αριθμού. Γενέθλια και επέτειοι, όλο τον χρόνο."], ["Κεντρικό τραπεζιού", "3 R12 σε βαρίδι με πινελιές R5. Μικρό, γρήγορο, και η πιο εύκολη πρώτη πώληση."]],
    "example_body": "Αρχικό απόθεμα: {p0}, {p1}, {p2} και {p3} σε R12 και R5, συν φουσκωτήρα, τρόμπα χειρός και sizer. Φωτογράφισε κάθε κομμάτι με φως ημέρας μπροστά σε καθαρό τοίχο.",
    "client_label": "Ρωτάει αρχάριος", "client_title": "Τι απαντάς όταν ρωτάει ένας αρχάριος",
    "client_answers": [
        "Ναι. Οι πελάτες έρχονται πριν από το logo. Φτιάξε 3 κομμάτια στο σπίτι, φωτογράφισέ τα με φως ημέρας μπροστά σε καθαρό τοίχο και πες στον κύκλο σου ότι δέχεσαι κρατήσεις. Το logo και το site έρχονται μετά τον πρώτο πελάτη που πληρώνει.",
        "Από ανθρώπους που ήδη ξέρεις. Η Denise, μία από τις εκπαιδεύτριές μας, έκλεισε την πρώτη της δουλειά μέσα από τον κύκλο του πατέρα της. Πες το σε οικογένεια και φίλους, και στους τοπικούς φωτογράφους, χώρους, ανθοπωλεία και planners που οι πελάτες τους χρειάζονται διακόσμηση.",
        "Ναι, σε κάθε δουλειά. Το να δέχεσαι δουλειά χωρίς προκαταβολή είναι ένα από τα 5 λάθη που κοστίζουν χρήματα στους αρχάριους. Η προκαταβολή επιβεβαιώνει την ημερομηνία, καλύπτει το απόθεμα και φιλτράρει όσους δεν θα έκλειναν ποτέ.",
    ],
    "avoid_lead": "Οι πρώτες 30 μέρες σου, σε 5 βήματα:",
    "steps5": ["Μάθε 3 δεξιότητες: γιρλάντα, σωστή τάση, clusters ασφαλή στη μεταφορά", "Αγόρασε μικρό απόθεμα: τα χρώματα και μεγέθη που θα χρησιμοποιείς πιο συχνά, συν φουσκωτήρα, τρόμπα και sizer", "Φτιάξε 3 κομμάτια στο σπίτι και φωτογράφισέ τα με φως ημέρας μπροστά σε καθαρό τοίχο", "Διάλεξε 1 πλατφόρμα και ενημέρωσε τον κύκλο σου και 4 είδη τοπικών επιχειρήσεων", "Ζήτα προκαταβολή σε κάθε δουλειά, και συνέχισε"],
    "client_body": "Θέλεις το πλήρες πλάνο 30 ημερών; Το Start Your Balloon Business είναι το 2ήμερο workshop της Sempertex Europe: τεχνική, ο υπολογιστής τιμών, προσέγγιση πελατών και το επίσημο βιβλιαράκι. Ημερομηνίες στο sempertexeurope.com/events.",
    "cta_label": "Παραγγελία",
    "s3_cover_a": "Ξεκίνημα με Sempertex:", "s3_cover_b": "πρώτα το logo", "s3_cover_c": "vs.", "s3_cover_d": "πρώτα ο πελάτης",
    "s3_left": "ΠΡΩΤΑ ΤΟ LOGO", "s3_right": "ΠΡΩΤΑ Ο ΠΕΛΑΤΗΣ", "s3_left_meta": "site, κάρτες, 0 πελάτες", "s3_right_meta": "3 κομμάτια, 1 μήνυμα, 1 προκαταβολή",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["Logo", "Site", "Κάθε πλατφόρμα"], "s3_new_tags": ["Εκπαίδευση", "Μικρό απόθεμα", "3 κομμάτια", "Προκαταβολή"],
    "s3_new_quote": "“Τρία κομμάτια στο σπίτι, ένα μήνυμα στον κύκλο μου, προκαταβολή σε κάθε δουλειά. Πρώτος πελάτης που πληρώνει σε 30 μέρες.”", "s3_new_badge": "1ος πελάτης σε 30 μέρες",
    "s3_changed_bottom": "Ίδια μπαλόνια, ίδια χέρια.\nΤώρα με τη σωστή σειρά.",
    "s3_topic_lbl": "ΓΙΑΤΙ", "s3_rule1_topic": "Σειρά", "s3_rule1_old": "Πρώτα το logo, μετά πελάτες",
    "s3_rule1_quote": "“Πρώτα εκπαίδευση και απόθεμα. Το logo έρχεται μετά τον πρώτο πελάτη που πληρώνει.”",
    "s3_rule2_topic": "Λάθη", "s3_rule2_old": "Κερδίζει ο φθηνότερος της περιοχής",
    "s3_rule2_quote": "“5 λάθη κοστίζουν στους αρχάριους τον πρώτο χρόνο. Η τιμή είναι μόνο το ένα.”",
    "s3_example_lbl": "ΠΑΡΑΔΕΙΓΜΑ", "s3_example_quote": "“{p0}, {p1}, {p2} και {p3} σε R12 και R5: αρκούν για γιρλάντα, αριθμό και κεντρικό τραπεζιού.”",
    "s3_client_lbl": "ΑΡΧΑΡΙΟΣ", "s3_client_topic": "Πρώτοι πελάτες",
    "s3_client_quote": "“Οι πρώτοι σου πελάτες σε ξέρουν ήδη. Πες τους το.”",
    "s3_cta_kicker": "Ξεκίνα με μικρό απόθεμα, με τη σωστή σειρά",
    "garland_lbl": "γιρλάντα", "stack_lbl": "αριθμός", "centre_lbl": "κεντρικό", "logo_lbl": "logo;", "clients_lbl": "0 πελάτες", "builds_lbl": "3 κομμάτια", "stock_lbl": "αρχικό απόθεμα", "tools": ["φουσκωτήρας", "τρόμπα χειρός", "sizer"],
},
"hu": {
    "cover_pills": ["Első ügyfél 30 nap alatt…", "3 portfóliódarab…", "A logó ráér…"], "cover_with": "ezzel:", "cover_brand": "Sempertex Europe", "cover_tag": "Indulás…",
    "steps_title": "Az ügyfél előbb jön, mint a logó. 4 dolog, ami először kell", "steps_lead": "Az első fizető ügyfeled előtt:",
    "steps": ["Készségek: egy girland, a megfelelő feszesség, clusterek, amik kibírják a szállítást", "Egy kis munkakészlet: a színek és méretek, amiket a leggyakrabban használsz, plusz inflátor, kézipumpa és lufiméretező", "3 portfóliódarab, nappali fényben, tiszta fal előtt lefotózva", "Egy egyszerű fizetési mód, minden munkánál előleggel"],
    "steps_label": "Az alapok",
    "rule1_label": "Sorrend", "rule1_title": "Költs a helyes sorrendben: képzés és készlet először, a logó utoljára",
    "rule1_body": "Az induláskor a legnagyobb költségkockázat nem a készlet. Hanem a rossz sorrend: logó, névjegy és weboldal, mielőtt egyetlen fizető ügyfeled lenne. Először képzésbe és egy kis munkakészletbe fektess. A branding várhat, amíg tudod, mit kínálsz és ki fizet érte.",
    "rule1_facts": [["1.", "képzés: girland, feszesség, szállítás"], ["2.", "egy kis munkakészlet"], ["3.", "3 portfóliódarab"], ["utoljára", "logó, névjegy, weboldal"]],
    "rule2_label": "Hibák", "rule2_title": "5 hiba, ami a kezdőknek az első évükbe kerül",
    "rule2_body": "A legtöbb új lufiművész nem a technikán bukik el. Hanem ezek egyikén:",
    "alts": [["Minden platform egyszerre", "fiók mindenhol, jelenlét sehol. Előbb 1 platformot tanulj meg."], ["Branding az ügyfelek előtt", "logó, névjegy és weboldal abból a keretből, amiből képzést és készletet kellett volna venni."], ["Árversenyzés", "a környék legolcsóbb dekoratőre azokat az ügyfeleket vonzza, akiket senki nem akar."], ["Nincs előleg", "az előleg nélküli munka olyan munka, amit előző nap le lehet mondani."], ["Túl korán feladni", "a vállalkozáshoz idő kell. Az első 30 nap az üzenetküldésről szól, nem a tökéletes girlandról."]],
    "example_label": "Példa", "example_title": "3 portfóliódarab 1 kezdőkészletből",
    "ex_items": [["Organic girland", "R12 és R5 {p0}, {p1}, {p2} és {p3} színben. Az első fotód, és a darab, amit a legtöbb ügyfél kér."], ["Számdekoráció", "ugyanaz a 4 szín egy számkeret körül. Szülinapok és évfordulók, egész évben."], ["Asztaldísz", "3 R12 egy nehezéken, R5 kiegészítőkkel. Kicsi, gyors, és a legkönnyebb első eladás."]],
    "example_body": "Kezdőkészlet: {p0}, {p1}, {p2} és {p3} R12 és R5 méretben, plusz inflátor, kézipumpa és lufiméretező. Minden darabot nappali fényben, tiszta fal előtt fotózz le.",
    "client_label": "Kezdő kérdezi", "client_title": "Mit válaszolsz, ha egy kezdő kérdezi",
    "client_answers": [
        "Igen. Az ügyfél előbb jön, mint a logó. Építs 3 darabot otthon, fotózd le őket nappali fényben, tiszta fal előtt, és szólj az ismerőseidnek, hogy foglalásokat vállalsz. A logó és a weboldal az első fizető ügyfél után jön.",
        "Olyanoktól, akiket már ismersz. Denise, az egyik workshop-oktatónk, a legelső munkáját az apja ismeretségi körén keresztül kapta. Szólj a családnak és a barátoknak, és a helyi fotósoknak, rendezvényhelyszíneknek, virágosoknak és szervezőknek, akiknek az ügyfelei dekorációt keresnek.",
        "Igen, minden munkánál. Az előleg nélküli munkavállalás az 5 hiba egyike, ami pénzbe kerül a kezdőknek. Az előleg megerősíti a dátumot, fedezi a készletet, és kiszűri azokat, akik úgysem foglaltak volna.",
    ],
    "avoid_lead": "Az első 30 napod, 5 lépésben:",
    "steps5": ["Tanulj meg 3 készséget: girland, megfelelő feszesség, szállításbiztos clusterek", "Vegyél kis készletet: a leggyakrabban használt színek és méretek, plusz inflátor, kézipumpa és méretező", "Építs 3 darabot otthon, és fotózd le nappali fényben, tiszta fal előtt", "Válassz 1 platformot, és szólj az ismerőseidnek és 4 féle helyi vállalkozásnak", "Kérj előleget minden munkánál, és ne add fel"],
    "client_body": "Kell a teljes 30 napos terv? A Start Your Balloon Business a Sempertex Europe 2 napos workshopja: technika, az árkalkulátor, ügyfélszerzés és a hivatalos füzet. Időpontok: sempertexeurope.com/events.",
    "cta_label": "Rendelés",
    "s3_cover_a": "Indulás Sempertex-szel:", "s3_cover_b": "előbb a logó", "s3_cover_c": "vs.", "s3_cover_d": "előbb az ügyfél",
    "s3_left": "ELŐBB A LOGÓ", "s3_right": "ELŐBB AZ ÜGYFÉL", "s3_left_meta": "weboldal, névjegy, 0 ügyfél", "s3_right_meta": "3 darab, 1 üzenet, 1 előleg",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "RÉGI", "s3_new_lbl": "ÚJ",
    "s3_old_tags": ["Logó", "Weboldal", "Minden platform"], "s3_new_tags": ["Képzés", "Kis készlet", "3 darab", "Előleg"],
    "s3_new_quote": "“Három darab otthon, egy üzenet az ismerőseimnek, előleg minden munkánál. Első fizető ügyfél 30 napon belül.”", "s3_new_badge": "Első ügyfél 30 nap alatt",
    "s3_changed_bottom": "Ugyanazok a lufik, ugyanazok a kezek.\nMost a helyes sorrendben.",
    "s3_topic_lbl": "MIÉRT", "s3_rule1_topic": "Sorrend", "s3_rule1_old": "Előbb a logó, aztán az ügyfelek",
    "s3_rule1_quote": "“Előbb képzés és készlet. A logó az első fizető ügyfél után jön.”",
    "s3_rule2_topic": "Hibák", "s3_rule2_old": "A környék legolcsóbbja nyer",
    "s3_rule2_quote": "“5 hiba kerül a kezdőknek az első évükbe. Az ár csak az egyik.”",
    "s3_example_lbl": "PÉLDA", "s3_example_quote": "“{p0}, {p1}, {p2} és {p3} R12 és R5 méretben: elég egy girlandhoz, egy számhoz és egy asztaldíszhez.”",
    "s3_client_lbl": "KEZDŐ", "s3_client_topic": "Első ügyfelek",
    "s3_client_quote": "“Az első ügyfeleid már ismernek. Szólj nekik.”",
    "s3_cta_kicker": "Indulj kis készlettel, a helyes sorrendben",
    "garland_lbl": "girland", "stack_lbl": "szám", "centre_lbl": "asztaldísz", "logo_lbl": "logó?", "clients_lbl": "0 ügyfél", "builds_lbl": "3 darab", "stock_lbl": "kezdőkészlet", "tools": ["inflátor", "kézipumpa", "méretező"],
},
"lt": {
    "cover_pills": ["1 klientas per 30 dienų…", "3 portfolio darbai…", "Logotipas vėliau…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Pradžia…",
    "steps_title": "Klientai svarbiau už logotipą. 4 dalykai, kurių reikia pirmiausia", "steps_lead": "Prieš pirmą mokantį klientą:",
    "steps": ["Įgūdžiai: girlianda, tinkamas įtempimas, klasteriai, kurie atlaiko transportavimą", "Mažos darbinės atsargos: spalvos ir dydžiai, kuriuos naudosi dažniausiai, plius pūstuvas, rankinė pompa ir balionų matuoklis", "3 portfolio darbai, nufotografuoti dienos šviesoje prie švarios sienos", "Paprastas būdas gauti apmokėjimą, su avansu už kiekvieną užsakymą"],
    "steps_label": "Pagrindai",
    "rule1_label": "Tvarka", "rule1_title": "Leisk pinigus teisinga tvarka: mokymai ir atsargos pirma, logotipas paskutinis",
    "rule1_body": "Didžiausia išlaidų rizika pradžioje yra ne atsargos. Tai leidimas netinkama tvarka: logotipas, vizitinės ir svetainė, kol dar neturi nė vieno mokančio kliento. Pirmiausia investuok į mokymus ir mažas darbines atsargas. Prekės ženklas gali palaukti, kol žinosi, ką siūlai ir kas už tai moka.",
    "rule1_facts": [["1.", "mokymai: girlianda, įtempimas, transportas"], ["2.", "mažos darbinės atsargos"], ["3.", "3 portfolio darbai"], ["paskutinis", "logotipas, vizitinės, svetainė"]],
    "rule2_label": "Klaidos", "rule2_title": "5 klaidos, kurios pradedantiesiems kainuoja pirmus metus",
    "rule2_body": "Dauguma naujų menininkų suklumpa ne dėl technikos. Jie suklumpa dėl vienos iš šių:",
    "alts": [["Visos platformos iš karto", "paskyra visur, o buvimo niekur. Pirmiausia įvaldyk 1 platformą."], ["Prekės ženklas prieš klientus", "logotipas, vizitinės ir svetainė iš biudžeto, kuris turėjo būti skirtas mokymams ir atsargoms."], ["Konkuravimas kaina", "pigiausias dekoratorius apylinkėje pritraukia klientus, kurių niekas nenori."], ["Be avanso", "užsakymas be avanso yra užsakymas, kurį galima atšaukti dieną prieš."], ["Per anksti pasiduoti", "verslui reikia laiko. Pirmos 30 dienų skirtos žinutėms siųsti, o ne tobulinti girliandas."]],
    "example_label": "Pavyzdys", "example_title": "3 portfolio darbai iš 1 pradinių atsargų",
    "ex_items": [["Organinė girlianda", "R12 ir R5 spalvomis {p0}, {p1}, {p2} ir {p3}. Tavo pirma nuotrauka ir darbas, kurio prašo dauguma klientų."], ["Skaičius iš balionų", "tos pačios 4 spalvos aplink skaičiaus karkasą. Gimtadieniai ir jubiliejai, visus metus."], ["Stalo puošmena", "3 R12 ant svarelio su R5 akcentais. Maža, greita ir lengviausias pirmas pardavimas."]],
    "example_body": "Pradinės atsargos: {p0}, {p1}, {p2} ir {p3} R12 ir R5 dydžiais, plius pūstuvas, rankinė pompa ir balionų matuoklis. Kiekvieną darbą fotografuok dienos šviesoje prie švarios sienos.",
    "client_label": "Klausia pradedantysis", "client_title": "Ką atsakai, kai klausia pradedantysis",
    "client_answers": [
        "Taip. Klientai svarbiau už logotipą. Padaryk 3 darbus namuose, nufotografuok juos dienos šviesoje prie švarios sienos ir pranešk savo aplinkai, kad priimi užsakymus. Logotipas ir svetainė ateina po pirmo mokančio kliento.",
        "Iš žmonių, kuriuos jau pažįsti. Denise, viena mūsų dirbtuvių instruktorių, pirmą užsakymą gavo per savo tėvo pažįstamus. Pasakyk šeimai ir draugams, taip pat vietiniams fotografams, renginių erdvėms, floristams ir planuotojams, kurių klientams reikia dekoracijų.",
        "Taip, už kiekvieną užsakymą. Darbas be avanso yra viena iš 5 klaidų, kurios pradedantiesiems kainuoja pinigus. Avansas patvirtina datą, padengia atsargas ir atsijoja tuos, kurie vis tiek niekada nebūtų užsakę.",
    ],
    "avoid_lead": "Tavo pirmos 30 dienų, 5 žingsniais:",
    "steps5": ["Išmok 3 įgūdžius: girliandą, tinkamą įtempimą, transportui saugius klasterius", "Nusipirk mažas atsargas: dažniausiai naudojamas spalvas ir dydžius, plius pūstuvą, rankinę pompą ir matuoklį", "Padaryk 3 darbus namuose ir nufotografuok dienos šviesoje prie švarios sienos", "Pasirink 1 platformą ir pranešk savo aplinkai bei 4 tipų vietiniams verslams", "Prašyk avanso už kiekvieną užsakymą ir nesustok"],
    "client_body": "Nori viso 30 dienų plano? Start Your Balloon Business yra 2 dienų Sempertex Europe dirbtuvės: technika, kainų skaičiuoklė, klientų paieška ir oficiali knygelė. Datos: sempertexeurope.com/events.",
    "cta_label": "Užsakyti",
    "s3_cover_a": "Pradžia su Sempertex:", "s3_cover_b": "pirma logotipas", "s3_cover_c": "vs.", "s3_cover_d": "pirma klientas",
    "s3_left": "PIRMA LOGOTIPAS", "s3_right": "PIRMA KLIENTAS", "s3_left_meta": "svetainė, vizitinės, 0 klientų", "s3_right_meta": "3 darbai, 1 žinutė, 1 avansas",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "SENA", "s3_new_lbl": "NAUJA",
    "s3_old_tags": ["Logotipas", "Svetainė", "Visos platformos"], "s3_new_tags": ["Mokymai", "Mažos atsargos", "3 darbai", "Avansas"],
    "s3_new_quote": "“Trys darbai namuose, viena žinutė savo aplinkai, avansas už kiekvieną užsakymą. Pirmas mokantis klientas per 30 dienų.”", "s3_new_badge": "1 klientas per 30 dienų",
    "s3_changed_bottom": "Tie patys balionai, tos pačios rankos.\nDabar teisinga tvarka.",
    "s3_topic_lbl": "KODĖL", "s3_rule1_topic": "Tvarka", "s3_rule1_old": "Pirma logotipas, tada klientai",
    "s3_rule1_quote": "“Pirma mokymai ir atsargos. Logotipas ateina po pirmo mokančio kliento.”",
    "s3_rule2_topic": "Klaidos", "s3_rule2_old": "Laimi pigiausias apylinkėje",
    "s3_rule2_quote": "“5 klaidos pradedantiesiems kainuoja pirmus metus. Kaina yra tik viena iš jų.”",
    "s3_example_lbl": "PAVYZDYS", "s3_example_quote": "“{p0}, {p1}, {p2} ir {p3} R12 ir R5 dydžiais: užtenka girliandai, skaičiui ir stalo puošmenai.”",
    "s3_client_lbl": "PRADŽIA", "s3_client_topic": "Pirmi klientai",
    "s3_client_quote": "“Tavo pirmi klientai tave jau pažįsta. Pasakyk jiems.”",
    "s3_cta_kicker": "Pradėk nuo mažų atsargų, teisinga tvarka",
    "garland_lbl": "girlianda", "stack_lbl": "skaičius", "centre_lbl": "stalo puošmena", "logo_lbl": "logotipas?", "clients_lbl": "0 klientų", "builds_lbl": "3 darbai", "stock_lbl": "pradinės atsargos", "tools": ["pūstuvas", "rankinė pompa", "matuoklis"],
},
}

# ---------------------------------------------------------------- VARIANTEN
VARIANTS = {
"nl": {
  "cover_title": ["Je eerste betalende klant binnen 30 dagen: zo start je een ballonbusiness met Sempertex", "Een ballonbusiness starten? Training en Sempertex voorraad eerst, het logo kan wachten", "Van eerste slinger tot eerste betalende klant: start je ballonbusiness met Sempertex"],
  "cover_sub": ["Training, een kleine voorraad, 3 portfoliostukken en een eenvoudige manier om betaald te worden. De meeste starters boeken binnen 30 dagen gericht werk een eerste betalende klant.", "Waar je eerste klanten echt vandaan komen, de 5 fouten die je vermijdt, en wat je als eerste koopt."],
  "client_question": ["Ik heb nog geen logo of website. Kan ik al boekingen aannemen?", "Waar komen mijn eerste klanten eigenlijk vandaan?", "Het is maar een kleine slinger voor een kennis. Vraag ik dan toch een voorschot?"],
  "s3_old_quote": ["“Ik begin zodra de branding klaar is”", "“Ik post overal en wacht af”", "“Ik ben nog niet goed genoeg om geld te vragen”"],
  "s3_client_old": ["“Ik wacht tot de website live staat”", "“Een voorschot voelt raar voor zo'n kleine opdracht”"],
  "cta_title_tpl": "Bestel je Sempertex startersvoorraad bij {name}", "cta_sub_generic": "4 kleuren in R12 en R5, plus inflator, handpomp en ballonsizer.",
},
"en": {
  "cover_title": ["Your first paying customer within 30 days: how to start a balloon business with Sempertex", "Starting a balloon business? Training and Sempertex stock first, the logo can wait", "From first garland to first paying customer: start your balloon business with Sempertex"],
  "cover_sub": ["Training, a small stock, 3 portfolio builds and a simple way to get paid. Most starters book a first paying client within 30 days of focused work.", "Where your first clients really come from, the 5 mistakes to avoid, and what to buy first."],
  "client_question": ["I don't have a logo or website yet. Can I already take bookings?", "Where do my first customers actually come from?", "It's only a small garland for a friend of a friend. Do I still ask for a deposit?"],
  "s3_old_quote": ["“I'll start once the branding is ready”", "“I'll post everywhere and wait”", "“I'm not good enough to charge yet”"],
  "s3_client_old": ["“I'll wait until the website is live”", "“A deposit feels awkward for a small job”"],
  "cta_title_tpl": "Order your Sempertex starter stock at {name}", "cta_sub_generic": "4 colours in R12 and R5, plus inflator, hand pump and balloon sizer.",
},
"de": {
  "cover_title": ["Dein erster zahlender Kunde in 30 Tagen: So startest du ein Ballongeschäft mit Sempertex", "Ballongeschäft starten? Training und Sempertex Vorrat zuerst, das Logo kann warten", "Von der ersten Girlande zum ersten zahlenden Kunden: Starte dein Ballongeschäft mit Sempertex"],
  "cover_sub": ["Training, ein kleiner Vorrat, 3 Portfolio-Stücke und eine einfache Art, bezahlt zu werden. Die meisten Starter buchen innerhalb von 30 Tagen gezielter Arbeit einen ersten zahlenden Kunden.", "Woher deine ersten Kunden wirklich kommen, die 5 Fehler, die du vermeidest, und was du zuerst kaufst."],
  "client_question": ["Ich habe noch kein Logo und keine Website. Kann ich trotzdem schon Buchungen annehmen?", "Woher kommen meine ersten Kunden eigentlich?", "Es ist nur eine kleine Girlande für eine Bekannte. Verlange ich trotzdem eine Anzahlung?"],
  "s3_old_quote": ["“Ich starte, sobald das Branding fertig ist”", "“Ich poste überall und warte ab”", "“Ich bin noch nicht gut genug, um Geld zu verlangen”"],
  "s3_client_old": ["“Ich warte, bis die Website online ist”", "“Eine Anzahlung fühlt sich bei so einem kleinen Auftrag komisch an”"],
  "cta_title_tpl": "Bestell deinen Sempertex Startervorrat bei {name}", "cta_sub_generic": "4 Farben in R12 und R5, plus Inflator, Handpumpe und Ballonsizer.",
},
"fr": {
  "cover_title": ["Ton premier client payant en 30 jours : comment lancer une activité ballons avec Sempertex", "Lancer une activité ballons ? Formation et stock Sempertex d'abord, le logo peut attendre", "De la première guirlande au premier client payant : lance ton activité ballons avec Sempertex"],
  "cover_sub": ["Formation, un petit stock, 3 pièces portfolio et une façon simple d'être payé. La plupart des débutants décrochent un premier client payant en 30 jours de travail ciblé.", "D'où viennent vraiment tes premiers clients, les 5 erreurs à éviter, et ce que tu achètes en premier."],
  "client_question": ["Je n'ai pas encore de logo ni de site. Je peux déjà prendre des réservations ?", "D'où viennent mes premiers clients, concrètement ?", "C'est juste une petite guirlande pour une connaissance. Je demande quand même un acompte ?"],
  "s3_old_quote": ["“Je me lance quand le branding sera prêt”", "“Je poste partout et j'attends”", "“Je ne suis pas encore assez bon pour facturer”"],
  "s3_client_old": ["“J'attends que le site soit en ligne”", "“Un acompte, ça fait bizarre pour une si petite commande”"],
  "cta_title_tpl": "Commande ton stock de départ Sempertex chez {name}", "cta_sub_generic": "4 couleurs en R12 et R5, plus gonfleur, pompe à main et calibreur.",
},
"it": {
  "cover_title": ["Il tuo primo cliente pagante in 30 giorni: come avviare un'attività di palloncini con Sempertex", "Avviare un'attività di palloncini? Prima formazione e scorta Sempertex, il logo può aspettare", "Dalla prima ghirlanda al primo cliente pagante: avvia la tua attività di palloncini con Sempertex"],
  "cover_sub": ["Formazione, una piccola scorta, 3 pezzi portfolio e un modo semplice per farti pagare. La maggior parte di chi inizia trova un primo cliente pagante in 30 giorni di lavoro mirato.", "Da dove arrivano davvero i tuoi primi clienti, i 5 errori da evitare, e cosa comprare per primo."],
  "client_question": ["Non ho ancora logo né sito. Posso già accettare prenotazioni?", "Da dove arrivano davvero i miei primi clienti?", "È solo una piccola ghirlanda per una conoscente. Chiedo comunque un acconto?"],
  "s3_old_quote": ["“Parto appena il branding è pronto”", "“Posto ovunque e aspetto”", "“Non sono ancora abbastanza brava per farmi pagare”"],
  "s3_client_old": ["“Aspetto che il sito sia online”", "“Un acconto mi sembra strano per un lavoro così piccolo”"],
  "cta_title_tpl": "Ordina la tua scorta iniziale Sempertex da {name}", "cta_sub_generic": "4 colori in R12 e R5, più gonfiatore, pompa a mano e calibratore.",
},
"pl": {
  "cover_title": ["Twój pierwszy płacący klient w 30 dni: jak założyć biznes balonowy z Sempertex", "Zakładasz biznes balonowy? Najpierw szkolenie i zapas Sempertex, logo może poczekać", "Od pierwszej girlandy do pierwszego płacącego klienta: załóż biznes balonowy z Sempertex"],
  "cover_sub": ["Szkolenie, mały zapas, 3 prace do portfolio i prosty sposób przyjmowania płatności. Większość początkujących zdobywa pierwszego płacącego klienta w 30 dni skupionej pracy.", "Skąd naprawdę biorą się pierwsi klienci, 5 błędów, których unikasz, i co kupić najpierw."],
  "client_question": ["Nie mam jeszcze logo ani strony. Mogę już przyjmować rezerwacje?", "Skąd właściwie biorą się moi pierwsi klienci?", "To tylko mała girlanda dla znajomej znajomej. Czy i tak proszę o zaliczkę?"],
  "s3_old_quote": ["“Zacznę, jak branding będzie gotowy”", "“Będę postować wszędzie i czekać”", "“Nie jestem jeszcze dość dobra, żeby brać pieniądze”"],
  "s3_client_old": ["“Poczekam, aż strona będzie online”", "“Zaliczka przy tak małym zleceniu wydaje się dziwna”"],
  "cta_title_tpl": "Zamów zapas startowy Sempertex w {name}", "cta_sub_generic": "4 kolory w R12 i R5, plus inflator, pompka ręczna i kalibrator.",
},
"el": {
  "cover_title": ["Ο πρώτος σου πελάτης που πληρώνει σε 30 μέρες: πώς ξεκινάς επιχείρηση με μπαλόνια με Sempertex", "Ξεκινάς επιχείρηση με μπαλόνια; Εκπαίδευση και απόθεμα Sempertex πρώτα, το logo μπορεί να περιμένει", "Από την πρώτη γιρλάντα στον πρώτο πελάτη που πληρώνει: ξεκίνα την επιχείρησή σου με Sempertex"],
  "cover_sub": ["Εκπαίδευση, μικρό απόθεμα, 3 κομμάτια portfolio και ένας απλός τρόπος πληρωμής. Οι περισσότεροι αρχάριοι κλείνουν τον πρώτο πελάτη που πληρώνει μέσα σε 30 μέρες στοχευμένης δουλειάς.", "Από πού έρχονται πραγματικά οι πρώτοι σου πελάτες, τα 5 λάθη που αποφεύγεις, και τι αγοράζεις πρώτο."],
  "client_question": ["Δεν έχω ακόμα logo ή site. Μπορώ ήδη να δέχομαι κρατήσεις;", "Από πού έρχονται τελικά οι πρώτοι μου πελάτες;", "Είναι μόνο μια μικρή γιρλάντα για μια γνωστή. Ζητάω και πάλι προκαταβολή;"],
  "s3_old_quote": ["“Ξεκινάω μόλις είναι έτοιμο το branding”", "“Ποστάρω παντού και περιμένω”", "“Δεν είμαι ακόμα αρκετά καλή για να χρεώνω”"],
  "s3_client_old": ["“Περιμένω να βγει το site”", "“Η προκαταβολή μου φαίνεται περίεργη για τόσο μικρή δουλειά”"],
  "cta_title_tpl": "Παράγγειλε το αρχικό σου απόθεμα Sempertex από {name}", "cta_sub_generic": "4 χρώματα σε R12 και R5, συν φουσκωτήρα, τρόμπα χειρός και sizer.",
},
"hu": {
  "cover_title": ["Az első fizető ügyfeled 30 napon belül: így indítasz lufis vállalkozást Sempertex-szel", "Lufis vállalkozást indítasz? Képzés és Sempertex készlet először, a logó ráér", "Az első girlandtól az első fizető ügyfélig: indítsd el a lufis vállalkozásod Sempertex-szel"],
  "cover_sub": ["Képzés, kis készlet, 3 portfóliódarab és egy egyszerű fizetési mód. A legtöbb kezdő 30 nap célzott munkával megszerzi az első fizető ügyfelét.", "Honnan jönnek valójában az első ügyfeleid, az 5 hiba, amit elkerülsz, és mit vegyél meg először."],
  "client_question": ["Még nincs logóm és weboldalam. Vállalhatok már foglalást?", "Honnan jönnek tulajdonképpen az első ügyfeleim?", "Csak egy kis girland egy ismerősnek. Akkor is kérjek előleget?"],
  "s3_old_quote": ["“Akkor kezdek, ha kész a branding”", "“Mindenhova posztolok, és várok”", "“Még nem vagyok elég jó, hogy pénzt kérjek”"],
  "s3_client_old": ["“Megvárom, amíg él a weboldal”", "“Az előleg furcsa egy ilyen kis munkánál”"],
  "cta_title_tpl": "Rendeld a Sempertex kezdőkészleted innen: {name}", "cta_sub_generic": "4 szín R12 és R5 méretben, plusz inflátor, kézipumpa és lufiméretező.",
},
"lt": {
  "cover_title": ["Tavo pirmas mokantis klientas per 30 dienų: kaip pradėti balionų verslą su Sempertex", "Pradedi balionų verslą? Pirma mokymai ir Sempertex atsargos, logotipas gali palaukti", "Nuo pirmos girliandos iki pirmo mokančio kliento: pradėk balionų verslą su Sempertex"],
  "cover_sub": ["Mokymai, mažos atsargos, 3 portfolio darbai ir paprastas būdas gauti apmokėjimą. Dauguma pradedančiųjų pirmą mokantį klientą gauna per 30 dienų kryptingo darbo.", "Iš kur iš tikrųjų ateina pirmi klientai, 5 klaidos, kurių išvengsi, ir ką pirkti pirmiausia."],
  "client_question": ["Dar neturiu logotipo ir svetainės. Ar jau galiu priimti užsakymus?", "Iš kur iš tikrųjų ateina mano pirmi klientai?", "Tai tik maža girlianda pažįstamai. Ar vis tiek prašyti avanso?"],
  "s3_old_quote": ["“Pradėsiu, kai bus paruoštas prekės ženklas”", "“Skelbsiu visur ir lauksiu”", "“Dar nesu pakankamai gera, kad imčiau pinigus”"],
  "s3_client_old": ["“Palauksiu, kol veiks svetainė”", "“Avansas už tokį mažą darbą atrodo keistai”"],
  "cta_title_tpl": "Užsisakyk Sempertex pradines atsargas iš {name}", "cta_sub_generic": "4 spalvos R12 ir R5 dydžiais, plius pūstuvas, rankinė pompa ir matuoklis.",
},
}

CAPTIONS_TPL = {
 "nl": "Een ballonbusiness starten? Klanten komen voor logo's. In deze carousel: de 4 dingen die je eerst nodig hebt (vaardigheden, een kleine werkvoorraad, 3 portfoliostukken en een eenvoudige manier om betaald te worden), waarom je in de juiste volgorde uitgeeft, de 5 fouten die starters hun eerste jaar kosten, en waar je eerste klanten echt vandaan komen. De meeste starters boeken binnen 30 dagen gericht werk een eerste betalende klant.\n\nBestel je Sempertex startersvoorraad bij {domain}.\n\n#ballonbusiness #startyourballoonbusiness #sempertex #{tag} #ballondecoratie #ballonartiest",
 "en": "Starting a balloon business? Customers come before logos. In this carousel: the 4 things you need first (skills, a small working stock, 3 portfolio builds and a simple way to get paid), why you spend in the right order, the 5 mistakes that cost starters their first year, and where your first clients really come from. Most starters book a first paying client within 30 days of focused work.\n\nOrder your Sempertex starter stock at {domain}.\n\n#balloonbusiness #startyourballoonbusiness #sempertex #{tag} #balloondecor #balloonartist",
 "de": "Ballongeschäft starten? Kunden kommen vor Logos. Im Carousel: die 4 Dinge, die du zuerst brauchst (Können, ein kleiner Arbeitsvorrat, 3 Portfolio-Stücke und eine einfache Art, bezahlt zu werden), warum du in der richtigen Reihenfolge ausgibst, die 5 Fehler, die Starter ihr erstes Jahr kosten, und woher deine ersten Kunden wirklich kommen. Die meisten Starter buchen innerhalb von 30 Tagen gezielter Arbeit einen ersten zahlenden Kunden.\n\nBestell deinen Sempertex Startervorrat bei {domain}.\n\n#ballongeschäft #startyourballoonbusiness #sempertex #{tag} #ballondeko #ballonkünstler",
 "fr": "Lancer une activité ballons ? Les clients passent avant le logo. Dans ce carrousel : les 4 choses à avoir d'abord (les gestes, un petit stock de travail, 3 pièces portfolio et une façon simple d'être payé), pourquoi dépenser dans le bon ordre, les 5 erreurs qui coûtent leur première année aux débutants, et d'où viennent vraiment tes premiers clients. La plupart des débutants décrochent un premier client payant en 30 jours de travail ciblé.\n\nCommande ton stock de départ Sempertex chez {domain}.\n\n#activiteballons #startyourballoonbusiness #sempertex #{tag} #decorationballons #artisteballon",
 "it": "Avviare un'attività di palloncini? I clienti vengono prima del logo. Nel carosello: le 4 cose che ti servono subito (tecniche, una piccola scorta di lavoro, 3 pezzi portfolio e un modo semplice per farti pagare), perché spendere nell'ordine giusto, i 5 errori che costano il primo anno a chi inizia, e da dove arrivano davvero i tuoi primi clienti. La maggior parte di chi inizia trova un primo cliente pagante in 30 giorni di lavoro mirato.\n\nOrdina la tua scorta iniziale Sempertex da {domain}.\n\n#attivitapalloncini #startyourballoonbusiness #sempertex #{tag} #palloncini #balloonartist",
 "pl": "Zakładasz biznes balonowy? Klienci są ważniejsi niż logo. W karuzeli: 4 rzeczy, które musisz mieć najpierw (umiejętności, mały zapas roboczy, 3 prace do portfolio i prosty sposób przyjmowania płatności), dlaczego wydawać we właściwej kolejności, 5 błędów, które kosztują początkujących pierwszy rok, i skąd naprawdę biorą się pierwsi klienci. Większość początkujących zdobywa pierwszego płacącego klienta w 30 dni skupionej pracy.\n\nZamów zapas startowy Sempertex w {domain}.\n\n#biznesbalonowy #startyourballoonbusiness #sempertex #{tag} #dekoracjebalonowe #artystabalonowy",
 "el": "Ξεκινάς επιχείρηση με μπαλόνια; Οι πελάτες έρχονται πριν από το logo. Στο carousel: τα 4 πράγματα που χρειάζεσαι πρώτα (δεξιότητες, μικρό απόθεμα εργασίας, 3 κομμάτια portfolio και έναν απλό τρόπο πληρωμής), γιατί ξοδεύεις με τη σωστή σειρά, τα 5 λάθη που κοστίζουν στους αρχάριους τον πρώτο χρόνο, και από πού έρχονται πραγματικά οι πρώτοι σου πελάτες. Οι περισσότεροι αρχάριοι κλείνουν τον πρώτο πελάτη που πληρώνει μέσα σε 30 μέρες στοχευμένης δουλειάς.\n\nΠαράγγειλε το αρχικό σου απόθεμα Sempertex από {domain}.\n\n#επιχειρησημπαλονια #startyourballoonbusiness #sempertex #{tag} #μπαλονια #balloonartist",
 "hu": "Lufis vállalkozást indítasz? Az ügyfél előbb jön, mint a logó. A carouselben: a 4 dolog, ami először kell (készségek, kis munkakészlet, 3 portfóliódarab és egy egyszerű fizetési mód), miért költs a helyes sorrendben, az 5 hiba, ami a kezdőknek az első évükbe kerül, és honnan jönnek valójában az első ügyfeleid. A legtöbb kezdő 30 nap célzott munkával megszerzi az első fizető ügyfelét.\n\nRendeld a Sempertex kezdőkészleted innen: {domain}.\n\n#lufisvallalkozas #startyourballoonbusiness #sempertex #{tag} #lufidekoracio #lufiművész",
 "lt": "Pradedi balionų verslą? Klientai svarbiau už logotipą. Karuselėje: 4 dalykai, kurių reikia pirmiausia (įgūdžiai, mažos darbinės atsargos, 3 portfolio darbai ir paprastas būdas gauti apmokėjimą), kodėl leisti pinigus teisinga tvarka, 5 klaidos, kurios pradedantiesiems kainuoja pirmus metus, ir iš kur iš tikrųjų ateina pirmi klientai. Dauguma pradedančiųjų pirmą mokantį klientą gauna per 30 dienų kryptingo darbo.\n\nUžsisakyk Sempertex pradines atsargas iš {domain}.\n\n#balionuverslas #startyourballoonbusiness #sempertex #{tag} #balionai #balionumenininkas",
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

def garland(keys, big=84, small=56, n=6):
    out = '<div style="display:flex;align-items:flex-end;justify-content:center;gap:0">'
    for i in range(n):
        k = keys[i % len(keys)]; s = big if i % 2 == 0 else small
        rotv = (-10, 12, -6, 10, -12, 8, -9)[i % 7]
        out += f'<div style="margin:0 -8px"><div style="transform:rotate({rotv}deg)">{_bl(k, s)}</div></div>'
    return out + '</div>'

def number_stack(keys, size=58, w=170, h=300, ink="#111"):
    """Cijferstack: een kolom ballonnen (groot/klein) rond een dunne frame-lijn, met een voet van 3 kleine."""
    ratio = G["PHOTO_RATIO"]; bh = int(size * ratio)
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    out += f'<div style="position:absolute;left:{w//2-3}px;top:10px;width:6px;height:{h-30}px;background:{ink};opacity:.35;border-radius:3px"></div>'
    y = 0; i = 0
    while y < h - bh - 30:
        s = size if i % 2 == 0 else int(size * .72)
        x = w // 2 - s // 2 + (14 if i % 2 else -14)
        out += f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({(i*53)%40-20}deg)">{_bl(keys[i % len(keys)], s)}</div>'
        y += int(s * ratio * .62); i += 1
    foot = int(size * .62)
    for j, x in enumerate((w//2 - foot - foot//2 - 4, w//2 - foot//2, w//2 + foot//2 + 4)):
        out += f'<div style="position:absolute;left:{x}px;top:{h - int(foot*ratio) - 2}px;transform:rotate({(j-1)*25}deg)">{_bl(keys[(i+j) % len(keys)], foot)}</div>'
    return out + '</div>'

def centrepiece(keys, size=76, w=230, h=250, ink="#111"):
    """Tafelstuk: 3 R12 op korte lintjes naar een voet, met 2 kleine R5-accenten."""
    ratio = G["PHOTO_RATIO"]; bh = int(size * ratio)
    pos = [(int(w*0.06), 30), (int(w*0.5 - size/2), 0), (int(w*0.94 - size), 26)]
    bx0, by0 = w // 2, h - 46
    svg = f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="position:absolute;left:0;top:0">'
    for (x, y) in pos:
        cx, cy = x + size // 2, y + bh - 4
        svg += f'<path d="M{cx} {cy} C {cx} {cy+30}, {bx0} {by0-40}, {bx0} {by0}" fill="none" stroke="{ink}" stroke-width="2.5" stroke-linecap="round" opacity=".8"/>'
    svg += '</svg>'
    out = f'<div style="position:relative;width:{w}px;height:{h}px">{svg}'
    for (x, y), k in zip(pos, keys):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px">{_bl(k, size)}</div>'
    small = int(size * .5)
    out += f'<div style="position:absolute;left:{bx0-small-30}px;top:{by0-int(small*ratio)-6}px;transform:rotate(-20deg)">{_bl(keys[3 % len(keys)], small)}</div>'
    out += f'<div style="position:absolute;left:{bx0+26}px;top:{by0-int(small*ratio)-2}px;transform:rotate(18deg)">{_bl(keys[1 % len(keys)], small)}</div>'
    out += f'<div style="position:absolute;left:{bx0-34}px;top:{by0-2}px;width:68px;height:34px;border-radius:0 0 14px 14px;background:{ink}"></div>'
    out += f'<div style="position:absolute;left:{bx0-60}px;top:{by0+30}px;width:120px;height:8px;border-radius:4px;background:{ink};opacity:.5"></div>'
    return out + '</div>'

def build_lbl(text, ink="#111"):
    return f'<div style="margin-top:10px;text-align:center;font-size:17px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:{ink};opacity:.65;white-space:nowrap">{G["esc"](text)}</div>'

def stock_row(keys, c, size=120, ink="#111"):
    """Startersvoorraad: 4 R12 met naam + code, daaronder 3 chips met het gereedschap."""
    SX = G["SX"]; esc = G["esc"]
    out = '<div style="display:flex;align-items:flex-end;justify-content:center;gap:18px">'
    for k in keys[:4]:
        nm = SX[k]["name"].replace("Fashion ", "").replace("Pastel ", "")
        out += f'<div style="text-align:center">{_bl(k, size)}<div style="font-size:17px;font-weight:700;margin-top:8px;white-space:nowrap">{esc(nm)} <span style="opacity:.6">{SX[k]["code"]}</span></div></div>'
    out += '</div>'
    chips = "".join(f'<span class="tchip" style="border-color:{ink};color:{ink}">{esc(t)}</span>' for t in c["tools"])
    return f'<div>{out}<div style="display:flex;justify-content:center;gap:10px;margin-top:16px;flex-wrap:wrap">{chips}</div></div>'

def logo_first(keys, c, ink="#111"):
    """'Logo eerst': een lege logo-kaart met vraagteken, chips website/kaartjes/elk platform, stempel 0 klanten, en ballonnen die ongebruikt blijven liggen."""
    esc = G["esc"]; w, h = 330, 380
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    out += (f'<div style="position:absolute;left:20px;top:0;width:290px;height:150px;border:4px dashed {ink};border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;opacity:.9">'
            f'<div style="font-size:64px;font-weight:900;line-height:1;color:{ink}">?</div><div style="font-size:20px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:{ink}">{esc(c["logo_lbl"])}</div></div>')
    chips = "".join(f'<span class="tchip" style="border-color:{ink};color:{ink};background:#fff">{esc(t)}</span>' for t in c["s3_old_tags"][1:])
    out += f'<div style="position:absolute;left:0;right:0;top:166px;display:flex;justify-content:center;gap:8px;flex-wrap:wrap">{chips}</div>'
    pos = [(20, 300, 60), (115, 312, 54), (210, 298, 62)]
    for i, (x, y, s) in enumerate(pos):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({(85, 100, 78)[i]}deg);opacity:.9">{_bl(keys[i % len(keys)], s)}</div>'
    out += (f'<div style="position:absolute;left:90px;top:222px;transform:rotate(-6deg);background:#fff;color:#E03131;border:3px solid {ink};'
            f'border-radius:10px;padding:8px 16px;font-size:22px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 4px 0 rgba(0,0,0,.18);white-space:nowrap">{esc(c["clients_lbl"])}</div>')
    return out + '</div>'

def portfolio(keys, c, ink="#111"):
    """'Klant eerst': 3 portfoliostukken (slinger, cijferstack, tafelstuk) met stempel 3 stukken."""
    esc = G["esc"]
    return (f'<div style="position:relative;width:330px;height:380px">'
            f'<div style="position:absolute;left:-10px;top:0;width:350px;transform:scale(.8);transform-origin:top left">{garland(keys, 84, 56, 6)}</div>'
            f'<div style="position:absolute;left:0;top:100px;transform:scale(.78);transform-origin:top left">{number_stack(keys, 58, 170, 300, ink)}</div>'
            f'<div style="position:absolute;left:138px;top:134px;transform:scale(.8);transform-origin:top left">{centrepiece(keys, 76, 230, 250, ink)}</div>'
            f'<div style="position:absolute;left:-6px;top:340px;transform:rotate(-5deg);background:#fff;color:{ink};border:3px solid {ink};border-radius:10px;padding:8px 16px;font-size:22px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 4px 0 rgba(0,0,0,.18);white-space:nowrap">✓ {esc(c["builds_lbl"])}</div></div>')

def three_builds(keys, c, ink="#111", font=None, body_size=21, lbl_size=24, gap=26, vh=230, sc=1.0):
    """Voorbeeldslide: 3 kolommen (slinger, cijferstack, tafelstuk) met titel + regel. vh = hoogte van het visual, sc = schaal."""
    esc = G["esc"]
    vis = [f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center;width:100%"><div style="transform:scale({.95*sc:.2f});transform-origin:bottom center">{garland(keys, 84, 56, 4)}</div></div>',
           f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center"><div style="transform:scale({.75*sc:.2f});transform-origin:bottom center">{number_stack(keys, 58, 170, 300, ink)}</div></div>',
           f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center"><div style="transform:scale({.9*sc:.2f});transform-origin:bottom center">{centrepiece(keys, 76, 230, 250, ink)}</div></div>']
    cols = ""
    for v, (t, body) in zip(vis, c["ex_items"]):
        cols += (f'<div style="flex:1;min-width:0;display:flex;flex-direction:column;align-items:center;gap:10px">{v}'
                 f'<div style="font-size:{body_size}px;line-height:1.3;text-align:center"><b style="font-size:{lbl_size}px;display:block;margin-bottom:4px">{esc(t)}</b>{esc(body)}</div></div>')
    ff = f"font-family:'{font}';" if font else ""
    return f'<div style="{ff}display:flex;gap:{gap}px;align-items:flex-start;width:100%">{cols}</div>'

def mistake_cards(c, cls="alts", title_size=24, body_size=18, font=None):
    """5 fouten als kaarten met nummer, titel en één regel. De 5e kaart spant beide kolommen."""
    esc = G["esc"]
    out = f'<div class="{cls}"' + (f' style="font-family:\'{font}\'"' if font else '') + '>'
    n = len(c["alts"])
    for i, (t, body) in enumerate(c["alts"]):
        span = ' style="grid-column:1/-1"' if (i == n - 1 and n % 2 == 1) else ''
        out += f'<div class="alt"{span}><b style="font-size:{title_size}px"><span class="num">{i+1}</span>{esc(t)}</b><span style="font-size:{body_size}px">{esc(body)}</span></div>'
    return out + '</div>'

def avoid_list(c, cls=""):
    esc = G["esc"]
    return ('<div class="' + cls + '">' + "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps5"])) + '</div>')

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
    L = sum(len(s) for s in c["steps"]); sfs = 26 if L <= 300 else (24 if L <= 335 else 23)
    steps = "".join(f'<div class="step" style="font-size:{sfs}px"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s1">
  <div class="box" style="left:70px;top:120px;width:790px;height:470px">
    <h2 data-fit style="font-size:72px;max-height:380px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:790px;top:60px;transform:scale(.85);transform-origin:top left">{centrepiece([b['hero'], P[0], P[1], P[2]], 76, 230, 250, b['ink'])}</div>
  <div style="position:absolute;left:120px;top:600px">{arrow_svg(b['ink'], 150, 140)}</div>
  <div class="box" style="left:270px;top:610px;width:740px;height:560px;padding:28px 38px">
    <div style="font-size:27px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:470px;padding:44px 50px">
    <h2 data-fit style="font-size:56px;max-height:150px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:26px">{esc(c['rule1_body'])}</div>
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
  <div style="position:absolute;left:80px;right:80px;top:325px;font-size:27px;line-height:1.35" class="body">{esc(c['rule2_body'])}</div>
  <div style="position:absolute;left:70px;right:70px;top:400px">{mistake_cards(c, "alts five", 28, 22, b["ui"])}</div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:690px;padding:36px 30px 30px">
    <h2 data-fit style="font-size:50px;margin-bottom:20px;text-align:center;max-height:120px">{esc(c['example_title'])}</h2>
    {three_builds(P, c, b['ink'], None, 21, 24, 26, 290, 1.18)}
  </div>
  <div class="box" style="left:70px;top:880px;width:940px;padding:22px 46px"><div class="body" style="font-size:23px">{esc(c['example_body'])}</div></div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:54px;max-height:140px">{esc(c['client_title'])}</h2>
  <div class="chat" style="top:320px;min-height:130px;padding-right:120px">{esc(c['client_question'])}<div class="send">↑</div></div>
  <div style="position:absolute;left:80px;right:80px;top:480px;display:flex;flex-direction:column;gap:14px">
    <div class="card" style="position:relative;left:auto;right:auto;padding:20px 32px"><div style="font-size:23px;line-height:1.32">{esc(c['client_answer'])}</div></div>
    <div class="card" style="position:relative;left:auto;right:auto;padding:16px 32px"><div style="font-size:22px;font-weight:{b['body_b']};margin-bottom:2px">{esc(c['avoid_lead'])}</div>{avoid_list(c, 'avoid')}</div>
    <div class="body" style="font-size:18px;line-height:1.3;padding-right:40px">{esc(c['client_body'])}</div>
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
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box"><div style="transform:scale(1.1)">{portfolio(P, c, '#111')}</div></div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px;font-size:26px"><b style="font-size:34px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:740px;width:930px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:340px;padding:20px 24px;box-sizing:border-box;background:#fff;color:#111"><div style="transform:scale(.92)">{stock_row(P, c, 120, '#111')}</div></div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:56px;max-height:160px">{esc(c['rule1_title'])}</h2>
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
    <div class="ph" style="height:auto;padding:26px 30px;box-sizing:border-box;align-items:stretch;background:#fff;color:#111">{mistake_cards(c, 'alts onwhite', 23, 17)}</div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:58px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:auto;padding:24px 24px;box-sizing:border-box;align-items:flex-start;background:#fff;color:#111">{three_builds(P, c, '#111', None, 20, 23, 20, 250, 1.08)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1010px;font-size:23px">{esc(c['example_body'])}</div>
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
      <div style="font-size:21px;line-height:1.32;color:{b['ink']}">{esc(c['client_answer'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:12px 0"></div>
      <div style="font-size:21px;font-weight:{b['body_b']};color:{b['ink']}">{esc(c['avoid_lead'])}</div>
      {avoid_list(c, 'onwhite')}
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1062px;font-size:18px;line-height:1.3">{esc(c['client_body'])}</div>
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
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{logo_first(loud, c, b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{portfolio(P, c, b['ink'])}</div>
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
    <div class="quote" style="font-size:29px">{esc(c['s3_new_quote'])}</div>
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
    vis2 = f'<div style="width:100%">{mistake_cards(c, "alts s3alts", 18, 14)}</div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    t = c['example_title']
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v" style="font-size:{44 if len(t) <= 24 else (36 if len(t) <= 30 else 30)}px">{esc(t)}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:640px;padding:36px 24px;display:flex;align-items:flex-start;justify-content:center">
    {three_builds(P, c, '#111', None, 22, 25, 18, 330, 1.3)}
  </div>
  <div class="bottom" style="top:920px;font-size:29px;font-weight:700">{esc(c['s3_example_quote'])}</div>
  {s3_footer(b)}
</section>""")
    vis6 = (f'<div style="width:100%"><div style="font-size:22px;line-height:1.3;font-style:italic;margin-bottom:12px">{esc(c["client_question"])}</div>'
            f'<div style="font-size:17px;line-height:1.3;margin-bottom:12px">{esc(c["client_answer"])}</div>'
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
.s1 .step{font-size:22px;margin-top:8px;line-height:1.25}
.s1 .avoid .step{font-size:20px;margin-top:6px;line-height:1.22}
.s2 .onwhite .step{color:#111;font-size:18px;margin-top:5px;line-height:1.22}
.s2 .onwhite .step b{color:#6b3fb9}
.s3 .s3steps .step{display:flex;gap:10px;font-size:15px;line-height:1.25;margin-top:5px}
.s3 .s3steps .step b{min-width:24px;font-weight:800}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.facts .fact{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:3px solid #111;border-radius:18px;padding:16px 12px;gap:6px;line-height:1.15}
.facts .fact b{letter-spacing:-.01em;line-height:1;white-space:nowrap}
.facts.onwhite .fact{color:#111}
.facts.s3facts{grid-template-columns:1fr;gap:12px}
.facts.s3facts .fact{border-width:2px;padding:10px 14px;border-radius:14px;align-items:flex-start;text-align:left;gap:3px}
.facts.s3facts .fact b{white-space:normal}
.alts{display:grid;grid-template-columns:1fr 1fr;gap:16px;width:100%}
.alts .alt{display:flex;flex-direction:column;gap:6px;border:3px solid #111;border-radius:18px;padding:18px 22px;background:#fff;line-height:1.3}
.alts .alt b{display:flex;align-items:center;gap:12px;line-height:1.15}
.alts .alt .num{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:#111;color:#fff;font-size:20px;flex:0 0 36px}
.alts.onwhite .alt{color:#111;border-color:#111}
.alts.five{gap:18px}
.alts.five .alt{padding:22px 26px;gap:10px;min-height:222px;justify-content:center}
.alts.five .alt .num{width:42px;height:42px;font-size:23px;flex-basis:42px}
.alts.s3alts{grid-template-columns:1fr;gap:8px}
.alts.s3alts .alt{border-width:2px;padding:8px 14px;border-radius:14px;gap:3px}
.alts.s3alts .alt .num{width:26px;height:26px;font-size:14px;flex-basis:26px}
.tchip{display:inline-block;border:2px solid #111;border-radius:999px;padding:6px 14px;font-size:17px;font-weight:700;white-space:nowrap}
"""
