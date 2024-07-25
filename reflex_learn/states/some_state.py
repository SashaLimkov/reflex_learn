import reflex as rx
import random


class State(rx.State):
    """The app state."""
    label = "Тест"
    size = "9"
    
    def reverse_label(self):
        self.label = self.label[::-1]
        
    def change_size(self):
        self.size = str(random.randint(1, 9))

    def handle_blur(self, val):
        self.label = val
