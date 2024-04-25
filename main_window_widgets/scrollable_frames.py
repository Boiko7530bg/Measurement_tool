import customtkinter


class MainWindowScrollableFrames(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.measurement_preview_frame = customtkinter.CTkScrollableFrame(master, width=470, height=230)
        self.measurement_preview_frame.place(x=155, y=200)
