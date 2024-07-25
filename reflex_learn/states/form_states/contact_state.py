import reflex as rx

class ContactState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data:dict):
        print(form_data)
        self.form_data = form_data
