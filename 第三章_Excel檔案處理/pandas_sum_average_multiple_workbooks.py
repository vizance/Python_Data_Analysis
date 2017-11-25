# -*- coding: utf-8 -*-
#!/ust/bin/env python3
#(pandas)計算每個Excel與工作表的Sales總和/平均(可同時多個workbook一起處理)
#merge跟concat的差異：merge是要合併不同df的欄位；concat是欄位相同狀況下，合併df
"""
Created on Thu Oct  5 09:10:10 2017

@author: vizance
"""
import pandas as pd
import sys
import glob
import os
input_path = sys.argv[1]
output_file = sys.argv[2]
all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))
data_frames = [] #最後輸出的data_frame
for workbook in all_workbooks:
    all_worksheet = pd.read_excel(workbook, sheetname=None, index_col=None)
    print(all_worksheet)
    workbook_total_sales = [] #計算Excel總共的sales
    workbook_number_of_sales = [] #計算Excel總共的sales數量
    worksheet_data_frames = [] #儲存1個worksheet的data_frame的串列
    worksheets_data_frame = None #儲存
    workbook_data_frame = None
    for worksheet_name, data in all_worksheet.items():#items中是worksheet_name:data的字典結構
        total_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) for value in data.loc[:, 'Sale Amount']]).sum()
        number_of_sales = len(data.loc[:,'Sale Amount'])
        average_sales = pd.DataFrame(total_sales / number_of_sales)
            
        workbook_total_sales.append(total_sales)
        workbook_number_of_sales.append(number_of_sales)
        
        data = {'workbook':os.path.basename(workbook),'worksheet':worksheet_name,'worksheet_total':total_sales,'worksheet_average':average_sales}
        print('data: {}'.format(data)) #data存放每一個worksheet的總和
        worksheet_data_frames.append(pd.DataFrame(data, columns=['workbook','worksheet','worksheet_total','worksheet_average']))#將data轉為df
        print('\n\nworksheet_data_frame: {}'.format(worksheet_data_frames))
        
    worksheets_data_frame = pd.concat(worksheet_data_frames, axis=0, ignore_index=True)#將worksheets_data_frame合併成單一workbook_data_frame
    print('\nworksheets_data_frame: {}'.format(worksheets_data_frame))
    workbook_total = pd.DataFrame(workbook_total_sales).sum()
    workbook_total_number_of_sales = pd.DataFrame(workbook_number_of_sales).sum()
    workbook_average = pd.DataFrame(workbook_total/workbook_total_number_of_sales)
        
    workbook_stats = {'workbook':os.path.basename(workbook),'workbook_total':workbook_total,'workbook_average':workbook_average}
    workbook_stats = pd.DataFrame(workbook_stats, columns = ['workbook','workbook_total','workbook_average'])
    workbook_data_frame = pd.merge(worksheets_data_frame, workbook_stats, on='workbook', how='left')#合併worksheets_df與workbook_stats
    print('\nworkbook_data_frame: {}'.format(workbook_data_frame))
    data_frames.append(workbook_data_frame)
    print('\ndata_frames: {}'.format(data_frames))
all_data_concat = pd.concat(data_frames, axis = 0,ignore_index=True)
        
writer = pd.ExcelWriter(output_file)
all_data_concat.to_excel(writer, sheet_name='sums_and_averages', index=False)
writer.save()
        