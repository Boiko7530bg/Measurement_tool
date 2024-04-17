import time


import customtkinter


from main_window.buttons import MainWindowButtons
from main_window.frames import MainWindowFrames
from measurement_tool.main_window.check_boxes import MainWindowCheckBoxes
from measurement_tool.main_window.labels import MainWindowLabels
from measurement_tool.main_window.option_menus import MainWindowOptionMenus
from measurement_tool.main_window.radio_buttons import MainWindowRaioButtons
from measurement_tool.main_window.text_boxes import MainWindowTextBoxes

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class MeasurementApp(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("Measurement tool V1.0")
        self.geometry(f"{800}x{480}")
        self.resizable(width=False, height=False)

        self.frames = MainWindowFrames(self)
        self.buttons = MainWindowButtons(self)
        self.labels = MainWindowLabels(self)
        self.check_boxes = MainWindowCheckBoxes(self)
        #self.radio_buttons = MainWindowRaioButtons(self)
        self.text_boxes = MainWindowTextBoxes(self)
        self.option_menus = MainWindowOptionMenus(self)

        self.start_time = None
        self.paused_time = None

        self.time_var = customtkinter.StringVar()
        self.time_var.set("00:00:00")
        self.elapsed_time = 0
        self.timer_running = False
        self.timer_stopped = False
        self.timer_label = customtkinter.CTkLabel(self, textvariable=self.time_var, fg_color="grey40", width=300,
                                                  height=100,
                                                  font=customtkinter.CTkFont(size=35, weight="bold"), corner_radius=10)
        self.timer_label.place(x=250, y=30)

    def start_stopwatch(self):
        result = self.handle_checkboxes_before_timer_start()
        if result:
            if self.timer_stopped:
                self.elapsed_time = 0
                self.timer_stopped = False

            if not self.timer_running:
                self.start_time = time.time() - self.elapsed_time
                self.update()
                self.timer_running = True

                self.buttons.start_button.configure(state=customtkinter.DISABLED)
                self.buttons.stop_button.configure(state=customtkinter.NORMAL)
                self.buttons.pause_button.configure(state=customtkinter.NORMAL)
                self.lock_checkboxes_after_timer_start()

    def stop_stopwatch(self):
        self.timer_running = False
        self.timer_stopped = True

        self.buttons.start_button.configure(state=customtkinter.NORMAL)
        self.buttons.stop_button.configure(state=customtkinter.DISABLED)
        self.buttons.pause_button.configure(state=customtkinter.DISABLED)
        self.unlock_checkboxes_after_timer_stop()

    def pause_stopwatch(self):
        if self.timer_running:
            self.paused_time = self.start_time
            self.timer_running = False

            self.buttons.start_button.configure(state=customtkinter.NORMAL)
            self.buttons.stop_button.configure(state=customtkinter.NORMAL)
            self.buttons.pause_button.configure(state=customtkinter.DISABLED)

    def update(self):
        if self.timer_running:
            self.elapsed_time = time.time() - self.start_time

        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)

        self.time_var.set("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
        self.after(1000, self.update)

    def handle_checkboxes_before_timer_start(self):
        checked_values = []
        if self.check_boxes.measure_by_lines.get() == "on":
            checked_values.append("on")
        if self.check_boxes.measure_by_items.get() == "on":
            checked_values.append("on")
        if self.check_boxes.measure_by_other.get() == "on":
            checked_values.append("on")

        return True if len(checked_values) == 1 else False

    def lock_checkboxes_after_timer_start(self):
        self.check_boxes.measure_by_lines.configure(state=customtkinter.DISABLED)
        self.check_boxes.measure_by_items.configure(state=customtkinter.DISABLED)
        self.check_boxes.measure_by_other.configure(state=customtkinter.DISABLED)

    def unlock_checkboxes_after_timer_stop(self):
        self.check_boxes.measure_by_lines.configure(state=customtkinter.NORMAL)
        self.check_boxes.measure_by_items.configure(state=customtkinter.NORMAL)
        self.check_boxes.measure_by_other.configure(state=customtkinter.NORMAL)


app = MeasurementApp()
app.mainloop()
