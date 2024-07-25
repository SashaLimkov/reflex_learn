"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .pages import *
from .data import routes


app = rx.App()
app.add_page(index)
app.add_page(about, routes.ABOUT_ROUTE)
app.add_page(pricing, routes.PRICING_ROUTE)
app.add_page(contact_us, routes.CONTACT_ROUTE)
