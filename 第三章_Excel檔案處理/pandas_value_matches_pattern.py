# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#(pandas)篩選特定資料列-特定文字組合的值(範例：找J開頭的顧客)
#正規表示可參考：https://goo.gl/Ngufha
"""
Created on Tue Oct  3 10:08:48 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file, 'january_2013',index_col=None)#index_col是否讀取欄標題
data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith("J")]
writer = pd.ExcelWriter(output_file)
data_frame_value_matches_pattern.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()

