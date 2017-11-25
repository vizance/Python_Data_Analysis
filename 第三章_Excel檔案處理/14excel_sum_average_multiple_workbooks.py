# -*- coding: utf-8 -*-
#!/ust/bin/env python3
#計算每個Excel與工作表的Sales總和/平均(可同時多個workbook一起處理)
"""
Created on Thu Oct  5 09:10:10 2017

@author: vizance
"""
import sys
import glob
import os
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
input_folder = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('sums_and_averages')
all_data=[]
sales_column_index =3
header = ['workbook','worksheet','worksheet_total','worksheet_average','workbook_total','workbook_average']
all_data.append(header)
for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
    with open_workbook(input_file) as workbook:
        list_of_totals = []#用來輸出workbook加總
        list_of_numbers = []#用來輸出workbook加總
        workbook_output = []
        for worksheet in workbook.sheets():
            total_sales = 0
            number_of_sales = 0
            worksheet_list = []#用來輸出worksheet
            worksheet_list.append(os.path.basename(input_file))
            worksheet_list.append(worksheet.name)
            for row_index in range(1, worksheet.nrows):
                try:
                    total_sales = total_sales + \
                    float(str(worksheet.cell_value(row_index, sales_column_index)).strip('$').replace(',',''))
                    number_of_sales = number_of_sales + 1
                except:
                    total_sales += 0
                    number_of_sales += 0
            average_sales = '%.2f' %(total_sales / number_of_sales)#傳回字串
            worksheet_list.append(total_sales)
            worksheet_list.append(float(average_sales))#將字串轉為float
            list_of_totals.append(total_sales)
            list_of_numbers.append(float(number_of_sales))
            workbook_output.append(worksheet_list)
        workbook_total = sum(list_of_totals)
        workbook_average = sum(list_of_totals)/sum(list_of_numbers)
        print('\nworkbook_output: {}'.format(workbook_output))
        for list_element in workbook_output: #將workbook_total、workbook_average附加到workbook_output中!!!
            list_element.append(workbook_total)
            list_element.append(workbook_average)
        print('\nafter_loop_workbook_out: {} '.format(workbook_output))
        all_data.extend(workbook_output)#使用extend將[xxx,xxx,xxx]變成all_data中的獨立element，而非三個element[xxx]
        print(all_data)
for list_index, output_list in enumerate(all_data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)