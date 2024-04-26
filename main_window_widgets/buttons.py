import customtkinter

from stopwatch import StopWatch


class MainWindowButtons(customtkinter.CTkButton):
    def __init__(self, master):
        super().__init__(master)

        self.start_button = customtkinter.CTkButton(master, text="Start timer",
                                                    command=master.start_measurement)
        self.start_button.place(x=5, y=10)

        self.pause_button = customtkinter.CTkButton(master, text="Pause",
                                                    command=master.pause_measurement,
                                                    state=customtkinter.DISABLED)
        self.pause_button.place(x=5, y=60)

        self.stop_button = customtkinter.CTkButton(master, text="End timer",
                                                   command=master.end_measurement,
                                                   state=customtkinter.DISABLED)
        self.stop_button.place(x=5, y=150)

        self.archive_button = customtkinter.CTkButton(master, text="Archive")
        self.archive_button.place(x=655, y=450)

        self.add_comment_button = customtkinter.CTkButton(master, text="Add comment")
        self.add_comment_button.place(x=508, y=155)

        self.admin_button = customtkinter.CTkButton(master, text="Admin")
        self.admin_button.place(x=1, y=450)
