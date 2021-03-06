#!/usr/bin/python3
# * 表示两个数相乘或是返回一个被重复若干次的字符串
print("2 * 9 = ", 2 * 9)
print("'adb' * 3: ", 'adb' * 3)
# / 的结果会是浮点数
# // 整除 结果向下取整
# % 被除数 - 除数 * 整除的结果
print("-9 / 5 = ", -9 / 5)
print("-9 // 5 = ", -9 // 5)
print("-9 % 5 = ", -9 % 5)
print("9 / -5 = ", 9 / -5)
print("9 // -5 = ", 9 // -5)
print("9 % -5 = ", 9 % -5)
"""
is与==的区别:
is用于判断两个变量引用对象是否为同一个，==用于判断引用变量的值是否相等
"""
a = [1, 2, 3]
b = a
c = a[:]
print("a与b是否是同一对象?", a is b)
print("a与b引用变量的值是否相等?", a == b)
print("a与c是否是同一对象?", a is c)
print("a与c引用变量的值是否相等?", a == c)
