import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h4(
                        "Délices Gourmets",
                        class_name="text-xl font-semibold text-neutral-200 mb-3",
                    ),
                    rx.el.p(
                        "L'art de recevoir avec goût.",
                        class_name="text-neutral-400 text-sm",
                    ),
                ),
                rx.el.div(
                    rx.el.h4(
                        "Contact",
                        class_name="text-lg font-semibold text-neutral-200 mb-3",
                    ),
                    rx.el.p(
                        "Téléphone: +33 1 23 45 67 89",
                        class_name="text-neutral-400 text-sm mb-1",
                    ),
                    rx.el.p(
                        "Email: contact@delicesgourmets.fr",
                        class_name="text-neutral-400 text-sm",
                    ),
                    rx.el.p(
                        "Adresse: 123 Rue de la Gastronomie, 75000 Paris",
                        class_name="text-neutral-400 text-sm mt-1",
                    ),
                ),
                rx.el.div(
                    rx.el.h4(
                        "Suivez-nous",
                        class_name="text-lg font-semibold text-neutral-200 mb-3",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon(
                                tag="instagram",
                                class_name="h-6 w-6 hover:text-yellow-400 transition-colors",
                            ),
                            href="#",
                            target="_blank",
                        ),
                        rx.el.a(
                            rx.icon(
                                tag="facebook",
                                class_name="h-6 w-6 hover:text-yellow-400 transition-colors",
                            ),
                            href="#",
                            target="_blank",
                        ),
                        rx.el.a(
                            rx.icon(
                                tag="message-circle",
                                class_name="h-6 w-6 hover:text-yellow-400 transition-colors",
                            ),
                            href="#",
                            target="_blank",
                        ),
                        class_name="flex space-x-4 text-neutral-300",
                    ),
                ),
                class_name="container mx-auto grid md:grid-cols-3 gap-8 py-12 px-6",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 Délices Gourmets. Tous droits réservés.",
                    class_name="text-neutral-500 text-sm",
                ),
                rx.el.a(
                    "Mentions Légales",
                    href="#",
                    class_name="text-neutral-500 hover:text-yellow-400 text-sm transition-colors",
                ),
                rx.icon(
                    tag="utensils",
                    class_name="h-5 w-5 text-neutral-600 ml-4",
                ),
                class_name="container mx-auto flex justify-between items-center border-t border-neutral-700 py-6 px-6",
            ),
            class_name="bg-neutral-900 text-neutral-300",
        )
    )