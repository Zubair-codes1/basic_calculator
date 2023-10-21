import customtkinter as ctk
from Buttons import Button, NumButton, OperatorButton
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

        # variables
        self.input_value = ctk.StringVar(value="")
        self.output_variable = ctk.StringVar(value="0")
        self.display_nums = []
        self.full_operation = []

        # calling classes
        Input(self, self.input_value)
        Output(self, self.output_variable)

        # buttons
        Button(
            parent=self, func=self.clear, text=OPERATORS["clear"]["text"], font=(FONT, NORMAL_FONT_SIZE),
            col=OPERATORS["clear"]["col"], row=OPERATORS["clear"]["row"]
        )
        Button(
            parent=self, func=self.invert, text=OPERATORS["invert"]["text"], font=(FONT, NORMAL_FONT_SIZE),
            col=OPERATORS["invert"]["col"], row=OPERATORS["invert"]["row"]
        )
        Button(
            parent=self, func=self.percent, text=OPERATORS["percent"]["text"], font=(FONT, NORMAL_FONT_SIZE),
            col=OPERATORS["percent"]["col"], row=OPERATORS["percent"]["row"]
        )

        for num, data in NUM_POSITIONS.items():
            NumButton(
                parent=self, text=num, font=(FONT, NORMAL_FONT_SIZE),
                func=self.num_press, col=data["col"],
                row=data["row"], span=data["span"]
            )

        for operator, dictionary in MATH_POSITIONS.items():
            OperatorButton(
                parent=self, text=operator, font=(FONT, NORMAL_FONT_SIZE),
                func=self.operator_press, col=dictionary["col"],
                row=dictionary["row"]
            )

        # run
        self.mainloop()

    # button functions
    def clear(self):
        self.display_nums.clear()
        self.full_operation.clear()
        self.output_variable.set(self.display_nums)
        self.input_value.set(self.full_operation)

    def percent(self):
        if self.display_nums:
            current_number = float("".join(self.display_nums))
            percent_number = current_number / 100

            self.display_nums = list(str(percent_number))
            self.output_variable.set("".join(self.display_nums))

    def invert(self):
        current_number = "".join(self.display_nums)
        if current_number:
            if float(current_number) > 0:
                self.display_nums.insert(0, "-")
            else:
                del self.display_nums[0]

            self.output_variable.set("".join(self.display_nums))

    def num_press(self, value):
        self.display_nums.append(str(value))
        full_number = "".join(self.display_nums)
        self.output_variable.set(full_number)

    def operator_press(self, operator_type):
        current_number = "".join(self.display_nums)

        if current_number:
            self.full_operation.append(current_number)

            if operator_type != "=":
                # update data
                self.full_operation.append(operator_type)
                self.display_nums.clear()

                # update output
                self.output_variable.set("")
                self.input_value.set(" ".join(self.full_operation))
            else:
                formula = " ".join(self.full_operation)
                result = eval(formula)

                # format the result
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 4)

                # update data
                self.full_operation.clear()
                self.display_nums = [str(result)]

                # update my output
                self.output_variable.set(result)
                self.input_value.set(formula)

    def title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_BAR_HEX_COLOURS["dark"]
            windll.dwmapi.DwmSetWindowAttribute(
                HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int)
            )
        except:
            pass


class Input(ctk.CTkLabel):
    def __init__(self, parent, input_value):
        super().__init__(
            master=parent, fg_color=BLACK, text="",
            textvariable=input_value, font=(FONT, NORMAL_FONT_SIZE)
        )
        self.grid(row=0, rowspan=1, column=0, columnspan=4, sticky="se")


class Output(ctk.CTkLabel):
    def __init__(self, parent, output_variable):
        super().__init__(
            master=parent, textvariable=output_variable, font=(FONT, OUTPUT_FONT_SIZE)
        )
        self.grid(row=1, rowspan=1, column=0, columnspan=4, sticky="se")

if __name__ == "__main__":
    App()