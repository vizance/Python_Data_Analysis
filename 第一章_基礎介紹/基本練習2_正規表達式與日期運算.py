# -*- coding: utf-8 -*-
#!usr/bin/evn python3 
#這一部分用來理解正規標達式 / 日期運算
#備註：當要搜尋特定文字時可以使用正規表達式

"""
Created on Tue Nov  7 13:56:09 2017

@author: vizance
"""

#===正規表達式與匹配文字組合(資料分析中，欄位資料的大小寫匹配非常重要)===
#呼叫re模組(正規表達式模組，使用中繼字元來匹配各種文字組合)
#中繼字元如 |、()、[]、*、+、?、^、$、(?P<name>)

import re #re模組用來創造或搜尋各種文字組合
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The",re.I) 
#re.compile代表將文字組合編譯成正規表達式
#不一定要做但做了可以提升電腦執行速度，re.I可以確保程式區分大小寫；
#r確保python不會處理字串的特殊序列，例如\ \t \n
count = 0
for word in string_list:
    if pattern.search(word):
        count = count + 1
print("output #38: {0:d}".format(count))

#將比對到的單字(The)印出在螢幕上
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)",re.I) 
#r"(?P<name>The)"透過(?P<name>)符號群組名稱<name>來使用匹配的字串，群組中放進The
print("output #39: ")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))
        #於pattern中搜尋是否匹配The，若找到則印出match_word群組中的值
##練習搜尋dog
pattern2 = re.compile(r"(?P<match_dog>dog)",re.I )
print("practice searching dog: ")
for word in string_list:
    if pattern2.search(word):
        print("{:s}".format(pattern2.search(word).group("match_dog")))
       

        
#將字串的The替換成a
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The" #將正規表達式指派給變數，方便程式碼閱讀
pattern = re.compile(string_to_find,re.I)
print("output #40: {:s}".format(pattern.sub("a", string)))

##練習替換dog為cat
string_to_find2 = r"dog"
pattern2=re.compile(string_to_find2, re.I)
print("practice to replace dog: {:s}".format(pattern2.sub("cat", string)))

    
#===正規表達式與匹配文字組合結束===

#===日期的運算處理===
from datetime import date, datetime, timedelta #引入datatime模組

##印出今天的年、月及日元素
today = date.today()#date物件只能秀出年、月、日
print("output #41: today:{0!s}".format(today)) #!s表示被傳入到print陳述式裡面的值都要轉換為string
print("output #42: {0!s}".format(today.year))
print("output #43: {0!s}".format(today.month))
print("output #44: {0!s}".format(today.day))

current_time = datetime.today() #使用datetime來表示詳細的時間、datetime物件可以秀出年月日、小時、分、秒
print("output #45: {0!s}".format(current_time))

##使用timedelta來計算新日期
one_day = timedelta(days=-1)
yesterday = today + one_day
print("output #46: yesterday:{0!s}".format(yesterday))

eight_hours = timedelta(hours=-8)
print("output #47: {0!s} {1!s} ".format(eight_hours.days,eight_hours.seconds))
#使用timedelta時，括號內的時間會被轉換成日、秒、毫秒，秒的計算過程是：24hr * 3,600秒 - 8hr * 3,600秒

date_diff = today - yesterday
print("output #48: {0!s}".format(date_diff)) #計算出來的結果是用datetime呈現
print("output #49: {0!s}".format(str(date_diff).split()[0])) 
#將date_diff換成string，利用split取出第[0]個索引，date_diff的內容為 1 day 0:00:00

##使用strftime，來用date物件建立特定格式的字串
print("output #50: {0!s}".format(today.strftime('%m/%d/%Y')))
print("output #51: {0!s}".format(today.strftime('%b %d, %Y')))

##使用strftime，以特定格式的字串建立datetime物件
#產生代表日期的字串
date1 = today.strftime('%m%d%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')

#兩個datetime物件、兩個date物件
###datetime中的strf跟strp的差別：strf用來正規化日期、strp用來將字串轉換為datetime格式
print("output #54: {0!s}".format(datetime.strptime(date1, '%m%d%Y'))) 

###只想取日期
print("output #56: {0!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))

#===日期的運算處理結束===