from django.db import models

from .site_content import PROBLEM_CHOICES


class DemandeDevis(models.Model):
    """Demande envoyée depuis le formulaire de contact."""

    nom = models.CharField("nom complet", max_length=100)
    telephone = models.CharField("téléphone", max_length=30)
    type_probleme = models.CharField(
        "type de problème",
        max_length=30,
        choices=PROBLEM_CHOICES,
    )
    message = models.TextField("message")
    consentement = models.BooleanField(
        "accord pour être recontacté",
        default=False,
    )
    cree_le = models.DateTimeField("créée le", auto_now_add=True)
    traite = models.BooleanField("traitée", default=False)

    class Meta:
        ordering = ["-cree_le"]
        verbose_name = "demande de service"
        verbose_name_plural = "demandes de service"

    def __str__(self):
        return f"{self.nom} – {self.get_type_probleme_display()} ({self.cree_le:%d/%m/%Y})"
