# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#(pandas)添加標題列
"""
Created on Thu Sep 21 11:38:42 2017

@author: vizance
"""
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
header_list = ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)#利用names來命名header
print (data_frame)
data_frame.to_csv(output_file, index=False)