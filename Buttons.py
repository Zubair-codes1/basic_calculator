import customtkinter as ctk
from settings import *

class Buttons(ctk.CTkButton):
    def __init__(self, parent, text, fg_colour, text_color, font, hover_color, col, row, command, output=None,
                 input_data=None):
        super().__init__(
            master=parent, text=text, fg_color=fg_colour, text_color=text_color, font=font,
            hover_color=hover_color, command=command
        )
        self.output = output
        self.input_data = input_data
        self.grid(row=row, column=col, sticky="NSEW")
    def clear(self):
        self.output.set("")
    def invert(self):
        self.output.set(f"{self.output.get() * -1}")
    def modulus(self):
        self.input_data.set(self.input_data.get() + "%")
