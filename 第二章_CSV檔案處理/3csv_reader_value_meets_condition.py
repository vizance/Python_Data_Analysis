# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#篩選特定資料列，並輸出至csv - 找尋符合特定條件的值(例如日期在某個區間、價格在1000元以上...)
#此範例以抓取supplier X或cost > 500的資料列
"""
Created on Wed Sep 20 11:16:53 2017

@author: vizance
"""
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:#以下開放設定搜尋條件~
            supplier = str(row_list[0].strip()) #要抓supplier
            cost = str(row_list[3].strip('$').replace(',','')) #要抓cost，去掉$號，去掉，
            if supplier == 'Supplier X' or float(cost) > 500.00: #設定搜尋條件
                filewriter.writerow(row_list)
