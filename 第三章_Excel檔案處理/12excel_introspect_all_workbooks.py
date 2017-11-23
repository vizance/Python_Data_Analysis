# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#計算總共有多少Excel檔案(workbook)，各Excel檔案中有多少worksheets、列與欄
"""
Created on Thu Oct  5 10:03:26 2017

@author: vizance
"""
import sys
import glob
import os
from xlrd import open_workbook
input_directory = sys.argv[1]#輸入路徑
workbook_counter = 0
for input_file in glob.glob(os.path.join(input_directory, '*.xls*')): #xls*包含xlsx
    workbook = open_workbook(input_file)
    print('Workbook: %s' %os.path.basename(input_file))#可以用%，不一定要用format
    print ('Number of worksheets: %d' % workbook.nsheets)#workbook.nsheets是返回worksheets的數量
    for worksheet in workbook.sheets():
        print('worksheet_name:', worksheet.name,'\tRows:', worksheet.nrows , 'Columns:', worksheet.ncols)
    workbook_counter += 1
print('number of workbooks: %d' %(workbook_counter))

