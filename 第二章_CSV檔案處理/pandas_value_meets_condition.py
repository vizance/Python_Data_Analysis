# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#使用pandas做3csv_reader_value_meets_condition.py
#篩選特定資料列，並輸出至csv - 找尋符合特定條件的值(例如日期在某個區間、價格在1000元以上...)
"""
Created on Wed Sep 20 11:32:49 2017

@author: vizance
"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$') #先把$刪掉
data_frame['Cost'] = (data_frame['Cost'].str.split()).apply(lambda x: float(x[0].replace(',',''))) 
#原書中是以沒有千分位符號為例，如果包含千分位逗點，要先把逗點取代掉之後，才可以轉換為float
data_frame_value_meets_condition = data_frame.loc[(data_frame["Supplier Name"].str.contains('A'))\
| (data_frame['Cost']> 500.00), :]
print(data_frame_value_meets_condition)
data_frame_value_meets_condition.to_csv(output_file, index = False)
