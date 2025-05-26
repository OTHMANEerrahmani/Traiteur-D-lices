import reflex as rx
from app.states.state import DelicesGourmetsState


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.icon(
                    tag="utensils-crossed",
                    class_name="h-8 w-8 text-yellow-500",
                ),
                href="/",
                class_name="text-2xl font-bold text-neutral-900",
            ),
            rx.el.nav(
                rx.el.ul(
                    rx.el.li(
                        rx.el.a(
                            "Accueil",
                            on_click=DelicesGourmetsState.scroll_to_section(
                                "hero"
                            ),
                            class_name="hover:text-yellow-500 transition-colors",
                        )
                    ),
                    rx.el.li(
                        rx.el.a(
                            "À Propos",
                            on_click=DelicesGourmetsState.scroll_to_section(
                                "about"
                            ),
                            class_name="hover:text-yellow-500 transition-colors",
                        )
                    ),
                    rx.el.li(
                        rx.el.a(
                            "Nos Services",
                            on_click=DelicesGourmetsState.scroll_to_section(
                                "services"
                            ),
                            class_name="hover:text-yellow-500 transition-colors",
                        )
                    ),
                    rx.el.li(
                        rx.el.a(
                            "Menu & Galerie",
                            on_click=DelicesGourmetsState.scroll_to_section(
                                "menu-gallery"
                            ),
                            class_name="hover:text-yellow-500 transition-colors",
                        )
                    ),
                    rx.el.li(
                        rx.el.a(
                            "Témoignages",
                            on_click=DelicesGourmetsState.scroll_to_section(
                                "testimonials"
                            ),
                            class_name="hover:text-yellow-500 transition-colors",
                        )
                    ),
                    rx.el.li(
                        rx.el.a(
                            "Contact",
                            on_click=DelicesGourmetsState.scroll_to_section(
                                "contact"
                            ),
                            class_name="hover:text-yellow-500 transition-colors",
                        )
                    ),
                    class_name="hidden md:flex space-x-6 items-center text-neutral-700 font-medium",
                )
            ),
            rx.el.button(
                "Réserver maintenant",
                on_click=DelicesGourmetsState.scroll_to_section(
                    "contact"
                ),
                class_name="bg-yellow-500 text-white px-6 py-2 rounded-lg font-semibold hover:bg-yellow-600 transition-colors shadow-md",
            ),
            rx.el.button(
                rx.icon(tag="menu", class_name="h-6 w-6"),
                class_name="md:hidden text-neutral-700",
            ),
            class_name="container mx-auto flex justify-between items-center py-4 px-6",
        ),
        class_name="sticky top-0 z-50 bg-stone-50/80 backdrop-blur-md shadow-sm",
    )