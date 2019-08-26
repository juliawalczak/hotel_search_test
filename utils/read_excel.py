import xlrd

class ExcelReader:

    def get_data(self):
        wb = xlrd.open_workbook("../utils/data.xlsx")
        sheet = wb.sheet_by_index(0)


