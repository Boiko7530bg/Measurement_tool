import customtkinter


class MainWindowOptionMenus(customtkinter.CTkOptionMenu):
    def __init__(self, master):
        super().__init__(master)

        self.select_team_option = customtkinter.CTkOptionMenu(master, values=["Team1", "Team2", "Team3"],
                                                              anchor="center")
        self.select_team_option.place(x=655, y=40)

        self.select_person_option = customtkinter.CTkOptionMenu(master, values=[f"Person{x}" for x in range(1, 20)],
                                                                anchor="center")
        self.select_person_option.place(x=655, y=120)
