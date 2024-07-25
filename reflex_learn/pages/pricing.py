import reflex as rx
from .base import base_page
from ..states.some_state import State

def pricing() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.heading("Pricing page", size=State.size),
            rx.text(
                "100 000$",
                size="5",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
        )
    )