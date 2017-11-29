# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#計算文字檔資料任意類別數量的統計數據(以MySQL中的錯誤檔案為例)
#此範例使用嵌套式字典 {day:{note:發生次數}}
"""
Created on Thu Oct 12 09:45:35 2017

@author: vizance
"""
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
messages = {}
notes = []
with open(input_file, 'r', newline='') as txt_file:
    for row in txt_file:
        if '[Note]' in row:#錯誤訊息都是[Note]開頭
            row_list = row.split(' ',4)#因為' ' 有很多個，強制用4個' '分開
            day = row_list[0].strip()#2014-02-03
            note = row_list[4].strip('\n').strip()#InnoDB: ...
            if note not in notes: #錯誤訊息
                notes.append(note)
            if day not in messages: #日期
                messages[day] = {}
            if note not in messages[day]: #錯誤訊息數量
                messages[day][note] = 1
            else:
                messages[day][note] += 1
filewriter = open(output_file, 'w', newline='')
header = ['Data']
header.extend(notes)
header = ','.join(map(str,header)) + '\n'
print(header)
filewriter.write(header)
for day, day_value in messages.items():
    row_of_output = []
    row_of_output.append(day)
    for index in range(len(notes)):
        if notes[index] in day_value.keys():
            row_of_output.append(day_value[notes[index]])
        else:
            row_of_output.append(0)
        output = ','.join(map(str,row_of_output)) + '\n'
    print(output)
    filewriter.write(output)
filewriter.close()