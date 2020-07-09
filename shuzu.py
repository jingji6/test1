#元组和数组的区别：元组写好后不可更改数据，数组可更改数据
#数组方法：index()、count()、append()、insert()
a = [1,2,3,4,"哈哈","嘻嘻",True,False]

#append()在末尾加入数据
# a.append(5)  
# a.append(6)
# print(a)

#insert()   往数组中指定的位置插入数据
# a.insert(4,"呵呵")
# print(a)

#pop() 剪切数据
# b = a.pop(1)
# c = a.pop(1)
# print(b,c)
# print(b+c)


#clear()  清空
# a.clear()
# print(a)

#extend()  插入数组(合并数组)
xx = ["heeh","enne"]
a.extend(xx)
print(a)
