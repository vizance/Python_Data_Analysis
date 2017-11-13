# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#使用特定欄位名稱-尋找特定欄位
#此範例要找"Invoice Number","Purchase Date"
"""
Created on Thu Sep 21 09:51:09 2017

@author: vizance
"""
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
my_columns = ['Invoice Number','Purchase Date']
my_columns_index = []#用來儲存搜尋欄位的index
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader,None) #處理標題欄位
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)#輸出結果為欄位index[0,3]
        filewriter.writerow(my_columns)
        for row_list in filereader:#處理內文欄位
            row_list_output = []
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)

