import customtkinter


class MainWindowFrames(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.left_frame = customtkinter.CTkFrame(master, width=150, height=600)
        self.left_frame.place(x=1, y=1)

        self.right_frame = customtkinter.CTkFrame(master, width=150, height=600)
        self.right_frame.place(x=650, y=1)
