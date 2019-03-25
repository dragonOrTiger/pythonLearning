#!/usr/bin/python3
'''
break语句用来终止循环，用在while和for循环中!!直接跳出整个嵌套循环，
break语句将停止执行最深层的循环，并开始执行下一行代码
break是跳出整个循环，continue是跳出当前循环
'''
for letter in 'python':
    if letter == 'h':
        break
    print("当前字母是:", letter)
print('******************************')
for letter in 'python':
    if letter == 'h':
        continue
    print("当前字母是:", letter)
print('******************************')
var = 10
while var > 0:
    print('当前数字是:', var)
    var -= 1
    if var == 5:
        break
print('******************************')
var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print('当前数字是:', var)
