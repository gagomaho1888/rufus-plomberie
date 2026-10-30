import json
from urllib.parse import urlencode

from django.shortcuts import redirect, render
from django.templatetags.static import static
from django.urls import reverse

from .forms import DemandeDevisForm
from .site_content import (
    BUSINESS,
    FAQ_ITEMS,
    PROCESS_STEPS,
    PROJECTS,
    REASONS,
    SERVICES,
    STATS,
    TESTIMONIALS,
)


def _build_schema(request):
    """Construit les données structurées Schema.org du plombier."""
    image_url = request.build_absolute_uri(static("img/hero-plombier-ci.webp"))
    schema = {
        "@context": "https://schema.org",
        "@type": "Plumber",
        "@id": request.build_absolute_uri() + "#business",
        "name": BUSINESS["name"],
        "description": BUSINESS["description"],
        "url": request.build_absolute_uri(),
        "image": image_url,
        "logo": request.build_absolute_uri(static("img/logo-rufus.png")),
        "telephone": BUSINESS["phone_href"],
        "email": BUSINESS["email"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": BUSINESS["street_address"],
            "addressLocality": BUSINESS["city"],
            "addressRegion": "Abidjan",
            "addressCountry": "CI",
        },
        "areaServed": [
            {"@type": "City", "name": area} for area in BUSINESS["area_list"]
        ],
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": BUSINESS["opening_days"],
                "opens": BUSINESS["opening_time"]["opens"],
                "closes": BUSINESS["opening_time"]["closes"],
            }
        ],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Services de plomberie",
            "itemListElement": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": service["title"],
                    },
                }
                for service in SERVICES
            ],
        },
    }
    return json.dumps(schema, ensure_ascii=False)


def _build_whatsapp_url(demande):
    """Prépare un lien WhatsApp avec la demande pré-remplie."""
    text = (
        "Nouvelle demande de service depuis le site\n\n"
        f"Nom : {demande.nom}\n"
        f"Téléphone / WhatsApp : {demande.telephone}\n"
        f"Type de problème : {demande.get_type_probleme_display()}\n"
        f"Message : {demande.message}"
    )
    return (
        f"https://wa.me/{BUSINESS['whatsapp']}?{urlencode({'text': text})}"
    )


def index(request):
    if request.method == "POST":
        # Champ piège invisible : les robots qui le remplissent sont ignorés.
        if request.POST.get("website"):
            return redirect(f"{reverse('site_vitrine:index')}#contact")

        form = DemandeDevisForm(request.POST)
        if form.is_valid():
            demande = form.save()
            return redirect(_build_whatsapp_url(demande))
    else:
        form = DemandeDevisForm()

    context = {
        "reasons": REASONS,
        "process_steps": PROCESS_STEPS,
        "projects": PROJECTS,
        "testimonials": TESTIMONIALS,
        "stats": STATS,
        "faq_items": FAQ_ITEMS,
        "form": form,
        "schema": _build_schema(request),
    }
    return render(request, "site_vitrine/index.html", context)


def mentions_legales(request):
    return render(request, "site_vitrine/mentions_legales.html")
