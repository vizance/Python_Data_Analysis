# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#篩選特定資料列-符合定購買日期(尋找01/24/2013 、 01/31/2013)
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
output_worksheet = output_workbook.add_sheet('jan_2013_output')
important_dates = ['01/24/2013','01/31/2013']#想要查找的日期
purchase_date_column_index = 4
with open_workbook(input_file)as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = [] #儲存最後output
    header = worksheet.row_values(0)#第0列為header
    data.append(header)
    for row_index in range(1, worksheet.nrows):
        row_list = [] #儲存被正規化的值
        purchase_datetime = xldate_as_tuple(worksheet.cell_value(row_index, purchase_date_column_index),\
                                            workbook.datemode)
        purchase_date = date(*purchase_datetime[0:3]).strftime('%m/%d/%Y')#此行目的為處理important dates的日期資料
        print('purchase_datetime: {}'.format(purchase_datetime))
        print('purchase_date: {}'.format(purchase_date))
        if purchase_date in important_dates:
            for column_index in range(worksheet.ncols):#把符合的列擷取出來
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
            
            
    
