import reflex as rx
from typing import TypedDict, List, Dict
from faker import Faker

fake = Faker()


class Service(TypedDict):
    icon: str
    title: str
    description: str


class MenuItem(TypedDict):
    name: str
    description: str
    image_url: str


class Testimonial(TypedDict):
    quote: str
    name: str
    avatar_url: str


class ContactFormData(TypedDict):
    first_name: str
    last_name: str
    email: str
    event_type: str
    event_date: str
    message: str


class DelicesGourmetsState(rx.State):
    form_data: ContactFormData = {
        "first_name": "",
        "last_name": "",
        "email": "",
        "event_type": "",
        "event_date": "",
        "message": "",
    }
    form_submitted_successfully: bool = False
    services: List[Service] = [
        {
            "icon": "martini-glass-citrus",
            "title": "Cocktails et réceptions",
            "description": "Des cocktails dinatoires élégants et des réceptions mémorables pour tous vos événements.",
        },
        {
            "icon": "heart",
            "title": "Mariages",
            "description": "Créez le mariage de vos rêves avec notre service traiteur sur mesure, alliant saveurs et raffinement.",
        },
        {
            "icon": "briefcase",
            "title": "Événements d’entreprise",
            "description": "Solutions gastronomiques pour séminaires, conférences et soirées d'entreprise.",
        },
        {
            "icon": "box",
            "title": "Livraison de plateaux-repas",
            "description": "Des plateaux-repas gourmets livrés directement chez vous ou au bureau, parfaits pour vos déjeuners.",
        },
    ]
    menu_items: List[MenuItem] = [
        {
            "name": "Amuse-bouche Signature",
            "description": "Fine sélection de bouchées créatives pour éveiller les papilles.",
            "image_url": "/placeholder.svg",
        },
        {
            "name": "Plat Principal d'Excellence",
            "description": "Un plat principal raffiné, mettant en valeur des produits de saison.",
            "image_url": "/placeholder.svg",
        },
        {
            "name": "Dessert Divin",
            "description": "Une touche sucrée et artistique pour conclure votre repas en beauté.",
            "image_url": "/placeholder.svg",
        },
    ]
    gallery_images: List[str] = [
        "/placeholder.svg",
        "/placeholder.svg",
        "/placeholder.svg",
        "/placeholder.svg",
        "/placeholder.svg",
        "/placeholder.svg",
    ]
    testimonials: List[Testimonial] = [
        {
            "quote": fake.paragraph(nb_sentences=3),
            "name": fake.name(),
            "avatar_url": f"https://api.dicebear.com/9.x/adventurer/svg?seed={fake.user_name()}",
        },
        {
            "quote": fake.paragraph(nb_sentences=3),
            "name": fake.name(),
            "avatar_url": f"https://api.dicebear.com/9.x/adventurer/svg?seed={fake.user_name()}",
        },
        {
            "quote": fake.paragraph(nb_sentences=3),
            "name": fake.name(),
            "avatar_url": f"https://api.dicebear.com/9.x/adventurer/svg?seed={fake.user_name()}",
        },
    ]

    @rx.event
    def handle_form_change(
        self, field_name: str, value: str
    ):
        self.form_data[field_name] = value

    @rx.event
    def handle_submit(self, form_data: Dict[str, str]):
        print(f"Form submitted: {form_data}")
        self.form_data = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "event_type": "",
            "event_date": "",
            "message": "",
        }
        self.form_submitted_successfully = True
        yield DelicesGourmetsState.reset_submission_status

    @rx.event
    def reset_submission_status(self):
        import asyncio

        yield asyncio.sleep(3)
        self.form_submitted_successfully = False

    def scroll_to_section(self, section_id: str):
        return rx.call_script(
            f"document.getElementById('{section_id}').scrollIntoView({{behavior: 'smooth'}})"
        )