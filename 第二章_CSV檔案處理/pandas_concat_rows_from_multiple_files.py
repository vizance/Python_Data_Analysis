# -*- coding: utf-8 -*-
#!/usrs/bin/env python3
#(pandas)串接多個檔案(假設欄位相同，串接列)
"""
Created on Fri Sep 22 10:43:21 2017

@author: vizance
"""
import pandas as pd
import sys
import glob
import os

input_file = sys.argv[1]
output_file = sys.argv[2]
all_files = glob.glob(os.path.join(input_file, 'sales_*')) #將所有檔案存到變數中
all_data_frame = []
for files in all_files:
   data_frame = pd.read_csv(files, index_col = None) #開啟csv檔
   all_data_frame.append(data_frame)#將csv檔案append在一個list

data_frame_concat = pd.concat(all_data_frame,axis=0, ignore_index=True)#將list中的串列用pd.concat串接
data_frame_concat.to_csv(output_file, index=False)
    
