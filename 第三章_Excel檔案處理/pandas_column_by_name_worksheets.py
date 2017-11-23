# -*- coding: utf-8 -*-
#!usr/bin/env python3
#(pandas)讀取所有工作表worksheets-篩選所有worksheets中特定欄位_by欄位標題(col_name)
"""
Created on Wed Oct  4 09:05:38 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file, sheetname=None, index_col=None)
column_output = []
for worksheet_name, data in data_frame.items():
    column_output.append(data.loc[:,['Customer Name','Sale Amount']])
selected_columns = pd.concat(column_output, axis=0,ignore_index=True)
writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(writer, sheet_name='selected_columns_all_worksheets', index=False)
writer.save()
