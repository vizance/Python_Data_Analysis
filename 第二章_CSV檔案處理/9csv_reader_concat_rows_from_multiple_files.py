# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#串接多個檔案(假設欄位相同，要串接列)
"""
Created on Fri Sep 22 10:01:47 2017

@author: vizance
"""
import sys
import csv
import glob
import os
input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'a', newline='') as csv_out_file: #使用append來串接
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                header = next(filereader, None)#若不為第一個檔案，將header拿掉
                for row in filereader:
                    filewriter.writerow(row)
 
