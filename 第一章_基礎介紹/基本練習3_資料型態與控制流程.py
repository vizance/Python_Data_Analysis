# -*- coding: utf-8 -*-
#!usr/bin/evn python3 #這行叫做shebang, unix為基礎的系統會使用這一行來尋找執行檔案中，python版本的程式碼
#練習串列、tuple、字典、控制流程(for迴圈、if-else/if-elif-else、while、try-except、try-except-else-finally)
"""
Created on Tue Nov  7 14:40:56 2017

@author: vizance
"""

#===串列(List)練習開始===

##建立串列(練習輸出、len()、max、min、)
a_list = [1,2,3]
print("output #58: {}".format(a_list))
print("output #59: {}".format(len(a_list)))
print("output #60: {}".format(max(a_list)))

##索引值，[0]是第一個元素、[-1]是最後一個元素
##串列切片(不加入開始索引值，會從頭開始；不加入結尾索引值，會存取到最後)
print("output #73: {}".format(a_list[0:2])) #不包含:後方的索引值
print("output #74: {}".format(a_list[:2]))
print("output #75: {}".format(a_list[1:]))#從:前的索引值開始
      
##複製串列
a_new_list = a_list[:] #[:]指定全部
print("output #77: {}".format(a_new_list))

##串接串列(使用+來將串列合併在一起)

##使用in、not in 來檢查特定元素是否在串列中
a = 2 in a_list
print("output #79: {}".format(a))

b = 4 not in a_list
print("output #81: {}".format(b))

