#!/usr/bin/python3
template = '零一二三四五六七八九'
num = input('请输入一个整数: ')
for i in num:
	print(template[eval(i)], end = '')
print()
