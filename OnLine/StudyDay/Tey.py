import xlrd
class Read_Excel():
    def read_excel(self,index,row,column):
        try:
            excel_path=r"D:\Test\Data.xlsx"
            workbook=xlrd.open_workbook(excel_path,formatting_info=True)
        except Exception as e:
            print('Error')
            print(e)
            sheets=workbook.sheet_by_index(index)
            cell_value=sheets.cell(row,column).value
            return cell_value
