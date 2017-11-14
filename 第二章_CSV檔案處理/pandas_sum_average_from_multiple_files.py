# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#(pandas)求出每個檔案中，一組值的總和與平均值
"""
Created on Fri Sep 22 11:23:54 2017

@author: vizance
"""
import pandas as pd
import sys
import glob
import os
input_path = sys.argv[1]
output_file = sys.argv[2]
all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames =[]
for input_file in all_files:
    data_frame = pd.read_csv(input_file, index_col=None)
    
    total_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) \
                                      for value in data_frame.loc[:,'Sale Amount']]).sum()
    average_sales = pd.DataFrame([float(str(value).strip('$').replace(',',''))\
                                  for value in data_frame.loc[:,'Sale Amount']]).mean()
    data = {'file_name':os.path.basename(input_file), 'total_sales':total_sales\
            ,'average_sales':average_sales} #建立一個dict叫做data
    
    all_data_frames.append(pd.DataFrame(data, columns=['file_name','total_sales','average_sales']))
    #創建名為data的dataframe，並將其append到all_data_frames的list中
    print(all_data_frames)
data_frame_concat = pd.concat(all_data_frames,axis=0,ignore_index=True)#ignore_index=True的目的為，重新排序df的index
print (data_frame_concat)
data_frame_concat.to_csv(output_file, index=False)
