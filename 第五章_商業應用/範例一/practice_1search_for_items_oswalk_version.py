# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#使用CSV檔案來尋找一群檔案(xls.xlsx、csv)中的特定資料
#使用os walk，讓來尋找一檔案夾的所有資料(包含子資料夾)
"""
Created on Sun Oct  8 10:03:47 2017

@author: vizance
"""
import sys
import csv
import glob
import os
from datetime import date
from xlrd import open_workbook, xldate_as_tuple

item_numbers_file = sys.argv[1]#要用甚麼東西找
path_to_folder = sys.argv[2]#要找的東西在哪裡
output_file = sys.argv[3]#要輸出到哪裡
path_list = []

item_numbers_to_find = []
with open(item_numbers_file, 'r', newline='') as item_numbers_csv_file:
    filereader = csv.reader(item_numbers_csv_file)
    for row in filereader:
        item_numbers_to_find.append(row[0])#將要找的東西讀到list中
print (item_numbers_to_find)
filewriter = csv.writer(open(output_file, 'a', newline=''))
filewriter.writerow(['Item Number','Description','Supplier','Cost','Date','FileName','WorksheetName'])

file_counter = 0#已被讀取的檔案數量
line_counter = 0#已被讀取檔案的列數量
count_of_item_numbers = 0#含有想要尋找項目的列數量

for dirPath, dirNames, fileNames in os.walk(path_to_folder):
    #dirPath資料夾路徑名稱；dirNames是資料夾名稱的list；fileNames是檔案名稱的list
    path_list.append(dirPath)
    for element in path_list:
        print("要尋找的檔案路徑：{}".format(path_list))
for path in path_list:
    for input_file in glob.glob(os.path.join(path,'*.*')):
        file_counter += 1
        if input_file.split('.')[1] == 'csv':#XXX.YYY,YYY為副檔名
            with open(input_file, 'r', newline='') as csv_in_file:
                filereader = csv.reader(csv_in_file)
                header = next(filereader)
                for row in filereader:
                    row_of_output = []
                    for column in range(len(header)):
                        if column == 3:#Cost
                            cell_value = str(row[column]).lstrip('$').replace(',','').strip()
                            row_of_output.append(cell_value)
                        else:
                            cell_value = str(row[column]).strip()
                            row_of_output.append(cell_value)
                    row_of_output.append(os.path.basename(input_file))
                    if row[0] in item_numbers_to_find:#對於每一列的第一個項目
                        filewriter.writerow(row_of_output)
                        count_of_item_numbers += 1
                    line_counter += 1
        elif input_file.split('.')[1] == 'xls' or input_file.split('.')[1] == 'xlsx':
            workbook = open_workbook(input_file)
            for worksheet in workbook.sheets():
                try:
                    header = worksheet.row_values(0)
                except IndexError:
                    print("下標越界囉!")
                    pass
                for row in range(1, worksheet.nrows):
                    row_of_output = []
                    for column in range(len(header)):
                        if worksheet.cell_type(row, column) == 3:
                            cell_value = xldate_as_tuple(worksheet.cell(row, column).value, workbook.datemode)
                            cell_value = str(date(*cell_value[0:3])).strip()
                            row_of_output.append(cell_value)
                        else:
                            cell_value = str(worksheet.cell_value(row, column)).strip()
                            row_of_output.append(cell_value)
                    row_of_output.append(os.path.basename(input_file))
                    row_of_output.append(worksheet.name)
                    if str(worksheet.cell(row,0).value).split('.')[0].strip() in item_numbers_to_find:#ex.1234.0
                        print(str(worksheet.cell_value(row,0)))
                        filewriter.writerow(row_of_output)
                        count_of_item_numbers += 1
                    line_counter += 1
print('Number of files:', file_counter)
print('Number of lines:', line_counter)
print('Number of item numbers:', count_of_item_numbers)