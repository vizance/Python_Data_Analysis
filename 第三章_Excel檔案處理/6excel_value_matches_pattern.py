# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#篩選特定資料列-特定文字組合的值(範例：找J開頭的顧客)
#正規表示可參考：https://goo.gl/Ngufha
"""
Created on Tue Oct  3 09:25:09 2017

@author: vizance
"""
import sys
import re
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
pattern = re.compile(r'(?P<my_pattern>^J.*)')#r'想要查找的對象'
customer_name_column_index = 1
with open_workbook(input_file)as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = [] #儲存最後output
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1, worksheet.nrows):
        row_list = [] #儲存被正規化的值
        if pattern.search(worksheet.cell_value(row_index, customer_name_column_index)):
            for column_index in range(worksheet.ncols):#針對找到列的每一欄
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index,column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                    print("row_list: {}".format(row_list))
                else:
                    row_list.append(cell_value)
                    print("row_list: {}".format(row_list))
        if row_list: #如果row_list有值
            data.append(row_list)
            print("data: {}".format(data))
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)
            
            
    
