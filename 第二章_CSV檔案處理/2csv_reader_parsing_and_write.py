# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Created on Wed Sep 20 10:49:12 2017

@author: vizance
"""
import csv #引入csv模組
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',') #delimiter是分隔符號(預設為,)
        filewriter = csv.writer(csv_out_file, delimiter=',')
        for row_list in filereader:
            print(row_list)
            filewriter.writerow(row_list)