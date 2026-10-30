"""Contenu éditorial du site vitrine.

Modifiez les informations ci-dessous pour personnaliser le site :
coordonnées, zones desservies, services, réalisations, témoignages et FAQ.
"""

BUSINESS = {
    "name": "Rufus Plomberie",
    "short_name": "Rufus",
    "tagline": "Intervention rapide. Travail garanti.",
    "city": "Abidjan",
    "areas": "Cocody, Plateau, Marcory, Treichville, Yopougon et environs",
    "areas_short": "Cocody · Plateau · Marcory",
    "description": (
        "Rufus Plomberie accompagne les particuliers, syndics, commerces et "
        "restaurants à Abidjan pour tous leurs travaux de plomberie : dépannage "
        "d'urgence, étanchéité, débouchage, installation sanitaire et "
        "rénovation de salle de bain."
    ),
    "meta_description": (
        "Plombier à Abidjan : dépannage 24h/24, fuites d'eau, débouchage, "
        "installation sanitaire et rénovation de salle de bain. Demande "
        "d’intervention simple et travail garanti par Rufus Plomberie."
    ),
    "phone_display": "+225 07 49 52 32 96",
    "phone_href": "+2250749523296",
    "whatsapp": "2250151225660",
    "whatsapp_message": (
        "Bonjour Rufus, j'ai besoin d'aide pour un problème de plomberie."
    ),
    "email": "contact@rufus-plomberie.ci",
    "address": "Cocody, Abidjan – Côte d’Ivoire",
    "hours_week": "7j/7 : 7h – 19h",
    "hours_emergency": "Urgences 24h/24, 7j/7",
    "opening_days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ],
    "opening_time": {"opens": "07:00", "closes": "19:00"},
    "experience": 15,
    "response_time": "30 min",
    "map_embed_url": (
        "https://www.openstreetmap.org/export/embed.html?"
        "bbox=-4.0610%2C5.3250%2C-3.9550%2C5.3990&layer=mapnik&marker=5.3620%2C-4.0080"
    ),
    "map_link": (
        "https://www.openstreetmap.org/?mlat=5.3620&mlon=-4.0080"
        "#map=14/5.3620/-4.0080"
    ),
    "area_list": [
        "Abidjan",
        "Cocody",
        "Plateau",
        "Marcory",
        "Treichville",
        "Yopougon",
        "Adjamé",
        "Koumassi",
        "Riviera",
    ],
    "socials": [
        {
            "label": "Facebook",
            "url": "https://www.facebook.com/profile.php?id=61587142389598",
            "icon": "facebook",
        },
    ],
}

NAV_LINKS = [
    {"label": "Accueil", "anchor": "accueil"},
    {"label": "Services", "anchor": "services"},
    {"label": "Réalisations", "anchor": "realisations"},
    {"label": "À propos", "anchor": "a-propos"},
    {"label": "Contact", "anchor": "contact"},
]

PROBLEM_CHOICES = [
    ("urgence", "Dépannage / urgence"),
    ("fuite", "Fuite d’eau"),
    ("debouchage", "Débouchage de canalisation"),
    ("installation", "Installation sanitaire"),
    ("renovation", "Rénovation de salle de bain"),
    ("recherche", "Étanchéité"),
    ("entretien", "Entretien / maintenance"),
    ("autre", "Autre demande"),
]

