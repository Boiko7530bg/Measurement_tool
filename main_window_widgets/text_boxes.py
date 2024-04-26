import customtkinter


class MainWindowTextBoxes(customtkinter.CTkTextbox):
    def __init__(self, master):
        super().__init__(master)

        self.measure_other_textbox = customtkinter.CTkTextbox(master, width=150, height=30, corner_radius=4,
                                                              border_width=2)
        self.measure_other_textbox.place(x=1, y=410)

        self.add_comment_textbox = customtkinter.CTkTextbox(master, width=320, height=20, corner_radius=6,
                                                            border_width=2)
        self.add_comment_textbox.place(x=169, y=155)

        self.measure_count_textbox = customtkinter.CTkTextbox(master, width=150, height=30, corner_radius=4,
                                                              border_width=2)
        self.measure_count_textbox.place(x=1, y=320)
