# -*- coding: utf-8 -*-
#!/ust/bin/env python3
#練習串接多個Excel(活頁簿)的資料，並篩選資料欄位(Customer Name, Purchase Date)→1,4
"""
Created on Thu Oct  5 09:10:10 2017

@author: vizance
"""
import sys
import glob
import os
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
input_folder = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('all_data_all_workbooks')
data=[]
first_workbook = True
my_column = [1,4]
for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
    print (os.path.basename(input_file))
    with open_workbook(input_file) as workbook:
        for worksheet in workbook.sheets():
            if first_workbook:
                data.append(["Customer Name","Purchase Date"])
                first_workbook = False
            for row_index in range(1, worksheet.nrows):
                row_list = []
                for column_index in my_column:
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)
                    if cell_type ==3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
                data.append(row_list)
for list_index, output_list in enumerate(data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)