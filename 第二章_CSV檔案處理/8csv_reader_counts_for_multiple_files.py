# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#計算檔案的數量，與各個檔案內的列與欄數量
"""
Created on Thu Sep 21 11:42:54 2017

@author: vizance
"""
import csv
import sys
import glob
import os
input_path = sys.argv[1] #檔案路徑
file_counter = 0 #有「多個」檔案時要用計數器追蹤處理數量
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
#glob.glob()找出含有特定文字組合的路徑名稱；os解析路徑名稱
    row_counter = 1 #header為一列
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader, None) #標題列與內容列的處理分開
        for row in filereader: #計算檔案數量
            row_counter += 1
        print('\n{0!s}:\t{1:d} rows:\t{2:d} columns'.format\
              (os.path.basename(input_file), row_counter, len(header)))#{!conversion}、{:format spec}
        file_counter += 1
    print ("Number of files: {0:d}".format(file_counter))

