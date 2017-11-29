# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#統計csv檔案中，任意類別數量的資料
#練習嵌套式字典資料結構(字典中的字典)
"""
Created on Wed Oct 11 10:34:16 2017

@author: vizance
"""
import csv
import sys
from datetime import date, datetime

def date_diff(date1, date2):
    try:
        diff = str(datetime.strptime(date1, '%m/%d/%Y') - datetime.strptime(date2, '%m/%d/%Y')).split()[0]
        print(str(datetime.strptime(date1, '%m/%d/%Y') - datetime.strptime(date2, '%m/%d/%Y')))#XXX days,0:00:00
    except:
        diff = 0
    if diff == '0:00:00':
        diff = 0
    return diff

input_file = sys.argv[1]
output_file = sys.argv[2]
packages = {}#建立字典來儲存客戶套餐訂閱狀況
previous_name = 'N/A'#初始值設為N/A
previous_package = 'N/A'
previous_package_date = 'N/A'
first_row = True
today = date.today().strftime('%m/%d/%Y')
with open(input_file, 'r', newline='') as csv_in_file:
    filereader = csv.reader(csv_in_file)
    header = next(filereader)
    for row in filereader:
        current_name = row[0]
        current_package = row[1]
        current_package_date = row[3]
        if current_name not in packages:#如果是一個新客戶
            packages[current_name] = {}#將新客戶的Name加入字典成為key
        if current_package not in packages:#如果是一個新方案
            packages[current_name][current_package] = 0 #{current_name:{current_package:0}
        if current_name != previous_name:
            if first_row:
                first_row = False
            else:
                diff = date_diff(today, previous_package_date)#新進來的資料-previous_package_date
                if previous_package not in packages[previous_name]:#為了處理第一筆
                    packages[previous_name][previous_package] = int(diff)
                else:
                    packages[previous_name][previous_package] += int(diff)
        else:
            diff = date_diff(current_package_date, previous_package_date)
            packages[previous_name][previous_package] += int(diff)
        previous_name = current_name
        previous_package = current_package
        previous_package_date = current_package_date
header = ['Customer_name','Category','Total_time(in Days)']
with open(output_file, 'w', newline='') as csv_out_file:
    filewriter = csv.writer(csv_out_file)
    filewriter.writerow(header)
    for customer_name, customer_name_value in packages.items():
        for package_category, packages_category_value in packages[customer_name].items():
            row_of_output = []
            print(customer_name, package_category, packages_category_value)
            row_of_output.append(customer_name)
            row_of_output.append(package_category)
            row_of_output.append(packages_category_value)
            filewriter.writerow(row_of_output)
