import xlrd
class Excel():
    def excel(self,row,col):
        path = r'C:\Users\Administrator\Desktop\Test.xlsx'
        workbook = xlrd.open_workbook(path)
        SheetName = workbook.sheets()[0]
        cell_value=SheetName.cell(row,col).value
        return cell_value