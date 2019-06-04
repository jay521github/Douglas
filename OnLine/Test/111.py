import xlrd

path=r'C:\Users\Administrator\Desktop\Test.xlsx'
workbook=xlrd.open_workbook(path)
SheetName=workbook.sheet_by_index(0)
print(SheetName.name)
url=SheetName.cell(0,1).value
uid=SheetName.cell(1,1).value
password=SheetName.cell(2,1).value
