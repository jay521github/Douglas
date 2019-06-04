import xlrd
def Ex(path):
    try:
        workbook=xlrd.open_workbook(path)
    except Exception as e:
        print(e)
        print('error')
    else:
        sheet=workbook.sheet_by_index(0)
        rows=sheet.nrows
        case_list=[]
        for i in range(rows):
            if i!=0:
                case_list.append(sheet.cell_value(i))