import xlrd
class Excel():
    def Ex(self,index,row,column):
        try:
            excel_path=r'D:\TestData\Data.xls'
            workbook=xlrd.open_workbook(excel_path,formatting_info=True)
        except Exception as e:
            print('读取文件失败')
            print(e)
        sheets=workbook.sheet_by_index(index)
        cell_value=sheets.cell(row,column).value
        return cell_value


