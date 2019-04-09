#!/usr/bin/python3
"""
在python中没有do...while循环
"""
n = 100
suma = 0
counter = 1
while counter <= n:
    suma = suma + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, suma))
"""
无限循环
我们可以通过设置条件表达式永远不为false来实现无限循环
"""
#var = 1
#while var == 1:
#    num = eval(input("输入一个数字: "))
#    print("你输入的数字是: ", num)
#print("Good bye!")
"""
在while...else在条件语句为false时执行else的语句块
"""
count = 5
while count < 5:
    print(count, "小于5")
    count = count + 1
else:
    print(count, "大于或等于5")
"""
简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将语句与while写在同一行中，如下所示:
"""
#flag = 1
#while flag: print("欢迎访问菜鸟教程！")
#print("Good bye!")
"""
python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
break语句用于跳出当前循环体
for循环的一般格式如下:
for <variable> in <sequence>:
    <statements>
else:
    <statements>
"""
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程！")
        break
    print("循环数据" + site)
else:
    print("没有循环数据！")
print("完成循环！")
"""
range(stop) -> range object
range(start, stop[, step]) -> range object
Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.  
range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  
range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
"""
for i in range(5):
    print(i)
for i in range(5, 9):
    print(i)
for i in range(0, 10, 3):
    print(i)
for i in range(-10, -100, -30):
    print(i)
a = ["Google", "Baidu", "Runoob", "Taobao", "QQ"]
for i in range(len(a)):
    print(i, a[i])
"""
break语句可以跳出for和while的循环体。如果你从for或者while循环中终止，任何对应的循环else块将不执行
continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
"""
for letter in 'Runoob':
    if letter == 'b':
        break
    print("当前字母为: ", letter)
var = 10
while var > 0:
    print('当前变量值为: ', var)
    var = var - 1
    if var == 5:
        break
print('Good bye!')
for letter in 'Runoob':
    if letter == 'o':
        continue
    print("当前字母为: ", letter)
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('当前变量值为: ', var)
print('Good bye!')
"""
循环语句可以有else语句，它在穷尽列表(以for循环)或条件变为false(以while循环)导致循环终止时被执行，但循环被break终止时不执行
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "等于", x, '*', n//x)
            break
    else:
        print(n, "是质数")
"""
Python pass是空语句，是为了保持程序结构的完整性
"""
for letter in 'Runoob':
    if letter == 'o':
        pass
        print("执行pass块")
    print("当前字母为: ", letter)
print('Good bye!')
