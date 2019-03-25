#!/usr/bin/python3
"""
exec用来执行储存在字符串中的python语句
eval(str[globals[locals]])函数将字符串str当成有效的python表达式来求值，并提供返回计算值
"""
exec('print("hello world")')
exec('a = 100')
exec('print("a = ", a)')
print(eval('3 + 5'))
print(type(eval('3 + 5')))
#exists(file)将文件名字符串作为参数，如果文件存在返回True，否则返回False
from os.path import exists
print(exists("tryCatch.py"))
