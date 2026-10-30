from urllib.parse import parse_qs, urlparse

from django.test import TestCase
from django.urls import reverse

from .models import DemandeDevis
from .site_content import BUSINESS, FAQ_ITEMS, PROJECTS, SERVICES, TESTIMONIALS


class SiteVitrineTests(TestCase):
    def test_home_page_renders_expected_content(self):
        response = self.client.get(reverse("site_vitrine:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Une fuite ?")
        self.assertContains(response, "Demander un service")
        self.assertContains(response, "Le montant vous est communiqué après l’intervention")
        self.assertContains(response, "Les portraits sont illustratifs")
        self.assertContains(response, "Petites réparations, remplacement de robinetterie")
        self.assertNotContains(response, "devis")
        self.assertContains(response, "application/ld+json")
        for service in SERVICES:
            self.assertContains(response, service["title"])
            self.assertContains(response, service["image"])
            if service.get("image_license"):
                self.assertContains(response, service["image_credit"])
                self.assertContains(response, service["image_license"])
        self.assertNotContains(response, "Photo : Unsplash")
        self.assertNotContains(response, "Photo : Pexels")
        for project in PROJECTS:
            self.assertContains(response, project["title"])
        for testimonial in TESTIMONIALS:
            self.assertContains(response, testimonial["name"])
            self.assertContains(response, testimonial["image"])
        for item in FAQ_ITEMS:
            self.assertContains(response, item["question"])

    def test_legal_page_renders(self):
        response = self.client.get(reverse("site_vitrine:mentions_legales"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mentions légales")
        self.assertContains(response, "Données personnelles")

    def test_valid_form_creates_request(self):
        response = self.client.post(
            reverse("site_vitrine:index"),
            {
                "nom": "Awa Koné",
                "telephone": "+225 07 49 52 32 96",
                "type_probleme": "fuite",
                "message": "Fuite sous l’évier de la cuisine, merci d’intervenir rapidement.",
                "consentement": "on",
            },
        )

        self.assertEqual(response.status_code, 302)
        whatsapp_url = urlparse(response.url)
        self.assertEqual(whatsapp_url.netloc, "wa.me")
        self.assertEqual(whatsapp_url.path, f"/{BUSINESS['whatsapp']}")
        text = parse_qs(whatsapp_url.query)["text"][0]
        self.assertIn("Awa Koné", text)
        self.assertIn("+225 07 49 52 32 96", text)
        self.assertIn("Fuite d’eau", text)
        self.assertIn("Fuite sous l’évier de la cuisine", text)

        self.assertEqual(DemandeDevis.objects.count(), 1)
        demande = DemandeDevis.objects.get()
        self.assertEqual(demande.nom, "Awa Koné")
        self.assertEqual(demande.type_probleme, "fuite")

    def test_invalid_phone_is_rejected(self):
        response = self.client.post(
            reverse("site_vitrine:index"),
            {
                "nom": "Awa Koné",
                "telephone": "abc",
                "type_probleme": "fuite",
                "message": "Fuite sous l’évier de la cuisine.",
                "consentement": "on",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Utilisez uniquement des chiffres")
        self.assertEqual(DemandeDevis.objects.count(), 0)

    def test_consent_is_required(self):
        response = self.client.post(
            reverse("site_vitrine:index"),
            {
                "nom": "Awa Koné",
                "telephone": "07 49 52 32 96",
                "type_probleme": "fuite",
                "message": "Fuite sous l’évier de la cuisine.",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Merci de cocher cette case")
        self.assertEqual(DemandeDevis.objects.count(), 0)
