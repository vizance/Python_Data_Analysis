# -*- coding: utf-8 -*-
#!/ust/bin/env python3
#(pandas)串接多個Excel(活頁簿)的資料
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
data_frame = []
for workbook in all_workbooks:#對於每一個workbook
    all_worksheets = pd.read_excel(workbook, sheetname=None, index= None)
    for worksheet_name, data in all_worksheets.items():#對於每一個worksheets
        data_frame.append(data)
#print('\n\ndata_frame: {}'.format(data_frame))
all_data_concat = pd.concat(data_frame, axis = 0, ignore_index=True)#要先存到list裡面才可以concat
print('all_data_concat: {}'.format(all_data_concat))
writer = pd.ExcelWriter(output_file)
all_data_concat.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
writer.save()
        