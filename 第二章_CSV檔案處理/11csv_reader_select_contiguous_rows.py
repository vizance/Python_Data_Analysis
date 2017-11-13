# -*- coding: utf-8 -*-
#!usr/bin/env python3
#選取特定連續「資料列」，避開不必要的列
"""
Created on Thu Sep 21 10:21:33 2017

@author: vizance
"""
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
row_counter = 0
with open(input_file, 'r', newline='')as csv_in_file:
    with open(output_file, 'w', newline='')as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >=3 and row_counter <=15:
                filewriter.writerow([value.strip()for value in row])#將符合特定的row(value)取出並strip
            row_counter += 1