##append、remove、pop
###使用append()將額外元素加到串列結尾
###使用remove()移除特定元素
###使用pop()來移除串列結尾的元素
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("output #83: {}".format(a_list))
a_list.remove(5)
print("output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("output #85: {}".format(a_list))

##reverse(將一個串列顛倒)
a_list.reverse()
print("output #86: {}".format(a_list))
a_list.reverse()

##sort(排序，由小->大)
b_list = [1,4,6,7,3,5,4,2,5,4]
b_list.sort()
print("output #90: {}".format(b_list))

##sorted(按照串列中的位置來排序)
my_lists = [[1,2,3,4],[4,3,2,1],[2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value:index_value[3])
print("output #91: {}".format(my_lists_sorted_by_index_3)) #1 ->3 ->4，sorted不會改變原始排序

###引入operator模組中的itemgetter幫忙排序
from operator import itemgetter
my_lists = [[123,2,2,444],[22,6,6,444],[354,4,4,678],[236,5,5,678],[578,1,1,290],[461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0)) #先用[3]進行排序後，再用[0]進行排序
print("output #92: {}".format(my_lists_sorted_by_index_3_and_0))

#===串列(List)練習結束===

#===Tuple練習開始===
#Tuple跟串列很像，但不能修改，應用的範圍如字典的key值

##建立tuple
my_tuple = ('x','y','z')
print(my_tuple)

###拆解Tuple(使用左邊的變數來拆解tuple，在互換值的時候很好用)
one, two, three = my_tuple
print("output #97: {}{}{}".format(one,two,three))

var1 = "red"
var2 = "robin"
var1, var2 = var2, var1
print("output #99: {} {}".format(var1,var2))

##可使用tuple()、list()將tuple換成List，或是list變成tuple

#===Tuple練習結束===

#===dictionary字典練習開始===
a_dict = {'one':1, 'two':2, 'three':3}
print("output # 102: {}".format(a_dict))
print("output # 103: a_dict has {!s} elements:".format(len(a_dict)))
print("output # 106: {}:".format(a_dict['two']))#使用key取value時

##copy
a_new_dict = a_dict.copy()
print("output # 107: {}:".format(a_new_dict))

##存取key、value與item
print("output # 109: {}".format(a_dict.keys()))
a_dict_keys = a_dict.keys()
print("output # 110: {}".format(a_dict_keys))
print("output # 111: {}".format(a_dict.values()))
print("output # 112: {}".format(a_dict.items()))

##使用in、not in與get(測試特定鍵是否在字典中，若有則回傳對應值；若無則回傳none或自己指定的文字)
print("output # 118: {}".format(a_dict.get('four','not in dict')))

##排序，使用sorted(會改變字典排序→跟list的sorted不會改變順序 不相同)
dict_copy = a_dict.copy()
orderded_dict1 = sorted(dict_copy.items(), key = lambda item: item[0]) #lamda是一個簡單的function define，用完即丟，expression不能放等號
print("output # 120 (ordered by keys): {}".format(orderded_dict1))#item函式回傳每一個key-value tuple，item[0]為key

orderded_dict2 = sorted(dict_copy.items(), key = lambda item: item[1])#item函式回傳每一個key-value tuple，item[1]為value
print("output # 121 (ordered by values): {}".format(orderded_dict2))

orderded_dict3 = sorted(dict_copy.items(), key = lambda x: x[1], reverse=True)#使用值來排序，降冪排序
print("output # 122 (ordered by values, descending): {}".format(orderded_dict3))

orderded_dict4 = sorted(dict_copy.items(), key = lambda x: x[1], reverse=False)#使用值來排序，升冪排序
print("output # 123 (ordered by values, ascending): {}".format(orderded_dict4))

#===dictionary字典練習結束===

#===控制流程練習開始===
##if-else / if-elif-else

##for 迴圈
y = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec',]
z = ['Annie','Betty','Claire','Daphne','Ellie','Franchesca','Greta','Holly','Isabel','Jenny']
a_dict = {'one':1,'two':2,'three':3}
print("output # 126:")
for month in y:
    print("{!s}".format(month))
    
print("output # 127: (index value: name in list)")
for i in range(len(z)):
    print ("{0!s}: {1:s}".format(i, z[i]))
    
print("output # 128: (access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('J'): #如果y[j]的值開頭是"J"的話
        print ("{!s}".format(y[j]))
        
print("output #129:")
for key, value in a_dict.items():
    print("{0:s}, {1}".format(key, value))
    
###串列生成式
my_data = [[1,2,3],[4,5,6],[7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]#row for row針對my_data中的每一個list都執行for 迴圈
print("output #130(list comprehension): {}".format(rows_to_keep))

###集合生成式
my_data = [(1,2,3),(4,5,6),(7,8,9),(7,8,9)]
set_of_tuple1 = {x for x in my_data} #針對my_data中的每一個tuple，若他是「獨一」則保留它
print("output #131 (set comprehension): {}".format(set_of_tuple1))
set_of_tuple2 = set(my_data)#用在tuple
print("output #132 (set function): {}".format(set_of_tuple2))#用python內建的set function一樣可以做到

###字典生成式
my_dict = {'customer1':7,'customer2':9,'customer3':11}
my_results = {key:value for key, value in my_dict.items() if value > 10}
print("output #133 (dict comprehension): {}".format(my_results))

##while 迴圈

##function
###計算一系列數字的平均值
def getmean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues) > 0 else float('nan') 
#可以寫成一個式子(a if b else c)，但盡量不要這樣做 
    
def getmean1(var):
    if len(var) > 0:
        return sum(var)/len(var)
    else: #記得else也要加一個:
        float('nan')
    
my_list = [2,2,4,4,6,6,8,8]
print("output #135 (mean): {!s}".format(getmean(my_list)))

##try except
###計算一系列數字的平均值
def getmean2(var1):
    return sum(var1)/len(var1)

my_list2 =[]
####簡短版本
try:
    print("output #138: {}".format(getmean2(my_list2)))
except ZeroDivisionError as detail: #如果發生除0的錯誤
    print("output #138: (Error):{}".format(float('nan')))
    print("output #138: (Error):{}".format(detail))

####長版本
try:
    result = getmean2(my_list2)
except ZeroDivisionError as detail:
    print("output #142 (Error): "+str(float('nan')))
    print("output #142 (Error):", detail)
else:
    print("output #142 (the mean is):", result)
finally:
    print("output #142 (finally): the finally block is executed every time")
#當try區塊的執行成功時，會執行else區塊；如果有錯誤就會執行except區塊；finally區塊一定會被執行

#===控制流程練習結束==="""