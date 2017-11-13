# -*- coding: utf-8 -*-
#!usr/bin/env python3
#篩選特定資料列，並輸出至csv - 找尋符合特定條件的集合(例如日期為'1/20/14','1/30/14')
#此範例以抓取date = {'1/20/14','1/30/14'}的資料列
"""
Created on Wed Sep 20 14:18:26 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
important_dates = ['1/20/14','1/30/14']
part_number = ['2341','5467']

data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates), :]
data_frame_value_in_set_two = data_frame_value_in_set.loc[data_frame['Part Number'].isin(part_number), :]
#isin代表選出列中包含特定值的行
#先篩選date，再塞選part number
data_frame_value_in_set_two.to_csv(output_file,index=False)

