import xlrd
ExcelName=xlrd.open_workbook('D:\\1.xlsx')
SheetName=ExcelName.sheet_by_name('test')
for i in range(0,SheetName.nrows):
    print(i)