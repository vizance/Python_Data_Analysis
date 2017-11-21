# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#(pandas)篩選特定資料列-符合定購買日期(尋找01/24/2013 、 01/31/2013)
"""
Created on Tue Oct  3 10:08:48 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file, 'january_2013')#(讀取檔案,讀取worksheet,是否帶入index_col)
print(data_frame)
important_dates = ['01/24/2013','01/31/2013']
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dates)]
#isin - 尋找包含特定值的列
writer = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_output', index = False)
writer.save()

