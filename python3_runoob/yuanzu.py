#!/usr/bin/python3
"""
Python的元组与列表类似，不同之处在于元组的元素不能修改
元组使用小括号，列表使用方括号
元组创建很简单，只需要在括号内添加元素，并使用逗号隔开即可
"""
aTup = ('Google', 'Runoob', 1997, 2000)
print(aTup)
bTup = (1, 2, 3, 4, 5)
print(bTup)
cTup = "a", "b", "c", "d"
print(type(cTup))
"""
元组只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
"""
dTup = (50)
print(type(dTup))
eTup = (50,)
print(type(eTup))
"""
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
"""
fTup = (12, 34.56)
gTup = ('abc', 'xyz')
hTup = fTup + gTup
print(hTup)
del hTup
#与字符串一样，元组之间可以使用+和*进行运算，这就意味着他们可以组合和复制，运算后生成一个新的元组
print(len((1, 2, 3)))
print((1, 2, 3) + (4, 5, 6))
print(('Hi!',) * 4)
print(3 in (1, 2, 3))
for x in (1, 2, 3):
    print(x)
#tuple(seq) 将列表转换为元组
jTup = tuple("Google")
print(jTup)
kTup = tuple([1, 2, 3])
print(kTup)
