# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#讀取所有工作表worksheets-篩選所有worksheets中所有 Sales > 2000的工作列
"""
Created on Tue Oct  3 09:25:09 2017

@author: vizance
"""
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('filtered_rows_all_worksheets')
sale_amount_column_index = 3
threshold = 2000.0
first_worksheet = True
with open_workbook(input_file)as workbook:
    data = [] #儲存最後output
    for worksheet in workbook.sheets():#多加此行，對於workbook
        if first_worksheet:
            header_row = worksheet.row_values(0)
            data.append(header_row)
            first_worksheet = False
        for row_index in range(1, worksheet.nrows):
            row_list = [] #儲存被正規化的值
            sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)
            if sale_amount > threshold:
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index,column_index)
                    print("cell_value: {}".format(cell_value))
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
            if row_list: #如果row_list有值
                data.append(row_list)
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)
            
            
    
