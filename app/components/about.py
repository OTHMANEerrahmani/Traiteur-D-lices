import reflex as rx


def about_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Notre Savoir-Faire",
                class_name="text-4xl font-bold text-neutral-900 text-center mb-4",
            ),
            rx.el.p(
                "Chez Délices Gourmets, nous croyons que chaque événement est unique.",
                class_name="text-yellow-600 text-center text-lg mb-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Notre Histoire",
                        class_name="text-2xl font-semibold text-neutral-800 mb-3",
                    ),
                    rx.el.p(
                        "Fondé par des passionnés de gastronomie, Délices Gourmets est né de l'envie de partager une cuisine authentique et créative. Notre parcours est jalonné d'expériences enrichissantes, nous permettant aujourd'hui de vous offrir un service traiteur d'excellence.",
                        class_name="text-neutral-700 leading-relaxed",
                    ),
                    class_name="md:w-1/2 p-6",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Nos Valeurs",
                        class_name="text-2xl font-semibold text-neutral-800 mb-3",
                    ),
                    rx.el.ul(
                        rx.el.li(
                            rx.icon(
                                tag="leaf",
                                class_name="text-green-500 mr-2",
                            ),
                            "Produits Frais & de Saison: Nous sélectionnons rigoureusement nos ingrédients auprès de producteurs locaux pour garantir fraîcheur et qualité.",
                            class_name="flex items-center mb-2 text-neutral-700",
                        ),
                        rx.el.li(
                            rx.icon(
                                tag="sparkles",
                                class_name="text-yellow-500 mr-2",
                            ),
                            "Créativité Culinaire: Notre chef et son équipe innovent constamment pour vous surprendre avec des saveurs audacieuses et des présentations élégantes.",
                            class_name="flex items-center mb-2 text-neutral-700",
                        ),
                        rx.el.li(
                            rx.icon(
                                tag="concierge-bell",
                                class_name="text-blue-500 mr-2",
                            ),
                            "Service Haut de Gamme: De la planification à la réalisation, nous vous accompagnons avec professionnalisme et attention pour un événement sans fausse note.",
                            class_name="flex items-center text-neutral-700",
                        ),
                        class_name="list-none space-y-3",
                    ),
                    class_name="md:w-1/2 p-6 bg-stone-100 rounded-lg",
                ),
                class_name="flex flex-col md:flex-row gap-8 items-stretch",
            ),
            class_name="container mx-auto py-16 px-6",
        ),
        id="about",
        class_name="bg-stone-50",
    )