"""
字典的特点：
1.字典中的值没有顺序
2.字典的结果必须是  键值对 结构  key：value
"""
a = {"name":"LiXiaoLong",
    0:"哈哈",
    "age":24
}
print(a)

#取值
print(a["age"])
#新增
a["高度"]="189cm"
print(a)
#修改
a["高度"]="190cm"
print(a)