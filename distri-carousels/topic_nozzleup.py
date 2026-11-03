# -*- coding: utf-8 -*-
"""Topic: 'What is Nozzle Up? Europe's balloon convention explained.'
(sempertexeurope.com/en_GB/blog/what-is-nozzle-up).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=nozzleup.
Uit de blog: Nozzle Up is de ballonconventie van Sempertex Europe; eerste editie 2018 in Duitsland met 52 deelnemers,
daarna naar Nederland en elke editie gegroeid; decorateurs en twisters samen; programma = leren (classes en workshops),
bouwen (live demo's, competities, groepsbuilds) en ontmoeten; avondgala en balloon fashion show; voor iedereen die
professioneel met ballonnen bezig is of dat van plan is (artiesten, decorateurs, twisters, starters, speciaalzaken);
geen jaren ervaring nodig; lessen in het Engels; 2027: 1 tot 3 oktober, Van der Valk Hotel Eindhoven, 8 internationale
teachers (o.a. Ting Yu en Denise van Dooren), thema Enchanted (magische bossen, kamer per kamer), all-inclusive eten en
drinken 3 dagen; ticketverkoop opent 1 oktober 2026; wachtlijst nozzleup.eu/waitinglist; oprichters leerden elkaar
kennen op een conventie in België begin jaren 2000; Sempertex Europe sinds 2011."""

