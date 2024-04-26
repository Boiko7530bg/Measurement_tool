import customtkinter


class MainWindowCheckBoxes(customtkinter.CTkCheckBox):
    def __init__(self, master):
        super().__init__(master)

        self.measure_by_lines = customtkinter.CTkCheckBox(master, text="Lines", onvalue="on", offvalue="off")
        self.measure_by_lines.place(x=5, y=260)
        self.measure_by_lines.configure(command=lambda: self.checkbox_state(self.measure_by_lines))

        self.measure_by_items = customtkinter.CTkCheckBox(master, text="Items", onvalue="on", offvalue="off")
        self.measure_by_items.place(x=5, y=290)
        self.measure_by_items.configure(command=lambda: self.checkbox_state(self.measure_by_items))

        self.measure_by_other = customtkinter.CTkCheckBox(master, text="Other", onvalue="on", offvalue="off")
        self.measure_by_other.place(x=5, y=380)
        self.measure_by_other.configure(command=lambda: self.checkbox_state(self.measure_by_other))

    def checkbox_state(self, checkbox):
        if checkbox == self.measure_by_lines:
            self.measure_by_items.deselect()
            self.measure_by_other.deselect()
        elif checkbox == self.measure_by_items:
            self.measure_by_lines.deselect()
            self.measure_by_other.deselect()
        else:
            self.measure_by_items.deselect()
            self.measure_by_lines.deselect()
