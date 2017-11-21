# -*- coding: utf-8 -*-
#!usr/bin/env python3
#(pandas)選擇特定欄位_by欄位索引值(col_index，範例為Customer Name, Purchase Date)
"""
Created on Wed Oct  4 09:05:38 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_by_index = data_frame.iloc[:,[1,4]]#iloc使用index; loc使用index name; [列:,欄]，空白代表all
writer = pd.ExcelWriter(output_file)
data_frame_by_index.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
