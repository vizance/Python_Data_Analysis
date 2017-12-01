# -*- coding: utf-8 -*-
#研究python os walk功能
"""
Created on Fri Dec  1 09:49:31 2017

@author: vizance
"""
import os

search_path = "C:\\Users\\vizance\\Desktop\\Python相關資料"
for dirPath, dirNames, fileNames in os.walk(search_path):
    #dirPath資料夾路徑名稱；dirNames是資料夾名稱的list；fileNames是檔案名稱的list
    print("dirpath→{}".format(dirPath))
    for direlement in dirNames:
        print("dirNames→{}".format(dirNames))
    if fileNames:
        for file in fileNames:
            print(os.path.join(dirPath,file))
    
    
    
