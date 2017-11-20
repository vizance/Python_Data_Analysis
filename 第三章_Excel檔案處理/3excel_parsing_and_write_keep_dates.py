# -*- coding: utf-8 -*-
#!usr/bin/env python3
#處理單張工作表(讀取單張worksheet，並對日期格式的cell_type進行處理)
"""
Created on Mon Oct  2 09:48:52 2017

@author: vizance
"""
import sys
from datetime import date #處理日期
from xlrd import open_workbook, xldate_as_tuple#處理日期
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):#這一大段都在處理日期格式
            if worksheet.cell_type(row_index, col_index) == 3:#http://www.lexicon.net/sjmachin/xlrd.html#xlrd.Cell-class
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index,col_index), workbook.datemode)
                #workbook.datemode是告訴電腦從1900年開始計算日期
                print(date_cell, '\n')
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y') #將日期轉變為日期格式的字串
                print(date_cell, '\n')
                row_list_output.append(date_cell)
                output_worksheet.write(row_index,col_index,date_cell)#指定列、欄，要寫入的資料格式
                
            else:
                none_date_cell = worksheet.cell_value(row_index,col_index)
                row_list_output.append(none_date_cell)
                output_worksheet.write(row_index,col_index,none_date_cell)
                
        print(row_list_output)
output_workbook.save(output_file)
