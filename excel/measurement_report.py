import datetime

import openpyxl


class MeasurementReport:
    REPORT_WB_PATH = "..\\excel\\database\\measurement_report.xlsx"
    REPORT_COLUMN_NAMES = {"measurement_id": "A",
                           "username": "B",
                           "time_start": "C",
                           "time_end": "D",
                           "pause_total": "E",
                           "productive_time": "F",
                           "measured_number": "G",
                           "client": "H",
                           "process": "I",
                           "team_member": "J",
                           "comment": "K"
                           }

    def __init__(self):
        self.report_wb = openpyxl.load_workbook(self.REPORT_WB_PATH)
        self.report_ws = self.report_wb.active
        self.last_row = self._increase_row_number_by_one(self.REPORT_COLUMN_NAMES['measurement_id'])

    def enter_measurement_id(self):
        pass

    def enter_start_time(self):
        target_cell = f"{self.REPORT_COLUMN_NAMES['time_start']}{str(self.last_row)}"
        start_time = datetime.datetime.now()
        self.report_ws[target_cell] = start_time

    def enter_stop_time(self):
        target_cell = f"{self.REPORT_COLUMN_NAMES['time_end']}{str(self.last_row)}"
        stop_time = datetime.datetime.now()
        self.report_ws[target_cell] = stop_time

    def save_report(self):
        try:
            self.report_wb.save(self.REPORT_WB_PATH)
        except:
            raise Exception("File is open")

    def _find_report_last_row(self, column):
        last_row = len(self.report_ws[column])
        return last_row

    def _increase_row_number_by_one(self, column: str):
        return self._find_report_last_row(column) + 1


wb = MeasurementReport()
wb.enter_start_time()
wb.enter_stop_time()
wb.save_report()
