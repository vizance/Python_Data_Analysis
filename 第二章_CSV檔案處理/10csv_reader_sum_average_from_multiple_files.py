# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#求出每個檔案中，一組值的總和與平均值
#不確定這裡的output_file為什麼要用舊式檔案讀取方法(猜測：header跟內容分開處理)
"""
Created on Fri Sep 22 10:59:29 2017

@author: vizance
"""
import csv
import sys
import glob
import os
input_path = sys.argv[1]
output_file = sys.argv[2]
output_file_header = ['file_name','total_sales','average_sales']
csv_out_file = open(output_file, 'w', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_file_header)#將標題列寫到輸出檔
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    with open(input_file, 'r', newline='')as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        header = next(filereader,None)
        total_sales = 0.0
        average_sales = 0.0
        number_of_sales = 0.0
        for row in filereader:
            sale_amount = row[3]
            total_sales = total_sales + float(str(sale_amount).strip('$').replace(',',''))
            number_of_sales += 1
        average_sales = '{0:.2f}'.format(total_sales/number_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)
        print("{0!s} {1!s} {2!s}".format(total_sales, average_sales, output_list))
csv_out_file.close()

