# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#(pandas)讀取所有工作表worksheets-篩選所有worksheets中所有 Sales > 2000的工作列
"""
Created on Tue Oct  3 10:08:48 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,sheetname=None,index_col=None)#sheetname=None為不指定工作表(即所有)
row_output = []#要迭代某項容器中的所有值，就需要使用list
for worksheet_name,data in data_frame.items():#篩選所有的data_frame，key:value = worksheet_name:data 
    row_output.append(data[data['Sale Amount'].astype(float) > 2000.0])
print(row_output)
filter_rows = pd.concat(row_output, axis = 0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
filter_rows.to_excel(writer, sheet_name = 'sale_amount_gt2000', index=False)#寫入function
writer.save()#儲存結果

