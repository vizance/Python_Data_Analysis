# -*- coding: utf-8 -*-
#!usr/bin/evn python3 #這行叫做shebang, unix為基礎的系統會使用這一行來尋找執行檔案中，python版本的程式碼
"""print("output#1: I'm excited to learn python")

#===========開始練習============

#P8~P10
## 練習一、將兩個數字相加
x = 4
y = 5
z = x + y
print("output#2: 4+5= {0:d}".format(z)) #{0:d}.format(z)是要被傳入print陳述式的值的預留位置，0指向變數z的第一個位置；d指定拉入的值應該轉換為不帶小數點的數字

## 練習二、將兩個list相加，以及format練習
a = [1,2,3,4]
b = ["first","second","third","fourth"]
c = a + b
print("output#3: {0}, {1}, {2}".format(a,b,c))

#P11~12
##數字_整數
x = 9
print("output #4: {0}".format(x))
print("output #5: {0}".format(3**4))
print("output #6: {0}".format(int(8.3)/int(2.7))) #數字轉譯成整數，並進行8/2的除法

##數字_浮點數
print("output #7: {0:.3f}".format(8.3/2.7)) #.3f指定到小數點後3位的浮點數

y = 2.5*4.8
print("output #8: {0:.1f}".format(y))

r=8/float(3)
print("output #9: {0:.2f}".format(r))
print("output #10: {0:.4f}".format(8.0/3))

##小插曲:type函數
type(2.0)

#呼叫內建運算模組
from math import exp, log, sqrt
print("output #11: {0:.4f}".format(exp(3)))
print("output #12: {0:.2f}".format(log(4)))
print("output #13: {0:.1f}".format(sqrt(81)))

#==========基本練習結束==========="""

#==========Python變數型態========

#字串
"""print("output #14: {0:s}".format('I\'m enjoying learning python.')) #如果用"來區隔字串，就不需要\'
print("output #15: {0:s}".format("this is a long string\
      it would run off of the page on the right in the")) #注意\後面不可以有空白鍵
print("output #16: {0:s}".format('''You can use triple single quotes for multi-line comment strings.'''))
print("output #17: {0:s}".format("You can also use triple double quotes"))"""

## 字串的運算_基本
"""str1 = "this is a "
str2 = "short string. "
sentence = str1 + str2
print("output #18: {0:s}".format(sentence))
print("output #19: {0:s} {1:s}{2:s}".format("She is", "very "*3, "cute. "))

m = len(sentence) #找出字串的字元數量
print("output #20: {0:d}".format(m))"""

## 字串的運算_split
"""str1 = "My deliverable is due in May"
str1_list1 = str1.split()
str1_list2 = str1.split(" ",2) #把string切「兩刀」
print("output #21: {0}".format(str1_list1))
print("output #22: first piece:{0} second piece:{1} third piece:{2}"\
      .format(str1_list2[0],str1_list2[1],str1_list2[2]))

str2 = "Your,deliverable,is,due,in,June"
str2_list = str2.split(",")
print("output #23: {0}".format(str2_list))
print("output #24: {0} {1} {2}".format(str2_list[1],str2_list[5],str2_list[-1])) """

##字串的運算_join
"""print("output #25: {0}".format(",".join(str2_list))) #用,來進行join"""

##字串的運算_strip
"""str3 = " Remove  unwanted characters   from this string.\t\t   \n" #\t表示tab、\n表示換行
print("output #26: {0:s}".format(str3))

str3_lstrip = str3.lstrip() #刪除左側空白
print("output #27: lstrip: {0:s}".format(str3_lstrip))

str3_rstrip = str3.rstrip() #刪除右側空白、\t、\n
print("output #28: rstrip: {0:s}".format(str3_rstrip))

str3_strip = str3.strip() #刪除兩側
print("output #29: strip: {0:s}".format(str3_strip))

str4 = "$$Here's another string that has unwanted characters.__---+++"
print("output #30: {0:s}".format(str4))
str4 = "$$The unwanted characters have been removed.__---+++"
str4_strip = str4.strip('$_-+') #移除特定字元
print("output #31: {0:s}".format(str4_strip))"""

##字串的運算_replace
"""str5 = "Lst's replace the spaces in this sentence with other charcters."
str5_replace = str5.replace(" ","!@!")
print("output #32: (with !@!){0:s}".format(str5_replace))

str5_replace = str5.replace(" ",",")
print("output #33: (with ,){0:s}".format(str5_replace))"""

##字串的運算_lower, upper, captilize
"""str6 = "Here's WHAT Happens WHEN You Use lower."
print("output #34: {0:s}".format(str6.lower()))

str7 = "Here WHAT Happens WHEN You Use UPPER."
print("output #34: {0:s}".format(str7.upper()))

str8 = "Here WHAT Happens WHEN You Use Capitalize."
print("output #34: {0:s}".format(str7.capitalize()))

str8_list = str8.split()
print("output #35: (on each word):")
for word in str8_list:
    print("{0:s}".format(word.capitalize()))"""
    
#==========Python變數型態練習結束========