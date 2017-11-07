# -*- coding: utf-8 -*-
#!usr/bin/evn python3 #這行叫做shebang, unix為基礎的系統會使用這一行來尋找執行檔案中，python版本的程式碼
#讀取

#===讀取/寫入文字檔練習開始===
##讀取文字檔(較舊的寫法)
"""import sys #引入sys模組，並在python script後面加入要開檔案的路徑
input_file = sys.argv[1] #讀取腳本後的第一個變數，這裡為路徑
print("output #143:")
filereader = open(input_file,'r')
for row in filereader:
    print (row.strip())
filereader.close()

##讀取文字檔(較新的寫法，python2.5之後)
import sys #引入sys模組，並在python script後面加入要開檔案的路徑
input_file = sys.argv[1]
print("output #144:")
with open(input_file,'r',newline="") as filereader:
    for row in filereader:
        print("{}".format(row.strip()))


##讀取多個文字檔(使用sys、glob、os)，在特定資料夾尋找特定文字組合
import sys
import glob
import os
print ("output #145:")
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
    with open(input_file, 'r',newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))
            
##寫入文字檔
import sys
import glob
import os
my_letters = ['a','b','c','d','e','f','g','h','i','j']#等下要將這些東西都寫入
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file,'w')
for index_value in range(len(my_letters)): 
    if index_value < (max_index -1):#當my_letters中的東西還沒寫完時
        filewriter.write(my_letters[index_value] + '\t')
    else:#當my_letters中的東西寫完後
        filewriter.write(my_letters[index_value] + '\n')
filewriter.close()
print("output #146: output written to file!!")

##寫到一個csv檔案中(附加非覆蓋)
my_numbers = [0,1,2,3,4,5,6,7,8,9] #等下要將這些東西全部寫入
max_index = len(my_numbers)
output_file = sys.argv[1]
filewriter = open(output_file,'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index -1):#當my_numbers中的東西還沒寫完時
        filewriter.write(str(my_numbers[index_value]) + ',')#記得要將int轉變成string
    else:#當my_numbers中的東西還寫完後
        filewriter.write(str(my_numbers[index_value]) + '\n')
filewriter.close()
print("output #147: output written to file!!")

#===讀取/寫入文字檔練習結束==="""