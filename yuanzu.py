# #元组写好后不可更改其内数据
#方法：index()、count()

a = (1,2,3,4,"哈哈","嘻嘻",True,False)
# print(type(a))
# #下标，由0开始
# print(a[4])
# #index查看下标
# print(a.index("哈哈"))
# #查看数量
# print(a.count("哈哈"))

#切片，左闭右开
print(a[2:5])



# #套娃，一层一层
# a = (1,2,3,4,"哈哈","嘻嘻",True,False)
# b = (a,"哈哈",True)
# #展示a里面所有的数据
# print(b[0])

# #展示a里面任意元素
# print(b[0][5])

