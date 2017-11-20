# -*- coding: utf-8 -*-
#!usr/bin/env python3
#處理單張工作表(將單張worksheet讀入到新檔案，但日期會有問題)
"""
Created on Mon Oct  2 09:48:52 2017

@author: vizance
"""
import sys
from xlrd import open_workbook
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()#寫出工作簿
output_worksheet = output_workbook.add_sheet('jan_2013_output')#寫出工作表
with open_workbook(input_file) as workbook:#讀取input_file
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):#先讀列
        for col_index in range(worksheet.ncols):#再讀欄
            output_worksheet.write(row_index, col_index, worksheet.cell_value(row_index, col_index))
output_workbook.save(output_file)