G = {}
def setup(g): G.update(g)

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["1 tot 3 oktober 2027…", "8 teachers…", "Thema: Enchanted…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Nozzle Up…",
    "steps_title": "Nozzle Up: 3 dagen leren, bouwen en ontmoeten in Eindhoven", "steps_lead": "Wat het is, in 4 regels:",
    "steps": ["De ballonconventie van Sempertex Europe, sinds 2018, voor decorateurs én twisters", "3 dagen classes, live demo's, competities en groepsbuilds, met een avondgala en een balloon fashion show", "8 internationale teachers, alle lessen in het Engels", "All-inclusive: eten en drinken voor 3 dagen. Thema 2027: Enchanted"],
    "steps_label": "Wat het is",
    "rule1_label": "In cijfers", "rule1_title": "Leren, bouwen, ontmoeten: Nozzle Up in 4 cijfers",
    "rule1_body": "De eerste editie in 2018 was klein en handgemaakt: 52 deelnemers in Duitsland. Sindsdien is Nozzle Up elke editie gegroeid en naar Nederland verhuisd. Het idee is nooit veranderd: internationale instructeurs, samen bouwen, en collega's uit heel Europa in één zaal. Sofie Vandewyer, CEO van Sempertex Europe, noemt het een warm, liefdevol leerbad voor de ballonartiest.",
    "rule1_facts": [["3", "dagen, 1 tot 3 oktober 2027"], ["8", "internationale teachers"], ["52", "deelnemers bij de eerste editie in 2018"], ["1 okt 2026", "start ticketverkoop"]],
    "rule2_label": "Voor wie", "rule2_title": "Voor wie is Nozzle Up? Voor iedereen die professioneel met ballonnen bezig is, of dat van plan is",
    "rule2_body": "Je hebt geen jaren ervaring nodig. De classes zijn gemaakt voor beginners én ervaren artiesten:",
    "alts": [["Ballonartiesten", "techniek verdiepen bij teachers die je anders alleen online ziet."], ["Decorateurs", "grootschalige installaties en de zakelijke kant van het vak."], ["Twisters", "sinds de eerste editie samen met de decorateurs, niet apart."], ["Starters", "geen jaren ervaring nodig. Je leert sneller in 3 dagen dan in 3 maanden tutorials."], ["Ballonspeciaalzaken", "zie wat je klanten volgend jaar gaan bouwen, en wat ze daarvoor bestellen."]],
    "example_label": "Voorbeeld", "example_title": "Alvast in de sfeer van Enchanted",
    "ex_items": [["Organic boog", "bouw thuis mee: een boog in {p0}, {p1}, {p2} en {p3}, R12 en R5. Zelfde codes als op de conventie."], ["Thema: Enchanted", "magische bossen en mysterieuze avonturen, kamer per kamer. Alles wat gebouwd wordt, is content die je aan je eigen klanten laat zien."]],
    "example_body": "Een vertrekpalet uit het rek van {name}: {p0}, {p1}, {p2} en {p3}. De volledige line-up van teachers, programma en tickets volgt op nozzleup.eu.",
    "client_label": "Collega vraagt", "client_title": "Wat je antwoordt als een collega vraagt",
    "client_answers": [
        "Ja. Nozzle Up is voor iedereen die professioneel met ballonnen bezig is of dat serieus van plan is. De classes zijn gemaakt voor beginners én ervaren artiesten, en je hebt geen jaren ervaring nodig. Starters leren er in 3 dagen meer dan in maanden tutorials.",
        "Alle lessen zijn in het Engels, met deelnemers en teachers van over de hele wereld. Je hoeft dus geen Nederlands te spreken, en je komt collega's tegen uit heel Europa.",
        "Je ticket is all-inclusive: eten en drinken voor de 3 dagen zitten erin, net als de classes, de live demo's, de competities, de groepsbuilds en het avondgala. De verkoop start op 1 oktober 2026, dus zet je op de wachtlijst.",
    ],
    "avoid_lead": "Zo zit je erbij, in 5 stappen:",
    "steps5": ["Schrijf je in op de wachtlijst via nozzleup.eu/waitinglist", "Blokkeer 1 tot 3 oktober 2027 in je agenda", "Koop je ticket vanaf 1 oktober 2026, all-inclusive", "Volg de blog voor de teachers en het programma", "Oefen thuis en neem je vragen mee naar de classes"],
    "client_body": "Onder de 8 teachers: Ting Yu en Sempertex-ambassadeur Denise van Dooren. De volledige line-up staat op nozzleup.eu. Locatie: Van der Valk Hotel Eindhoven.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Sempertex Nozzle Up:", "s3_cover_b": "tutorials thuis", "s3_cover_c": "vs.", "s3_cover_d": "3 dagen live",
    "s3_left": "TUTORIALS THUIS", "s3_right": "3 DAGEN LIVE", "s3_left_meta": "alleen, zelfde trucs", "s3_right_meta": "8 teachers, samen",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["Scherm", "Alleen", "Afkijken"], "s3_new_tags": ["8 teachers", "Live builds", "Competities", "Collega's"],
    "s3_new_quote": "“Drie dagen met teachers die ik anders alleen online zie, en met collega's uit heel Europa. Alles wat we bouwen, neem ik mee naar mijn klanten.”", "s3_new_badge": "1 tot 3 oktober 2027, Eindhoven",
    "s3_changed_bottom": "Zelfde ballonnen, zelfde handen.\nNu met 8 teachers naast je.",
    "s3_topic_lbl": "WAAROM", "s3_rule1_topic": "In cijfers", "s3_rule1_old": "Conventies zijn voor de grote namen",
    "s3_rule1_quote": "“Begonnen met 52 deelnemers in 2018. Elke editie gegroeid, en nog altijd voor iedereen.”",
    "s3_rule2_topic": "Voor wie", "s3_rule2_old": "Eerst goed genoeg worden, dan gaan",
    "s3_rule2_quote": "“Geen jaren ervaring nodig. De classes zijn gemaakt voor beginners én ervaren artiesten.”",
    "s3_example_lbl": "VOORBEELD", "s3_example_quote": "“Thema 2027: Enchanted. Bouw thuis alvast mee in {p0}, {p1}, {p2} en {p3}.”",
    "s3_client_lbl": "COLLEGA", "s3_client_topic": "Je ticket",
    "s3_client_quote": "“Wachtlijst nu, tickets vanaf 1 oktober 2026.”",
    "s3_cta_kicker": "Tot op Nozzle Up, 1 tot 3 oktober 2027",
    "arch_lbl": "organic boog", "theme_lbl": "enchanted", "screen_lbl": "tutorial", "alone_lbl": "alleen", "days_lbl": "3 dagen", "chips": ["8 teachers", "live builds", "all-inclusive"],
},
"en": {
    "cover_pills": ["1 to 3 October 2027…", "8 teachers…", "Theme: Enchanted…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Nozzle Up…",
    "steps_title": "Nozzle Up: 3 days of learning, building and meeting in Eindhoven", "steps_lead": "What it is, in 4 lines:",
    "steps": ["Sempertex Europe's balloon convention, since 2018, for decorators and twisters together", "3 days of classes, live demos, competitions and group builds, with an evening gala and a balloon fashion show", "8 international teachers, every class in English", "All-inclusive: food and drink for 3 days. 2027 theme: Enchanted"],
    "steps_label": "What it is",
    "rule1_label": "In numbers", "rule1_title": "Learn, build, meet: Nozzle Up in 4 numbers",
    "rule1_body": "The first edition in 2018 was small and handmade: 52 participants in Germany. Since then Nozzle Up has grown every edition and moved to the Netherlands. The idea never changed: international instructors, building together, and colleagues from all over Europe in one room. Sofie Vandewyer, CEO of Sempertex Europe, calls it a warm, loving, educational bath for the balloon artist.",
    "rule1_facts": [["3", "days, 1 to 3 October 2027"], ["8", "international teachers"], ["52", "participants at the first edition in 2018"], ["1 Oct 2026", "ticket sales open"]],
    "rule2_label": "Who it's for", "rule2_title": "Who is Nozzle Up for? Anyone professionally involved with balloons, or seriously planning to be",
    "rule2_body": "You don't need years of experience. The classes are built for beginners and experienced artists alike:",
    "alts": [["Balloon artists", "deepen your technique with teachers you otherwise only see online."], ["Decorators", "large-scale installations and the business side of the profession."], ["Twisters", "together with the decorators since the first edition, never a separate track."], ["Starters", "no years of experience needed. You learn more in 3 days than in 3 months of tutorials."], ["Balloon specialty shops", "see what your customers will build next year, and what they'll order for it."]],
    "example_label": "Example", "example_title": "Get in the Enchanted mood already",
    "ex_items": [["Organic arch", "build along at home: an arch in {p0}, {p1}, {p2} and {p3}, R12 and R5. Same codes as at the convention."], ["Theme: Enchanted", "magical forests and mysterious adventures, built room by room. Everything built becomes content you show your own clients."]],
    "example_body": "A starting palette from the shelf at {name}: {p0}, {p1}, {p2} and {p3}. The full line-up of teachers, programme and tickets follows on nozzleup.eu.",
    "client_label": "Colleague asks", "client_title": "What you answer when a colleague asks",
    "client_answers": [
        "Yes. Nozzle Up is for anyone professionally involved with balloons or seriously planning to be. The classes are built for beginners and experienced artists alike, and you don't need years of experience. Starters learn more in 3 days than in months of tutorials.",
        "Every class is in English, with participants and teachers from around the world. You don't need a word of Dutch, and you'll meet colleagues from all over Europe.",
        "Your ticket is all-inclusive: food and drink for the 3 days are covered, as are the classes, live demos, competitions, group builds and the evening gala. Sales open on 1 October 2026, so get on the waiting list.",
    ],
    "avoid_lead": "How to be there, in 5 steps:",
    "steps5": ["Join the waiting list at nozzleup.eu/waitinglist", "Block 1 to 3 October 2027 in your diary", "Buy your ticket from 1 October 2026, all-inclusive", "Follow the blog for the teachers and the programme", "Practise at home and bring your questions to the classes"],
    "client_body": "Among the 8 teachers: Ting Yu and Sempertex ambassador Denise van Dooren. The full line-up is on nozzleup.eu. Venue: Van der Valk Hotel Eindhoven.",
    "cta_label": "Order",
    "s3_cover_a": "Sempertex Nozzle Up:", "s3_cover_b": "tutorials at home", "s3_cover_c": "vs.", "s3_cover_d": "3 days live",
    "s3_left": "TUTORIALS AT HOME", "s3_right": "3 DAYS LIVE", "s3_left_meta": "alone, same tricks", "s3_right_meta": "8 teachers, together",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["Screen", "Alone", "Copying"], "s3_new_tags": ["8 teachers", "Live builds", "Competitions", "Colleagues"],
    "s3_new_quote": "“Three days with teachers I otherwise only see online, and colleagues from all over Europe. Everything we build, I take home to my clients.”", "s3_new_badge": "1 to 3 October 2027, Eindhoven",
    "s3_changed_bottom": "Same balloons, same hands.\nNow with 8 teachers beside you.",
    "s3_topic_lbl": "WHY", "s3_rule1_topic": "In numbers", "s3_rule1_old": "Conventions are for the big names",
    "s3_rule1_quote": "“Started with 52 participants in 2018. Grown every edition, and still for everyone.”",
    "s3_rule2_topic": "Who it's for", "s3_rule2_old": "Get good enough first, then go",
    "s3_rule2_quote": "“No years of experience needed. The classes are built for beginners and experienced artists alike.”",
    "s3_example_lbl": "EXAMPLE", "s3_example_quote": "“2027 theme: Enchanted. Build along at home in {p0}, {p1}, {p2} and {p3}.”",
    "s3_client_lbl": "COLLEAGUE", "s3_client_topic": "Your ticket",
    "s3_client_quote": "“Waiting list now, tickets from 1 October 2026.”",
    "s3_cta_kicker": "See you at Nozzle Up, 1 to 3 October 2027",
    "arch_lbl": "organic arch", "theme_lbl": "enchanted", "screen_lbl": "tutorial", "alone_lbl": "alone", "days_lbl": "3 days", "chips": ["8 teachers", "live builds", "all-inclusive"],
},
"de": {
    "cover_pills": ["1. bis 3. Oktober 2027…", "8 Teacher…", "Thema: Enchanted…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Nozzle Up…",
    "steps_title": "Nozzle Up: 3 Tage lernen, bauen und Leute treffen in Eindhoven", "steps_lead": "Was es ist, in 4 Zeilen:",
    "steps": ["Die Ballon-Convention von Sempertex Europe, seit 2018, für Dekorateure und Twister gemeinsam", "3 Tage Classes, Live-Demos, Wettbewerbe und Gruppenbuilds, mit Abendgala und Balloon Fashion Show", "8 internationale Teacher, alle Classes auf Englisch", "All-inclusive: Essen und Getränke für 3 Tage. Thema 2027: Enchanted"],
    "steps_label": "Was es ist",
    "rule1_label": "In Zahlen", "rule1_title": "Lernen, bauen, treffen: Nozzle Up in 4 Zahlen",
    "rule1_body": "Die erste Ausgabe 2018 war klein und handgemacht: 52 Teilnehmer in Deutschland. Seitdem ist Nozzle Up mit jeder Ausgabe gewachsen und in die Niederlande umgezogen. Die Idee blieb dieselbe: internationale Instruktoren, gemeinsam bauen, und Kollegen aus ganz Europa in einem Saal. Sofie Vandewyer, CEO von Sempertex Europe, nennt es ein warmes, liebevolles Lernbad für den Ballonkünstler.",
    "rule1_facts": [["3", "Tage, 1. bis 3. Oktober 2027"], ["8", "internationale Teacher"], ["52", "Teilnehmer bei der ersten Ausgabe 2018"], ["1. Okt 2026", "Start Ticketverkauf"]],
    "rule2_label": "Für wen", "rule2_title": "Für wen ist Nozzle Up? Für alle, die professionell mit Ballons arbeiten oder es ernsthaft vorhaben",
    "rule2_body": "Du brauchst keine jahrelange Erfahrung. Die Classes sind für Anfänger und erfahrene Artisten gemacht:",
    "alts": [["Ballonkünstler", "Technik vertiefen bei Teachern, die du sonst nur online siehst."], ["Dekorateure", "großflächige Installationen und die Geschäftsseite des Berufs."], ["Twister", "seit der ersten Ausgabe zusammen mit den Dekorateuren, nie getrennt."], ["Starter", "keine jahrelange Erfahrung nötig. In 3 Tagen lernst du mehr als in 3 Monaten Tutorials."], ["Ballon-Fachgeschäfte", "sieh, was deine Kunden nächstes Jahr bauen, und was sie dafür bestellen."]],
    "example_label": "Beispiel", "example_title": "Schon mal in Enchanted-Stimmung kommen",
    "ex_items": [["Organic Bogen", "bau zu Hause mit: ein Bogen in {p0}, {p1}, {p2} und {p3}, R12 und R5. Dieselben Codes wie auf der Convention."], ["Thema: Enchanted", "magische Wälder und geheimnisvolle Abenteuer, Raum für Raum gebaut. Alles, was gebaut wird, ist Content für deine eigenen Kunden."]],
    "example_body": "Eine Startpalette aus dem Regal bei {name}: {p0}, {p1}, {p2} und {p3}. Das komplette Line-up aus Teachern, Programm und Tickets folgt auf nozzleup.eu.",
    "client_label": "Kollegin fragt", "client_title": "Was du antwortest, wenn eine Kollegin fragt",
    "client_answers": [
        "Ja. Nozzle Up ist für alle, die professionell mit Ballons arbeiten oder es ernsthaft vorhaben. Die Classes sind für Anfänger und erfahrene Artisten gemacht, und du brauchst keine jahrelange Erfahrung. Starter lernen in 3 Tagen mehr als in Monaten Tutorials.",
        "Alle Classes sind auf Englisch, mit Teilnehmern und Teachern aus der ganzen Welt. Du brauchst kein Wort Niederländisch, und du triffst Kollegen aus ganz Europa.",
        "Dein Ticket ist all-inclusive: Essen und Getränke für die 3 Tage sind drin, genauso wie die Classes, Live-Demos, Wettbewerbe, Gruppenbuilds und die Abendgala. Der Verkauf startet am 1. Oktober 2026, also ab auf die Warteliste.",
    ],
    "avoid_lead": "So bist du dabei, in 5 Schritten:",
    "steps5": ["Trag dich auf die Warteliste ein: nozzleup.eu/waitinglist", "Blockier den 1. bis 3. Oktober 2027 im Kalender", "Kauf dein Ticket ab dem 1. Oktober 2026, all-inclusive", "Folg dem Blog für Teacher und Programm", "Üb zu Hause und bring deine Fragen mit in die Classes"],
    "client_body": "Unter den 8 Teachern: Ting Yu und Sempertex-Botschafterin Denise van Dooren. Das komplette Line-up steht auf nozzleup.eu. Ort: Van der Valk Hotel Eindhoven.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Sempertex Nozzle Up:", "s3_cover_b": "Tutorials zu Hause", "s3_cover_c": "vs.", "s3_cover_d": "3 Tage live",
    "s3_left": "TUTORIALS ZU HAUSE", "s3_right": "3 TAGE LIVE", "s3_left_meta": "allein, gleiche Tricks", "s3_right_meta": "8 Teacher, gemeinsam",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["Bildschirm", "Allein", "Abschauen"], "s3_new_tags": ["8 Teacher", "Live-Builds", "Wettbewerbe", "Kollegen"],
    "s3_new_quote": "“Drei Tage mit Teachern, die ich sonst nur online sehe, und mit Kollegen aus ganz Europa. Alles, was wir bauen, nehme ich mit zu meinen Kunden.”", "s3_new_badge": "1. bis 3. Oktober 2027, Eindhoven",
    "s3_changed_bottom": "Dieselben Ballons, dieselben Hände.\nJetzt mit 8 Teachern neben dir.",
    "s3_topic_lbl": "WARUM", "s3_rule1_topic": "In Zahlen", "s3_rule1_old": "Conventions sind für die großen Namen",
    "s3_rule1_quote": "“Gestartet mit 52 Teilnehmern in 2018. Jede Ausgabe gewachsen, und immer noch für alle.”",
    "s3_rule2_topic": "Für wen", "s3_rule2_old": "Erst gut genug werden, dann hingehen",
    "s3_rule2_quote": "“Keine jahrelange Erfahrung nötig. Die Classes sind für Anfänger und erfahrene Artisten gemacht.”",
    "s3_example_lbl": "BEISPIEL", "s3_example_quote": "“Thema 2027: Enchanted. Bau zu Hause schon mal mit, in {p0}, {p1}, {p2} und {p3}.”",
    "s3_client_lbl": "KOLLEGIN", "s3_client_topic": "Dein Ticket",
    "s3_client_quote": "“Jetzt auf die Warteliste, Tickets ab 1. Oktober 2026.”",
    "s3_cta_kicker": "Bis bald auf der Nozzle Up, 1. bis 3. Oktober 2027",
    "arch_lbl": "Organic Bogen", "theme_lbl": "enchanted", "screen_lbl": "Tutorial", "alone_lbl": "allein", "days_lbl": "3 Tage", "chips": ["8 Teacher", "Live-Builds", "all-inclusive"],
},
"fr": {
    "cover_pills": ["Du 1er au 3 octobre 2027…", "8 teachers…", "Thème : Enchanted…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Nozzle Up…",
    "steps_title": "Nozzle Up : 3 jours pour apprendre, construire et se rencontrer à Eindhoven", "steps_lead": "Ce que c'est, en 4 lignes :",
    "steps": ["La convention ballons de Sempertex Europe, depuis 2018, pour décorateurs et twisters réunis", "3 jours de classes, démos live, concours et constructions collectives, avec un gala du soir et un balloon fashion show", "8 teachers internationaux, toutes les classes en anglais", "All-inclusive : repas et boissons pendant 3 jours. Thème 2027 : Enchanted"],
    "steps_label": "Ce que c'est",
    "rule1_label": "En chiffres", "rule1_title": "Apprendre, construire, rencontrer : Nozzle Up en 4 chiffres",
    "rule1_body": "La première édition en 2018 était petite et faite main : 52 participants en Allemagne. Depuis, Nozzle Up a grandi à chaque édition et s'est installé aux Pays-Bas. L'idée n'a jamais changé : des instructeurs internationaux, construire ensemble, et des collègues de toute l'Europe dans une même salle. Sofie Vandewyer, CEO de Sempertex Europe, parle d'un bain d'apprentissage chaleureux pour l'artiste ballon.",
    "rule1_facts": [["3", "jours, du 1er au 3 octobre 2027"], ["8", "teachers internationaux"], ["52", "participants à la première édition en 2018"], ["1er oct 2026", "ouverture de la billetterie"]],
    "rule2_label": "Pour qui", "rule2_title": "Pour qui est Nozzle Up ? Pour tous ceux qui travaillent le ballon en pro, ou comptent sérieusement le faire",
    "rule2_body": "Pas besoin d'années d'expérience. Les classes sont conçues pour les débutants comme pour les artistes confirmés :",
    "alts": [["Artistes ballon", "approfondir ta technique avec des teachers que tu ne vois sinon qu'en ligne."], ["Décorateurs", "les installations grand format et le côté business du métier."], ["Twisters", "avec les décorateurs depuis la première édition, jamais à part."], ["Débutants", "pas besoin d'années d'expérience. Tu apprends plus en 3 jours qu'en 3 mois de tutos."], ["Boutiques spécialisées", "voir ce que tes clients vont construire l'an prochain, et ce qu'ils commanderont pour ça."]],
    "example_label": "Exemple", "example_title": "Déjà dans l'ambiance Enchanted",
    "ex_items": [["Arche organique", "construis chez toi : une arche en {p0}, {p1}, {p2} et {p3}, R12 et R5. Les mêmes codes qu'à la convention."], ["Thème : Enchanted", "forêts magiques et aventures mystérieuses, construites pièce par pièce. Tout ce qui est construit devient du contenu à montrer à tes propres clients."]],
    "example_body": "Une palette de départ sur l'étagère de {name} : {p0}, {p1}, {p2} et {p3}. Le line-up complet des teachers, le programme et les billets suivent sur nozzleup.eu.",
    "client_label": "Un collègue demande", "client_title": "Ce que tu réponds quand un collègue demande",
    "client_answers": [
        "Oui. Nozzle Up est pour tous ceux qui travaillent le ballon en pro ou comptent sérieusement le faire. Les classes sont conçues pour les débutants comme pour les confirmés, et tu n'as pas besoin d'années d'expérience. Un débutant apprend plus en 3 jours qu'en des mois de tutos.",
        "Toutes les classes sont en anglais, avec des participants et des teachers du monde entier. Pas besoin d'un mot de néerlandais, et tu rencontres des collègues de toute l'Europe.",
        "Ton billet est all-inclusive : repas et boissons pour les 3 jours sont compris, comme les classes, les démos live, les concours, les constructions collectives et le gala du soir. La vente ouvre le 1er octobre 2026, alors inscris-toi sur la liste d'attente.",
    ],
    "avoid_lead": "Pour y être, en 5 étapes :",
    "steps5": ["Inscris-toi sur la liste d'attente : nozzleup.eu/waitinglist", "Bloque du 1er au 3 octobre 2027 dans ton agenda", "Achète ton billet dès le 1er octobre 2026, all-inclusive", "Suis le blog pour les teachers et le programme", "Entraîne-toi chez toi et apporte tes questions en classe"],
    "client_body": "Parmi les 8 teachers : Ting Yu et Denise van Dooren, ambassadrice Sempertex. Le line-up complet est sur nozzleup.eu. Lieu : Van der Valk Hotel Eindhoven.",
    "cta_label": "Commander",
    "s3_cover_a": "Sempertex Nozzle Up :", "s3_cover_b": "tutos à la maison", "s3_cover_c": "vs.", "s3_cover_d": "3 jours en live",
    "s3_left": "TUTOS À LA MAISON", "s3_right": "3 JOURS EN LIVE", "s3_left_meta": "seul, les mêmes trucs", "s3_right_meta": "8 teachers, ensemble",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["Écran", "Seul", "Recopier"], "s3_new_tags": ["8 teachers", "Live builds", "Concours", "Collègues"],
    "s3_new_quote": "“Trois jours avec des teachers que je ne vois sinon qu'en ligne, et des collègues de toute l'Europe. Tout ce qu'on construit, je le ramène à mes clients.”", "s3_new_badge": "Du 1er au 3 octobre 2027, Eindhoven",
    "s3_changed_bottom": "Mêmes ballons, mêmes mains.\nMaintenant avec 8 teachers à côté de toi.",
    "s3_topic_lbl": "POURQUOI", "s3_rule1_topic": "En chiffres", "s3_rule1_old": "Les conventions, c'est pour les grands noms",
    "s3_rule1_quote": "“Parti de 52 participants en 2018. Plus grand à chaque édition, et toujours pour tout le monde.”",
    "s3_rule2_topic": "Pour qui", "s3_rule2_old": "D'abord devenir assez bon, ensuite y aller",
    "s3_rule2_quote": "“Pas besoin d'années d'expérience. Les classes sont faites pour les débutants comme pour les confirmés.”",
    "s3_example_lbl": "EXEMPLE", "s3_example_quote": "“Thème 2027 : Enchanted. Construis déjà chez toi en {p0}, {p1}, {p2} et {p3}.”",
    "s3_client_lbl": "COLLÈGUE", "s3_client_topic": "Ton billet",
    "s3_client_quote": "“Liste d'attente maintenant, billets dès le 1er octobre 2026.”",
    "s3_cta_kicker": "Rendez-vous à Nozzle Up, du 1er au 3 octobre 2027",
    "arch_lbl": "arche organique", "theme_lbl": "enchanted", "screen_lbl": "tuto", "alone_lbl": "seul", "days_lbl": "3 jours", "chips": ["8 teachers", "live builds", "all-inclusive"],
},
"it": {
    "cover_pills": ["Dal 1° al 3 ottobre 2027…", "8 teacher…", "Tema: Enchanted…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "Nozzle Up…",
    "steps_title": "Nozzle Up: 3 giorni per imparare, costruire e incontrarsi a Eindhoven", "steps_lead": "Cos'è, in 4 righe:",
    "steps": ["La convention dei palloncini di Sempertex Europe, dal 2018, per decoratori e twister insieme", "3 giorni di classi, demo dal vivo, competizioni e costruzioni di gruppo, con un gala serale e un balloon fashion show", "8 teacher internazionali, tutte le classi in inglese", "All-inclusive: cibo e bevande per 3 giorni. Tema 2027: Enchanted"],
    "steps_label": "Cos'è",
    "rule1_label": "In numeri", "rule1_title": "Imparare, costruire, incontrare: Nozzle Up in 4 numeri",
    "rule1_body": "La prima edizione nel 2018 era piccola e fatta a mano: 52 partecipanti in Germania. Da allora Nozzle Up è cresciuto a ogni edizione e si è spostato nei Paesi Bassi. L'idea non è mai cambiata: istruttori internazionali, costruire insieme, e colleghi da tutta Europa in una sola sala. Sofie Vandewyer, CEO di Sempertex Europe, lo chiama un bagno di formazione caldo e affettuoso per l'artista del palloncino.",
    "rule1_facts": [["3", "giorni, dal 1° al 3 ottobre 2027"], ["8", "teacher internazionali"], ["52", "partecipanti alla prima edizione nel 2018"], ["1° ott 2026", "apertura biglietteria"]],
    "rule2_label": "Per chi", "rule2_title": "Per chi è Nozzle Up? Per chiunque lavori con i palloncini da professionista, o lo stia seriamente pianificando",
    "rule2_body": "Non servono anni di esperienza. Le classi sono pensate sia per principianti che per artisti esperti:",
    "alts": [["Balloon artist", "approfondire la tecnica con teacher che altrimenti vedi solo online."], ["Decoratori", "installazioni su larga scala e il lato business del mestiere."], ["Twister", "insieme ai decoratori fin dalla prima edizione, mai separati."], ["Chi inizia", "non servono anni di esperienza. In 3 giorni impari più che in 3 mesi di tutorial."], ["Negozi specializzati", "vedi cosa costruiranno i tuoi clienti l'anno prossimo, e cosa ordineranno per farlo."]],
    "example_label": "Esempio", "example_title": "Già nell'atmosfera Enchanted",
    "ex_items": [["Arco organico", "costruisci a casa: un arco in {p0}, {p1}, {p2} e {p3}, R12 e R5. Gli stessi codici della convention."], ["Tema: Enchanted", "foreste magiche e avventure misteriose, costruite stanza per stanza. Tutto ciò che viene costruito diventa contenuto da mostrare ai tuoi clienti."]],
    "example_body": "Una palette di partenza dallo scaffale di {name}: {p0}, {p1}, {p2} e {p3}. La line-up completa di teacher, programma e biglietti segue su nozzleup.eu.",
    "client_label": "Un collega chiede", "client_title": "Cosa rispondi quando un collega chiede",
    "client_answers": [
        "Sì. Nozzle Up è per chiunque lavori con i palloncini da professionista o lo stia seriamente pianificando. Le classi sono pensate per principianti ed esperti, e non servono anni di esperienza. Chi inizia impara più in 3 giorni che in mesi di tutorial.",
        "Tutte le classi sono in inglese, con partecipanti e teacher da tutto il mondo. Non serve una parola di olandese, e incontri colleghi da tutta Europa.",
        "Il biglietto è all-inclusive: cibo e bevande per i 3 giorni sono compresi, come le classi, le demo dal vivo, le competizioni, le costruzioni di gruppo e il gala serale. La vendita apre il 1° ottobre 2026, quindi iscriviti alla lista d'attesa.",
    ],
    "avoid_lead": "Per esserci, in 5 passi:",
    "steps5": ["Iscriviti alla lista d'attesa su nozzleup.eu/waitinglist", "Blocca dal 1° al 3 ottobre 2027 in agenda", "Compra il biglietto dal 1° ottobre 2026, all-inclusive", "Segui il blog per i teacher e il programma", "Allenati a casa e porta le tue domande in classe"],
    "client_body": "Tra gli 8 teacher: Ting Yu e l'ambassador Sempertex Denise van Dooren. La line-up completa è su nozzleup.eu. Sede: Van der Valk Hotel Eindhoven.",
    "cta_label": "Ordina",
    "s3_cover_a": "Sempertex Nozzle Up:", "s3_cover_b": "tutorial a casa", "s3_cover_c": "vs.", "s3_cover_d": "3 giorni dal vivo",
    "s3_left": "TUTORIAL A CASA", "s3_right": "3 GIORNI DAL VIVO", "s3_left_meta": "solo, stessi trucchi", "s3_right_meta": "8 teacher, insieme",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["Schermo", "Da solo", "Copiare"], "s3_new_tags": ["8 teacher", "Live build", "Competizioni", "Colleghi"],
    "s3_new_quote": "“Tre giorni con teacher che altrimenti vedo solo online, e colleghi da tutta Europa. Tutto quello che costruiamo lo porto ai miei clienti.”", "s3_new_badge": "Dal 1° al 3 ottobre 2027, Eindhoven",
    "s3_changed_bottom": "Stessi palloncini, stesse mani.\nOra con 8 teacher accanto a te.",
    "s3_topic_lbl": "PERCHÉ", "s3_rule1_topic": "In numeri", "s3_rule1_old": "Le convention sono per i grandi nomi",
    "s3_rule1_quote": "“Partiti con 52 partecipanti nel 2018. Cresciuti a ogni edizione, e ancora per tutti.”",
    "s3_rule2_topic": "Per chi", "s3_rule2_old": "Prima diventare bravi, poi andare",
    "s3_rule2_quote": "“Non servono anni di esperienza. Le classi sono pensate per principianti ed esperti.”",
    "s3_example_lbl": "ESEMPIO", "s3_example_quote": "“Tema 2027: Enchanted. Costruisci già a casa in {p0}, {p1}, {p2} e {p3}.”",
    "s3_client_lbl": "COLLEGA", "s3_client_topic": "Il tuo biglietto",
    "s3_client_quote": "“Lista d'attesa ora, biglietti dal 1° ottobre 2026.”",
    "s3_cta_kicker": "Ci vediamo a Nozzle Up, dal 1° al 3 ottobre 2027",
    "arch_lbl": "arco organico", "theme_lbl": "enchanted", "screen_lbl": "tutorial", "alone_lbl": "da solo", "days_lbl": "3 giorni", "chips": ["8 teacher", "live build", "all-inclusive"],
},
"pl": {
    "cover_pills": ["1 do 3 października 2027…", "8 teacherów…", "Motyw: Enchanted…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Nozzle Up…",
    "steps_title": "Nozzle Up: 3 dni nauki, budowania i spotkań w Eindhoven", "steps_lead": "Co to jest, w 4 liniach:",
    "steps": ["Konwencja balonowa Sempertex Europe, od 2018, dla dekoratorów i twisterów razem", "3 dni zajęć, pokazów na żywo, konkursów i wspólnych budowli, z wieczorną galą i balloon fashion show", "8 międzynarodowych teacherów, wszystkie zajęcia po angielsku", "All-inclusive: jedzenie i napoje przez 3 dni. Motyw 2027: Enchanted"],
    "steps_label": "Co to jest",
    "rule1_label": "W liczbach", "rule1_title": "Uczyć się, budować, spotykać: Nozzle Up w 4 liczbach",
    "rule1_body": "Pierwsza edycja w 2018 była mała i zrobiona własnymi rękami: 52 uczestników w Niemczech. Od tamtej pory Nozzle Up rośnie z każdą edycją i przeniósł się do Holandii. Pomysł się nie zmienił: międzynarodowi instruktorzy, wspólne budowanie i koledzy z całej Europy w jednej sali. Sofie Vandewyer, CEO Sempertex Europe, nazywa to ciepłą, pełną serca kąpielą edukacyjną dla artysty balonowego.",
    "rule1_facts": [["3", "dni, 1 do 3 października 2027"], ["8", "międzynarodowych teacherów"], ["52", "uczestników pierwszej edycji w 2018"], ["1 paź 2026", "start sprzedaży biletów"]],
    "rule2_label": "Dla kogo", "rule2_title": "Dla kogo jest Nozzle Up? Dla każdego, kto zawodowo pracuje z balonami albo poważnie to planuje",
    "rule2_body": "Nie potrzebujesz lat doświadczenia. Zajęcia są zrobione dla początkujących i doświadczonych artystów:",
    "alts": [["Artyści balonowi", "pogłęb technikę u teacherów, których inaczej widzisz tylko online."], ["Dekoratorzy", "instalacje na dużą skalę i biznesowa strona zawodu."], ["Twisterzy", "razem z dekoratorami od pierwszej edycji, nigdy osobno."], ["Początkujący", "bez lat doświadczenia. W 3 dni nauczysz się więcej niż w 3 miesiące tutoriali."], ["Sklepy balonowe", "zobacz, co twoi klienci zbudują w przyszłym roku i co do tego zamówią."]],
    "example_label": "Przykład", "example_title": "Już teraz w klimacie Enchanted",
    "ex_items": [["Łuk organiczny", "zbuduj w domu: łuk w kolorach {p0}, {p1}, {p2} i {p3}, R12 i R5. Te same kody co na konwencji."], ["Motyw: Enchanted", "magiczne lasy i tajemnicze przygody, budowane pokój po pokoju. Wszystko, co powstanie, to treści, które pokażesz własnym klientom."]],
    "example_body": "Paleta startowa z półki {name}: {p0}, {p1}, {p2} i {p3}. Pełna lista teacherów, program i bilety pojawią się na nozzleup.eu.",
    "client_label": "Koleżanka pyta", "client_title": "Co odpowiadasz, gdy pyta koleżanka",
    "client_answers": [
        "Tak. Nozzle Up jest dla każdego, kto zawodowo pracuje z balonami albo poważnie to planuje. Zajęcia są zrobione dla początkujących i doświadczonych, i nie potrzebujesz lat doświadczenia. Początkujący uczą się tam w 3 dni więcej niż w miesiące tutoriali.",
        "Wszystkie zajęcia są po angielsku, z uczestnikami i teacherami z całego świata. Nie potrzebujesz ani słowa po holendersku, a poznasz kolegów z całej Europy.",
        "Bilet jest all-inclusive: jedzenie i napoje przez 3 dni są w cenie, tak samo zajęcia, pokazy na żywo, konkursy, wspólne budowle i wieczorna gala. Sprzedaż rusza 1 października 2026, więc zapisz się na listę oczekujących.",
    ],
    "avoid_lead": "Jak tam być, w 5 krokach:",
    "steps5": ["Zapisz się na listę oczekujących: nozzleup.eu/waitinglist", "Zablokuj 1 do 3 października 2027 w kalendarzu", "Kup bilet od 1 października 2026, all-inclusive", "Śledź blog, żeby poznać teacherów i program", "Ćwicz w domu i przynieś swoje pytania na zajęcia"],
    "client_body": "Wśród 8 teacherów: Ting Yu i ambasadorka Sempertex Denise van Dooren. Pełna lista na nozzleup.eu. Miejsce: Van der Valk Hotel Eindhoven.",
    "cta_label": "Zamów",
    "s3_cover_a": "Sempertex Nozzle Up:", "s3_cover_b": "tutoriale w domu", "s3_cover_c": "vs.", "s3_cover_d": "3 dni na żywo",
    "s3_left": "TUTORIALE W DOMU", "s3_right": "3 DNI NA ŻYWO", "s3_left_meta": "sam, te same triki", "s3_right_meta": "8 teacherów, razem",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "STARE", "s3_new_lbl": "NOWE",
    "s3_old_tags": ["Ekran", "Sam", "Odtwarzanie"], "s3_new_tags": ["8 teacherów", "Live buildy", "Konkursy", "Koledzy"],
    "s3_new_quote": "“Trzy dni z teacherami, których inaczej widzę tylko online, i z kolegami z całej Europy. Wszystko, co budujemy, zabieram do swoich klientów.”", "s3_new_badge": "1 do 3 października 2027, Eindhoven",
    "s3_changed_bottom": "Te same balony, te same ręce.\nTeraz z 8 teacherami obok ciebie.",
    "s3_topic_lbl": "DLACZEGO", "s3_rule1_topic": "W liczbach", "s3_rule1_old": "Konwencje są dla wielkich nazwisk",
    "s3_rule1_quote": "“Start od 52 uczestników w 2018. Większa z każdą edycją i wciąż dla każdego.”",
    "s3_rule2_topic": "Dla kogo", "s3_rule2_old": "Najpierw być dość dobrym, potem jechać",
    "s3_rule2_quote": "“Bez lat doświadczenia. Zajęcia są zrobione dla początkujących i doświadczonych.”",
    "s3_example_lbl": "PRZYKŁAD", "s3_example_quote": "“Motyw 2027: Enchanted. Zbuduj już w domu w kolorach {p0}, {p1}, {p2} i {p3}.”",
    "s3_client_lbl": "KOLEŻANKA", "s3_client_topic": "Twój bilet",
    "s3_client_quote": "“Lista oczekujących teraz, bilety od 1 października 2026.”",
    "s3_cta_kicker": "Do zobaczenia na Nozzle Up, 1 do 3 października 2027",
    "arch_lbl": "łuk organiczny", "theme_lbl": "enchanted", "screen_lbl": "tutorial", "alone_lbl": "sam", "days_lbl": "3 dni", "chips": ["8 teacherów", "live buildy", "all-inclusive"],
},
"el": {
    "cover_pills": ["1 έως 3 Οκτωβρίου 2027…", "8 teachers…", "Θέμα: Enchanted…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Nozzle Up…",
    "steps_title": "Nozzle Up: 3 μέρες μάθησης, κατασκευής και συναντήσεων στο Eindhoven", "steps_lead": "Τι είναι, σε 4 γραμμές:",
    "steps": ["Το balloon convention της Sempertex Europe, από το 2018, για διακοσμητές και twisters μαζί", "3 μέρες με μαθήματα, live demos, διαγωνισμούς και ομαδικές κατασκευές, με βραδινό gala και balloon fashion show", "8 διεθνείς teachers, όλα τα μαθήματα στα αγγλικά", "All-inclusive: φαγητό και ποτό για 3 μέρες. Θέμα 2027: Enchanted"],
    "steps_label": "Τι είναι",
    "rule1_label": "Σε αριθμούς", "rule1_title": "Μάθε, φτιάξε, γνώρισε: το Nozzle Up σε 4 αριθμούς",
    "rule1_body": "Η πρώτη διοργάνωση το 2018 ήταν μικρή και χειροποίητη: 52 συμμετέχοντες στη Γερμανία. Από τότε το Nozzle Up μεγαλώνει σε κάθε διοργάνωση και μεταφέρθηκε στην Ολλανδία. Η ιδέα δεν άλλαξε ποτέ: διεθνείς εκπαιδευτές, κατασκευή μαζί, και συνάδελφοι από όλη την Ευρώπη σε μία αίθουσα. Η Sofie Vandewyer, CEO της Sempertex Europe, το λέει ένα ζεστό, γεμάτο αγάπη εκπαιδευτικό λουτρό για τον καλλιτέχνη μπαλονιών.",
    "rule1_facts": [["3", "μέρες, 1 έως 3 Οκτωβρίου 2027"], ["8", "διεθνείς teachers"], ["52", "συμμετέχοντες στην πρώτη διοργάνωση το 2018"], ["1 Οκτ 2026", "έναρξη πώλησης εισιτηρίων"]],
    "rule2_label": "Για ποιον", "rule2_title": "Για ποιον είναι το Nozzle Up; Για όποιον ασχολείται επαγγελματικά με μπαλόνια, ή το σχεδιάζει σοβαρά",
    "rule2_body": "Δεν χρειάζεσαι χρόνια εμπειρίας. Τα μαθήματα είναι φτιαγμένα για αρχάριους και έμπειρους καλλιτέχνες:",
    "alts": [["Καλλιτέχνες μπαλονιών", "εμβάθυνε την τεχνική σου με teachers που αλλιώς βλέπεις μόνο online."], ["Διακοσμητές", "κατασκευές μεγάλης κλίμακας και η επιχειρηματική πλευρά του επαγγέλματος."], ["Twisters", "μαζί με τους διακοσμητές από την πρώτη διοργάνωση, ποτέ χωριστά."], ["Αρχάριοι", "χωρίς χρόνια εμπειρίας. Σε 3 μέρες μαθαίνεις περισσότερα από 3 μήνες tutorials."], ["Εξειδικευμένα καταστήματα", "δες τι θα φτιάξουν οι πελάτες σου του χρόνου, και τι θα παραγγείλουν γι' αυτό."]],
    "example_label": "Παράδειγμα", "example_title": "Από τώρα στο κλίμα Enchanted",
    "ex_items": [["Organic αψίδα", "φτιάξε στο σπίτι: μια αψίδα σε {p0}, {p1}, {p2} και {p3}, R12 και R5. Οι ίδιοι κωδικοί όπως στο convention."], ["Θέμα: Enchanted", "μαγικά δάση και μυστηριώδεις περιπέτειες, χτισμένα δωμάτιο με δωμάτιο. Ό,τι φτιάχνεται γίνεται περιεχόμενο που δείχνεις στους δικούς σου πελάτες."]],
    "example_body": "Μια παλέτα εκκίνησης από το ράφι του {name}: {p0}, {p1}, {p2} και {p3}. Η πλήρης λίστα teachers, πρόγραμμα και εισιτήρια ακολουθούν στο nozzleup.eu.",
    "client_label": "Ρωτάει συνάδελφος", "client_title": "Τι απαντάς όταν ρωτάει ένας συνάδελφος",
    "client_answers": [
        "Ναι. Το Nozzle Up είναι για όποιον ασχολείται επαγγελματικά με μπαλόνια ή το σχεδιάζει σοβαρά. Τα μαθήματα είναι φτιαγμένα για αρχάριους και έμπειρους, και δεν χρειάζεσαι χρόνια εμπειρίας. Οι αρχάριοι μαθαίνουν σε 3 μέρες περισσότερα από μήνες tutorials.",
        "Όλα τα μαθήματα είναι στα αγγλικά, με συμμετέχοντες και teachers από όλο τον κόσμο. Δεν χρειάζεσαι ούτε λέξη ολλανδικά, και γνωρίζεις συναδέλφους από όλη την Ευρώπη.",
        "Το εισιτήριο είναι all-inclusive: φαγητό και ποτό για τις 3 μέρες περιλαμβάνονται, όπως και τα μαθήματα, τα live demos, οι διαγωνισμοί, οι ομαδικές κατασκευές και το βραδινό gala. Η πώληση ανοίγει 1 Οκτωβρίου 2026, οπότε μπες στη λίστα αναμονής.",
    ],
    "avoid_lead": "Πώς θα είσαι εκεί, σε 5 βήματα:",
    "steps5": ["Γράψου στη λίστα αναμονής: nozzleup.eu/waitinglist", "Κλείσε 1 έως 3 Οκτωβρίου 2027 στην ατζέντα σου", "Αγόρασε εισιτήριο από 1 Οκτωβρίου 2026, all-inclusive", "Ακολούθησε το blog για teachers και πρόγραμμα", "Εξασκήσου στο σπίτι και φέρε τις ερωτήσεις σου στα μαθήματα"],
    "client_body": "Ανάμεσα στους 8 teachers: η Ting Yu και η Sempertex ambassador Denise van Dooren. Η πλήρης λίστα στο nozzleup.eu. Χώρος: Van der Valk Hotel Eindhoven.",
    "cta_label": "Παραγγελία",
    "s3_cover_a": "Sempertex Nozzle Up:", "s3_cover_b": "tutorials στο σπίτι", "s3_cover_c": "vs.", "s3_cover_d": "3 μέρες live",
    "s3_left": "TUTORIALS ΣΤΟ ΣΠΙΤΙ", "s3_right": "3 ΜΕΡΕΣ LIVE", "s3_left_meta": "μόνος, ίδια κόλπα", "s3_right_meta": "8 teachers, μαζί",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["Οθόνη", "Μόνος", "Αντιγραφή"], "s3_new_tags": ["8 teachers", "Live builds", "Διαγωνισμοί", "Συνάδελφοι"],
    "s3_new_quote": "“Τρεις μέρες με teachers που αλλιώς βλέπω μόνο online, και συναδέλφους από όλη την Ευρώπη. Ό,τι φτιάχνουμε, το παίρνω στους πελάτες μου.”", "s3_new_badge": "1 έως 3 Οκτωβρίου 2027, Eindhoven",
    "s3_changed_bottom": "Ίδια μπαλόνια, ίδια χέρια.\nΤώρα με 8 teachers δίπλα σου.",
    "s3_topic_lbl": "ΓΙΑΤΙ", "s3_rule1_topic": "Σε αριθμούς", "s3_rule1_old": "Τα conventions είναι για τα μεγάλα ονόματα",
    "s3_rule1_quote": "“Ξεκίνησε με 52 συμμετέχοντες το 2018. Μεγαλώνει κάθε φορά, και παραμένει για όλους.”",
    "s3_rule2_topic": "Για ποιον", "s3_rule2_old": "Πρώτα να γίνω αρκετά καλός, μετά πάω",
    "s3_rule2_quote": "“Χωρίς χρόνια εμπειρίας. Τα μαθήματα είναι φτιαγμένα για αρχάριους και έμπειρους.”",
    "s3_example_lbl": "ΠΑΡΑΔΕΙΓΜΑ", "s3_example_quote": "“Θέμα 2027: Enchanted. Φτιάξε από τώρα στο σπίτι σε {p0}, {p1}, {p2} και {p3}.”",
    "s3_client_lbl": "ΣΥΝΑΔΕΛΦΟΣ", "s3_client_topic": "Το εισιτήριό σου",
    "s3_client_quote": "“Λίστα αναμονής τώρα, εισιτήρια από 1 Οκτωβρίου 2026.”",
    "s3_cta_kicker": "Τα λέμε στο Nozzle Up, 1 έως 3 Οκτωβρίου 2027",
    "arch_lbl": "organic αψίδα", "theme_lbl": "enchanted", "screen_lbl": "tutorial", "alone_lbl": "μόνος", "days_lbl": "3 μέρες", "chips": ["8 teachers", "live builds", "all-inclusive"],
},
"hu": {
    "cover_pills": ["2027. október 1-től 3-ig…", "8 teacher…", "Téma: Enchanted…"], "cover_with": "ezzel:", "cover_brand": "Sempertex Europe", "cover_tag": "Nozzle Up…",
    "steps_title": "Nozzle Up: 3 nap tanulás, építés és találkozás Eindhovenben", "steps_lead": "Mi ez, 4 sorban:",
    "steps": ["A Sempertex Europe lufis konvenciója 2018 óta, dekoratőröknek és twistereknek együtt", "3 nap órák, élő bemutatók, versenyek és közös építések, esti gálával és balloon fashion show-val", "8 nemzetközi teacher, minden óra angolul", "All-inclusive: étel és ital 3 napra. 2027-es téma: Enchanted"],
    "steps_label": "Mi ez",
    "rule1_label": "Számokban", "rule1_title": "Tanulj, építs, találkozz: a Nozzle Up 4 számban",
    "rule1_body": "Az első kiadás 2018-ban kicsi és kézzel összerakott volt: 52 résztvevő Németországban. Azóta a Nozzle Up minden kiadással nőtt, és Hollandiába költözött. Az ötlet nem változott: nemzetközi oktatók, közös építés, és kollégák egész Európából egy teremben. Sofie Vandewyer, a Sempertex Europe vezérigazgatója meleg, szeretetteli tanulófürdőnek nevezi a lufiművészek számára.",
    "rule1_facts": [["3", "nap, 2027. október 1-től 3-ig"], ["8", "nemzetközi teacher"], ["52", "résztvevő az első kiadáson 2018-ban"], ["2026. okt. 1.", "jegyértékesítés indul"]],
    "rule2_label": "Kinek", "rule2_title": "Kinek szól a Nozzle Up? Mindenkinek, aki hivatásszerűen foglalkozik lufival, vagy komolyan tervezi",
    "rule2_body": "Nem kell hozzá több év tapasztalat. Az órák kezdőknek és tapasztalt művészeknek egyaránt készültek:",
    "alts": [["Lufiművészek", "mélyítsd a technikád olyan teachereknél, akiket különben csak online látsz."], ["Dekoratőrök", "nagyléptékű installációk és a szakma üzleti oldala."], ["Twisterek", "az első kiadás óta a dekoratőrökkel együtt, sosem külön."], ["Kezdők", "nem kell több év tapasztalat. 3 nap alatt többet tanulsz, mint 3 hónap tutorialból."], ["Lufis szaküzletek", "nézd meg, mit építenek jövőre az ügyfeleid, és mit rendelnek hozzá."]],
    "example_label": "Példa", "example_title": "Már most Enchanted-hangulatban",
    "ex_items": [["Organic ív", "építsd otthon: egy ív {p0}, {p1}, {p2} és {p3} színben, R12 és R5. Ugyanazok a kódok, mint a konvención."], ["Téma: Enchanted", "varázslatos erdők és titokzatos kalandok, teremről teremre felépítve. Minden, ami elkészül, tartalom, amit a saját ügyfeleidnek mutathatsz."]],
    "example_body": "Egy kiindulási paletta a(z) {name} polcáról: {p0}, {p1}, {p2} és {p3}. A teljes teacher-felhozatal, a program és a jegyek a nozzleup.eu oldalon követnek.",
    "client_label": "Kolléga kérdezi", "client_title": "Mit válaszolsz, ha egy kolléga kérdezi",
    "client_answers": [
        "Igen. A Nozzle Up mindenkinek szól, aki hivatásszerűen foglalkozik lufival, vagy komolyan tervezi. Az órák kezdőknek és tapasztaltaknak egyaránt készültek, és nem kell hozzá több év tapasztalat. A kezdők 3 nap alatt többet tanulnak, mint hónapokig tartó tutorialokból.",
        "Minden óra angolul van, résztvevőkkel és teacherekkel a világ minden tájáról. Egy szó holland sem kell, és kollégákkal találkozol egész Európából.",
        "A jegy all-inclusive: a 3 nap étele és itala benne van, ahogy az órák, az élő bemutatók, a versenyek, a közös építések és az esti gála is. Az értékesítés 2026. október 1-jén indul, úgyhogy iratkozz fel a várólistára.",
    ],
    "avoid_lead": "Így leszel ott, 5 lépésben:",
    "steps5": ["Iratkozz fel a várólistára: nozzleup.eu/waitinglist", "Foglald le 2027. október 1-től 3-ig a naptáradban", "Vedd meg a jegyed 2026. október 1-től, all-inclusive", "Kövesd a blogot a teacherekért és a programért", "Gyakorolj otthon, és hozd a kérdéseidet az órákra"],
    "client_body": "A 8 teacher között: Ting Yu és a Sempertex-nagykövet Denise van Dooren. A teljes felhozatal a nozzleup.eu oldalon. Helyszín: Van der Valk Hotel Eindhoven.",
    "cta_label": "Rendelés",
    "s3_cover_a": "Sempertex Nozzle Up:", "s3_cover_b": "tutorial otthon", "s3_cover_c": "vs.", "s3_cover_d": "3 nap élőben",
    "s3_left": "TUTORIAL OTTHON", "s3_right": "3 NAP ÉLŐBEN", "s3_left_meta": "egyedül, régi trükkök", "s3_right_meta": "8 teacher, együtt",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "RÉGI", "s3_new_lbl": "ÚJ",
    "s3_old_tags": ["Képernyő", "Egyedül", "Másolás"], "s3_new_tags": ["8 teacher", "Élő építés", "Versenyek", "Kollégák"],
    "s3_new_quote": "“Három nap teacherekkel, akiket különben csak online látok, és kollégákkal egész Európából. Amit építünk, azt hazaviszem az ügyfeleimnek.”", "s3_new_badge": "2027. október 1-től 3-ig, Eindhoven",
    "s3_changed_bottom": "Ugyanazok a lufik, ugyanazok a kezek.\nMost 8 teacherrel melletted.",
    "s3_topic_lbl": "MIÉRT", "s3_rule1_topic": "Számokban", "s3_rule1_old": "A konvenciók a nagy neveknek valók",
    "s3_rule1_quote": "“52 résztvevővel indult 2018-ban. Minden kiadással nőtt, és még mindig mindenkié.”",
    "s3_rule2_topic": "Kinek", "s3_rule2_old": "Előbb elég jó leszek, aztán megyek",
    "s3_rule2_quote": "“Nem kell több év tapasztalat. Az órák kezdőknek és tapasztaltaknak egyaránt készültek.”",
    "s3_example_lbl": "PÉLDA", "s3_example_quote": "“2027-es téma: Enchanted. Építs már otthon {p0}, {p1}, {p2} és {p3} színben.”",
    "s3_client_lbl": "KOLLÉGA", "s3_client_topic": "A jegyed",
    "s3_client_quote": "“Várólista most, jegyek 2026. október 1-től.”",
    "s3_cta_kicker": "Találkozunk a Nozzle Upon, 2027. október 1-től 3-ig",
    "arch_lbl": "organic ív", "theme_lbl": "enchanted", "screen_lbl": "tutorial", "alone_lbl": "egyedül", "days_lbl": "3 nap", "chips": ["8 teacher", "élő építés", "all-inclusive"],
},
"lt": {
    "cover_pills": ["2027 m. spalio 1-3 d.…", "8 teacheriai…", "Tema: Enchanted…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Nozzle Up…",
    "steps_title": "Nozzle Up: 3 dienos mokytis, kurti ir susitikti Eindhovene", "steps_lead": "Kas tai, 4 eilutėmis:",
    "steps": ["Sempertex Europe balionų konvencija nuo 2018 m., dekoratoriams ir twisteriams kartu", "3 dienos pamokų, gyvų demonstracijų, konkursų ir bendrų kūrinių, su vakaro gala ir balloon fashion show", "8 tarptautiniai teacheriai, visos pamokos anglų kalba", "All-inclusive: maistas ir gėrimai 3 dienas. 2027 m. tema: Enchanted"],
    "steps_label": "Kas tai",
    "rule1_label": "Skaičiais", "rule1_title": "Mokykis, kurk, susitik: Nozzle Up 4 skaičiais",
    "rule1_body": "Pirmasis renginys 2018 m. buvo mažas ir rankų darbo: 52 dalyviai Vokietijoje. Nuo tada Nozzle Up auga su kiekvienu renginiu ir persikėlė į Nyderlandus. Idėja nepasikeitė: tarptautiniai instruktoriai, kūrimas kartu ir kolegos iš visos Europos vienoje salėje. Sofie Vandewyer, Sempertex Europe vadovė, vadina tai šilta, meilės kupina mokymosi vonia balionų menininkui.",
    "rule1_facts": [["3", "dienos, 2027 m. spalio 1-3 d."], ["8", "tarptautiniai teacheriai"], ["52", "dalyviai pirmajame renginyje 2018 m."], ["2026 spalio 1", "prasideda bilietų prekyba"]],
    "rule2_label": "Kam", "rule2_title": "Kam skirtas Nozzle Up? Visiems, kurie profesionaliai dirba su balionais arba rimtai tai planuoja",
    "rule2_body": "Nereikia metų patirties. Pamokos sukurtos ir pradedantiesiems, ir patyrusiems menininkams:",
    "alts": [["Balionų menininkai", "gilink techniką pas teacherius, kuriuos kitaip matai tik internete."], ["Dekoratoriai", "didelio masto instaliacijos ir verslo pusė."], ["Twisteriai", "kartu su dekoratoriais nuo pirmo renginio, niekada atskirai."], ["Pradedantieji", "nereikia metų patirties. Per 3 dienas išmoksi daugiau nei per 3 mėnesius tutorialų."], ["Balionų parduotuvės", "pamatyk, ką tavo klientai kurs kitais metais ir ką tam užsisakys."]],
    "example_label": "Pavyzdys", "example_title": "Jau dabar Enchanted nuotaikoje",
    "ex_items": [["Organinė arka", "kurk namuose: arka spalvomis {p0}, {p1}, {p2} ir {p3}, R12 ir R5. Tie patys kodai kaip konvencijoje."], ["Tema: Enchanted", "stebuklingi miškai ir paslaptingi nuotykiai, kuriami kambarys po kambario. Viskas, kas sukuriama, tampa turiniu, kurį rodai savo klientams."]],
    "example_body": "Pradinė paletė iš {name} lentynos: {p0}, {p1}, {p2} ir {p3}. Visas teacherių sąrašas, programa ir bilietai bus nozzleup.eu.",
    "client_label": "Klausia kolegė", "client_title": "Ką atsakai, kai klausia kolegė",
    "client_answers": [
        "Taip. Nozzle Up skirtas visiems, kurie profesionaliai dirba su balionais arba rimtai tai planuoja. Pamokos sukurtos ir pradedantiesiems, ir patyrusiems, o metų patirties nereikia. Pradedantieji per 3 dienas išmoksta daugiau nei per mėnesius tutorialų.",
        "Visos pamokos vyksta anglų kalba, su dalyviais ir teacheriais iš viso pasaulio. Nereikia nė žodžio olandiškai, o sutiksi kolegų iš visos Europos.",
        "Bilietas all-inclusive: maistas ir gėrimai 3 dienas įskaičiuoti, kaip ir pamokos, gyvos demonstracijos, konkursai, bendri kūriniai ir vakaro gala. Prekyba prasideda 2026 m. spalio 1 d., tad užsirašyk į laukiančiųjų sąrašą.",
    ],
    "avoid_lead": "Kaip ten būti, 5 žingsniais:",
    "steps5": ["Užsirašyk į laukiančiųjų sąrašą: nozzleup.eu/waitinglist", "Pasižymėk 2027 m. spalio 1-3 d. kalendoriuje", "Pirk bilietą nuo 2026 m. spalio 1 d., all-inclusive", "Sek tinklaraštį dėl teacherių ir programos", "Treniruokis namuose ir atsinešk klausimus į pamokas"],
    "client_body": "Tarp 8 teacherių: Ting Yu ir Sempertex ambasadorė Denise van Dooren. Visas sąrašas nozzleup.eu. Vieta: Van der Valk Hotel Eindhoven.",
    "cta_label": "Užsakyti",
    "s3_cover_a": "Sempertex Nozzle Up:", "s3_cover_b": "tutorialai namuose", "s3_cover_c": "vs.", "s3_cover_d": "3 dienos gyvai",
    "s3_left": "TUTORIALAI NAMUOSE", "s3_right": "3 DIENOS GYVAI", "s3_left_meta": "vienas, seni triukai", "s3_right_meta": "8 teacheriai, kartu",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "SENA", "s3_new_lbl": "NAUJA",
    "s3_old_tags": ["Ekranas", "Vienas", "Kopijavimas"], "s3_new_tags": ["8 teacheriai", "Gyvi kūriniai", "Konkursai", "Kolegos"],
    "s3_new_quote": "“Trys dienos su teacheriais, kuriuos kitaip matau tik internete, ir kolegomis iš visos Europos. Viską, ką kuriame, parsivežu savo klientams.”", "s3_new_badge": "2027 m. spalio 1-3 d., Eindhovenas",
    "s3_changed_bottom": "Tie patys balionai, tos pačios rankos.\nDabar su 8 teacheriais šalia.",
    "s3_topic_lbl": "KODĖL", "s3_rule1_topic": "Skaičiais", "s3_rule1_old": "Konvencijos skirtos dideliems vardams",
    "s3_rule1_quote": "“Prasidėjo nuo 52 dalyvių 2018 m. Auga su kiekvienu renginiu ir vis dar skirta visiems.”",
    "s3_rule2_topic": "Kam", "s3_rule2_old": "Pirma tapsiu pakankamai geras, tada važiuosiu",
    "s3_rule2_quote": "“Nereikia metų patirties. Pamokos sukurtos ir pradedantiesiems, ir patyrusiems.”",
    "s3_example_lbl": "PAVYZDYS", "s3_example_quote": "“2027 m. tema: Enchanted. Kurk jau dabar namuose spalvomis {p0}, {p1}, {p2} ir {p3}.”",
    "s3_client_lbl": "KOLEGĖ", "s3_client_topic": "Tavo bilietas",
    "s3_client_quote": "“Laukiančiųjų sąrašas dabar, bilietai nuo 2026 m. spalio 1 d.”",
    "s3_cta_kicker": "Iki pasimatymo Nozzle Up, 2027 m. spalio 1-3 d.",
    "arch_lbl": "organinė arka", "theme_lbl": "enchanted", "screen_lbl": "tutorialas", "alone_lbl": "vienas", "days_lbl": "3 dienos", "chips": ["8 teacheriai", "gyvi kūriniai", "all-inclusive"],
},
}

# ---------------------------------------------------------------- VARIANTEN
VARIANTS = {
"nl": {
  "cover_title": ["Nozzle Up 2027: de ballonconventie van Sempertex, 1 tot 3 oktober in Eindhoven", "Wat is Nozzle Up? 3 dagen, 8 teachers en heel ballon-Europa in één zaal, met Sempertex", "Van 52 deelnemers in 2018 tot de grootste ballonconventie van Europa: Nozzle Up by Sempertex"],
  "cover_sub": ["Wat Nozzle Up is, wat er gebeurt in 3 dagen, voor wie het is en hoe je erbij bent. Tickets vanaf 1 oktober 2026.", "Leren bij 8 internationale teachers, samen bouwen en collega's uit heel Europa ontmoeten. Thema 2027: Enchanted."],
  "client_question": ["Ik ben pas begonnen. Is Nozzle Up iets voor mij?", "Ik spreek geen Nederlands. Kan ik de lessen volgen?", "Wat zit er precies in het ticket?"],
  "s3_old_quote": ["“Ik leer alles toch wel van YouTube”", "“Conventies zijn voor de pro's”", "“Te ver, te duur, te druk”"],
  "s3_client_old": ["“Ik ga wel als ik goed genoeg ben”", "“Ik wacht op de volgende editie”"],
  "cta_title_tpl": "Bestel je Sempertex ballonnen bij {name}", "cta_sub_generic": "En tot op Nozzle Up 2027, 1 tot 3 oktober in Eindhoven.",
},
"en": {
  "cover_title": ["Nozzle Up 2027: Sempertex's balloon convention, 1 to 3 October in Eindhoven", "What is Nozzle Up? 3 days, 8 teachers and all of balloon Europe in one room, with Sempertex", "From 52 participants in 2018 to Europe's balloon convention: Nozzle Up by Sempertex"],
  "cover_sub": ["What Nozzle Up is, what happens in 3 days, who it's for and how to be there. Tickets from 1 October 2026.", "Learn from 8 international teachers, build together and meet colleagues from all over Europe. 2027 theme: Enchanted."],
  "client_question": ["I've only just started. Is Nozzle Up for me?", "I don't speak Dutch. Can I follow the classes?", "What exactly is included in the ticket?"],
  "s3_old_quote": ["“I learn everything from YouTube anyway”", "“Conventions are for the pros”", "“Too far, too expensive, too busy”"],
  "s3_client_old": ["“I'll go once I'm good enough”", "“I'll wait for the next edition”"],
  "cta_title_tpl": "Order your Sempertex balloons at {name}", "cta_sub_generic": "And see you at Nozzle Up 2027, 1 to 3 October in Eindhoven.",
},
"de": {
  "cover_title": ["Nozzle Up 2027: die Ballon-Convention von Sempertex, 1. bis 3. Oktober in Eindhoven", "Was ist Nozzle Up? 3 Tage, 8 Teacher und ganz Ballon-Europa in einem Saal, mit Sempertex", "Von 52 Teilnehmern 2018 zur Ballon-Convention Europas: Nozzle Up by Sempertex"],
  "cover_sub": ["Was Nozzle Up ist, was in 3 Tagen passiert, für wen es ist und wie du dabei bist. Tickets ab 1. Oktober 2026.", "Lernen bei 8 internationalen Teachern, gemeinsam bauen und Kollegen aus ganz Europa treffen. Thema 2027: Enchanted."],
  "client_question": ["Ich habe gerade erst angefangen. Ist Nozzle Up etwas für mich?", "Ich spreche kein Niederländisch. Kann ich den Classes folgen?", "Was genau ist im Ticket drin?"],
  "s3_old_quote": ["“Ich lerne sowieso alles von YouTube”", "“Conventions sind für die Profis”", "“Zu weit, zu teuer, zu voll”"],
  "s3_client_old": ["“Ich gehe hin, wenn ich gut genug bin”", "“Ich warte auf die nächste Ausgabe”"],
  "cta_title_tpl": "Bestell deine Sempertex Ballons bei {name}", "cta_sub_generic": "Und bis bald auf der Nozzle Up 2027, 1. bis 3. Oktober in Eindhoven.",
},
"fr": {
  "cover_title": ["Nozzle Up 2027 : la convention ballons de Sempertex, du 1er au 3 octobre à Eindhoven", "C'est quoi Nozzle Up ? 3 jours, 8 teachers et toute l'Europe du ballon dans une salle, avec Sempertex", "De 52 participants en 2018 à la convention ballons de l'Europe : Nozzle Up by Sempertex"],
  "cover_sub": ["Ce qu'est Nozzle Up, ce qui se passe en 3 jours, pour qui c'est et comment y être. Billets dès le 1er octobre 2026.", "Apprendre avec 8 teachers internationaux, construire ensemble et rencontrer des collègues de toute l'Europe. Thème 2027 : Enchanted."],
  "client_question": ["Je viens de commencer. Nozzle Up, c'est pour moi ?", "Je ne parle pas néerlandais. Je peux suivre les classes ?", "Qu'est-ce qui est compris dans le billet, exactement ?"],
  "s3_old_quote": ["“J'apprends tout sur YouTube de toute façon”", "“Les conventions, c'est pour les pros”", "“Trop loin, trop cher, trop de monde”"],
  "s3_client_old": ["“J'irai quand je serai assez bon”", "“J'attends la prochaine édition”"],
  "cta_title_tpl": "Commande tes ballons Sempertex chez {name}", "cta_sub_generic": "Et rendez-vous à Nozzle Up 2027, du 1er au 3 octobre à Eindhoven.",
},
"it": {
  "cover_title": ["Nozzle Up 2027: la convention dei palloncini di Sempertex, dal 1° al 3 ottobre a Eindhoven", "Cos'è Nozzle Up? 3 giorni, 8 teacher e tutta l'Europa dei palloncini in una sala, con Sempertex", "Da 52 partecipanti nel 2018 alla convention dei palloncini d'Europa: Nozzle Up by Sempertex"],
  "cover_sub": ["Cos'è Nozzle Up, cosa succede in 3 giorni, per chi è e come esserci. Biglietti dal 1° ottobre 2026.", "Imparare da 8 teacher internazionali, costruire insieme e incontrare colleghi da tutta Europa. Tema 2027: Enchanted."],
  "client_question": ["Ho appena iniziato. Nozzle Up fa per me?", "Non parlo olandese. Posso seguire le classi?", "Cosa è compreso esattamente nel biglietto?"],
  "s3_old_quote": ["“Tanto imparo tutto da YouTube”", "“Le convention sono per i professionisti”", "“Troppo lontano, troppo caro, troppa gente”"],
  "s3_client_old": ["“Ci vado quando sarò abbastanza bravo”", "“Aspetto la prossima edizione”"],
  "cta_title_tpl": "Ordina i tuoi palloncini Sempertex da {name}", "cta_sub_generic": "E ci vediamo a Nozzle Up 2027, dal 1° al 3 ottobre a Eindhoven.",
},
"pl": {
  "cover_title": ["Nozzle Up 2027: konwencja balonowa Sempertex, 1 do 3 października w Eindhoven", "Czym jest Nozzle Up? 3 dni, 8 teacherów i cała balonowa Europa w jednej sali, z Sempertex", "Od 52 uczestników w 2018 do balonowej konwencji Europy: Nozzle Up by Sempertex"],
  "cover_sub": ["Czym jest Nozzle Up, co dzieje się przez 3 dni, dla kogo jest i jak tam być. Bilety od 1 października 2026.", "Nauka u 8 międzynarodowych teacherów, wspólne budowanie i spotkania z kolegami z całej Europy. Motyw 2027: Enchanted."],
  "client_question": ["Dopiero zaczynam. Czy Nozzle Up jest dla mnie?", "Nie mówię po holendersku. Czy nadążę na zajęciach?", "Co dokładnie zawiera bilet?"],
  "s3_old_quote": ["“I tak wszystkiego uczę się z YouTube'a”", "“Konwencje są dla zawodowców”", "“Za daleko, za drogo, za tłoczno”"],
  "s3_client_old": ["“Pojadę, jak będę dość dobra”", "“Poczekam na następną edycję”"],
  "cta_title_tpl": "Zamów balony Sempertex w {name}", "cta_sub_generic": "I do zobaczenia na Nozzle Up 2027, 1 do 3 października w Eindhoven.",
},
"el": {
  "cover_title": ["Nozzle Up 2027: το balloon convention της Sempertex, 1 έως 3 Οκτωβρίου στο Eindhoven", "Τι είναι το Nozzle Up; 3 μέρες, 8 teachers και όλη η Ευρώπη του μπαλονιού σε μία αίθουσα, με Sempertex", "Από 52 συμμετέχοντες το 2018 στο balloon convention της Ευρώπης: Nozzle Up by Sempertex"],
  "cover_sub": ["Τι είναι το Nozzle Up, τι γίνεται σε 3 μέρες, για ποιον είναι και πώς θα είσαι εκεί. Εισιτήρια από 1 Οκτωβρίου 2026.", "Μάθε από 8 διεθνείς teachers, φτιάξε μαζί και γνώρισε συναδέλφους από όλη την Ευρώπη. Θέμα 2027: Enchanted."],
  "client_question": ["Μόλις ξεκίνησα. Είναι το Nozzle Up για μένα;", "Δεν μιλάω ολλανδικά. Μπορώ να παρακολουθήσω τα μαθήματα;", "Τι ακριβώς περιλαμβάνει το εισιτήριο;"],
  "s3_old_quote": ["“Όλα τα μαθαίνω από το YouTube έτσι κι αλλιώς”", "“Τα conventions είναι για τους επαγγελματίες”", "“Πολύ μακριά, πολύ ακριβά, πολύς κόσμος”"],
  "s3_client_old": ["“Θα πάω όταν γίνω αρκετά καλή”", "“Περιμένω την επόμενη διοργάνωση”"],
  "cta_title_tpl": "Παράγγειλε τα μπαλόνια Sempertex σου από {name}", "cta_sub_generic": "Και τα λέμε στο Nozzle Up 2027, 1 έως 3 Οκτωβρίου στο Eindhoven.",
},
"hu": {
  "cover_title": ["Nozzle Up 2027: a Sempertex lufis konvenciója, október 1-től 3-ig Eindhovenben", "Mi az a Nozzle Up? 3 nap, 8 teacher és egész lufis Európa egy teremben, Sempertex-szel", "52 résztvevőtől 2018-ban Európa lufis konvenciójáig: Nozzle Up by Sempertex"],
  "cover_sub": ["Mi az a Nozzle Up, mi történik 3 nap alatt, kinek szól, és hogyan lehetsz ott. Jegyek 2026. október 1-től.", "Tanulj 8 nemzetközi teachertől, építs együtt, és találkozz kollégákkal egész Európából. 2027-es téma: Enchanted."],
  "client_question": ["Most kezdtem. Nekem való a Nozzle Up?", "Nem beszélek hollandul. Tudom követni az órákat?", "Pontosan mit tartalmaz a jegy?"],
  "s3_old_quote": ["“Úgyis mindent a YouTube-ról tanulok”", "“A konvenciók a profiknak valók”", "“Túl messze, túl drága, túl sok ember”"],
  "s3_client_old": ["“Majd megyek, ha elég jó leszek”", "“Megvárom a következő kiadást”"],
  "cta_title_tpl": "Rendeld a Sempertex lufijaidat innen: {name}", "cta_sub_generic": "És találkozunk a Nozzle Up 2027-en, október 1-től 3-ig Eindhovenben.",
},
"lt": {
  "cover_title": ["Nozzle Up 2027: Sempertex balionų konvencija, spalio 1-3 d. Eindhovene", "Kas yra Nozzle Up? 3 dienos, 8 teacheriai ir visa balionų Europa vienoje salėje, su Sempertex", "Nuo 52 dalyvių 2018 m. iki Europos balionų konvencijos: Nozzle Up by Sempertex"],
  "cover_sub": ["Kas yra Nozzle Up, kas vyksta per 3 dienas, kam skirta ir kaip ten būti. Bilietai nuo 2026 m. spalio 1 d.", "Mokykis iš 8 tarptautinių teacherių, kurk kartu ir sutik kolegų iš visos Europos. 2027 m. tema: Enchanted."],
  "client_question": ["Tik pradėjau. Ar Nozzle Up man tinka?", "Nekalbu olandiškai. Ar galėsiu sekti pamokas?", "Kas tiksliai įskaičiuota į bilietą?"],
  "s3_old_quote": ["“Vis tiek visko išmokstu iš YouTube”", "“Konvencijos skirtos profesionalams”", "“Per toli, per brangu, per daug žmonių”"],
  "s3_client_old": ["“Važiuosiu, kai būsiu pakankamai gera”", "“Palauksiu kito renginio”"],
  "cta_title_tpl": "Užsisakyk Sempertex balionus iš {name}", "cta_sub_generic": "Ir iki pasimatymo Nozzle Up 2027, spalio 1-3 d. Eindhovene.",
},
}

CAPTIONS_TPL = {
 "nl": "Nozzle Up is de ballonconventie van Sempertex Europe: 3 dagen leren, bouwen en ontmoeten. Editie 2027: 1 tot 3 oktober in het Van der Valk Hotel Eindhoven, 8 internationale teachers, alle lessen in het Engels, all-inclusive eten en drinken, thema Enchanted. Voor iedereen die professioneel met ballonnen bezig is of dat van plan is, zonder jaren ervaring. Tickets vanaf 1 oktober 2026; zet je op de wachtlijst via nozzleup.eu/waitinglist.\n\nBestel je Sempertex ballonnen bij {domain}.\n\n#nozzleup #nozzleup2027 #sempertex #{tag} #ballonconventie #ballonartiest",
 "en": "Nozzle Up is Sempertex Europe's balloon convention: 3 days of learning, building and meeting. 2027 edition: 1 to 3 October at the Van der Valk Hotel Eindhoven, 8 international teachers, every class in English, all-inclusive food and drink, theme Enchanted. For anyone professionally involved with balloons or planning to be, no years of experience needed. Tickets from 1 October 2026; join the waiting list at nozzleup.eu/waitinglist.\n\nOrder your Sempertex balloons at {domain}.\n\n#nozzleup #nozzleup2027 #sempertex #{tag} #balloonconvention #balloonartist",
 "de": "Nozzle Up ist die Ballon-Convention von Sempertex Europe: 3 Tage lernen, bauen und Leute treffen. Ausgabe 2027: 1. bis 3. Oktober im Van der Valk Hotel Eindhoven, 8 internationale Teacher, alle Classes auf Englisch, all-inclusive Essen und Getränke, Thema Enchanted. Für alle, die professionell mit Ballons arbeiten oder es vorhaben, ohne jahrelange Erfahrung. Tickets ab 1. Oktober 2026; ab auf die Warteliste: nozzleup.eu/waitinglist.\n\nBestell deine Sempertex Ballons bei {domain}.\n\n#nozzleup #nozzleup2027 #sempertex #{tag} #ballonconvention #ballonkünstler",
 "fr": "Nozzle Up, c'est la convention ballons de Sempertex Europe : 3 jours pour apprendre, construire et se rencontrer. Édition 2027 : du 1er au 3 octobre au Van der Valk Hotel Eindhoven, 8 teachers internationaux, toutes les classes en anglais, repas et boissons all-inclusive, thème Enchanted. Pour tous ceux qui travaillent le ballon en pro ou comptent le faire, sans années d'expérience. Billets dès le 1er octobre 2026 ; liste d'attente sur nozzleup.eu/waitinglist.\n\nCommande tes ballons Sempertex chez {domain}.\n\n#nozzleup #nozzleup2027 #sempertex #{tag} #conventionballons #artisteballon",
 "it": "Nozzle Up è la convention dei palloncini di Sempertex Europe: 3 giorni per imparare, costruire e incontrarsi. Edizione 2027: dal 1° al 3 ottobre al Van der Valk Hotel Eindhoven, 8 teacher internazionali, tutte le classi in inglese, cibo e bevande all-inclusive, tema Enchanted. Per chiunque lavori con i palloncini da professionista o lo stia pianificando, senza anni di esperienza. Biglietti dal 1° ottobre 2026; lista d'attesa su nozzleup.eu/waitinglist.\n\nOrdina i tuoi palloncini Sempertex da {domain}.\n\n#nozzleup #nozzleup2027 #sempertex #{tag} #balloonconvention #balloonartist",
 "pl": "Nozzle Up to konwencja balonowa Sempertex Europe: 3 dni nauki, budowania i spotkań. Edycja 2027: 1 do 3 października w Van der Valk Hotel Eindhoven, 8 międzynarodowych teacherów, wszystkie zajęcia po angielsku, jedzenie i napoje all-inclusive, motyw Enchanted. Dla każdego, kto zawodowo pracuje z balonami albo to planuje, bez lat doświadczenia. Bilety od 1 października 2026; lista oczekujących na nozzleup.eu/waitinglist.\n\nZamów balony Sempertex w {domain}.\n\n#nozzleup #nozzleup2027 #sempertex #{tag} #konwencjabalonowa #artystabalonowy",
 "el": "Το Nozzle Up είναι το balloon convention της Sempertex Europe: 3 μέρες μάθησης, κατασκευής και συναντήσεων. Διοργάνωση 2027: 1 έως 3 Οκτωβρίου στο Van der Valk Hotel Eindhoven, 8 διεθνείς teachers, όλα τα μαθήματα στα αγγλικά, φαγητό και ποτό all-inclusive, θέμα Enchanted. Για όποιον ασχολείται επαγγελματικά με μπαλόνια ή το σχεδιάζει, χωρίς χρόνια εμπειρίας. Εισιτήρια από 1 Οκτωβρίου 2026· λίστα αναμονής στο nozzleup.eu/waitinglist.\n\nΠαράγγειλε τα μπαλόνια Sempertex σου από {domain}.\n\n#nozzleup #nozzleup2027 #sempertex #{tag} #balloonconvention #balloonartist",
 "hu": "A Nozzle Up a Sempertex Europe lufis konvenciója: 3 nap tanulás, építés és találkozás. 2027-es kiadás: október 1-től 3-ig a Van der Valk Hotel Eindhovenben, 8 nemzetközi teacher, minden óra angolul, all-inclusive étel és ital, téma: Enchanted. Mindenkinek, aki hivatásszerűen foglalkozik lufival vagy tervezi, több év tapasztalat nélkül. Jegyek 2026. október 1-től; várólista: nozzleup.eu/waitinglist.\n\nRendeld a Sempertex lufijaidat innen: {domain}.\n\n#nozzleup #nozzleup2027 #sempertex #{tag} #lufikonvencio #lufiművész",
 "lt": "Nozzle Up yra Sempertex Europe balionų konvencija: 3 dienos mokytis, kurti ir susitikti. 2027 m. renginys: spalio 1-3 d. Van der Valk Hotel Eindhoven, 8 tarptautiniai teacheriai, visos pamokos anglų kalba, all-inclusive maistas ir gėrimai, tema Enchanted. Visiems, kurie profesionaliai dirba su balionais arba tai planuoja, be metų patirties. Bilietai nuo 2026 m. spalio 1 d.; laukiančiųjų sąrašas nozzleup.eu/waitinglist.\n\nUžsisakyk Sempertex balionus iš {domain}.\n\n#nozzleup #nozzleup2027 #sempertex #{tag} #balionukonvencija #balionumenininkas",
}

# ---------------------------------------------------------------- VISUALS
CUR = {"pal": ["rosewood", "eucalyptus", "greentea", "golddust"]}

def fill_pal(b, c):
    lab = {f"p{i}": G["pal_label"](k, short=False).replace("Fashion ", "").replace("Pastel ", "") for i, k in enumerate(b["pal"][:4])}
    lab["name"] = b["name"]
    def f(v): return v.format(**lab) if isinstance(v, str) and ("{p" in v or "{name}" in v) else v
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
        L = len(n); return num_size if L <= 6 else (int(num_size * .66) if L <= 11 else int(num_size * .5))
    cells = "".join(f'<div class="fact"><b style="font-size:{fs(n)}px">{esc(n)}</b><span style="font-size:{lab_size}px">{esc(l)}</span></div>' for n, l in items)
    return f'<div class="{cls}">{cells}</div>'

def arch(keys, w=330, h=250, n=9, big=74, small=50):
    """Organic boog: ballonnen langs een halve ellips, afwisselend groot en klein."""
    import math
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    cx, cy, rx, ry = w / 2, h - 10, w / 2 - 40, h - 50
    for i in range(n):
        t = math.pi * (1 - i / (n - 1))
        s = big if i % 2 == 0 else small
        x, y = cx + rx * math.cos(t), cy - ry * math.sin(t)
        ang = int(-math.degrees(t) + 90)
        out += f'<div style="position:absolute;left:{int(x - s/2)}px;top:{int(y - s*0.7)}px;transform:rotate({ang}deg)">{_bl(keys[i % len(keys)], s)}</div>'
    return out + '</div>'

def forest(keys, ink="#111", w=250, h=250):
    """Enchanted: een cluster van 4 met kleine 'vuurvliegjes' (R5) eromheen en een maanvormige boog."""
    ratio = G["PHOTO_RATIO"]; size = 90; bh = int(size * ratio)
    cx, cy = w // 2, h // 2 + 20
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    out += f'<div style="position:absolute;left:{cx-95}px;top:{cy-110}px;width:190px;height:190px;border-radius:50%;border:3px dashed {ink};opacity:.35"></div>'
    for k, a in zip(keys[:4], (-40, 40, 140, 220)):
        out += f'<div style="position:absolute;left:{cx - size//2}px;top:{cy - bh}px;transform-origin:50% 100%;transform:rotate({a}deg)">{_bl(k, size)}</div>'
    for i, (x, y) in enumerate(((10, 30), (w-45, 20), (20, h-60), (w-40, h-70), (cx-10, 0))):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({(i*47)%50-25}deg);opacity:.95">{_bl(keys[(i+1) % len(keys)], 30)}</div>'
    return out + '</div>'

def chips_row(items, ink="#111", bg="#fff", small=False):
    esc = G["esc"]; extra = "font-size:15px;padding:4px 10px;" if small else ""
    return '<div style="display:flex;justify-content:center;gap:6px;flex-wrap:wrap">' + "".join(f'<span class="tchip" style="{extra}border-color:{ink};color:{ink};background:{bg}">{esc(t)}</span>' for t in items) + '</div>'

def tutorial_visual(keys, c, ink="#111"):
    """'Tutorials thuis': een scherm met play-knop, 1 ballon ernaast, stempel 'alleen'."""
    esc = G["esc"]; w, h = 330, 380
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    out += (f'<div style="position:absolute;left:20px;top:10px;width:290px;height:180px;border:4px solid {ink};border-radius:16px;background:#fff;display:flex;align-items:center;justify-content:center;opacity:.95">'
            f'<div style="width:0;height:0;border-left:46px solid {ink};border-top:28px solid transparent;border-bottom:28px solid transparent;margin-left:10px;opacity:.75"></div></div>')
    out += f'<div style="position:absolute;left:150px;top:190px;width:30px;height:18px;background:{ink};opacity:.6"></div><div style="position:absolute;left:110px;top:206px;width:110px;height:8px;border-radius:4px;background:{ink};opacity:.6"></div>'
    out += f'<div style="position:absolute;left:0;right:0;top:14px;text-align:center;font-size:15px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:{ink};opacity:.55">{esc(c["screen_lbl"])}</div>'
    out += f'<div style="position:absolute;left:40px;top:240px;transform:rotate(-8deg)">{_bl(keys[0], 80)}</div>'
    out += f'<div style="position:absolute;left:150px;top:300px;transform:rotate(92deg);opacity:.8">{_bl(keys[1 % len(keys)], 54)}</div>'
    out += (f'<div style="position:absolute;left:170px;top:250px;transform:rotate(-6deg);background:#fff;color:#E03131;border:3px solid {ink};'
            f'border-radius:10px;padding:8px 16px;font-size:22px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 4px 0 rgba(0,0,0,.18);white-space:nowrap">{esc(c["alone_lbl"])}</div>')
    return out + '</div>'

def convention_visual(keys, c, ink="#111"):
    """'3 dagen live': grote boog + chips + stempel '3 dagen'."""
    esc = G["esc"]
    return (f'<div style="position:relative;width:330px;height:380px">'
            f'<div style="position:absolute;left:0;top:0;transform:scale(1);transform-origin:top left">{arch(keys, 330, 250, 9, 74, 50)}</div>'
            f'<div style="position:absolute;left:-30px;right:-30px;top:258px">{chips_row(c["chips"], ink, "#fff", True)}</div>'
            f'<div style="position:absolute;left:90px;top:316px;transform:rotate(-4deg);background:#fff;color:{ink};border:3px solid {ink};border-radius:10px;padding:8px 16px;font-size:22px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 4px 0 rgba(0,0,0,.18);white-space:nowrap">✓ {esc(c["days_lbl"])}</div></div>')

def pal_row(keys, size=100):
    SX = G["SX"]; esc = G["esc"]
    out = '<div style="display:flex;align-items:flex-end;justify-content:center;gap:16px">'
    for k in keys[:4]:
        nm = SX[k]["name"].replace("Fashion ", "").replace("Pastel ", "")
        out += f'<div style="text-align:center">{_bl(k, size)}<div style="font-size:16px;font-weight:700;margin-top:6px;white-space:nowrap">{esc(nm)} <span style="opacity:.6">{SX[k]["code"]}</span></div></div>'
    return out + '</div>'

def two_builds(keys, c, ink="#111", body_size=21, lbl_size=24, gap=26, vh=250, sc=1.0):
    """Voorbeeldslide: links organic boog, rechts Enchanted-cluster, elk met titel + regel."""
    esc = G["esc"]
    vis = [f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center;width:100%"><div style="transform:scale({sc:.2f});transform-origin:bottom center">{arch(keys, 330, 250, 9, 74, 50)}</div></div>',
           f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center;width:100%"><div style="transform:scale({sc:.2f});transform-origin:bottom center">{forest(keys, ink)}</div></div>']
    cols = ""
    for v, (t, body) in zip(vis, c["ex_items"]):
        cols += (f'<div style="flex:1;min-width:0;display:flex;flex-direction:column;align-items:center;gap:10px">{v}'
                 f'<div style="font-size:{body_size}px;line-height:1.3;text-align:center"><b style="font-size:{lbl_size}px;display:block;margin-bottom:4px">{esc(t)}</b>{esc(body)}</div></div>')
    return f'<div style="display:flex;gap:{gap}px;align-items:flex-start;width:100%">{cols}</div>'

def who_cards(c, cls="alts", title_size=24, body_size=18, font=None):
    """5 profielen als kaarten met nummer, titel en één regel. De 5e kaart spant beide kolommen."""
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
    L = sum(len(s) for s in c["steps"]); sfs = 26 if L <= 300 else (24 if L <= 345 else 23)
    steps = "".join(f'<div class="step" style="font-size:{sfs}px"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s1">
  <div class="box" style="left:70px;top:120px;width:790px;height:470px">
    <h2 data-fit style="font-size:72px;max-height:380px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:800px;top:40px;transform:scale(.78);transform-origin:top left">{forest([b['hero']] + P[:3], b['ink'])}</div>
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
  <div class="box" style="left:70px;top:160px;width:940px;height:470px;padding:40px 48px">
    <h2 data-fit style="font-size:56px;max-height:140px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:18px;font-size:25px">{esc(c['rule1_body'])}</div>
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
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:50px;max-height:150px">{esc(c['rule2_title'])}</h2>
  <div style="position:absolute;left:80px;right:80px;top:325px;font-size:26px;line-height:1.35" class="body">{esc(c['rule2_body'])}</div>
  <div style="position:absolute;left:70px;right:70px;top:410px">{who_cards(c, "alts five", 28, 22, b["ui"])}</div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:690px;padding:36px 30px 30px">
    <h2 data-fit style="font-size:50px;margin-bottom:20px;text-align:center;max-height:120px">{esc(c['example_title'])}</h2>
    {two_builds(P, c, b['ink'], 21, 24, 26, 320, 1.22)}
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
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box"><div style="transform:scale(1.1)">{convention_visual(P, c, '#111')}</div></div>
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
  <div class="frame" style="left:80px;top:760px;width:930px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:320px;padding:20px 24px;box-sizing:border-box;background:#fff;color:#111;flex-direction:row;gap:14px;align-items:center;justify-content:center"><div style="transform:scale(.72);transform-origin:center;width:280px;flex:0 0 280px">{arch(P, 330, 250, 9, 74, 50)}</div><div style="flex:0 0 auto">{pal_row(P, 76)}</div></div>
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
  <div class="body" style="position:absolute;left:70px;right:70px;top:860px;font-size:24px">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:50px;max-height:150px">{esc(c['rule2_title'])}</h2>
  <div class="body" style="position:absolute;left:70px;right:70px;top:330px;font-size:25px">{esc(c['rule2_body'])}</div>
  <div class="frame" style="left:70px;top:420px;width:940px;transform:rotate({rot(b,1)}deg)">
    <div class="ph" style="height:auto;padding:26px 30px;box-sizing:border-box;align-items:stretch;background:#fff;color:#111">{who_cards(c, 'alts onwhite', 23, 17)}</div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:58px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:auto;padding:24px 24px;box-sizing:border-box;align-items:flex-start;background:#fff;color:#111">{two_builds(P, c, '#111', 20, 23, 20, 280, 1.1)}</div>
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
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{tutorial_visual(loud, c, b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{convention_visual(P, c, b['ink'])}</div>
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
    <div class="quote" style="font-size:28px">{esc(c['s3_new_quote'])}</div>
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
    vis1 = f'<div style="width:100%">{facts_grid(c["rule1_facts"], "facts s3facts", 34, 17)}</div>'
    S.append(topic_slide(c["s3_rule1_topic"], c["s3_rule1_old"], vis1, c["s3_rule1_quote"]))
    vis2 = f'<div style="width:100%">{who_cards(c, "alts s3alts", 18, 14)}</div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    t = c['example_title']
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v" style="font-size:{44 if len(t) <= 24 else (36 if len(t) <= 30 else 30)}px">{esc(t)}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:640px;padding:36px 24px;display:flex;align-items:flex-start;justify-content:center">
    {two_builds(P, c, '#111', 22, 25, 18, 360, 1.35)}
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
