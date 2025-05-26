import reflex as rx
from app.states.state import DelicesGourmetsState
from app.components.navbar import navbar
from app.components.hero import hero_section
from app.components.about import about_section
from app.components.services import services_section
from app.components.menu_gallery import menu_gallery_section
from app.components.testimonials import testimonials_section
from app.components.contact_form import contact_section
from app.components.footer import footer


def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        hero_section(),
        about_section(),
        services_section(),
        menu_gallery_section(),
        testimonials_section(),
        contact_section(),
        footer(),
        class_name="font-['Inter'] bg-stone-50 text-neutral-800",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
        rx.el.style(
            "\n            html {\n                scroll-behavior: smooth;\n            }\n            /* Custom scrollbar for webkit browsers */\n            ::-webkit-scrollbar {\n                width: 8px;\n            }\n            ::-webkit-scrollbar-track {\n                background: #f1f1f1;\n            }\n            ::-webkit-scrollbar-thumb {\n                background: #eab308; /* yellow-500 */\n                border-radius: 4px;\n            }\n            ::-webkit-scrollbar-thumb:hover {\n                background: #ca8a04; /* yellow-600 */\n            }\n            "
        ),
    ],
)
app.add_page(
    index, title="Délices Gourmets - Traiteur d'Exception"
)