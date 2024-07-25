import reflex as rx
from ...states.form_states.contact_state import ContactState

def contuct_us_form() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="First Name",
                    name="first_name",
                    required=True,
                    width="100%",
                ),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                    width="100%",
                ),
                rx.text_area(
                    name="message",
                    placeholder="Message",
                    width="100%",
                    ),
                rx.button("Submit", type="submit"),
                align="center",
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(ContactState.form_data.to_string()),
    )