import reflex as rx
from .base import base_page
from ..states.some_state import State

def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.heading(State.label, size=State.size),
            rx.input(on_blur=State.handle_blur),
            rx.text(
                "Get started by editing ",
                size="5",
            ),
            rx.hstack(
                rx.button("Reverse", on_click=State.reverse_label),
                rx.button("Change size", on_click=State.change_size)
                ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            text_align="center",
            align="center",
        )
    )