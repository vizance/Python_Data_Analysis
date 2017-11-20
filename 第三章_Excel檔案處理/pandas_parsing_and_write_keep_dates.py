# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#(pandas)處理單張工作表(讀取單張worksheet，並對日期格式的cell_type進行處理)
"""
Created on Mon Oct  2 11:21:50 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file, sheetname = 'january_2013')
writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index = False)
writer.save()