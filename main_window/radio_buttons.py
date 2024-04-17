import customtkinter


class MainWindowRaioButtons(customtkinter.CTkRadioButton):
    def __init__(self, master):
        super().__init__(master)

        self.measure_lines_radio = customtkinter.CTkRadioButton(master, text="Lines", border_color="grey40")
        self.measure_lines_radio.place(x=5, y=290)

        self.measure_items_radio = customtkinter.CTkRadioButton(master, text="Items", border_color="grey40")
        self.measure_items_radio.place(x=5, y=320)

        self.measure_other_radio = customtkinter.CTkRadioButton(master, text="Other", border_color="grey40")
        self.measure_other_radio.place(x=5, y=350)
