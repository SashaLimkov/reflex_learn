import reflex as rx
from .base import base_page
from ..states.some_state import State
from ..components.forms.contact_us import contuct_us_form

def contact_us() -> rx.Component:
    
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.heading("Contact us", size=State.size),
            rx.desktop_only(
                rx.box(
                    contuct_us_form(),
                    width="50vw"
                    ),
                ),
            rx.mobile_and_tablet(
                rx.box(
                    contuct_us_form(),
                    width="50vw"
                    ),
                ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
        )
    )