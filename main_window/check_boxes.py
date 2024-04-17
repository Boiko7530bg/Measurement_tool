import customtkinter


class MainWindowCheckBoxes(customtkinter.CTkCheckBox):
    def __init__(self, master):
        super().__init__(master)

        self.measure_by_lines = customtkinter.CTkCheckBox(master, text="Lines", onvalue="on", offvalue="off")
        self.measure_by_lines.place(x=5, y=290)

        self.measure_by_items = customtkinter.CTkCheckBox(master, text="Items", onvalue="on", offvalue="off")
        self.measure_by_items.place(x=5, y=320)

        self.measure_by_other = customtkinter.CTkCheckBox(master, text="Other", onvalue="on", offvalue="off")
        self.measure_by_other.place(x=5, y=350)
