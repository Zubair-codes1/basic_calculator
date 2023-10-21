import customtkinter as ctk
from main import *
from settings import *

class Button(ctk.CTkButton):
    def __init__(self, parent, text, font, func, col, row, span=1, colour='dark-gray'):
        super().__init__(
            master=parent, command=func, text=text,
            corner_radius=STYLING["corner-radius"], font=font,
            fg_color=COLORS[colour]["fg"][1], hover_color=COLORS[colour]["hover"][1],
            text_color=COLORS[colour]["text"][1]
        )
        self.grid(
            column=col, columnspan=span, row=row, sticky="nsew",
            padx=STYLING["gap"], pady=STYLING["gap"]
        )

class NumButton(Button):
    def __init__(self, parent, text, font, func, col, row, span, colour='light-gray'):
        super().__init__(
            parent=parent, text=text, func=lambda: func(text), font=font, col=col,
            row=row, colour=colour, span=span
        )

class OperatorButton(Button):
    def __init__(self, parent, text, font, func, col, row):
        super().__init__(
            parent=parent, text=text, font=font,
            func=lambda: func(MATH_POSITIONS[text]["operator"]), col=col, row=row
        )
        self.configure(
            fg_color=COLORS["orange"]["fg"], text_color=COLORS["orange"]["text"][1],
            hover_color=COLORS["orange"]["hover"]
        )