#!/usr/bin/env python3
#篩選特定資料列-符合特定值(sales >1400)

import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

sale_amount_column_index = 3
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1,worksheet.nrows):#不包含header
        row_list = []
        sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)
        if sale_amount > 1400.0:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index,column_index)
                cell_type = worksheet.cell_type(row_index, column_index)#判斷是否為日期格式
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:#如果row_list有值就會為True
            data.append(row_list)
    for list_index, output_list in enumerate(data):#迭代data內各個串列，以及串列中的值，確保輸出檔的列之間沒有空白
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
            print("list_index:{0!s}  output_list:{1!s}  element_index:{2!s}  element:{3!s}".format(list_index, output_list, element_index, element))

output_workbook.save(output_file)