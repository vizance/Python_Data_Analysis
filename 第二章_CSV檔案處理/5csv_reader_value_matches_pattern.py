# -*- coding: utf-8 -*-
#!usr/bin/env python3
#篩選特定資料列，並輸出至csv - 找尋符合特定文字組合(例如發票為001-開頭，並且是Supplier Y)
"""
Created on Wed Sep 20 14:37:48 2017

@author: vizance
"""
import csv
import sys
import re
input_file = sys.argv[1]
output_file = sys.argv[2]
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)
pattern_Y = re.compile(r'(?P<patter_group>^Supplier Y)', re.I)
#將文字組合進行編譯，不一定要這麼做，但做了可以提升程式速度；re.I讓程式可以區分大小寫
with open (input_file, 'r', newline='') as csv_in_file:
    with open (output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)#將標題列寫出
        for row_list in filereader:
            invoice_number = row_list[1]
            supplier = row_list[0]
            if pattern.search(invoice_number) and pattern_Y.search(supplier):
                filewriter.writerow(row_list)
