import customtkinter as ctk
from Buttons import *
from settings import *
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BLACK)

        # App attributes
        self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}")
        self.resizable(False, False)
        self.title("")
        self.title_bar_color()

        # making the grid
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform="a")
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform="a")

        # calling classes
        Input(self)
        Output(self)

        # buttons
        Numbers(self)

        # run
        self.mainloop()

    def title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_BAR_HEX_COLOURS["dark"]
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass


class Input(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=BLACK)
        global input_variable
        input_variable = ctk.StringVar(value="")
        input_label = ctk.CTkLabel(
            master=self, font=(FONT, NORMAL_FONT_SIZE), text=input_variable.get(), fg_color=BLACK, text_color=WHITE
        )
        input_label.pack()
        self.grid(row=0, rowspan=1, column=0, columnspan=4, sticky="e")


class Output(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        global output_variable
        output_variable = ctk.StringVar(value="")
        output_label = ctk.CTkLabel(
            master=self, font=(FONT, OUTPUT_FONT_SIZE), text=output_variable.get(), fg_color=BLACK, text_color=WHITE
        )
        output_label.pack()
        self.grid(row=1, rowspan=1, column=0, columnspan=4, sticky="e")

if __name__ == "__main__":
    App()