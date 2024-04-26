import customtkinter


from main_window_widgets.buttons import MainWindowButtons
from main_window_widgets.frames import MainWindowFrames
from excel.measurement_report import MeasurementReport
from main_window_widgets.check_boxes import MainWindowCheckBoxes
from main_window_widgets.labels import MainWindowLabels
from main_window_widgets.option_menus import MainWindowOptionMenus
from main_window_widgets.scrollable_frames import MainWindowScrollableFrames
from main_window_widgets.text_boxes import MainWindowTextBoxes
from stopwatch import StopWatch

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class MeasurementApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Measurement tool V1.0")
        self.geometry(f"{800}x{480}")
        self.resizable(width=False, height=False)

        self.report = MeasurementReport()
        self.stopwatch = StopWatch(self)

        self.frames = MainWindowFrames(self)
        self.buttons = MainWindowButtons(self)
        self.labels = MainWindowLabels(self)
        self.check_boxes = MainWindowCheckBoxes(self)
        self.text_boxes = MainWindowTextBoxes(self)
        self.option_menus = MainWindowOptionMenus(self)
        self.scrollable_frames = MainWindowScrollableFrames(self)

    def start_measurement(self):
        self.stopwatch.start_stopwatch()
        self.populate_measurement_report_start()

        self.buttons.start_button.configure(state=customtkinter.DISABLED)
        self.buttons.stop_button.configure(state=customtkinter.NORMAL)
        self.buttons.pause_button.configure(state=customtkinter.NORMAL)
        self.lock_checkboxes_after_timer_start()

    def end_measurement(self):
        self.stopwatch.stop_stopwatch()
        self.populate_measurement_report_end()

        self.buttons.start_button.configure(state=customtkinter.NORMAL)
        self.buttons.stop_button.configure(state=customtkinter.DISABLED)
        self.buttons.pause_button.configure(state=customtkinter.DISABLED)
        self.unlock_checkboxes_after_timer_stop()

    def pause_measurement(self):
        self.stopwatch.pause_stopwatch()

        self.buttons.start_button.configure(state=customtkinter.NORMAL)
        self.buttons.stop_button.configure(state=customtkinter.NORMAL)
        self.buttons.pause_button.configure(state=customtkinter.DISABLED)

    def lock_checkboxes_after_timer_start(self):
        self.check_boxes.measure_by_lines.configure(state=customtkinter.DISABLED)
        self.check_boxes.measure_by_items.configure(state=customtkinter.DISABLED)
        self.check_boxes.measure_by_other.configure(state=customtkinter.DISABLED)

    def unlock_checkboxes_after_timer_stop(self):
        self.check_boxes.measure_by_lines.configure(state=customtkinter.NORMAL)
        self.check_boxes.measure_by_items.configure(state=customtkinter.NORMAL)
        self.check_boxes.measure_by_other.configure(state=customtkinter.NORMAL)

    def populate_measurement_report_start(self):
        self.report.enter_measurement_id()
        self.report.enter_measurer()
        self.report.enter_start_time()
        self.report.enter_team_name(self.option_menus)
        self.report.enter_process_name(self.option_menus)
        self.report.enter_team_member(self.option_menus)

    def populate_measurement_report_end(self):
        self.report.enter_elapsed_time(self.stopwatch.elapsed_time)
        self.report.enter_stop_time()
        self.report.save_report()


app = MeasurementApp()
app.mainloop()
