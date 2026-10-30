/* ==========================================================================
   Rufus Plomberie — Interactions du site
   JavaScript natif, sans dépendance.
   ========================================================================== */

(() => {
    "use strict";

    const prefersReducedMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    /* ---------------------------------------------------------------------
       En-tête, menu mobile et bouton retour en haut
       --------------------------------------------------------------------- */
    const header = document.querySelector("[data-header]");
    const menuToggle = document.querySelector("[data-menu-toggle]");
    const nav = document.querySelector("[data-nav]");
    const menuLabel = document.querySelector("[data-menu-label]");
    const backToTop = document.querySelector("[data-back-to-top]");

    const closeMenu = () => {
        if (!header || !menuToggle) return;
        header.classList.remove("is-open");
        document.body.classList.remove("menu-open");
        menuToggle.setAttribute("aria-expanded", "false");
        if (menuLabel) menuLabel.textContent = "Ouvrir le menu";
    };

    const openMenu = () => {
        if (!header || !menuToggle) return;
        header.classList.add("is-open");
        document.body.classList.add("menu-open");
        menuToggle.setAttribute("aria-expanded", "true");
        if (menuLabel) menuLabel.textContent = "Fermer le menu";
    };

    if (menuToggle) {
        menuToggle.addEventListener("click", () => {
            const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
            isOpen ? closeMenu() : openMenu();
        });
    }

    if (nav) {
        nav.addEventListener("click", (event) => {
            if (event.target.closest("a")) closeMenu();
        });
    }

    document.addEventListener("click", (event) => {
        if (
            header &&
            header.classList.contains("is-open") &&
            !header.contains(event.target)
        ) {
            closeMenu();
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && header?.classList.contains("is-open")) {
            closeMenu();
            menuToggle?.focus();
        }
    });

    window.addEventListener(
        "resize",
        () => {
            if (window.innerWidth >= 980) closeMenu();
        },
        { passive: true }
    );

    const handleScroll = () => {
        if (header) {
            header.classList.toggle("is-scrolled", window.scrollY > 8);
        }
        if (backToTop) {
            backToTop.hidden = window.scrollY < 600;
        }
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    handleScroll();

    if (backToTop) {
        backToTop.addEventListener("click", () => {
            window.scrollTo({
                top: 0,
                behavior: prefersReducedMotion ? "auto" : "smooth",
            });
        });
    }

    /* ---------------------------------------------------------------------
       Apparition douce des blocs au défilement
       --------------------------------------------------------------------- */
    const revealItems = document.querySelectorAll(".reveal");

    if (!prefersReducedMotion && "IntersectionObserver" in window) {
        const revealObserver = new IntersectionObserver(
            (entries, observer) => {
                entries.forEach((entry) => {
                    if (!entry.isIntersecting) return;
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                });
            },
            { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
        );

        revealItems.forEach((item) => revealObserver.observe(item));
    } else {
        revealItems.forEach((item) => item.classList.add("is-visible"));
    }

    /* ---------------------------------------------------------------------
       Compteurs des chiffres clés
       --------------------------------------------------------------------- */
    const counters = document.querySelectorAll("[data-counter]");

    if (counters.length && !prefersReducedMotion && "IntersectionObserver" in window) {
        const numberFormatter = new Intl.NumberFormat("fr-FR");

        const animateCounter = (element) => {
            const target = Number.parseInt(element.dataset.counter, 10);
            if (Number.isNaN(target)) return;

            const duration = 1400;
            const startTime = performance.now();

            const update = (now) => {
                const progress = Math.min((now - startTime) / duration, 1);
                const eased = 1 - Math.pow(1 - progress, 3);
                element.textContent = numberFormatter.format(
                    Math.round(target * eased)
                );
                if (progress < 1) {
                    window.requestAnimationFrame(update);
                } else {
                    element.textContent = numberFormatter.format(target);
                }
            };

            window.requestAnimationFrame(update);
        };

        const counterObserver = new IntersectionObserver(
            (entries, observer) => {
                entries.forEach((entry) => {
                    if (!entry.isIntersecting) return;
                    animateCounter(entry.target);
                    observer.unobserve(entry.target);
                });
            },
            { threshold: 0.6 }
        );

        counters.forEach((counter) => counterObserver.observe(counter));
    }

    /* ---------------------------------------------------------------------
       Comparateur avant / après
       --------------------------------------------------------------------- */
    document.querySelectorAll("[data-compare]").forEach((compare) => {
        const range = compare.querySelector("[data-compare-range]");
        if (!range) return;

        const updatePosition = () => {
            compare.style.setProperty("--position", `${range.value}%`);
        };

        range.addEventListener("input", updatePosition);
        range.addEventListener("change", updatePosition);
        updatePosition();
    });

    /* ---------------------------------------------------------------------
       Accordéon FAQ : une seule réponse ouverte à la fois
       --------------------------------------------------------------------- */
    const faqItems = document.querySelectorAll(".faq__item");

    faqItems.forEach((item) => {
        item.addEventListener("toggle", () => {
            if (!item.open) return;
            faqItems.forEach((other) => {
                if (other !== item) other.open = false;
            });
        });
    });

    /* ---------------------------------------------------------------------
       Préremplissage du formulaire depuis une carte de service
       --------------------------------------------------------------------- */
    const problemSelect = document.getElementById("id_type_probleme");

    document.querySelectorAll("[data-service-link]").forEach((link) => {
        link.addEventListener("click", () => {
            if (!problemSelect) return;
            problemSelect.value = link.dataset.serviceLink;
            problemSelect.dispatchEvent(new Event("change", { bubbles: true }));
        });
    });

    /* ---------------------------------------------------------------------
       Validation côté client du formulaire de demande de service
       --------------------------------------------------------------------- */
    const form = document.querySelector("[data-contact-form]");

    if (form) {
        const fields = {
            nom: document.getElementById("id_nom"),
            telephone: document.getElementById("id_telephone"),
            type_probleme: document.getElementById("id_type_probleme"),
            message: document.getElementById("id_message"),
            consentement: document.getElementById("id_consentement"),
        };

        const getErrorElement = (field) =>
            document.querySelector(`[data-error-for="${field.id}"]`);

        const setFieldError = (field, message) => {
            const wrapper = field.closest(".field");
            const errorElement = getErrorElement(field);

            wrapper?.classList.add("field--error");
            field.setAttribute("aria-invalid", "true");
            if (errorElement) errorElement.textContent = message;
        };

        const clearFieldError = (field) => {
            const wrapper = field.closest(".field");
            const errorElement = getErrorElement(field);

            wrapper?.classList.remove("field--error");
            field.removeAttribute("aria-invalid");
            if (errorElement) errorElement.textContent = "";
        };

        const validateField = (field) => {
            if (!field) return true;

            let message = "";
            const value = field.value.trim();

            switch (field.id) {
                case "id_nom":
                    if (value.length < 2) {
                        message = "Merci d’indiquer votre nom complet.";
                    }
                    break;

                case "id_telephone": {
                    if (!value) {
                        message = "Merci d’indiquer votre numéro de téléphone.";
                        break;
                    }
                    if (!/^[0-9+\s().-]+$/.test(value)) {
                        message =
                            "Utilisez uniquement des chiffres, espaces, tirets ou le signe +.";
                        break;
                    }
                    const digits = value.replace(/\D/g, "");
                    if (digits.length < 8 || digits.length > 15) {
                        message = "Le numéro doit contenir entre 8 et 15 chiffres.";
                    }
                    break;
                }

                case "id_type_probleme":
                    if (!value) {
                        message = "Sélectionnez le type de problème.";
                    }
                    break;

                case "id_message":
                    if (value.length < 10) {
                        message = "Décrivez votre besoin en au moins 10 caractères.";
                    }
                    break;

                case "id_consentement":
                    if (!field.checked) {
                        message =
                            "Merci de cocher cette case pour envoyer votre demande.";
                    }
                    break;

                default:
                    break;
            }

            if (message) {
                setFieldError(field, message);
                return false;
            }

            clearFieldError(field);
            return true;
        };

        Object.values(fields).forEach((field) => {
            if (!field) return;

            field.addEventListener("blur", () => validateField(field));
            field.addEventListener("change", () => validateField(field));

            if (field.type !== "checkbox" && field.tagName !== "SELECT") {
                field.addEventListener("input", () => {
                    if (field.closest(".field")?.classList.contains("field--error")) {
                        validateField(field);
                    }
                });
            }
        });

        form.addEventListener("submit", (event) => {
            const invalidFields = [];

            Object.values(fields).forEach((field) => {
                if (field && !validateField(field)) invalidFields.push(field);
            });

            if (invalidFields.length) {
                event.preventDefault();
                invalidFields[0].focus({ preventScroll: true });
                invalidFields[0].scrollIntoView({
                    behavior: prefersReducedMotion ? "auto" : "smooth",
                    block: "center",
                });
                return;
            }

            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.classList.add("is-loading");
                const label = submitButton.querySelector("span");
                if (label) label.textContent = "Envoi en cours…";
            }
        });

        const firstServerError = form.querySelector(".field--error");
        if (firstServerError) {
            window.setTimeout(() => {
                firstServerError.scrollIntoView({
                    behavior: prefersReducedMotion ? "auto" : "smooth",
                    block: "center",
                });
            }, 250);
        }
    }
})();
