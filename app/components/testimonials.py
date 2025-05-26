import reflex as rx
from app.states.state import DelicesGourmetsState


def testimonial_card(
    testimonial: rx.Var[dict],
) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=testimonial["avatar_url"],
            alt=testimonial["name"],
            class_name="w-20 h-20 rounded-full mx-auto mb-4 border-4 border-yellow-400",
        ),
        rx.el.p(
            f'''"{testimonial['quote']}"''',
            class_name="text-neutral-700 italic mb-4 text-center",
        ),
        rx.el.p(
            f"- {testimonial['name']}",
            class_name="text-neutral-900 font-semibold text-center",
        ),
        class_name="bg-white p-8 rounded-lg shadow-xl",
    )


def testimonials_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Ce que nos clients disent",
                class_name="text-4xl font-bold text-neutral-900 text-center mb-4",
            ),
            rx.el.p(
                "La satisfaction de nos clients est notre plus grande récompense.",
                class_name="text-yellow-600 text-center text-lg mb-12",
            ),
            rx.el.div(
                rx.foreach(
                    DelicesGourmetsState.testimonials,
                    testimonial_card,
                ),
                class_name="grid md:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto py-16 px-6",
        ),
        id="testimonials",
        class_name="bg-stone-100",
    )