# -*- coding: utf-8 -*-
#!usr/bin/env python3
#讀取所有工作表worksheets-篩選所有worksheets中特定欄位_by欄位標題(col_name)
"""
Created on Wed Oct  4 08:50:54 2017

@author: vizance
"""
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('selected_columns_all_worksheets')
my_column = ['Customer Name','Sale Amount']#指定要選擇的欄
first_worksheet = True
with open_workbook(input_file)as workbook:
    data = [my_column] #儲存最後output，先把header存進去
    index_of_col_to_keep = []#儲存找到col_name的index
    for worksheet in workbook.sheets():
        if first_worksheet:
            header = worksheet.row_values(0)
            for column_index in range(len(header)):
                if header[column_index] in my_column:
                    index_of_col_to_keep.append(column_index)
        first_worksheet = False
        for row_index in range(1, worksheet.nrows):
            row_list = [] #儲存被正規化的值
            for column_index in index_of_col_to_keep:
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
            data.append(row_list)
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)
            
            
    

