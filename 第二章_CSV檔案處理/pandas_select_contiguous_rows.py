# -*- coding: utf-8 -*-
#!usr/bin/env python3
#(pandas)選取特定連續「資料列」
"""
Created on Thu Sep 21 10:39:42 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file,header=None)#不要將header算在index中
data_frame = data_frame.drop([0,1,2,16,17,18])
print(data_frame)
data_frame.columns = data_frame.iloc[0] #指定第0列成為新的欄位索引
print(data_frame.columns)
data_frame = data_frame.reindex(data_frame.index.drop(3)) #將重複列(原header)的label=3給drop掉
print("\n")
print (data_frame)
data_frame.to_csv(output_file, index=False)
