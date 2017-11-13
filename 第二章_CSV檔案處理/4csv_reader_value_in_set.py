# -*- coding: utf-8 -*-
#!usr\bin\env python3
#篩選特定資料列，並輸出至csv - 找尋符合特定條件的集合(例如日期為'1/20/14','1/30/14')
#此範例以抓取date = {'1/20/14','1/30/14'}的資料列
"""
Created on Wed Sep 20 13:47:47 2017

@author: vizance
"""
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
important_dates = ['1/20/14','1/30/14'] #等下要找的日期範圍
part_number = ['2341','5467']#等下要找的產品編號
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            a_date = row_list[4]
            a_part_number = row_list[2]
            if a_date in important_dates and a_part_number in part_number:#須同時符合才會輸出
                filewriter.writerow(row_list)

