import reflex as rx
from app.states.state import DelicesGourmetsState


def form_input(
    label: str,
    name: str,
    type: str = "text",
    placeholder: str = "",
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            html_for=name,
            class_name="block text-sm font-medium text-neutral-700 mb-1",
        ),
        rx.el.input(
            type=type,
            id=name,
            name=name,
            placeholder=placeholder,
            on_change=lambda value: DelicesGourmetsState.handle_form_change(
                name, value
            ),
            default_value=DelicesGourmetsState.form_data[
                name
            ],
            class_name="w-full p-3 border border-neutral-300 rounded-md shadow-sm focus:ring-yellow-500 focus:border-yellow-500",
        ),
        class_name="mb-4",
    )


def contact_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Contactez-Nous",
                class_name="text-4xl font-bold text-neutral-900 text-center mb-4",
            ),
            rx.el.p(
                "Discutons de votre prochain événement et créons ensemble une expérience culinaire mémorable.",
                class_name="text-yellow-600 text-center text-lg mb-12",
            ),
            rx.el.form(
                rx.el.div(
                    form_input(
                        "Prénom",
                        "first_name",
                        placeholder="Votre prénom",
                    ),
                    form_input(
                        "Nom",
                        "last_name",
                        placeholder="Votre nom",
                    ),
                    class_name="grid md:grid-cols-2 gap-6",
                ),
                form_input(
                    "E-mail",
                    "email",
                    type="email",
                    placeholder="Votre adresse e-mail",
                ),
                form_input(
                    "Type d'événement",
                    "event_type",
                    placeholder="Ex: Mariage, Cocktail, Entreprise",
                ),
                form_input(
                    "Date souhaitée",
                    "event_date",
                    type="date",
                ),
                rx.el.div(
                    rx.el.label(
                        "Votre message",
                        html_for="message",
                        class_name="block text-sm font-medium text-neutral-700 mb-1",
                    ),
                    rx.el.textarea(
                        id="message",
                        name="message",
                        placeholder="Décrivez-nous vos besoins...",
                        on_change=lambda value: DelicesGourmetsState.handle_form_change(
                            "message", value
                        ),
                        default_value=DelicesGourmetsState.form_data[
                            "message"
                        ],
                        rows=4,
                        class_name="w-full p-3 border border-neutral-300 rounded-md shadow-sm focus:ring-yellow-500 focus:border-yellow-500",
                    ),
                    class_name="mb-6",
                ),
                rx.el.button(
                    "Envoyer la demande",
                    type="submit",
                    class_name="w-full bg-yellow-500 text-white py-3 px-6 rounded-lg font-semibold hover:bg-yellow-600 transition-colors shadow-md",
                ),
                rx.cond(
                    DelicesGourmetsState.form_submitted_successfully,
                    rx.el.div(
                        rx.icon(
                            tag="check_check",
                            class_name="text-green-500 mr-2",
                        ),
                        "Votre message a été envoyé avec succès!",
                        class_name="mt-4 p-3 bg-green-100 border border-green-300 text-green-700 rounded-md flex items-center",
                    ),
                    rx.fragment(),
                ),
                on_submit=DelicesGourmetsState.handle_submit,
                reset_on_submit=True,
                class_name="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-xl",
            ),
            class_name="container mx-auto py-16 px-6",
        ),
        id="contact",
        class_name="bg-stone-50",
    )