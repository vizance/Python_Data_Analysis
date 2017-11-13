# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#(pandas)利用特定欄位名稱來尋找特定欄位
#此範例要找"Invoice Number","Purchase Date"
"""
Created on Thu Sep 21 10:13:05 2017

@author: vizance
"""
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:,['Invoice Number','Purchase Date']]
data_frame_column_by_name.to_csv(output_file, index=False)
