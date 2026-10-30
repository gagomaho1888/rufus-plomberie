from django.contrib import admin

from .models import DemandeDevis


@admin.register(DemandeDevis)
class DemandeDevisAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "telephone",
        "type_probleme",
        "cree_le",
        "traite",
    )
    list_filter = ("traite", "type_probleme", "cree_le")
    search_fields = ("nom", "telephone", "message")
    list_editable = ("traite",)
    readonly_fields = (
        "nom",
        "telephone",
        "type_probleme",
        "message",
        "consentement",
        "cree_le",
    )
    date_hierarchy = "cree_le"
    actions = ["marquer_comme_traitees"]

    @admin.action(description="Marquer les demandes sélectionnées comme traitées")
    def marquer_comme_traitees(self, request, queryset):
        nombre = queryset.update(traite=True)
        self.message_user(
            request,
            f"{nombre} demande(s) marquée(s) comme traitée(s).",
        )
