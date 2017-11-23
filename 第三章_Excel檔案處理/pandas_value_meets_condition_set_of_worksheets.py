# -*- coding: utf-8 -*-
#!/ust/bin/env python3
#(pandas)讀取Excel活頁簿中特定幾張工作表(上一個範例檔是讀取所有的worksheets，此節只找第1、2張worksheets，sales>1900)
"""
Created on Thu Oct  5 09:44:05 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
my_sheets = [0,1]
threshold = 1900.0
data_frame = pd.read_excel(input_file, sheetname=my_sheets, index_col=None)#sheetname指定要處理的worksheet
row_list = []
for worksheet_name, data in data_frame.items():
    row_list.append(data[data['Sale Amount'].astype(float) > threshold])
filtered_rows = pd.concat(row_list, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='set_of_worksheets', index = False)
writer.save()
