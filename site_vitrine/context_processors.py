from .site_content import BUSINESS, NAV_LINKS, SERVICES


def site_globals(request):
    """Expose les informations communes à tous les templates."""
    return {
        "business": BUSINESS,
        "nav_links": NAV_LINKS,
        "services": SERVICES,
    }
