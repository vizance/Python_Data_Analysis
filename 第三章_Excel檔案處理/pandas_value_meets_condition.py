# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#(pandas)篩選特定資料列-符合特定值(sales >1400)
"""
Created on Tue Oct  3 10:08:48 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file, 'january_2013',index_col=None)
data_frame_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]#將df的值轉換為float
writer = pd.ExcelWriter(output_file)
data_frame_meets_condition.to_excel(writer, sheet_name = 'jan_2013_output', index = False)
writer.save()

