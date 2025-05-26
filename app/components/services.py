import reflex as rx
from app.states.state import DelicesGourmetsState


def service_card(service: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.icon(
            tag=service["icon"],
            class_name="h-12 w-12 text-yellow-500 mb-4",
        ),
        rx.el.h3(
            service["title"],
            class_name="text-xl font-semibold text-neutral-800 mb-2",
        ),
        rx.el.p(
            service["description"],
            class_name="text-neutral-700 text-sm mb-4 leading-relaxed",
        ),
        rx.el.button(
            "En savoir plus",
            on_click=DelicesGourmetsState.scroll_to_section(
                "contact"
            ),
            class_name="mt-auto bg-neutral-800 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-neutral-900 transition-colors",
        ),
        class_name="bg-white p-6 rounded-lg shadow-lg flex flex-col items-center text-center h-full transform hover:scale-105 transition-transform duration-300",
    )


def services_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Nos Prestations Sur Mesure",
                class_name="text-4xl font-bold text-neutral-900 text-center mb-4",
            ),
            rx.el.p(
                "Des solutions adaptées à chaque occasion, pour des moments inoubliables.",
                class_name="text-yellow-600 text-center text-lg mb-12",
            ),
            rx.el.div(
                rx.foreach(
                    DelicesGourmetsState.services,
                    service_card,
                ),
                class_name="grid md:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="container mx-auto py-16 px-6",
        ),
        id="services",
        class_name="bg-stone-100",
    )