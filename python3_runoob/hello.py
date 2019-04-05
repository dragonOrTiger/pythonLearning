#!/usr/bin/python3
#第一注释
#第二注释
'''
第三注释
第四注释
'''
"""
第五注释
第六注释
"""
print("Hello World!")
if True:
	print("True")
else:
	print("False")
if False:
	print("True")
else:
	print("False")
'''
多行语句
Python通常是一行写完一条语句，但如果语句过长，我们可以使用反斜杠(\)来实现多行语句
在[],(),{}中的多行语句，不需要使用反斜杠(\)
'''
total = 'item_one' + \
        'item_two' + \
        'item_three'
print(total)
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)
'''
字符串
'''
word = '字符串'
print(word)
sentence = "这是个句子"
print(sentence)
#使用三引号('''或""")可以指定一个多行字符串
paragraph = '''这是一个段落，
可以由多行组成'''
print(paragraph)
str = "Runoob"
print(str)
#字符串截取的语法格式:变量[头下标:尾下标:步长]
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
#用*表示运算符重复
print(str * 2)
print(str + "你好")
print('----------------------------------')
#反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
print('hello\nrunoob')
print(r'hello\nrunoob')
'''
input函数
'''
input("\n\n按下Enter键继续")
print('----------------------------------------')
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
'''
print输出
print默认输出是换行的，如果要实现不换行需要在变量末尾加上end=""
'''
x = 'a'
y = 'b'
#换行输出
print(x)
print(y)
print('----------')
print(x, end="")
print(y, end="")
print()
'''
import 与from...import
'''
print('命令行参数:')
for i in sys.argv:
	print(i)
print('\n python路径为', sys.path)
