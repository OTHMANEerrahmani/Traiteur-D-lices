import reflex as rx
from app.states.state import DelicesGourmetsState


def menu_item_card(item: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=item["image_url"],
            class_name="w-full h-48 object-cover rounded-t-lg",
        ),
        rx.el.div(
            rx.el.h3(
                item["name"],
                class_name="text-xl font-semibold text-neutral-800 mb-1",
            ),
            rx.el.p(
                item["description"],
                class_name="text-neutral-700 text-sm",
            ),
            class_name="p-4",
        ),
        class_name="bg-white rounded-lg shadow-lg overflow-hidden",
    )


def gallery_image_item(
    image_url: rx.Var[str],
) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=image_url,
            class_name="w-full h-full object-cover rounded-lg transform hover:scale-105 transition-transform duration-300",
        ),
        class_name="aspect-square",
    )


def menu_gallery_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Saveurs & Inspirations",
                class_name="text-4xl font-bold text-neutral-900 text-center mb-4",
            ),
            rx.el.p(
                "Découvrez un aperçu de nos créations culinaires et des événements que nous avons sublimés.",
                class_name="text-yellow-600 text-center text-lg mb-12",
            ),
            rx.el.h3(
                "Extraits de Menus",
                class_name="text-3xl font-semibold text-neutral-800 mb-8 text-center",
            ),
            rx.el.div(
                rx.foreach(
                    DelicesGourmetsState.menu_items,
                    menu_item_card,
                ),
                class_name="grid md:grid-cols-3 gap-8 mb-16",
            ),
            rx.el.h3(
                "Galerie d'Événements",
                class_name="text-3xl font-semibold text-neutral-800 mb-8 text-center",
            ),
            rx.el.div(
                rx.foreach(
                    DelicesGourmetsState.gallery_images,
                    gallery_image_item,
                ),
                class_name="grid grid-cols-2 md:grid-cols-3 gap-4",
            ),
            class_name="container mx-auto py-16 px-6",
        ),
        id="menu-gallery",
        class_name="bg-stone-50",
    )