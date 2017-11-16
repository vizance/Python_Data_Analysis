# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#檢視Excel活頁簿中的工作表資訊
"""
Created on Mon Oct  2 09:34:48 2017

@author: vizance
"""
import sys
from xlrd import open_workbook
input_file = sys.argv[1]
workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet Name:", worksheet.name, "\tRows:", worksheet.nrows, \
          "\tColumns:", worksheet.ncols)