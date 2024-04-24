import customtkinter


class MainWindowLabels(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)

        self.measure_type_label = customtkinter.CTkLabel(master, text="Measure by:", fg_color="grey20", width=150,
                                                         font=("halvetika", 15))
        self.measure_type_label.place(x=1, y=250)

        self.select_team_label = customtkinter.CTkLabel(master, text="Client:", fg_color="grey20", width=150,
                                                        font=("halvetika", 15))
        self.select_team_label.place(x=650, y=1)

        self.select_team_person = customtkinter.CTkLabel(master, text="Team member:", fg_color="grey20", width=150,
                                                         font=("halvetika", 15))
        self.select_team_person.place(x=650, y=80)

        self.comments_label = customtkinter.CTkLabel(master, text="", fg_color="grey20", corner_radius=6, width=350, height=40,
                                                         font=("halvetika", 10))
        self.comments_label.place(x=155, y=150)

        self.select_team_process = customtkinter.CTkLabel(master, text="Process:", fg_color="grey20", width=150,
                                                         font=("halvetika", 15))
        self.select_team_process.place(x=650, y=160)