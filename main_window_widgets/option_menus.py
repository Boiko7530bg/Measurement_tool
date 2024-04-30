import customtkinter


class MainWindowOptionMenus(customtkinter.CTkOptionMenu):
    def __init__(self, master):
        super().__init__(master)

        self.select_client_option = customtkinter.CTkOptionMenu(master, values=[f"Client{x}" for x in range(1, 5)],
                                                                anchor="center")
        self.select_client_option.place(x=655, y=40)

        self.select_team_option = customtkinter.CTkOptionMenu(master, values=[f"Team{x}" for x in range(1, 5)],
                                                              anchor="center")
        self.select_team_option.place(x=655, y=120)

        self.select_person_option = customtkinter.CTkOptionMenu(master, values=[f"Person{x}" for x in range(1, 20)],
                                                                anchor="center")
        self.select_person_option.place(x=655, y=200)

        self.select_process_option = customtkinter.CTkOptionMenu(master, values=[f"Process{x}" for x in range(1, 20)],
                                                                 anchor="center")
        self.select_process_option.place(x=655, y=280)
