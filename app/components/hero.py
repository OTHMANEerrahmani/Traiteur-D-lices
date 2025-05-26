import reflex as rx
from app.states.state import DelicesGourmetsState


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                "L’art de recevoir avec goût",
                class_name="text-5xl md:text-7xl font-bold text-white text-center shadow-lg",
            ),
            rx.el.p(
                "Délices Gourmets, votre partenaire d'exception pour des événements inoubliables.",
                class_name="text-xl md:text-2xl text-stone-200 mt-4 text-center max-w-2xl shadow-md",
            ),
            rx.el.button(
                "Demander un devis",
                on_click=DelicesGourmetsState.scroll_to_section(
                    "contact"
                ),
                class_name="mt-8 bg-yellow-500 text-white px-8 py-3 rounded-lg font-semibold text-lg hover:bg-yellow-600 transition-colors shadow-xl hover:shadow-2xl transform hover:scale-105",
            ),
            class_name="absolute inset-0 flex flex-col items-center justify-center bg-black/50 p-8",
        ),
        id="hero",
        style={
            "background_image": "url('/placeholder.svg')",
            "background_size": "cover",
            "background_position": "center",
        },
        class_name="relative h-screen flex items-center justify-center",
    )