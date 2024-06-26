import customtkinter

from stopwatch import StopWatch


class MainWindowLabels(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)

        self.measure_type_label = customtkinter.CTkLabel(master, text="Measure by:", fg_color="grey20", width=150,
                                                         font=("halvetika", 15))
        self.measure_type_label.place(x=1, y=220)

        self.select_client_label = customtkinter.CTkLabel(master, text="Client:", fg_color="grey20", width=150,
                                                          font=("halvetika", 15))
        self.select_client_label.place(x=650, y=1)

        self.select_team_label = customtkinter.CTkLabel(master, text="Team:", fg_color="grey20", width=150,
                                                        font=("halvetika", 15))
        self.select_team_label.place(x=650, y=80)

        self.select_team_member_label = customtkinter.CTkLabel(master, text="Team member:", fg_color="grey20",
                                                               width=150,
                                                               font=("halvetika", 15))
        self.select_team_member_label.place(x=650, y=160)

        self.comments_label = customtkinter.CTkLabel(master, text="", fg_color="grey20", corner_radius=6, width=350,
                                                     height=40,
                                                     font=("halvetika", 10))
        self.comments_label.place(x=155, y=150)

        self.select_team_process_label = customtkinter.CTkLabel(master, text="Process:", fg_color="grey20", width=150,
                                                                font=("halvetika", 15))
        self.select_team_process_label.place(x=650, y=240)

        self.timer_label = customtkinter.CTkLabel(master, textvariable=master.stopwatch.time_var, fg_color="grey40",
                                                  width=300,
                                                  height=100,
                                                  font=customtkinter.CTkFont(size=35, weight="bold"), corner_radius=10)
        self.timer_label.place(x=250, y=30)
