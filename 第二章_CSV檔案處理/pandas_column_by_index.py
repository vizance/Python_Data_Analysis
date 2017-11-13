# -*- coding: utf-8 -*-
#!usr/bin/env python3
#使用pandas搜尋特定欄位-使用索引值
#範例想保留Supplier與Cost
"""
Created on Wed Sep 20 15:21:29 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame_column_by_index = data_frame.iloc[:,[0,3]]#以index來找位置，要0跟3欄
data_frame_column_by_index.to_csv(output_file, index=False)
