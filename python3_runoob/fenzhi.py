#!/usr/bin/python3
"""
在python中没有switch-case语句
"""
var1 = 100
if var1:
    print("1 - if表达式为ture")
    print(var1)
var2 = 0
if var2:
    print("2 - if表达式为true")
    print(var2)
print("Good Bye!")
age = eval(input("请输入你家狗狗的年龄: "))
print()
if age < 0:
    print("你是在逗我吧！")
elif age == 1:
    print("相当于14岁的人。")
elif age == 2:
    print("相当于22岁的人。")
elif age > 2:
    human = 22 + (age -2) * 5
    print("对应人类年龄: ", human)
input("点击Enter键退出")
number = 10
guess = -1
print("数字猜谜游戏！")
while guess != number:
    guess = eval(input("请输入你猜的数字: "))
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字太小了...")
    elif guess > number:
        print("猜的数字太大了...")
num = eval(input("输入一个数字: "))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字%s可以整除2和3" % num)
    else:
        print("你输入的数字%s可以整除2但不可以整除3" % num)
else:
    if num % 3 == 0:
        print("你输入的数字%s不可以整除2但可以整除3" % num)
    else:
        print("你输入的数字%s既不可以整除2也可以整除3" % num)