SERVICES = [
    {
        "title": "Dépannage & urgences",
        "description": (
            "Fuite, panne de chauffe-eau ou coupure d’eau : notre équipe "
            "intervient 24h/24 et vous rappelle en moins de 5 minutes."
        ),
        "image": "img/service-urgence-plomberie.webp",
        "image_alt": "Plombier en train de réparer une canalisation sous un évier",
        "icon": "clock",
        "form_value": "urgence",
    },
    {
        "title": "Évacuation au sol",
        "description": (
            "Installation et débouchage des évacuations au sol pour un "
            "écoulement rapide et sans mauvaises odeurs."
        ),
        "image": "img/service-evacuation-sol.webp",
        "image_alt": "Bonde d’évacuation installée dans le sol d’une salle de bain",
        "image_credit": "Unsplash",
        "image_source": "https://unsplash.com/photos/un-drain-dans-le-sol-dune-salle-de-bain-Bsw-804FEtQ",
        "icon": "pipe",
        "form_value": "debouchage",
    },
    {
        "title": "Installation de chauffe-eau solaire et électrique",
        "description": (
            "Installation et raccordement de chauffe-eau solaires et électriques "
            "pour une eau chaude fiable et économique."
        ),
        "image": "img/service-chauffe-eau.webp",
        "image_alt": "Chauffe-eau électrique installé au-dessus d’un lavabo",
        "image_credit": "Unsplash",
        "image_source": "https://unsplash.com/photos/water-heater-on-wall-above-sink-ii5IRyypPhs",
        "icon": "wrench",
        "form_value": "installation",
    },
    {
        "title": "Installation sanitaire",
        "description": (
            "Pose et remplacement de WC, lavabos, douches, baignoires, "
            "chauffe-eau et équipements de cuisine."
        ),
        "image": "img/service-installation-sanitaire.webp",
        "image_alt": "Salle de bain avec toilettes et douche récemment aménagées",
        "image_credit": "Unsplash",
        "image_source": "https://unsplash.com/photos/salle-de-bain-avec-toilettes-blanches-et-douche-48mTwDzizqE",
        "icon": "wrench",
        "form_value": "installation",
    },
    {
        "title": "Évacuation sous plancher",
        "description": (
            "Installation et réparation des conduites d’évacuation sous "
            "plancher pour un écoulement fiable."
        ),
        "image": "img/service-evacuation-sous-plancher.webp",
        "image_alt": "Canalisation bleue installée dans une tranchée de terre",
        "image_credit": "Unsplash",
        "image_source": "https://unsplash.com/photos/un-tuyau-bleu-pose-sur-un-tas-de-terre-MzPnzK3prTU",
        "icon": "pipe",
        "form_value": "installation",
    },
    {
        "title": "Étanchéité",
        "description": (
            "Traitement et imperméabilisation de vos surfaces pour prévenir "
            "les infiltrations d'eau et protéger durablement votre habitat."
        ),
        "image": "img/service-etancheite-toiture.webp",
        "image_alt": "Professionnel appliquant un revêtement sur une toiture",
        "image_credit": "Unsplash",
        "image_source": "https://unsplash.com/photos/un-homme-en-combinaison-blanche-peignant-un-toit-ce2r9sPR_9E",
        "icon": "search",
        "form_value": "recherche",
    },
    {
        "title": "Entretien & maintenance",
        "description": (
            "Contrats sur mesure pour particuliers, syndics, commerces et "
            "restaurants afin de prévenir les pannes et maîtriser les coûts."
        ),
        "image": "img/service-maintenance-plomberie.webp",
        "image_alt": "Professionnelle en équipement de sécurité tenant une clé de plomberie",
        "image_credit": "Pexels",
        "image_source": "https://www.pexels.com/photo/handywoman-holding-a-plumbers-wrench-8486978/",
        "icon": "shield",
        "form_value": "entretien",
    },
    {
        "title": "Branchement d’une Polytank",
        "description": (
            "Raccordement de votre Polytank au réseau d’eau pour une "
            "alimentation fiable de votre habitation."
        ),
        "image": "img/service-reservoir-eau.webp",
        "image_alt": "Réservoirs d’eau installés sur le toit d’un bâtiment",
        "image_credit": "Unsplash",
        "image_source": "https://unsplash.com/photos/deux-reservoirs-deau-orange-sur-un-toit-sous-un-ciel-bleu-Pl4FYiTW79Y",
        "icon": "wrench",
        "form_value": "installation",
    },
    {
        "title": "Autres services",
        "description": (
            "Petites réparations, remplacement de robinetterie et autres "
            "travaux de plomberie adaptés à votre besoin."
        ),
        "image": "img/apropos-plombier.webp",
        "image_alt": "Technicien en train de réparer un raccord de plomberie",
        "icon": "wrench",
        "form_value": "autre",
    },
]

REASONS = [
    {
        "title": "Une réponse en moins de 5 minutes",
        "description": (
            "Un technicien vous rappelle rapidement pour qualifier votre besoin "
            "et planifier une intervention au plus vite."
        ),
        "icon": "phone",
    },
    {
        "title": "Votre problème, notre priorité",
        "description": (
            "Nous nous concentrons d’abord sur la résolution de votre problème. "
            "Le montant est communiqué après l’intervention."
        ),
        "icon": "wrench",
    },
    {
        "title": "Montant communiqué après le service",
        "description": (
            "Le montant est expliqué après le service, selon les travaux "
            "réalisés pour résoudre votre problème."
        ),
        "icon": "check",
    },
    {
        "title": "Travaux garantis 12 mois",
        "description": (
            "Nos interventions sont couvertes par une garantie pièces et "
            "main-d’œuvre pour votre tranquillité."
        ),
        "icon": "shield-check",
    },
    {
        "title": "Techniciens qualifiés et assurés",
        "description": (
            "Des professionnels formés, équipés et respectueux de votre "
            "installation comme de votre intérieur."
        ),
        "icon": "badge-check",
    },
]

PROCESS_STEPS = [
    {
        "title": "Vous appelez",
        "description": (
            "Décrivez-nous votre panne ou votre projet par téléphone ou WhatsApp."
        ),
        "icon": "phone",
    },
    {
        "title": "Diagnostic",
        "description": (
            "Nos techniciens identifient l’origine du problème et les solutions "
            "possibles."
        ),
        "icon": "search",
    },
    {
        "title": "Intervention",
        "description": (
            "Nous intervenons pour résoudre votre problème et réalisons les "
            "travaux nécessaires."
        ),
        "icon": "wrench",
    },
    {
        "title": "Montant et garantie",
        "description": (
            "Après le service, nous vous communiquons le montant des travaux "
            "réalisés et les conditions de garantie."
        ),
        "icon": "shield-check",
    },
]

