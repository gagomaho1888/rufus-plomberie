import re

from django import forms

from .models import DemandeDevis
from .site_content import PROBLEM_CHOICES


class DemandeDevisForm(forms.ModelForm):
    """Formulaire de demande de service avec validation côté serveur."""

    class Meta:
        model = DemandeDevis
        fields = ["nom", "telephone", "type_probleme", "message", "consentement"]
        widgets = {
            "nom": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex. Awa Koné",
                    "autocomplete": "name",
                    "aria-describedby": "error-id_nom",
                }
            ),
            "telephone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "tel",
                    "inputmode": "tel",
                    "placeholder": "Ex. 05 85 36 66 65",
                    "autocomplete": "tel",
                    "aria-describedby": "error-id_telephone",
                }
            ),
            "type_probleme": forms.Select(
                attrs={
                    "class": "form-control",
                    "aria-describedby": "error-id_type_probleme",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": (
                        "Décrivez votre problème ou votre projet : type de fuite, "
                        "pièce concernée, délai souhaité…"
                    ),
                    "aria-describedby": "error-id_message",
                }
            ),
            "consentement": forms.CheckboxInput(
                attrs={
                    "class": "checkbox",
                    "aria-describedby": "error-id_consentement",
                }
            ),
        }
        labels = {
            "nom": "Nom complet",
            "telephone": "Téléphone / WhatsApp",
            "type_probleme": "Type de problème",
            "message": "Votre message",
            "consentement": (
                "J’accepte d’être contacté(e) au sujet de ma demande."
            ),
        }
        error_messages = {
            "consentement": {
                "required": "Merci de cocher cette case pour envoyer votre demande.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["type_probleme"].choices = [
            ("", "Sélectionnez votre besoin")
        ] + list(PROBLEM_CHOICES)

    def clean_nom(self):
        nom = self.cleaned_data["nom"].strip()
        if len(nom) < 2:
            raise forms.ValidationError("Merci d’indiquer votre nom complet.")
        return nom

    def clean_telephone(self):
        telephone = self.cleaned_data["telephone"].strip()
        if not re.fullmatch(r"[0-9+\s().-]+", telephone):
            raise forms.ValidationError(
                "Utilisez uniquement des chiffres, espaces, tirets ou le signe +."
            )
        chiffres = re.sub(r"\D", "", telephone)
        if not 8 <= len(chiffres) <= 15:
            raise forms.ValidationError(
                "Le numéro doit contenir entre 8 et 15 chiffres."
            )
        return telephone

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 10:
            raise forms.ValidationError(
                "Décrivez votre besoin en au moins 10 caractères."
            )
        return message

    def clean_consentement(self):
        consentement = self.cleaned_data.get("consentement")
        if not consentement:
            raise forms.ValidationError(
                "Merci de cocher cette case pour envoyer votre demande."
            )
        return consentement
