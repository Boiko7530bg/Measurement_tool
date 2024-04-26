import time

import customtkinter


class StopWatch:
    def __init__(self, master):
        super().__init__()

        self.start_time = None
        self.paused_time = None
        self.time_var = customtkinter.StringVar()
        self.time_var.set("00:00:00")
        self.elapsed_time = 0
        self.timer_running = False
        self.timer_stopped = False
        self.after = master.after

    def start_stopwatch(self):
        if self.timer_stopped:
            self.elapsed_time = 0
            self.timer_stopped = False

        if not self.timer_running:
            self.start_time = time.time() - self.elapsed_time
            self.update()
            self.timer_running = True

    def stop_stopwatch(self):
        self.timer_running = False
        self.timer_stopped = True

    def pause_stopwatch(self):
        if self.timer_running:
            self.paused_time = self.start_time
            self.timer_running = False

    def update(self):
        if self.timer_running:
            self.elapsed_time = time.time() - self.start_time

        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)

        self.time_var.set("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
        self.after(1000, self.update)