PROJECTS = [
    {
        "title": "Salle de bain clé en main",
        "location": "Cocody",
        "description": (
            "Dépose de l’ancienne baignoire, reprise complète de la plomberie "
            "et pose d’une douche à l’italienne."
        ),
        "before_image": "img/realisation-salle-de-bain-avant.webp",
        "before_alt": (
            "Salle de bain en cours de rénovation avec des travaux de plâtrerie"
        ),
        "after_image": "img/realisation-salle-de-bain-apres.webp",
        "after_alt": (
            "Salle de bain moderne terminée avec douche vitrée et meuble vasque"
        ),
    },
    {
        "title": "Remplacement de robinetterie",
        "location": "Marcory",
        "description": (
            "Mise à niveau du réseau et remplacement d’un robinet de cuisine "
            "pour un restaurant en activité."
        ),
        "before_image": "img/realisation-robinetterie-avant.webp",
        "before_alt": "Anciennes canalisations apparentes avant remplacement",
        "after_image": "img/realisation-robinetterie-apres.webp",
        "after_alt": "Robinetterie moderne installée sur un évier après travaux",
    },
    {
        "title": "Rénovation d’une salle d’eau",
        "location": "Plateau",
        "description": (
            "Réfection du réseau, remplacement des sanitaires et création d’un "
            "espace plus lumineux et fonctionnel."
        ),
        "before_image": "img/realisation-salle-eau-avant.webp",
        "before_alt": "Salle d’eau avant rénovation avec des tuyaux apparents",
        "after_image": "img/realisation-salle-eau-apres.webp",
        "after_alt": "Salle d’eau rénovée avec baignoire et vasque moderne",
    },
]

TESTIMONIALS = [
    {
        "quote": (
            "Fuite sous l’évier un dimanche matin. J’ai été rappelée en quelques "
            "minutes et un technicien est arrivé avant midi. Travail propre et "
            "montant expliqué après l’intervention."
        ),
        "name": "Aïcha K.",
        "role": "Propriétaire · Cocody",
        "image": "img/testimonial-portrait-1.webp",
    },
    {
        "quote": (
            "Nous confions l’entretien de plusieurs immeubles à Rufus. Les "
            "interventions sont rapides, les comptes rendus clairs et les "
            "résidents satisfaits."
        ),
        "name": "Marc A.",
        "role": "Gestionnaire de syndic · Plateau",
        "image": "img/testimonial-portrait-2.webp",
    },
    {
        "quote": (
            "Canalisation bouchée en pleine service : l’équipe est intervenue "
            "sans interrompre notre activité. Réactifs, efficaces et très "
            "professionnels."
        ),
        "name": "Fatou D.",
        "role": "Restauratrice · Marcory",
        "image": "img/testimonial-portrait-3.webp",
    },
]

STATS = [
    {"value": 15, "suffix": "+", "label": "années d’expérience"},
    {"value": 2500, "suffix": "+", "label": "interventions réalisées"},
    {"value": 98, "suffix": "%", "label": "clients satisfaits"},
]

FAQ_ITEMS = [
    {
        "question": "En combien de temps pouvez-vous intervenir ?",
        "answer": (
            "À Abidjan, nous visons une intervention en 30 à 45 minutes pour "
            "les urgences, selon votre quartier et la circulation. Un technicien "
            "vous confirme le délai exact lors de votre appel."
        ),
    },
    {
        "question": "Quand le prix du service est-il communiqué ?",
        "answer": (
            "Notre priorité est de résoudre votre problème. Le montant vous est "
            "communiqué après l’intervention, en fonction des travaux réalisés."
        ),
    },
    {
        "question": "Quels moyens de paiement acceptez-vous ?",
        "answer": (
            "Nous acceptons les espèces, le Mobile Money et le virement. Une "
            "facture est systématiquement remise pour les particuliers comme "
            "pour les entreprises."
        ),
    },
    {
        "question": "Intervenez-vous pour les syndics et les commerces ?",
        "answer": (
            "Oui, nous accompagnons les syndics, agences immobilières, commerces "
            "et restaurants avec des interventions ponctuelles ou des contrats "
            "d’entretien adaptés à leurs contraintes."
        ),
    },
    {
        "question": "Vos travaux sont-ils garantis ?",
        "answer": (
            "Nos interventions bénéficient d’une garantie de 12 mois sur la "
            "main-d’œuvre et les pièces installées. Les conditions vous sont "
            "précisées après l’intervention."
        ),
    },
    {
        "question": "Que faire en cas de fuite importante ?",
        "answer": (
            "Coupez immédiatement l’arrivée d’eau générale, éloignez les "
            "appareils électriques de la zone et appelez-nous. Évitez de "
            "démonter vous-même les raccords pour ne pas aggraver la fuite."
        ),
    },
    {
        "question": "Quels quartiers d’Abidjan couvrez-vous ?",
        "answer": (
            "Nous intervenons à Cocody, Plateau, Marcory, Treichville, Yopougon, "
            "Adjamé, Koumassi, Riviera et dans les zones voisines. Appelez-nous "
            "pour confirmer la prise en charge de votre adresse."
        ),
    },
]
