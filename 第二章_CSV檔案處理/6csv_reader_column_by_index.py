# -*- coding: utf-8 -*-
#!usr/bin/env python3
#選擇特定欄位-使用欄位index(如果欄位資訊不會太複雜/欄位資訊不會變動/所有資料欄位資訊都相同)
#範例想保留Supplier與Cost
"""
Created on Wed Sep 20 15:07:45 2017

@author: vizance
"""
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
my_columns = [0,3]#要保留第0行與第3行
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:#讀取列
            row_list_output = [] #建立串列來儲存結果
            for row_index in my_columns:#讀取欄
                row_list_output.append(row_list[row_index])
            filewriter.writerow(row_list_output)
