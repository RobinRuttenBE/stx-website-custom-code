# Vertaaltabel voor de MBP-pagina (bron: Robins mbp-certification-page.html, Engels).
# Sleutel = tekst zoals hij in de bron staat. Een sleutel met HTML (koppen met een
# gekleurde markering) wordt als geheel vervangen; de rest per tekststuk.
# INJECT = extra markup die niet in de bron staat (knoppen naar /mbp-listing, Robin 27/10/2026).
# Duits met du (zoals mbp-v1 en de rest van de site), Frans met vous.

SOURCE = 'en'
LANGS = ['nl', 'fr', 'de']

KEEP = ['Master Balloon Professional', 'h', 'Sempertex Europe']

PATTERNS = []

# (na deze tekst in de bron, deze markup invoegen)
INJECT = [
    ('<a class="btn btn-ghost" href="#exam">How the exam works</a>',
     '\n        <a class="btn btn-ghost" href="https://www.sempertexeurope.com/mbp-listing">See all MBPs</a>'),
    ('<a class="btn btn-ghost" href="https://www.sempertexeurope.com/events">See the exam dates and register</a>',
     '\n      <a class="btn btn-ghost" href="https://www.sempertexeurope.com/mbp-listing">Find a certified MBP</a>'),
]

T = {
    # ---- koppen met markering (als geheel) ----
    'Become a <span class="hl">Master</span> Balloon Professional': {
        'nl': 'Word een <span class="hl">Master</span> Balloon Professional',
        'fr': 'Devenez <span class="hl">Master</span> Balloon Professional',
        'de': 'Werde <span class="hl">Master</span> Balloon Professional'},
    'What is an <span class="hl">MBP</span>?': {
        'nl': 'Wat is een <span class="hl">MBP</span>?',
        'fr': 'Qu’est-ce qu’un <span class="hl">MBP</span> ?',
        'de': 'Was ist ein <span class="hl">MBP</span>?'},
    'Why certification is <span class="hl">worth it</span>': {
        'nl': 'Waarom certificering <span class="hl">loont</span>',
        'fr': 'Pourquoi la certification <span class="hl">en vaut la peine</span>',
        'de': 'Warum sich die Zertifizierung <span class="hl">lohnt</span>'},
    'Certification is the only proof of your skill a client can check <span class="hl">before</span> they book you.': {
        'nl': 'Certificering is het enige bewijs van je kunnen dat een klant kan nagaan <span class="hl">voor</span> hij je boekt.',
        'fr': 'La certification est la seule preuve de votre savoir-faire qu’un client peut vérifier <span class="hl">avant</span> de vous réserver.',
        'de': 'Die Zertifizierung ist der einzige Nachweis deines Könnens, den ein Kunde prüfen kann, <span class="hl">bevor</span> er dich bucht.'},
    'What you <span class="hl">get</span>': {
        'nl': 'Wat je <span class="hl">krijgt</span>',
        'fr': 'Ce que vous <span class="hl">obtenez</span>',
        'de': 'Was du <span class="hl">bekommst</span>'},
    'Inside the <span class="hl">exam</span>': {
        'nl': 'Zo werkt het <span class="hl">examen</span>',
        'fr': 'L’<span class="hl">examen</span> en détail',
        'de': 'Die <span class="hl">Prüfung</span> im Detail'},
    'How to <span class="hl">register</span>': {
        'nl': 'Zo schrijf je je <span class="hl">in</span>',
        'fr': 'Comment <span class="hl">s’inscrire</span>',
        'de': 'So meldest du dich <span class="hl">an</span>'},
    'Questions, <span class="hl">answered</span>': {
        'nl': 'Vragen, <span class="hl">beantwoord</span>',
        'fr': 'Vos questions, <span class="hl">nos réponses</span>',
        'de': 'Fragen und <span class="hl">Antworten</span>'},
    'Ready to get <span class="hl">certified</span>?': {
        'nl': 'Klaar om je te laten <span class="hl">certificeren</span>?',
        'fr': 'Prêt à vous faire <span class="hl">certifier</span> ?',
        'de': 'Bereit für deine <span class="hl">Zertifizierung</span>?'},

    # ---- hero ----
    'Anyone can call themselves a balloon professional. MBP is how you prove it.': {
        'nl': 'Iedereen kan zich een ballonprofessional noemen. Met MBP bewijs je het.',
        'fr': 'Tout le monde peut se dire professionnel du ballon. Le MBP, c’est la façon de le prouver.',
        'de': 'Jeder kann sich Ballonprofi nennen. Mit MBP beweist du es.'},
    'See exam dates': {'nl': 'Bekijk de examendata', 'fr': 'Voir les dates d’examen', 'de': 'Prüfungstermine ansehen'},
    'How the exam works': {'nl': 'Zo werkt het examen', 'fr': 'Comment se passe l’examen', 'de': 'So läuft die Prüfung'},
    'See all MBPs': {'nl': 'Bekijk alle MBP’s', 'fr': 'Voir tous les MBP', 'de': 'Alle MBPs ansehen'},
    'Internationally recognised &middot; Exams across Europe': {
        'nl': 'Internationaal erkend &middot; Examens in heel Europa',
        'fr': 'Reconnu à l’international &middot; Examens dans toute l’Europe',
        'de': 'International anerkannt &middot; Prüfungen in ganz Europa'},
    'New Master Balloon Professionals on stage with their diplomas': {
        'nl': 'Nieuwe Master Balloon Professionals op het podium met hun diploma',
        'fr': 'De nouveaux Master Balloon Professionals sur scène avec leur diplôme',
        'de': 'Neue Master Balloon Professionals mit ihrem Diplom auf der Bühne'},
    'New MBPs with their diploma': {'nl': 'Nieuwe MBP’s met hun diploma', 'fr': 'De nouveaux MBP avec leur diplôme', 'de': 'Neue MBPs mit ihrem Diplom'},

    # ---- cijfers ----
    'Points total': {'nl': 'Punten in totaal', 'fr': 'Points au total', 'de': 'Punkte insgesamt'},
    'Needed to pass': {'nl': 'Nodig om te slagen', 'fr': 'Pour réussir', 'de': 'Zum Bestehen'},
    'Exam parts': {'nl': 'Examendelen', 'fr': 'Parties d’examen', 'de': 'Prüfungsteile'},
    'On the day': {'nl': 'Op de dag zelf', 'fr': 'Le jour J', 'de': 'Am Prüfungstag'},

    # ---- wat is MBP ----
    'MBP stands for Master Balloon Professional. It is the internationally recognised Sempertex certification for professional balloon decorators, awarded after you pass a practical exam assessed against the official Sempertex decoration standards.': {
        'nl': 'MBP staat voor Master Balloon Professional. Het is de internationaal erkende Sempertex-certificering voor professionele ballondecorateurs. Je krijgt ze als je slaagt voor een praktijkexamen dat beoordeeld wordt volgens de officiële decoratienormen van Sempertex.',
        'fr': 'MBP signifie Master Balloon Professional. C’est la certification Sempertex reconnue à l’international pour les décorateurs ballons professionnels, délivrée après la réussite d’un examen pratique évalué selon les normes de décoration officielles de Sempertex.',
        'de': 'MBP steht für Master Balloon Professional. Es ist die international anerkannte Sempertex-Zertifizierung für professionelle Ballondekorateure. Du erhältst sie, wenn du eine praktische Prüfung bestehst, die nach den offiziellen Dekorationsstandards von Sempertex bewertet wird.'},
    'It covers three things at once: creativity, technical execution, and the business knowledge behind a professional job. You do not submit a portfolio. You build, in the room, in front of a jury, within the time given.': {
        'nl': 'Het examen toetst drie dingen tegelijk: creativiteit, technische uitvoering en de zakelijke kennis achter een professionele opdracht. Je stuurt geen portfolio in. Je bouwt, ter plaatse, voor een jury, binnen de gegeven tijd.',
        'fr': 'Il couvre trois choses à la fois : la créativité, l’exécution technique et les connaissances commerciales derrière un travail professionnel. Vous n’envoyez pas de portfolio. Vous construisez, sur place, devant un jury, dans le temps imparti.',
        'de': 'Sie deckt drei Dinge auf einmal ab: Kreativität, technische Ausführung und das betriebswirtschaftliche Wissen hinter einem professionellen Auftrag. Du reichst kein Portfolio ein. Du baust, vor Ort, vor einer Jury, in der vorgegebenen Zeit.'},
    'The one credential in this industry that is earned with balloons in your hands.': {
        'nl': 'Het enige getuigschrift in deze sector dat je verdient met ballonnen in je handen.',
        'fr': 'Le seul titre de ce secteur qui se gagne avec des ballons entre les mains.',
        'de': 'Der einzige Nachweis in dieser Branche, den du dir mit Ballons in den Händen verdienst.'},
    'A Sempertex jury member discussing a design with a candidate': {
        'nl': 'Een Sempertex-jurylid bespreekt een ontwerp met een kandidaat',
        'fr': 'Un membre du jury Sempertex discute d’une création avec un candidat',
        'de': 'Ein Sempertex-Jurymitglied bespricht einen Entwurf mit einer Kandidatin'},
    'Scored against fixed criteria, explained face to face': {
        'nl': 'Gescoord op vaste criteria, persoonlijk toegelicht',
        'fr': 'Noté selon des critères fixes, expliqué en face à face',
        'de': 'Nach festen Kriterien bewertet, persönlich erklärt'},

    # ---- waarom ----
    'Certification is not a badge for your website. It changes what you can charge, who you can work with, and how clients decide.': {
        'nl': 'Certificering is geen badge voor je website. Het verandert wat je kunt vragen, met wie je kunt werken en hoe klanten beslissen.',
        'fr': 'La certification n’est pas un badge pour votre site web. Elle change ce que vous pouvez facturer, avec qui vous pouvez travailler et la façon dont les clients décident.',
        'de': 'Die Zertifizierung ist kein Abzeichen für deine Website. Sie verändert, was du verlangen kannst, mit wem du arbeiten kannst und wie Kunden entscheiden.'},
    'TRUST': {'nl': 'VERTROUWEN', 'fr': 'CONFIANCE', 'de': 'VERTRAUEN'},
    'Proof a client can check': {'nl': 'Bewijs dat een klant kan nagaan', 'fr': 'Une preuve que le client peut vérifier', 'de': 'Ein Nachweis, den Kunden prüfen können'},
    'Most clients cannot judge a tapered garland from a photo. They can check whether Sempertex has certified you. That shifts the conversation from price to standard.': {
        'nl': 'De meeste klanten kunnen een taps toelopende guirlande niet beoordelen op een foto. Ze kunnen wel nagaan of Sempertex je gecertificeerd heeft. Dan gaat het gesprek niet meer over prijs, maar over niveau.',
        'fr': 'La plupart des clients ne savent pas juger une guirlande effilée sur une photo. Ils peuvent en revanche vérifier si Sempertex vous a certifié. La discussion passe alors du prix au niveau.',
        'de': 'Die meisten Kunden können eine sich verjüngende Girlande auf einem Foto nicht beurteilen. Sie können aber prüfen, ob Sempertex dich zertifiziert hat. Damit geht es im Gespräch nicht mehr um den Preis, sondern um den Standard.'},
    'PRICING': {'nl': 'PRIJS', 'fr': 'PRIX', 'de': 'PREIS'},
    'A reason for your rate': {'nl': 'Een reden voor je tarief', 'fr': 'Une raison pour votre tarif', 'de': 'Ein Grund für deinen Preis'},
    'A certified decorator is not selling balloons, but a guaranteed level of work. That is the difference between quoting a price and defending one.': {
        'nl': 'Een gecertificeerde decorateur verkoopt geen ballonnen, maar een gegarandeerd niveau van werk. Dat is het verschil tussen een prijs noemen en een prijs verdedigen.',
        'fr': 'Un décorateur certifié ne vend pas des ballons, mais un niveau de travail garanti. C’est la différence entre annoncer un prix et le défendre.',
        'de': 'Ein zertifizierter Dekorateur verkauft keine Ballons, sondern ein garantiertes Arbeitsniveau. Das ist der Unterschied zwischen einen Preis nennen und einen Preis verteidigen.'},
    'BUSINESS': {'nl': 'BUSINESS', 'fr': 'BUSINESS', 'de': 'BUSINESS'},
    'The numbers, not just the design': {'nl': 'De cijfers, niet alleen het ontwerp', 'fr': 'Les chiffres, pas seulement le design', 'de': 'Die Zahlen, nicht nur das Design'},
    'The exam asks for a marketing proposal and a cost calculation alongside your designs. Building an organic arch and knowing what it should cost are two different skills.': {
        'nl': 'Naast je ontwerpen vraagt het examen een marketingvoorstel en een kostprijsberekening. Een organische boog bouwen en weten wat hij moet kosten zijn twee verschillende vaardigheden.',
        'fr': 'En plus de vos créations, l’examen demande une proposition marketing et un calcul des coûts. Construire une arche organique et savoir ce qu’elle doit coûter sont deux compétences différentes.',
        'de': 'Neben deinen Entwürfen verlangt die Prüfung einen Marketingvorschlag und eine Kostenkalkulation. Einen organischen Bogen bauen und wissen, was er kosten muss, sind zwei verschiedene Fähigkeiten.'},
    'LEVEL': {'nl': 'NIVEAU', 'fr': 'NIVEAU', 'de': 'NIVEAU'},
    'An honest benchmark': {'nl': 'Een eerlijke maatstaf', 'fr': 'Une référence honnête', 'de': 'Ein ehrlicher Maßstab'},
    'Working alone makes it hard to measure yourself. A jury scoring against a fixed standard gives you a straight answer and a clear list of what to improve.': {
        'nl': 'Wie alleen werkt, kan zichzelf moeilijk meten. Een jury die scoort volgens een vaste norm geeft je een eerlijk antwoord en een duidelijke lijst van wat beter kan.',
        'fr': 'Quand on travaille seul, il est difficile de se situer. Un jury qui note selon une norme fixe vous donne une réponse franche et une liste claire de ce qu’il faut améliorer.',
        'de': 'Wer allein arbeitet, kann sich schwer einschätzen. Eine Jury, die nach einem festen Standard bewertet, gibt dir eine klare Antwort und eine klare Liste, was du verbessern kannst.'},
    'ACCESS': {'nl': 'TOEGANG', 'fr': 'ACCÈS', 'de': 'ZUGANG'},
    'A door into the brand': {'nl': 'Een deur naar het merk', 'fr': 'Une porte vers la marque', 'de': 'Eine Tür zur Marke'},
    'MBP is where collaborations with Sempertex Europe start. Certified artists work with us on projects and content, and receive PR boxes with new colours and launches.': {
        'nl': 'Met MBP beginnen samenwerkingen met Sempertex Europe. Gecertificeerde artiesten werken met ons aan projecten en content, en krijgen PR-boxen met nieuwe kleuren en lanceringen.',
        'fr': 'C’est avec le MBP que commencent les collaborations avec Sempertex Europe. Les artistes certifiés travaillent avec nous sur des projets et du contenu, et reçoivent des box PR avec les nouvelles couleurs et nouveautés.',
        'de': 'Mit MBP beginnen Kooperationen mit Sempertex Europe. Zertifizierte Künstler arbeiten mit uns an Projekten und Content und bekommen PR-Boxen mit neuen Farben und Neuheiten.'},
    'VISIBILITY': {'nl': 'ZICHTBAARHEID', 'fr': 'VISIBILITÉ', 'de': 'SICHTBARKEIT'},
    'Found, not just followed': {'nl': 'Gevonden, niet alleen gevolgd', 'fr': 'Trouvé, pas seulement suivi', 'de': 'Gefunden, nicht nur gefolgt'},
    'Certified artists are recognised through the Sempertex channels, in front of the clients, wholesalers and partners who go looking for professionals.': {
        'nl': 'Gecertificeerde artiesten krijgen erkenning via de kanalen van Sempertex, bij de klanten, groothandels en partners die op zoek gaan naar professionals.',
        'fr': 'Les artistes certifiés sont mis en avant sur les canaux Sempertex, auprès des clients, grossistes et partenaires qui cherchent des professionnels.',
        'de': 'Zertifizierte Künstler werden über die Sempertex-Kanäle sichtbar, bei den Kunden, Großhändlern und Partnern, die nach Profis suchen.'},
    'The short version': {'nl': 'Kort gezegd', 'fr': 'En bref', 'de': 'Kurz gesagt'},

    # ---- wat je krijgt ----
    'Pass the exam and you join the MBP community, with everything that comes with it.': {
        'nl': 'Slaag je voor het examen, dan hoor je bij de MBP-community, met alles wat daarbij hoort.',
        'fr': 'Réussissez l’examen et vous rejoignez la communauté MBP, avec tout ce qui va avec.',
        'de': 'Bestehst du die Prüfung, gehörst du zur MBP-Community, mit allem, was dazugehört.'},
    'Master Balloon Professional, certified by Sempertex': {
        'nl': 'Master Balloon Professional, gecertificeerd door Sempertex',
        'fr': 'Master Balloon Professional, certifié par Sempertex',
        'de': 'Master Balloon Professional, zertifiziert von Sempertex'},
    'MBP diploma': {'nl': 'MBP-diploma', 'fr': 'Diplôme MBP', 'de': 'MBP-Diplom'},
    'Officially recognised by Sempertex, worldwide.': {
        'nl': 'Officieel erkend door Sempertex, wereldwijd.', 'fr': 'Officiellement reconnu par Sempertex, dans le monde entier.', 'de': 'Offiziell von Sempertex anerkannt, weltweit.'},
    'Welcome kit': {'nl': 'Welkomstpakket', 'fr': 'Kit de bienvenue', 'de': 'Willkommenspaket'},
    'Exclusive MBP merchandise, yours on the day.': {
        'nl': 'Exclusieve MBP-merchandise, voor jou op de dag zelf.', 'fr': 'Des articles MBP exclusifs, remis le jour même.', 'de': 'Exklusives MBP-Merchandise, für dich am Prüfungstag.'},
    'E-learning access': {'nl': 'Toegang tot e-learning', 'fr': 'Accès e-learning', 'de': 'E-Learning-Zugang'},
    'Including the Marketing and Costing modules.': {
        'nl': 'Met de modules Marketing en Kostprijs.', 'fr': 'Avec les modules Marketing et Calcul des coûts.', 'de': 'Mit den Modulen Marketing und Kalkulation.'},
    'Discount': {'nl': 'Korting', 'fr': 'Réduction', 'de': 'Rabatt'},
    'On Sempertex Europe workshops and events.': {
        'nl': 'Op workshops en events van Sempertex Europe.', 'fr': 'Sur les ateliers et événements Sempertex Europe.', 'de': 'Auf Workshops und Events von Sempertex Europe.'},
    'PR boxes': {'nl': 'PR-boxen', 'fr': 'Box PR', 'de': 'PR-Boxen'},
    'New colours, finishes and launches at your door.': {
        'nl': 'Nieuwe kleuren, finishes en lanceringen aan je deur.', 'fr': 'Nouvelles couleurs, finitions et nouveautés livrées chez vous.', 'de': 'Neue Farben, Finishes und Neuheiten direkt vor deiner Tür.'},
    'Collaborations': {'nl': 'Samenwerkingen', 'fr': 'Collaborations', 'de': 'Kooperationen'},
    'Work with Sempertex Europe on projects and content.': {
        'nl': 'Werk met Sempertex Europe aan projecten en content.', 'fr': 'Travaillez avec Sempertex Europe sur des projets et du contenu.', 'de': 'Arbeite mit Sempertex Europe an Projekten und Content.'},
    'Recognition': {'nl': 'Erkenning', 'fr': 'Reconnaissance', 'de': 'Anerkennung'},
    'Your name out through the Sempertex channels.': {
        'nl': 'Je naam in de kijker via de kanalen van Sempertex.', 'fr': 'Votre nom diffusé sur les canaux Sempertex.', 'de': 'Dein Name in den Sempertex-Kanälen.'},
    'A network': {'nl': 'Een netwerk', 'fr': 'Un réseau', 'de': 'Ein Netzwerk'},
    'Certified professionals across the whole of Europe.': {
        'nl': 'Gecertificeerde professionals in heel Europa.', 'fr': 'Des professionnels certifiés dans toute l’Europe.', 'de': 'Zertifizierte Profis in ganz Europa.'},

    # ---- examen ----
    'A practical exam in two parts, three hours in total. Pick a part to see what the jury scores.': {
        'nl': 'Een praktijkexamen in twee delen, drie uur in totaal. Kies een deel om te zien wat de jury beoordeelt.',
        'fr': 'Un examen pratique en deux parties, trois heures au total. Choisissez une partie pour voir ce que le jury évalue.',
        'de': 'Eine praktische Prüfung in zwei Teilen, insgesamt drei Stunden. Wähle einen Teil, um zu sehen, was die Jury bewertet.'},
    'Choose a part': {'nl': 'Kies een deel', 'fr': 'Choisissez une partie', 'de': 'Wähle einen Teil'},
    'Exam parts': {'nl': 'Examendelen', 'fr': 'Parties d’examen', 'de': 'Prüfungsteile'},
    'Part 1: Free Creativity': {'nl': 'Deel 1: Vrije creativiteit', 'fr': 'Partie 1 : Créativité libre', 'de': 'Teil 1: Freie Kreativität'},
    'Part 2: Jury assignments': {'nl': 'Deel 2: Opdrachten van de jury', 'fr': 'Partie 2 : Épreuves du jury', 'de': 'Teil 2: Aufgaben der Jury'},
    'Free Creativity, 30 points': {'nl': 'Vrije creativiteit, 30 punten', 'fr': 'Créativité libre, 30 points', 'de': 'Freie Kreativität, 30 Punkte'},
    'Your own designs, your own balloons. Creativity carries this part.': {
        'nl': 'Je eigen ontwerpen, je eigen ballonnen. In dit deel draait alles om creativiteit.',
        'fr': 'Vos propres créations, vos propres ballons. La créativité porte cette partie.',
        'de': 'Deine eigenen Entwürfe, deine eigenen Ballons. In diesem Teil zählt die Kreativität.'},
    'Assignment': {'nl': 'Opdracht', 'fr': 'Épreuve', 'de': 'Aufgabe'},
    'Points': {'nl': 'Punten', 'fr': 'Points', 'de': 'Punkte'},
    'Centerpiece': {'nl': 'Centerpiece', 'fr': 'Centre de table', 'de': 'Tischdeko'},
    'Personal design': {'nl': 'Persoonlijk ontwerp', 'fr': 'Création personnelle', 'de': 'Eigener Entwurf'},
    'Marketing proposal': {'nl': 'Marketingvoorstel', 'fr': 'Proposition marketing', 'de': 'Marketingvorschlag'},
    'Cost calculation': {'nl': 'Kostprijsberekening', 'fr': 'Calcul des coûts', 'de': 'Kostenkalkulation'},
    '1 hour 30 minutes': {'nl': '1 uur 30 minuten', 'fr': '1 heure 30 minutes', 'de': '1 Stunde 30 Minuten'},
    'Use your own Sempertex balloons.': {
        'nl': 'Je gebruikt je eigen Sempertex-ballonnen.', 'fr': 'Utilisez vos propres ballons Sempertex.', 'de': 'Du verwendest deine eigenen Sempertex-Ballons.'},
    'Every design includes at least three different balloon sizes.': {
        'nl': 'Elk ontwerp bevat minstens drie verschillende ballonmaten.', 'fr': 'Chaque création comprend au moins trois tailles de ballons différentes.', 'de': 'Jeder Entwurf enthält mindestens drei verschiedene Ballongrößen.'},
    'The marketing proposal and cost calculation are prepared in advance with the e-learning modules.': {
        'nl': 'Het marketingvoorstel en de kostprijsberekening bereid je vooraf voor met de e-learningmodules.',
        'fr': 'La proposition marketing et le calcul des coûts se préparent à l’avance avec les modules e-learning.',
        'de': 'Marketingvorschlag und Kostenkalkulation bereitest du vorab mit den E-Learning-Modulen vor.'},
    'A candidate building a balloon design during the MBP exam': {
        'nl': 'Een kandidaat bouwt een ballonontwerp tijdens het MBP-examen',
        'fr': 'Une candidate réalise une création en ballons pendant l’examen MBP',
        'de': 'Eine Kandidatin baut während der MBP-Prüfung einen Ballonentwurf'},
    'Your design, your balloons, 60 minutes': {
        'nl': 'Jouw ontwerp, jouw ballonnen, 60 minuten', 'fr': 'Votre création, vos ballons, 60 minutes', 'de': 'Dein Entwurf, deine Ballons, 60 Minuten'},
    'Decoration at the jury\'s request, 70 points': {
        'nl': 'Decoratie op vraag van de jury, 70 punten', 'fr': 'Décoration à la demande du jury, 70 points', 'de': 'Dekoration nach Vorgabe der Jury, 70 Punkte'},
    'Technical skill and execution, under instruction, with balloons provided by Sempertex.': {
        'nl': 'Techniek en uitvoering, volgens instructies, met ballonnen van Sempertex.',
        'fr': 'Technique et exécution, selon les consignes, avec des ballons fournis par Sempertex.',
        'de': 'Technik und Ausführung nach Anweisung, mit Ballons von Sempertex.'},
    'Round balloon techniques': {'nl': 'Technieken met ronde ballonnen', 'fr': 'Techniques avec ballons ronds', 'de': 'Techniken mit Rundballons'},
    'Link-O-Loon&reg; design': {'nl': 'Link-O-Loon&reg; ontwerp', 'fr': 'Création Link-O-Loon&reg;', 'de': 'Link-O-Loon&reg; Entwurf'},
    'Organic design': {'nl': 'Organisch ontwerp', 'fr': 'Création organique', 'de': 'Organischer Entwurf'},
    'Use of basic tools': {'nl': 'Gebruik van basistools', 'fr': 'Utilisation des outils de base', 'de': 'Umgang mit Basiswerkzeugen'},
    'Balloons for this part are provided by Sempertex.': {
        'nl': 'De ballonnen voor dit deel krijg je van Sempertex.', 'fr': 'Les ballons de cette partie sont fournis par Sempertex.', 'de': 'Die Ballons für diesen Teil stellt Sempertex.'},
    'Assignments are carried out to the jury\'s instructions.': {
        'nl': 'Je voert de opdrachten uit volgens de instructies van de jury.', 'fr': 'Les épreuves se font selon les consignes du jury.', 'de': 'Die Aufgaben führst du nach den Anweisungen der Jury aus.'},
    'You apply different sizes and techniques across the assignments.': {
        'nl': 'Over de opdrachten heen gebruik je verschillende maten en technieken.', 'fr': 'Vous utilisez différentes tailles et techniques au fil des épreuves.', 'de': 'Über die Aufgaben hinweg setzt du verschiedene Größen und Techniken ein.'},
    'A Sempertex jury member assessing a balloon centerpiece with a scoring sheet': {
        'nl': 'Een Sempertex-jurylid beoordeelt een ballon-centerpiece met een scoreformulier',
        'fr': 'Un membre du jury Sempertex évalue un centre de table en ballons avec une grille de notation',
        'de': 'Ein Sempertex-Jurymitglied bewertet eine Ballon-Tischdeko mit einem Bewertungsbogen'},
    'Every assignment scored against the official criteria': {
        'nl': 'Elke opdracht gescoord op de officiële criteria', 'fr': 'Chaque épreuve notée selon les critères officiels', 'de': 'Jede Aufgabe nach den offiziellen Kriterien bewertet'},

    # ---- inschrijven ----
    'Choose an available exam date from the events calendar.': {
        'nl': 'Kies een beschikbare examendatum in de eventkalender.', 'fr': 'Choisissez une date d’examen disponible dans le calendrier des événements.', 'de': 'Wähle einen freien Prüfungstermin im Eventkalender.'},
    'Add the MBP exam to your cart and complete your order.': {
        'nl': 'Leg het MBP-examen in je winkelmandje en rond je bestelling af.', 'fr': 'Ajoutez l’examen MBP à votre panier et finalisez votre commande.', 'de': 'Lege die MBP-Prüfung in deinen Warenkorb und schließe die Bestellung ab.'},
    'Once your payment is received, we register you officially with Sempertex.': {
        'nl': 'Zodra je betaling binnen is, schrijven we je officieel in bij Sempertex.', 'fr': 'Dès réception de votre paiement, nous vous inscrivons officiellement auprès de Sempertex.', 'de': 'Sobald deine Zahlung eingegangen ist, melden wir dich offiziell bei Sempertex an.'},
    'You receive a confirmation email with the location, the schedule and your e-learning access.': {
        'nl': 'Je krijgt een bevestigingsmail met de locatie, de planning en je toegang tot de e-learning.', 'fr': 'Vous recevez un e-mail de confirmation avec le lieu, le programme et votre accès e-learning.', 'de': 'Du bekommst eine Bestätigungsmail mit Ort, Ablauf und deinem E-Learning-Zugang.'},
    'Prepare': {'nl': 'Voorbereiden', 'fr': 'Préparer', 'de': 'Vorbereiten'},
    'Before the day': {'nl': 'Voor de examendag', 'fr': 'Avant le jour J', 'de': 'Vor dem Prüfungstag'},
    'Work through the Marketing and Costing modules on the e-learning platform.': {
        'nl': 'Doorloop de modules Marketing en Kostprijs op het e-learningplatform.', 'fr': 'Suivez les modules Marketing et Calcul des coûts sur la plateforme e-learning.', 'de': 'Arbeite die Module Marketing und Kalkulation auf der E-Learning-Plattform durch.'},
    'Design your centerpiece and personal design, with three balloon sizes in each.': {
        'nl': 'Ontwerp je centerpiece en je persoonlijk ontwerp, met telkens drie ballonmaten.', 'fr': 'Concevez votre centre de table et votre création personnelle, avec trois tailles de ballons dans chacun.', 'de': 'Entwirf deine Tischdeko und deinen eigenen Entwurf, jeweils mit drei Ballongrößen.'},
    'Print your marketing proposal and your cost calculation.': {
        'nl': 'Print je marketingvoorstel en je kostprijsberekening af.', 'fr': 'Imprimez votre proposition marketing et votre calcul des coûts.', 'de': 'Drucke deinen Marketingvorschlag und deine Kostenkalkulation aus.'},
    'Bring': {'nl': 'Meebrengen', 'fr': 'À apporter', 'de': 'Mitbringen'},
    'Your own Sempertex balloons for the Free Creativity part.': {
        'nl': 'Je eigen Sempertex-ballonnen voor het deel Vrije creativiteit.', 'fr': 'Vos propres ballons Sempertex pour la partie Créativité libre.', 'de': 'Deine eigenen Sempertex-Ballons für den Teil Freie Kreativität.'},
    'Both printed documents.': {'nl': 'Beide geprinte documenten.', 'fr': 'Les deux documents imprimés.', 'de': 'Beide ausgedruckten Dokumente.'},
    'Yourself, 30 minutes before the start.': {
        'nl': 'Jezelf, 30 minuten voor de start.', 'fr': 'Vous-même, 30 minutes avant le début.', 'de': 'Dich selbst, 30 Minuten vor Beginn.'},

    # ---- FAQ ----
    'Who is the MBP exam for?': {'nl': 'Voor wie is het MBP-examen?', 'fr': 'À qui s’adresse l’examen MBP ?', 'de': 'Für wen ist die MBP-Prüfung?'},
    'Working balloon decorators and artists. It is a professional certification, not an introduction. You are expected to arrive with the technique already in your hands.': {
        'nl': 'Voor ballondecorateurs en artiesten die al actief zijn. Het is een professionele certificering, geen kennismaking. We verwachten dat je de techniek al in de vingers hebt.',
        'fr': 'Aux décorateurs et artistes ballons en activité. C’est une certification professionnelle, pas une initiation. Vous êtes censé maîtriser déjà la technique.',
        'de': 'Für aktive Ballondekorateure und Künstler. Es ist eine professionelle Zertifizierung, keine Einführung. Wir erwarten, dass du die Technik schon beherrschst.'},
    'Do I need to take a course first?': {'nl': 'Moet ik eerst een opleiding volgen?', 'fr': 'Dois-je d’abord suivre une formation ?', 'de': 'Muss ich vorher einen Kurs machen?'},
    'No course is required. Registration gives you access to the Marketing and Costing modules on the e-learning platform, and those cover exam components you cannot prepare any other way.': {
        'nl': 'Nee, een opleiding is niet verplicht. Met je inschrijving krijg je toegang tot de modules Marketing en Kostprijs op het e-learningplatform. Die behandelen examenonderdelen die je op geen andere manier kunt voorbereiden.',
        'fr': 'Aucune formation n’est obligatoire. L’inscription vous donne accès aux modules Marketing et Calcul des coûts sur la plateforme e-learning, qui couvrent des parties de l’examen impossibles à préparer autrement.',
        'de': 'Nein, ein Kurs ist nicht nötig. Mit der Anmeldung bekommst du Zugang zu den Modulen Marketing und Kalkulation auf der E-Learning-Plattform. Sie decken Prüfungsteile ab, auf die du dich anders nicht vorbereiten kannst.'},
    'What happens if I do not reach 85 points?': {'nl': 'Wat als ik geen 85 punten haal?', 'fr': 'Que se passe-t-il si je n’atteins pas 85 points ?', 'de': 'Was passiert, wenn ich keine 85 Punkte erreiche?'},
    'You can sit the exam again on a future date. The scoring tells you exactly which components to work on.': {
        'nl': 'Dan kun je het examen opnieuw afleggen op een latere datum. De score toont je precies aan welke onderdelen je moet werken.',
        'fr': 'Vous pouvez repasser l’examen à une date ultérieure. La notation vous indique précisément les points à travailler.',
        'de': 'Du kannst die Prüfung an einem späteren Termin wiederholen. Die Bewertung zeigt dir genau, woran du arbeiten musst.'},
    'Which balloons do I use?': {'nl': 'Welke ballonnen gebruik ik?', 'fr': 'Quels ballons dois-je utiliser ?', 'de': 'Welche Ballons verwende ich?'},
    'Your own Sempertex balloons for Free Creativity. Sempertex provides the balloons for the jury assignments.': {
        'nl': 'Je eigen Sempertex-ballonnen voor Vrije creativiteit. Voor de opdrachten van de jury zorgt Sempertex voor de ballonnen.',
        'fr': 'Vos propres ballons Sempertex pour la Créativité libre. Sempertex fournit les ballons pour les épreuves du jury.',
        'de': 'Deine eigenen Sempertex-Ballons für die Freie Kreativität. Für die Aufgaben der Jury stellt Sempertex die Ballons.'},
    'How long does the exam take?': {'nl': 'Hoe lang duurt het examen?', 'fr': 'Combien de temps dure l’examen ?', 'de': 'Wie lange dauert die Prüfung?'},
    'Three hours in total, split into two parts of 1 hour 30 minutes each.': {
        'nl': 'Drie uur in totaal, verdeeld over twee delen van elk 1 uur 30 minuten.', 'fr': 'Trois heures au total, en deux parties de 1 heure 30 minutes chacune.', 'de': 'Insgesamt drei Stunden, aufgeteilt in zwei Teile von je 1 Stunde 30 Minuten.'},
    'Where do the exams take place?': {'nl': 'Waar vinden de examens plaats?', 'fr': 'Où se déroulent les examens ?', 'de': 'Wo finden die Prüfungen statt?'},
    'Exam dates are organised at locations across Europe throughout the year. The events calendar shows the next available date and venue.': {
        'nl': 'Het hele jaar door organiseren we examens op locaties in heel Europa. In de eventkalender zie je de eerstvolgende datum en locatie.',
        'fr': 'Des examens sont organisés tout au long de l’année dans toute l’Europe. Le calendrier des événements indique la prochaine date et le lieu.',
        'de': 'Das ganze Jahr über gibt es Prüfungen an Orten in ganz Europa. Im Eventkalender siehst du den nächsten Termin und Ort.'},

    # ---- afsluiter ----
    'Exam dates are scheduled across Europe throughout the year. Pick your date, bring your balloons, and show the jury what you can do.': {
        'nl': 'Het hele jaar door staan er examendata gepland in heel Europa. Kies je datum, breng je ballonnen mee en toon de jury wat je kunt.',
        'fr': 'Des dates d’examen sont prévues dans toute l’Europe tout au long de l’année. Choisissez votre date, apportez vos ballons et montrez au jury ce que vous savez faire.',
        'de': 'Das ganze Jahr über gibt es Prüfungstermine in ganz Europa. Wähle deinen Termin, bring deine Ballons mit und zeig der Jury, was du kannst.'},
    'See the exam dates and register': {'nl': 'Bekijk de examendata en schrijf je in', 'fr': 'Voir les dates et s’inscrire', 'de': 'Termine ansehen und anmelden'},
    'Find a certified MBP': {'nl': 'Vind een gecertificeerde MBP', 'fr': 'Trouver un MBP certifié', 'de': 'Zertifizierte MBPs finden'},
    'MBP certification': {'nl': 'MBP-certificering', 'fr': 'Certification MBP', 'de': 'MBP-Zertifizierung'},
}
