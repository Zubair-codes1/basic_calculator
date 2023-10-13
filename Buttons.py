import customtkinter as ctk
from settings import *

class Numbers(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(row=4, rowspan=4, column=0, columnspan=3)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")

        self.make_buttons()

    def make_buttons(self):
        number = ctk.StringVar(value="1")
        for i in range(1, 10):
            button = ctk.CTkButton(
                self, fg_color=COLORS["light-gray"]["fg"][1], textvariable=number.get(), text_color=BLACK,
                hover_color=COLORS["light-gray"]["hover"][0]
            )
            button.pack()
            number.set(int(number.get()) + 1)

